#!/usr/bin/env python3
"""Rat (with nest) feature extraction utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import cv2
import pandas as pd  # type: ignore

DEFAULT_FIXED_POINTS: Dict[str, Tuple[int, int]] = {
    "c1": (0, 0),
    "c2": (1266, 0),
    "c3": (1266, 688),
    "c4": (0, 688),
    "pipeEnd": (445, 426),
    "pipeMid": (518, 381),
    "pipeStart": (581, 346),
    "foodhopperBottom": (610, 362),
    "foodhopperLeft": (472, 117),
    "foodhopperRight": (1016, 122),
    "foodhopperMid": (654, 222),
    "Pups_Location": (1018, 590),
}


def _euclidean_distance(p1: Tuple[float, float] | None,
                        p2: Tuple[float, float] | None) -> float | None:
    if p1 is None or p2 is None:
        return None
    if any(v is None for v in p1) or any(v is None for v in p2):
        return None
    return float(((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5)


def _analyze_mask(mask: np.ndarray) -> Dict[str, float | int | None]:
    base_keys = [
        "area", "perimeter", "centroid_x", "centroid_y",
        "bbox_x", "bbox_y", "bbox_w", "bbox_h", "aspect_ratio",
        "solidity", "extent", "orientation", "eccentricity",
        "RL_x", "RL_y", "RR_x", "RR_y", "RT_x", "RT_y", "RB_x", "RB_y"
    ]
    hu_keys = [f"hu_{i}" for i in range(7)]
    adv_keys = [
        "Dist_RL_RR", "Dist_RT_RB", "Dist_RL_RT", "Dist_RT_RR",
        "Dist_RR_RB", "Dist_RB_RL", "Centroid_To_Bbox_TL", "Centroid_To_Bbox_TR",
        "Centroid_To_Bbox_BR", "Centroid_To_Bbox_BL"
    ]
    extreme_keys = [
        "Dist_RL_To_Bbox_TL", "Dist_RL_To_Bbox_TR", "Dist_RL_To_Bbox_BR", "Dist_RL_To_Bbox_BL",
        "Dist_RR_To_Bbox_TL", "Dist_RR_To_Bbox_TR", "Dist_RR_To_Bbox_BR", "Dist_RR_To_Bbox_BL",
        "Dist_RT_To_Bbox_TL", "Dist_RT_To_Bbox_TR", "Dist_RT_To_Bbox_BR", "Dist_RT_To_Bbox_BL",
        "Dist_RB_To_Bbox_TL", "Dist_RB_To_Bbox_TR", "Dist_RB_To_Bbox_BR", "Dist_RB_To_Bbox_BL"
    ]

    all_keys = base_keys + hu_keys + adv_keys + extreme_keys

    mask = np.squeeze(mask)
    if mask.ndim != 2:
        return {k: None for k in all_keys}
    mask = (mask > 0).astype(np.uint8)
    if not np.any(mask):
        return {k: None for k in all_keys}

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return {k: None for k in all_keys}

    c = max(contours, key=cv2.contourArea)
    features: Dict[str, float | int | None] = {}

    area = float(cv2.contourArea(c))
    features['area'] = area
    features['perimeter'] = float(cv2.arcLength(c, True))

    M = cv2.moments(c)
    centroid = (M['m10'] / M['m00'], M['m01'] / M['m00']) if M['m00'] != 0 else (None, None)
    features['centroid_x'], features['centroid_y'] = centroid

    x, y, w, h = cv2.boundingRect(c)
    features.update({'bbox_x': int(x), 'bbox_y': int(y), 'bbox_w': int(w), 'bbox_h': int(h)})
    features['aspect_ratio'] = float(w) / float(h) if h > 0 else None
    features['extent'] = float(area) / float(w * h) if (w * h) > 0 else None

    hull = cv2.convexHull(c)
    hull_area = float(cv2.contourArea(hull))
    features['solidity'] = float(area) / float(hull_area) if hull_area > 0 else None

    if len(c) >= 5:
        (_, _), (a1, a2), angle = cv2.fitEllipse(c)
        major, minor = (max(a1, a2), min(a1, a2))
        features['orientation'] = float(angle)
        features['eccentricity'] = ((1 - (minor / major) ** 2) ** 0.5) if major > 0 else None
    else:
        features['orientation'] = None
        features['eccentricity'] = None

    rl = tuple(c[c[:, :, 0].argmin()][0])
    rr = tuple(c[c[:, :, 0].argmax()][0])
    rt = tuple(c[c[:, :, 1].argmin()][0])
    rb = tuple(c[c[:, :, 1].argmax()][0])
    features.update({
        'RL_x': int(rl[0]), 'RL_y': int(rl[1]),
        'RR_x': int(rr[0]), 'RR_y': int(rr[1]),
        'RT_x': int(rt[0]), 'RT_y': int(rt[1]),
        'RB_x': int(rb[0]), 'RB_y': int(rb[1]),
    })

    hu = cv2.HuMoments(cv2.moments(c)).flatten()
    for i in range(7):
        features[f'hu_{i}'] = float(hu[i])

    features['Dist_RL_RR'] = _euclidean_distance(rl, rr)
    features['Dist_RT_RB'] = _euclidean_distance(rt, rb)
    features['Dist_RL_RT'] = _euclidean_distance(rl, rt)
    features['Dist_RT_RR'] = _euclidean_distance(rt, rr)
    features['Dist_RR_RB'] = _euclidean_distance(rr, rb)
    features['Dist_RB_RL'] = _euclidean_distance(rb, rl)

    tl, tr, br, bl = (x, y), (x + w, y), (x + w, y + h), (x, y + h)
    features['Centroid_To_Bbox_TL'] = _euclidean_distance(centroid, tl)
    features['Centroid_To_Bbox_TR'] = _euclidean_distance(centroid, tr)
    features['Centroid_To_Bbox_BR'] = _euclidean_distance(centroid, br)
    features['Centroid_To_Bbox_BL'] = _euclidean_distance(centroid, bl)

    for ep_name, ep_coords in {'RL': rl, 'RR': rr, 'RT': rt, 'RB': rb}.items():
        for cname, cpt in {'TL': tl, 'TR': tr, 'BR': br, 'BL': bl}.items():
            features[f'Dist_{ep_name}_To_Bbox_{cname}'] = _euclidean_distance(ep_coords, cpt)

    return features


def extract_rat_features(
    npz_path: str,
    fixed_points: Dict[str, Tuple[int, int]] | None = None,
    rat_id: int = 2,
    nest_id: int = 1,
) -> str:
    """Extract features for rat+nest NPZ. Returns the CSV path."""

    npz_file = Path(npz_path).expanduser().resolve()
    if not npz_file.exists():
        raise FileNotFoundError(f'NPZ not found: {npz_file}')

    fixed_points = fixed_points or DEFAULT_FIXED_POINTS

    data = np.load(str(npz_file), allow_pickle=True)
    video_segments: Dict[int, Dict[int, np.ndarray]] = {}

    for key in data.files:
        identifier = key.replace('frame', '')
        identifier = identifier.replace('obj_', 'obj')
        parts = identifier.split('_obj')
        if len(parts) != 2:
            continue
        try:
            frame_idx = int(parts[0])
            obj_id = int(parts[1])
        except ValueError:
            continue
        video_segments.setdefault(frame_idx, {})[obj_id] = data[key]

    if not video_segments:
        raise RuntimeError('No frames parsed from NPZ. Check key format (e.g., "frame12_obj2").')

    all_features: Dict[int, Dict[str, float | int | None]] = {}
    previous_masks: Dict[str, np.ndarray | None] = {}

    ordered_frames = sorted(video_segments.keys())

    for frame_idx in ordered_frames:
        all_features[frame_idx] = {}

        for obj_name, obj_id in [("Rat", rat_id), ("Nest", nest_id)]:
            mask = video_segments[frame_idx].get(obj_id, np.zeros((1, 1), dtype=np.uint8))
            feats = _analyze_mask(mask)
            for key, value in feats.items():
                all_features[frame_idx][f"{obj_name}_{key}"] = value

        for obj_name, obj_id in [("Rat", rat_id), ("Nest", nest_id)]:
            curr_mask = video_segments[frame_idx].get(obj_id)
            prev_mask = previous_masks.get(obj_name)
            curr_area = all_features[frame_idx].get(f"{obj_name}_area")
            prev_area = all_features.get(frame_idx - 1, {}).get(f"{obj_name}_area")

            if curr_area is not None and prev_area is not None:
                all_features[frame_idx][f"{obj_name}_Area_Diff_Abs"] = abs(curr_area - prev_area)
            else:
                all_features[frame_idx][f"{obj_name}_Area_Diff_Abs"] = None

            if curr_mask is not None and prev_mask is not None:
                curr_bin = (np.squeeze(curr_mask) > 0)
                prev_bin = (np.squeeze(prev_mask) > 0)
                if curr_bin.shape != prev_bin.shape:
                    h = min(curr_bin.shape[0], prev_bin.shape[0])
                    w = min(curr_bin.shape[1], prev_bin.shape[1])
                    curr_bin = curr_bin[:h, :w]
                    prev_bin = prev_bin[:h, :w]

                inter = np.logical_and(curr_bin, prev_bin)
                union = np.logical_or(curr_bin, prev_bin)
                denom = np.sum(union)
                all_features[frame_idx][f"{obj_name}_Mask_IoU"] = (float(np.sum(inter)) / float(denom)) if denom > 0 else None
            else:
                all_features[frame_idx][f"{obj_name}_Mask_IoU"] = None

            previous_masks[obj_name] = curr_mask

        rat_pos = (
            all_features[frame_idx].get("Rat_centroid_x"),
            all_features[frame_idx].get("Rat_centroid_y"),
        )
        nest_pos = (
            all_features[frame_idx].get("Nest_centroid_x"),
            all_features[frame_idx].get("Nest_centroid_y"),
        )
        all_features[frame_idx]["Rat_To_Nest_Distance"] = _euclidean_distance(rat_pos, nest_pos)

        prev_rat_pos = (
            all_features.get(frame_idx - 1, {}).get("Rat_centroid_x"),
            all_features.get(frame_idx - 1, {}).get("Rat_centroid_y"),
        )

        if None not in rat_pos and None not in prev_rat_pos:
            dx = float(rat_pos[0]) - float(prev_rat_pos[0])
            dy = float(rat_pos[1]) - float(prev_rat_pos[1])
            speed = (dx ** 2 + dy ** 2) ** 0.5
            direction_deg = float(np.degrees(np.arctan2(dy, dx)))
            all_features[frame_idx]["Rat_Speed_px_per_frame"] = speed
            all_features[frame_idx]["Rat_Direction_deg"] = direction_deg
        else:
            all_features[frame_idx]["Rat_Speed_px_per_frame"] = None
            all_features[frame_idx]["Rat_Direction_deg"] = None

        prev_speed = all_features.get(frame_idx - 1, {}).get("Rat_Speed_px_per_frame")
        curr_speed = all_features[frame_idx].get("Rat_Speed_px_per_frame")
        all_features[frame_idx]["Rat_Acceleration_px_per_frame2"] = (
            float(curr_speed - prev_speed) if (curr_speed is not None and prev_speed is not None) else None
        )

        prev_dist = all_features.get(frame_idx - 1, {}).get("Rat_To_Nest_Distance")
        curr_dist = all_features[frame_idx].get("Rat_To_Nest_Distance")
        all_features[frame_idx]["Rat_To_Nest_Dist_Change"] = (
            float(curr_dist - prev_dist) if (curr_dist is not None and prev_dist is not None) else None
        )

        for pname, pcoords in fixed_points.items():
            all_features[frame_idx][f"{pname}_Rat_Distance"] = _euclidean_distance(pcoords, rat_pos)
            all_features[frame_idx][f"{pname}_Nest_Distance"] = _euclidean_distance(pcoords, nest_pos)

    base = npz_file.stem
    csv_path = npz_file.with_name(f"{base}.csv")

    df = pd.DataFrame.from_dict(all_features, orient='index')
    df.index.name = 'Frame'
    df = df.sort_index().reset_index()
    df = df.ffill()
    if 'Actual_Activity' in df.columns:
        df = df.drop(columns=['Actual_Activity'])

    df.to_csv(csv_path, index=False)

    return str(csv_path)


