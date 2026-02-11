#!/usr/bin/env python3
"""Utilities for generating review flag windows around prediction changes."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import numpy as np
import pandas as pd


PRED_COL_CANDS = ["Predicted_Activity", "predicted", "prediction", "pred"]
FRAME_COL_CANDS = ["frames", "frame", "Frame", "Frames", "FRAME"]
TIME_COL_CANDS = ["Time", "time", "seconds", "Seconds"]


@dataclass
class ReviewStats:
    total_rows: int
    predicted_change_points: int
    flagged_frames: int
    flagged_frames_pct: float
    windows_count: int
    rows_covered_by_windows: int
    effective_fps: float
    frame_stride: int
    seconds_window: float


def _find_col(df: pd.DataFrame, candidates: Sequence[str]) -> str | None:
    for cand in candidates:
        if cand in df.columns:
            return cand
    return None


def _merge_intervals(intervals: Iterable[Tuple[int, int]]) -> List[Tuple[int, int]]:
    iv = sorted(intervals, key=lambda x: x[0])
    if not iv:
        return []
    merged: List[List[int]] = [list(iv[0])]
    for start, end in iv[1:]:
        if start <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return [(int(s), int(e)) for s, e in merged]


def generate_review_flags(
    csv_path: Path,
    *,
    fps_video: float = 30.0,
    frame_stride: int = 10,
    seconds_window: float = 3.0,
) -> Tuple[Path, Path, ReviewStats, List[int]]:
    """Generate review flags CSVs and stats from prediction output.

    Returns:
        flags_csv_path: Path to the CSV with an added ``flag_window`` column.
        summary_path: Path to a CSV summary row with aggregate stats.
        stats: ReviewStats object with metrics for UI display.
        flagged_frames: Sorted list of frame indices flagged for review.
    """

    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Prediction CSV not found: {csv_path}")

    df0 = pd.read_csv(csv_path)

    pred_col = _find_col(df0, PRED_COL_CANDS)
    frame_col = _find_col(df0, FRAME_COL_CANDS)
    time_col = _find_col(df0, TIME_COL_CANDS)

    if pred_col is None:
        raise ValueError(
            f"Prediction CSV missing predicted column. Tried {PRED_COL_CANDS}. Available: {list(df0.columns)}"
        )

    if frame_col is None and time_col is None:
        raise ValueError(
            "Prediction CSV must contain a frame or time column to compute review windows."
        )

    df = df0.copy()
    df["_PRED_"] = df[pred_col].astype(str).str.strip().str.upper()

    if frame_col is not None:
        df["_FRAME_"] = pd.to_numeric(df[frame_col], errors="coerce").astype("Int64")
        df = df[df["_FRAME_"].notna()].reset_index(drop=True)
        df["_FRAME_"] = df["_FRAME_"].astype(int)
        effective_fps = float(fps_video) / max(1, int(frame_stride))
    else:
        df["_TIME_"] = pd.to_numeric(df[time_col], errors="coerce")
        if df["_TIME_"].notna().sum() > 1:
            tvals = df["_TIME_"].dropna().values
            diffs = np.diff(tvals)
            diffs = diffs[diffs > 0]
            dt = float(np.median(diffs)) if len(diffs) else 0.0
            effective_fps = (1.0 / dt) if dt else (float(fps_video) / max(1, int(frame_stride)))
        else:
            effective_fps = float(fps_video) / max(1, int(frame_stride))
        df["_FRAME_"] = np.arange(len(df), dtype=int)

    half_win = int(round((seconds_window * effective_fps) / 2.0))

    pred_change = (df["_PRED_"].shift(1) != df["_PRED_"]).fillna(False)
    change_frames = df.loc[pred_change, "_FRAME_"].astype(int).tolist()

    min_f = int(df["_FRAME_"].min()) if len(df) else 0
    max_f = int(df["_FRAME_"].max()) if len(df) else -1

    windows = []
    for frame_idx in change_frames:
        start = max(min_f, frame_idx - half_win)
        end = min(max_f, frame_idx + half_win)
        windows.append((start, end))

    merged_windows = _merge_intervals(windows)

    flag_mask = pd.Series(False, index=df.index)
    for start, end in merged_windows:
        mask = (df["_FRAME_"] >= start) & (df["_FRAME_"] <= end)
        if mask.any():
            flag_mask[mask] = True

    out = df[df0.columns].copy()
    out["flag_window"] = flag_mask.values

    n_changes = int(pred_change.sum())
    n_flagged = int(flag_mask.sum())
    pct_flagged = 100.0 * n_flagged / max(1, len(df))
    frames_in_windows = sum((end - start + 1) for start, end in merged_windows)
    n_windows = len(merged_windows)

    stats = ReviewStats(
        total_rows=int(len(out)),
        predicted_change_points=n_changes,
        flagged_frames=n_flagged,
        flagged_frames_pct=float(round(pct_flagged, 2)),
        windows_count=n_windows,
        rows_covered_by_windows=int(frames_in_windows),
        effective_fps=float(round(effective_fps, 3)),
        frame_stride=int(frame_stride),
        seconds_window=float(seconds_window),
    )

    flags_path = csv_path.with_name(csv_path.stem + "_flags.csv")
    summary_path = csv_path.with_name(csv_path.stem + "_flags_summary.csv")

    out.to_csv(flags_path, index=False)
    pd.DataFrame([
        {
            "total_rows": stats.total_rows,
            "predicted_change_points": stats.predicted_change_points,
            "flagged_frames": stats.flagged_frames,
            "flagged_frames_pct": stats.flagged_frames_pct,
            "windows_count": stats.windows_count,
            "rows_covered_by_windows": stats.rows_covered_by_windows,
            "effective_fps": stats.effective_fps,
            "frame_stride": stats.frame_stride,
            "seconds_window": stats.seconds_window,
        }
    ]).to_csv(summary_path, index=False)

    flagged_frame_indices = sorted(df.loc[flag_mask, "_FRAME_"].astype(int).unique().tolist())

    return flags_path, summary_path, stats, flagged_frame_indices


__all__ = [
    "ReviewStats",
    "generate_review_flags",
]





