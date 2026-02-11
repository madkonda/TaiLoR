#!/usr/bin/env python3
"""Run activity predictions using tree_logic modules."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
from typing import Optional

import pandas as pd  # type: ignore


def load_tree_logic(module_path: Path):
    """Dynamically import a tree_logic module from disk."""

    module_path = module_path.expanduser().resolve()
    if not module_path.exists():
        raise FileNotFoundError(f"tree_logic module not found: {module_path}")

    spec = importlib.util.spec_from_file_location("tree_logic_runtime", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load spec for module at {module_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


def run_prediction(
    csv_path: Path,
    module_path: Path,
    output_path: Optional[Path] = None,
    preview: bool = False,
) -> Path:
    """Predict activities using the provided tree_logic module."""

    csv_path = csv_path.expanduser().resolve()
    if not csv_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {csv_path}")

    module = load_tree_logic(module_path)

    df = pd.read_csv(csv_path)
    pred_df = module.predict_df(df, gt_col=None, unify=True, print_report=False)

    if "Predicted_Activity" not in pred_df.columns:
        raise RuntimeError('predict_df did not return "Predicted_Activity" column.')

    if output_path is None:
        output_path = csv_path.with_name(csv_path.stem + "output.csv")

    output_path = output_path.expanduser().resolve()
    pred_df.to_csv(output_path, index=False)

    if preview:
        print("\n[Preview] First 8 predictions:")
        print(pred_df.head(8).to_string(index=False))
        print("\n[Counts]")
        print(pred_df["Predicted_Activity"].value_counts())

    return output_path


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run predictions using a tree_logic module.")
    parser.add_argument(
        "--module",
        default="./mouse_outputs/tree_logic.py",
        help="Path to generated tree_logic.py",
    )
    parser.add_argument(
        "--csv",
        required=True,
        help="Input CSV with features (no ground-truth required)",
    )
    parser.add_argument(
        "--out",
        default=None,
        help='Output CSV path. Default: "<input_stem>output.csv" next to input.',
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Print a small preview and label counts",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    module_path = Path(args.module)
    csv_path = Path(args.csv)
    out_path = Path(args.out) if args.out else None

    output = run_prediction(csv_path, module_path, out_path, preview=args.preview)
    print(f"[OK] Wrote predictions → {output}")


if __name__ == "__main__":
    main()






