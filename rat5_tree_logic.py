# THIS FILE IS AUTO-GENERATED: pure if/else logic for your hierarchical classifier.
# Requires only Python + numpy/pandas at runtime (sklearn not required).
# Do not edit by hand; regenerate after retraining.

import numpy as np

# --- constants learned at training time ---
ROUTER_COLS = ["Actor_To_Nest_Distance", "Nest_bbox_h", "Nest_aspect_ratio", "Nest_bbox_y", "Nest_RT_y", "Nest_RB_y", "Nest_Dist_RT_To_Bbox_BR", "Nest_Dist_RL_To_Bbox_TL", "foodhopperMid_Rat_Distance", "foodhopperBottom_Rat_Distance", "Nest_area", "Nest_hu_1", "Nest_Dist_RR_To_Bbox_BR", "Nest_Dist_RT_RB", "Nest_Dist_RB_To_Bbox_TR", "foodhopperBottom_Nest_Distance", "Nest_Dist_RB_To_Bbox_TL", "Nest_eccentricity", "pipeEnd_Rat_Distance", "Nest_hu_6", "pipeStart_Rat_Distance", "Nest_RL_x", "Actor_bbox_y", "Actor_RT_y", "pipeMid_Rat_Distance", "pipeStart_Nest_Distance", "Nest_bbox_x", "foodhopperMid_Nest_Distance", "Nest_Dist_RR_To_Bbox_TR", "Nest_Dist_RT_RR", "Actor_centroid_x", "c2_Rat_Distance", "Nest_RT_x", "c2_Nest_Distance", "Actor_centroid_y", "Nest_RR_y", "pipeEnd_Nest_Distance", "Nest_hu_0", "Nest_RR_x", "foodhopperLeft_Nest_Distance", "c1_Rat_Distance", "foodhopperRight_Nest_Distance", "c4_Rat_Distance", "Nest_orientation", "Nest_Centroid_To_Bbox_TR", "Nest_Dist_RL_RR", "Nest_Dist_RB_RL", "Pups_Location_Rat_Distance", "Nest_Centroid_To_Bbox_TL", "Actor_RL_x", "Nest_Dist_RL_To_Bbox_TR", "c3_Rat_Distance", "c1_Nest_Distance", "Nest_Dist_RT_To_Bbox_TR", "Nest_Dist_RB_To_Bbox_BL", "Nest_Dist_RT_To_Bbox_TL", "Nest_Centroid_To_Bbox_BR", "c4_Nest_Distance", "Actor_RR_x", "Actor_RL_y", "Actor_bbox_x", "Nest_centroid_y", "Nest_Dist_RT_To_Bbox_BL", "foodhopperLeft_Rat_Distance", "Nest_Dist_RR_To_Bbox_BL", "Actor_Dist_RL_To_Bbox_TL", "pipeMid_Nest_Distance", "Nest_extent", "Nest_centroid_x", "Actor_aspect_ratio", "Nest_RL_y", "Actor_area", "c3_Nest_Distance", "Nest_Centroid_To_Bbox_BL", "Actor_Centroid_To_Bbox_BL", "Nest_RB_x", "foodhopperRight_Rat_Distance", "Actor_Dist_RB_To_Bbox_TL", "Nest_bbox_w", "Nest_Dist_RR_To_Bbox_TL", "Nest_Dist_RL_To_Bbox_BL", "Pups_Location_Nest_Distance", "Nest_Dist_RL_RT", "Actor_Centroid_To_Bbox_TL", "Nest_Dist_RR_RB", "Actor_Dist_RB_RL", "Nest_perimeter", "Nest_Dist_RL_To_Bbox_BR", "Actor_Dist_RL_To_Bbox_BR", "Actor_RT_x", "Actor_bbox_h", "Actor_hu_1", "Actor_Dist_RT_To_Bbox_BR", "Nest_hu_2", "Actor_Dist_RL_RR", "Actor_eccentricity", "Actor_RR_y", "Actor_hu_0", "Actor_Dist_RL_To_Bbox_BL", "Actor_Dist_RB_To_Bbox_TR", "Actor_RB_x", "Nest_solidity", "Actor_Dist_RB_To_Bbox_BR", "Actor_Centroid_To_Bbox_TR", "Actor_Dist_RB_To_Bbox_BL", "Actor_Dist_RR_To_Bbox_BL", "Actor_Centroid_To_Bbox_BR", "Actor_RB_y", "Actor_Dist_RR_To_Bbox_TL", "Actor_bbox_w", "Actor_perimeter", "Actor_Dist_RT_To_Bbox_BL", "Actor_Dist_RL_To_Bbox_TR", "Nest_hu_5", "Actor_solidity", "Actor_Dist_RR_To_Bbox_TR", "Actor_orientation", "Nest_hu_3", "Actor_Dist_RT_To_Bbox_TR", "Nest_Dist_RB_To_Bbox_BR", "Actor_Dist_RT_RB", "Actor_hu_3", "Actor_Dist_RT_To_Bbox_TL", "Actor_Dist_RR_To_Bbox_BR", "Actor_Dist_RR_RB", "Nest_hu_4", "Actor_hu_2", "Actor_Dist_RT_RR", "Actor_extent", "Actor_Dist_RL_RT", "Actor_Mask_IoU", "Actor_hu_5", "Nest_Mask_IoU", "Actor_Area_Diff_Abs", "Actor_Direction_deg", "Nest_Area_Diff_Abs", "Actor_To_Nest_Dist_Change", "Actor_hu_6", "Actor_hu_4"]
OENB_COLS   = ["Actor_area", "Actor_perimeter", "Actor_centroid_x", "Actor_centroid_y", "Actor_bbox_x", "Actor_bbox_y", "Actor_bbox_w", "Actor_bbox_h", "Actor_aspect_ratio", "Actor_extent", "Actor_solidity", "Actor_orientation", "Actor_eccentricity", "Actor_RL_x", "Actor_RL_y", "Actor_RR_x", "Actor_RR_y", "Actor_RT_x", "Actor_RT_y", "Actor_RB_x", "Actor_RB_y", "Actor_hu_0", "Actor_hu_1", "Actor_hu_2", "Actor_hu_3", "Actor_hu_4", "Actor_hu_5", "Actor_hu_6", "Actor_Dist_RL_RR", "Actor_Dist_RT_RB", "Actor_Dist_RL_RT", "Actor_Dist_RT_RR", "Actor_Dist_RR_RB", "Actor_Dist_RB_RL", "Actor_Centroid_To_Bbox_TL", "Actor_Centroid_To_Bbox_TR", "Actor_Centroid_To_Bbox_BR", "Actor_Centroid_To_Bbox_BL", "Actor_Dist_RL_To_Bbox_TL", "Actor_Dist_RL_To_Bbox_TR", "Actor_Dist_RL_To_Bbox_BR", "Actor_Dist_RL_To_Bbox_BL", "Actor_Dist_RR_To_Bbox_TL", "Actor_Dist_RR_To_Bbox_TR", "Actor_Dist_RR_To_Bbox_BR", "Actor_Dist_RR_To_Bbox_BL", "Actor_Dist_RT_To_Bbox_TL", "Actor_Dist_RT_To_Bbox_TR", "Actor_Dist_RT_To_Bbox_BR", "Actor_Dist_RT_To_Bbox_BL", "Actor_Dist_RB_To_Bbox_TL", "Actor_Dist_RB_To_Bbox_TR", "Actor_Dist_RB_To_Bbox_BR", "Actor_Dist_RB_To_Bbox_BL", "Nest_area", "Nest_perimeter", "Nest_centroid_x", "Nest_centroid_y", "Nest_bbox_x", "Nest_bbox_y", "Nest_bbox_w", "Nest_bbox_h", "Nest_aspect_ratio", "Nest_extent", "Nest_solidity", "Nest_orientation", "Nest_eccentricity", "Nest_RL_x", "Nest_RL_y", "Nest_RR_x", "Nest_RR_y", "Nest_RT_x", "Nest_RT_y", "Nest_RB_x", "Nest_RB_y", "Nest_hu_0", "Nest_hu_1", "Nest_hu_2", "Nest_hu_3", "Nest_hu_4", "Nest_hu_5", "Nest_hu_6", "Nest_Dist_RL_RR", "Nest_Dist_RT_RB", "Nest_Dist_RL_RT", "Nest_Dist_RT_RR", "Nest_Dist_RR_RB", "Nest_Dist_RB_RL", "Nest_Centroid_To_Bbox_TL", "Nest_Centroid_To_Bbox_TR", "Nest_Centroid_To_Bbox_BR", "Nest_Centroid_To_Bbox_BL", "Nest_Dist_RL_To_Bbox_TL", "Nest_Dist_RL_To_Bbox_TR", "Nest_Dist_RL_To_Bbox_BR", "Nest_Dist_RL_To_Bbox_BL", "Nest_Dist_RR_To_Bbox_TL", "Nest_Dist_RR_To_Bbox_TR", "Nest_Dist_RR_To_Bbox_BR", "Nest_Dist_RR_To_Bbox_BL", "Nest_Dist_RT_To_Bbox_TL", "Nest_Dist_RT_To_Bbox_TR", "Nest_Dist_RT_To_Bbox_BR", "Nest_Dist_RT_To_Bbox_BL", "Nest_Dist_RB_To_Bbox_TL", "Nest_Dist_RB_To_Bbox_TR", "Nest_Dist_RB_To_Bbox_BR", "Nest_Dist_RB_To_Bbox_BL", "Actor_Area_Diff_Abs", "Actor_Mask_IoU", "Nest_Area_Diff_Abs", "Nest_Mask_IoU", "Actor_To_Nest_Distance", "Actor_Direction_deg", "Actor_To_Nest_Dist_Change", "c1_Rat_Distance", "c1_Nest_Distance", "c2_Rat_Distance", "c2_Nest_Distance", "c3_Rat_Distance", "c3_Nest_Distance", "c4_Rat_Distance", "c4_Nest_Distance", "pipeEnd_Rat_Distance", "pipeEnd_Nest_Distance", "pipeMid_Rat_Distance", "pipeMid_Nest_Distance", "pipeStart_Rat_Distance", "pipeStart_Nest_Distance", "foodhopperBottom_Rat_Distance", "foodhopperBottom_Nest_Distance", "foodhopperLeft_Rat_Distance", "foodhopperLeft_Nest_Distance", "foodhopperRight_Rat_Distance", "foodhopperRight_Nest_Distance", "foodhopperMid_Rat_Distance", "foodhopperMid_Nest_Distance", "Pups_Location_Rat_Distance", "Pups_Location_Nest_Distance"]
RATIO_FEATURE = "Actor_aspect_ratio"
RATIO_THRESH  = 0.5588361145
RATIO_FLIP    = True

def _get(d, k):
    try:
        return float(d.get(k, float("nan")))
    except Exception:
        return float("nan")


def router_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Nest_bbox_h <= 137.5000000000
    if _get(features, "Nest_bbox_h") <= 137.5000000000:
        # if Actor_To_Nest_Distance <= 217.3423461914
        if _get(features, "Actor_To_Nest_Distance") <= 217.3423461914:
            # if Nest_Dist_RB_RL <= 327.4637298584
            if _get(features, "Nest_Dist_RB_RL") <= 327.4637298584:
                # if foodhopperRight_Nest_Distance <= 459.9259948730
                if _get(features, "foodhopperRight_Nest_Distance") <= 459.9259948730:
                    # if c4_Nest_Distance <= 958.3240661621
                    if _get(features, "c4_Nest_Distance") <= 958.3240661621:
                        # if Actor_Centroid_To_Bbox_BL <= 189.2966232300
                        if _get(features, "Actor_Centroid_To_Bbox_BL") <= 189.2966232300:
                            # if Nest_Dist_RR_To_Bbox_BR <= 10.5476179123
                            if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 10.5476179123:
                                # if Actor_RB_y <= 584.0000000000
                                if _get(features, "Actor_RB_y") <= 584.0000000000:
                                    # if Actor_RB_x <= 1141.5000000000
                                    if _get(features, "Actor_RB_x") <= 1141.5000000000:
                                        # if Actor_Dist_RL_To_Bbox_TL <= 132.5000000000
                                        if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 132.5000000000:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
                                    else:
                                        return "PI_SI"
                                else:
                                    # if Nest_Dist_RR_RB <= 57.4372787476
                                    if _get(features, "Nest_Dist_RR_RB") <= 57.4372787476:
                                        return "OENB"
                                    else:
                                        # if Nest_aspect_ratio <= 3.9533168077
                                        if _get(features, "Nest_aspect_ratio") <= 3.9533168077:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                            else:
                                # if Nest_hu_3 <= 0.0024813365
                                if _get(features, "Nest_hu_3") <= 0.0024813365:
                                    # if Nest_RT_x <= 1024.5000000000
                                    if _get(features, "Nest_RT_x") <= 1024.5000000000:
                                        # if c3_Nest_Distance <= 335.0324707031
                                        if _get(features, "c3_Nest_Distance") <= 335.0324707031:
                                            return "OENB"
                                        else:
                                            # if Actor_Dist_RR_To_Bbox_TR <= 42.5122528076
                                            if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 42.5122528076:
                                                return "OENB"
                                            else:
                                                # if Actor_Dist_RB_To_Bbox_TR <= 314.6767120361
                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 314.6767120361:
                                                    return "PI_SI"
                                                else:
                                                    # if Actor_Dist_RT_To_Bbox_BR <= 191.1833267212
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 191.1833267212:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                    else:
                                        return "OENB"
                                else:
                                    # if Actor_Dist_RR_RB <= 51.6773128510
                                    if _get(features, "Actor_Dist_RR_RB") <= 51.6773128510:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                        else:
                            # if Nest_hu_0 <= 0.6301884055
                            if _get(features, "Nest_hu_0") <= 0.6301884055:
                                # if Actor_RR_x <= 1260.5000000000
                                if _get(features, "Actor_RR_x") <= 1260.5000000000:
                                    # if Nest_Dist_RR_To_Bbox_BR <= 17.0294876099
                                    if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 17.0294876099:
                                        # if Nest_orientation <= 87.7051010132
                                        if _get(features, "Nest_orientation") <= 87.7051010132:
                                            return "PI_SI"
                                        else:
                                            # if Actor_Area_Diff_Abs <= 6728.7500000000
                                            if _get(features, "Actor_Area_Diff_Abs") <= 6728.7500000000:
                                                return "OENB"
                                            else:
                                                # if Nest_Dist_RT_To_Bbox_BL <= 180.6808395386
                                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 180.6808395386:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                    else:
                                        # if Actor_Dist_RB_To_Bbox_BR <= 87.0058250427
                                        if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 87.0058250427:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                else:
                                    # if Nest_Centroid_To_Bbox_TL <= 145.4732742310
                                    if _get(features, "Nest_Centroid_To_Bbox_TL") <= 145.4732742310:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                            else:
                                return "PI_SI"
                    else:
                        # if foodhopperBottom_Rat_Distance <= 524.8204345703
                        if _get(features, "foodhopperBottom_Rat_Distance") <= 524.8204345703:
                            # if Nest_Dist_RL_To_Bbox_TL <= 86.0000000000
                            if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 86.0000000000:
                                # if Nest_Centroid_To_Bbox_BR <= 150.7951202393
                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 150.7951202393:
                                    # if Actor_hu_2 <= 0.0018340775
                                    if _get(features, "Actor_hu_2") <= 0.0018340775:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    # if Actor_hu_1 <= 0.0002127115
                                    if _get(features, "Actor_hu_1") <= 0.0002127115:
                                        return "OENB"
                                    else:
                                        # if Actor_hu_2 <= 0.0016230445
                                        if _get(features, "Actor_hu_2") <= 0.0016230445:
                                            return "PI_SI"
                                        else:
                                            # if Nest_hu_5 <= -0.0000088500
                                            if _get(features, "Nest_hu_5") <= -0.0000088500:
                                                # if Nest_Mask_IoU <= 0.9805088639
                                                if _get(features, "Nest_Mask_IoU") <= 0.9805088639:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                            else:
                                                return "PI_SI"
                            else:
                                # if Nest_RB_x <= 1037.5000000000
                                if _get(features, "Nest_RB_x") <= 1037.5000000000:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                        else:
                            return "OENB"
                else:
                    # if Nest_hu_6 <= 0.0000373000
                    if _get(features, "Nest_hu_6") <= 0.0000373000:
                        # if Nest_Dist_RL_RT <= 10.7934918404
                        if _get(features, "Nest_Dist_RL_RT") <= 10.7934918404:
                            # if Nest_RT_x <= 766.5000000000
                            if _get(features, "Nest_RT_x") <= 766.5000000000:
                                return "OENB"
                            else:
                                # if Pups_Location_Nest_Distance <= 80.4034957886
                                if _get(features, "Pups_Location_Nest_Distance") <= 80.4034957886:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                        else:
                            # if foodhopperMid_Rat_Distance <= 443.7254180908
                            if _get(features, "foodhopperMid_Rat_Distance") <= 443.7254180908:
                                # if Actor_hu_1 <= 0.0014640950
                                if _get(features, "Actor_hu_1") <= 0.0014640950:
                                    # if Actor_Dist_RB_RL <= 96.4831237793
                                    if _get(features, "Actor_Dist_RB_RL") <= 96.4831237793:
                                        # if c1_Rat_Distance <= 1097.8311767578
                                        if _get(features, "c1_Rat_Distance") <= 1097.8311767578:
                                            # if Actor_RB_x <= 904.0000000000
                                            if _get(features, "Actor_RB_x") <= 904.0000000000:
                                                return "PI_SI"
                                            else:
                                                # if Actor_Dist_RT_To_Bbox_BR <= 234.6548995972
                                                if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 234.6548995972:
                                                    return "PI_SI"
                                                else:
                                                    # if Actor_RT_y <= 407.0000000000
                                                    if _get(features, "Actor_RT_y") <= 407.0000000000:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                        else:
                                            return "PI_SI"
                                    else:
                                        # if Actor_Mask_IoU <= 0.8728031516
                                        if _get(features, "Actor_Mask_IoU") <= 0.8728031516:
                                            # if Actor_Direction_deg <= 145.1915130615
                                            if _get(features, "Actor_Direction_deg") <= 145.1915130615:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                        else:
                                            # if Actor_Dist_RT_To_Bbox_BL <= 243.7570495605
                                            if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 243.7570495605:
                                                # if Actor_eccentricity <= 0.6448756754
                                                if _get(features, "Actor_eccentricity") <= 0.6448756754:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                            else:
                                                # if Nest_Dist_RL_To_Bbox_BL <= 39.5000000000
                                                if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 39.5000000000:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                else:
                                    # if Actor_hu_1 <= 0.0023797085
                                    if _get(features, "Actor_hu_1") <= 0.0023797085:
                                        # if c1_Rat_Distance <= 1092.2313842773
                                        if _get(features, "c1_Rat_Distance") <= 1092.2313842773:
                                            # if c2_Rat_Distance <= 612.2660217285
                                            if _get(features, "c2_Rat_Distance") <= 612.2660217285:
                                                # if Actor_bbox_y <= 427.5000000000
                                                if _get(features, "Actor_bbox_y") <= 427.5000000000:
                                                    # if pipeMid_Rat_Distance <= 464.0116729736
                                                    if _get(features, "pipeMid_Rat_Distance") <= 464.0116729736:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                                                else:
                                                    return "PI_SI"
                                            else:
                                                # if foodhopperLeft_Rat_Distance <= 635.2344665527
                                                if _get(features, "foodhopperLeft_Rat_Distance") <= 635.2344665527:
                                                    # if Actor_Mask_IoU <= 0.9790107906
                                                    if _get(features, "Actor_Mask_IoU") <= 0.9790107906:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                                else:
                                                    return "OENB"
                                        else:
                                            # if Actor_bbox_h <= 200.5000000000
                                            if _get(features, "Actor_bbox_h") <= 200.5000000000:
                                                # if Actor_Dist_RB_To_Bbox_BR <= 192.5026016235
                                                if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 192.5026016235:
                                                    # if Actor_Centroid_To_Bbox_TR <= 172.5654525757
                                                    if _get(features, "Actor_Centroid_To_Bbox_TR") <= 172.5654525757:
                                                        # if Actor_Dist_RT_To_Bbox_BL <= 235.0583572388
                                                        if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 235.0583572388:
                                                            # if Actor_Direction_deg <= -178.6737899780
                                                            if _get(features, "Actor_Direction_deg") <= -178.6737899780:
                                                                return "OENB"
                                                            else:
                                                                # if Actor_Direction_deg <= 175.8600234985
                                                                if _get(features, "Actor_Direction_deg") <= 175.8600234985:
                                                                    # if Actor_Dist_RT_To_Bbox_BR <= 242.4066848755
                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 242.4066848755:
                                                                        # if Actor_eccentricity <= 0.6971670091
                                                                        if _get(features, "Actor_eccentricity") <= 0.6971670091:
                                                                            return "PI_SI"
                                                                        else:
                                                                            # if c4_Rat_Distance <= 970.2908020020
                                                                            if _get(features, "c4_Rat_Distance") <= 970.2908020020:
                                                                                return "PI_SI"
                                                                            else:
                                                                                return "OENB"
                                                                    else:
                                                                        # if Actor_Dist_RT_To_Bbox_BR <= 242.7948989868
                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 242.7948989868:
                                                                            return "OENB"
                                                                        else:
                                                                            return "PI_SI"
                                                                else:
                                                                    return "OENB"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        return "OENB"
                                                else:
                                                    return "OENB"
                                            else:
                                                # if foodhopperBottom_Rat_Distance <= 387.7748413086
                                                if _get(features, "foodhopperBottom_Rat_Distance") <= 387.7748413086:
                                                    # if Actor_Centroid_To_Bbox_BL <= 147.7610702515
                                                    if _get(features, "Actor_Centroid_To_Bbox_BL") <= 147.7610702515:
                                                        return "OENB"
                                                    else:
                                                        # if Actor_orientation <= 74.1950988770
                                                        if _get(features, "Actor_orientation") <= 74.1950988770:
                                                            return "OENB"
                                                        else:
                                                            # if Actor_orientation <= 83.3676109314
                                                            if _get(features, "Actor_orientation") <= 83.3676109314:
                                                                # if Actor_hu_1 <= 0.0018119170
                                                                if _get(features, "Actor_hu_1") <= 0.0018119170:
                                                                    # if Actor_Direction_deg <= 7.7875871658
                                                                    if _get(features, "Actor_Direction_deg") <= 7.7875871658:
                                                                        return "OENB"
                                                                    else:
                                                                        return "PI_SI"
                                                                else:
                                                                    return "PI_SI"
                                                            else:
                                                                # if Actor_RL_y <= 543.5000000000
                                                                if _get(features, "Actor_RL_y") <= 543.5000000000:
                                                                    return "PI_SI"
                                                                else:
                                                                    return "OENB"
                                                else:
                                                    # if c4_Rat_Distance <= 982.6058044434
                                                    if _get(features, "c4_Rat_Distance") <= 982.6058044434:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                                    else:
                                        # if Actor_To_Nest_Distance <= 123.9867439270
                                        if _get(features, "Actor_To_Nest_Distance") <= 123.9867439270:
                                            # if Nest_Centroid_To_Bbox_BL <= 120.5299911499
                                            if _get(features, "Nest_Centroid_To_Bbox_BL") <= 120.5299911499:
                                                # if foodhopperMid_Rat_Distance <= 425.6952667236
                                                if _get(features, "foodhopperMid_Rat_Distance") <= 425.6952667236:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                            else:
                                                # if Actor_Dist_RR_To_Bbox_TL <= 307.0807037354
                                                if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 307.0807037354:
                                                    return "PI_SI"
                                                else:
                                                    # if pipeEnd_Rat_Distance <= 566.8040466309
                                                    if _get(features, "pipeEnd_Rat_Distance") <= 566.8040466309:
                                                        # if Actor_RR_y <= 484.5000000000
                                                        if _get(features, "Actor_RR_y") <= 484.5000000000:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        return "PI_SI"
                                        else:
                                            # if c1_Nest_Distance <= 587.6543579102
                                            if _get(features, "c1_Nest_Distance") <= 587.6543579102:
                                                # if Nest_Centroid_To_Bbox_BR <= 171.7997131348
                                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 171.7997131348:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                            else:
                                                # if Actor_RB_x <= 1150.5000000000
                                                if _get(features, "Actor_RB_x") <= 1150.5000000000:
                                                    # if Actor_Dist_RL_To_Bbox_BL <= 29.5000000000
                                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 29.5000000000:
                                                        # if foodhopperBottom_Rat_Distance <= 255.2897567749
                                                        if _get(features, "foodhopperBottom_Rat_Distance") <= 255.2897567749:
                                                            return "OENB"
                                                        else:
                                                            # if Actor_RB_x <= 1034.5000000000
                                                            if _get(features, "Actor_RB_x") <= 1034.5000000000:
                                                                # if Actor_RT_x <= 1057.5000000000
                                                                if _get(features, "Actor_RT_x") <= 1057.5000000000:
                                                                    # if Actor_area <= 20578.7500000000
                                                                    if _get(features, "Actor_area") <= 20578.7500000000:
                                                                        return "OENB"
                                                                    else:
                                                                        return "PI_SI"
                                                                else:
                                                                    return "OENB"
                                                            else:
                                                                return "OENB"
                                                    else:
                                                        # if Actor_hu_1 <= 0.1185563579
                                                        if _get(features, "Actor_hu_1") <= 0.1185563579:
                                                            # if Nest_Dist_RR_RB <= 11.4425196648
                                                            if _get(features, "Nest_Dist_RR_RB") <= 11.4425196648:
                                                                # if Actor_hu_0 <= 0.2317398116
                                                                if _get(features, "Actor_hu_0") <= 0.2317398116:
                                                                    return "OENB"
                                                                else:
                                                                    return "PI_SI"
                                                            else:
                                                                # if Actor_hu_3 <= 0.0000132500
                                                                if _get(features, "Actor_hu_3") <= 0.0000132500:
                                                                    # if Actor_Dist_RR_To_Bbox_BR <= 38.5129871368
                                                                    if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 38.5129871368:
                                                                        # if Actor_hu_1 <= 0.0184763903
                                                                        if _get(features, "Actor_hu_1") <= 0.0184763903:
                                                                            return "PI_SI"
                                                                        else:
                                                                            # if c2_Rat_Distance <= 606.2239990234
                                                                            if _get(features, "c2_Rat_Distance") <= 606.2239990234:
                                                                                # if pipeStart_Rat_Distance <= 402.9228057861
                                                                                if _get(features, "pipeStart_Rat_Distance") <= 402.9228057861:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                            else:
                                                                                return "PI_SI"
                                                                    else:
                                                                        # if Nest_Mask_IoU <= 0.8064685762
                                                                        if _get(features, "Nest_Mask_IoU") <= 0.8064685762:
                                                                            # if Actor_RL_x <= 733.5000000000
                                                                            if _get(features, "Actor_RL_x") <= 733.5000000000:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                        else:
                                                                            # if Actor_Area_Diff_Abs <= 6853.0000000000
                                                                            if _get(features, "Actor_Area_Diff_Abs") <= 6853.0000000000:
                                                                                # if Actor_eccentricity <= 0.8919133246
                                                                                if _get(features, "Actor_eccentricity") <= 0.8919133246:
                                                                                    # if Actor_area <= 22538.2500000000
                                                                                    if _get(features, "Actor_area") <= 22538.2500000000:
                                                                                        # if Actor_RL_y <= 574.0000000000
                                                                                        if _get(features, "Actor_RL_y") <= 574.0000000000:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    # if c2_Rat_Distance <= 606.3230285645
                                                                                    if _get(features, "c2_Rat_Distance") <= 606.3230285645:
                                                                                        # if Actor_Dist_RT_To_Bbox_TR <= 106.5000000000
                                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 106.5000000000:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                            else:
                                                                                # if Actor_Dist_RL_To_Bbox_TR <= 352.6542663574
                                                                                if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 352.6542663574:
                                                                                    return "PI_SI"
                                                                                else:
                                                                                    return "OENB"
                                                                else:
                                                                    # if Actor_RT_x <= 247.5000000000
                                                                    if _get(features, "Actor_RT_x") <= 247.5000000000:
                                                                        # if Nest_Dist_RR_RB <= 257.4113464355
                                                                        if _get(features, "Nest_Dist_RR_RB") <= 257.4113464355:
                                                                            return "PI_SI"
                                                                        else:
                                                                            return "OENB"
                                                                    else:
                                                                        # if Actor_Centroid_To_Bbox_BR <= 128.3674545288
                                                                        if _get(features, "Actor_Centroid_To_Bbox_BR") <= 128.3674545288:
                                                                            # if Actor_Dist_RL_To_Bbox_BL <= 68.5000000000
                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 68.5000000000:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                        else:
                                                                            # if Actor_hu_6 <= -0.0000026050
                                                                            if _get(features, "Actor_hu_6") <= -0.0000026050:
                                                                                # if Actor_bbox_y <= 383.5000000000
                                                                                if _get(features, "Actor_bbox_y") <= 383.5000000000:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                            else:
                                                                                # if Actor_eccentricity <= 0.7042044699
                                                                                if _get(features, "Actor_eccentricity") <= 0.7042044699:
                                                                                    # if Actor_eccentricity <= 0.7041812837
                                                                                    if _get(features, "Actor_eccentricity") <= 0.7041812837:
                                                                                        # if Actor_centroid_x <= 956.2054138184
                                                                                        if _get(features, "Actor_centroid_x") <= 956.2054138184:
                                                                                            # if Actor_centroid_x <= 944.7493591309
                                                                                            if _get(features, "Actor_centroid_x") <= 944.7493591309:
                                                                                                return "PI_SI"
                                                                                            else:
                                                                                                return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                                else:
                                                                                    # if Actor_centroid_y <= 551.5358276367
                                                                                    if _get(features, "Actor_centroid_y") <= 551.5358276367:
                                                                                        # if Actor_centroid_x <= 963.3227233887
                                                                                        if _get(features, "Actor_centroid_x") <= 963.3227233887:
                                                                                            # if Actor_To_Nest_Dist_Change <= -12.5646409988
                                                                                            if _get(features, "Actor_To_Nest_Dist_Change") <= -12.5646409988:
                                                                                                # if Actor_RR_x <= 1040.5000000000
                                                                                                if _get(features, "Actor_RR_x") <= 1040.5000000000:
                                                                                                    return "OENB"
                                                                                                else:
                                                                                                    return "PI_SI"
                                                                                            else:
                                                                                                # if Actor_hu_5 <= 0.0000842500
                                                                                                if _get(features, "Actor_hu_5") <= 0.0000842500:
                                                                                                    return "PI_SI"
                                                                                                else:
                                                                                                    # if foodhopperRight_Rat_Distance <= 428.6218414307
                                                                                                    if _get(features, "foodhopperRight_Rat_Distance") <= 428.6218414307:
                                                                                                        # if foodhopperRight_Rat_Distance <= 427.3877716064
                                                                                                        if _get(features, "foodhopperRight_Rat_Distance") <= 427.3877716064:
                                                                                                            return "PI_SI"
                                                                                                        else:
                                                                                                            # if c1_Rat_Distance <= 1067.1205444336
                                                                                                            if _get(features, "c1_Rat_Distance") <= 1067.1205444336:
                                                                                                                return "OENB"
                                                                                                            else:
                                                                                                                return "PI_SI"
                                                                                                    else:
                                                                                                        # if Actor_centroid_x <= 921.6277465820
                                                                                                        if _get(features, "Actor_centroid_x") <= 921.6277465820:
                                                                                                            return "OENB"
                                                                                                        else:
                                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            # if Actor_centroid_x <= 963.4056396484
                                                                                            if _get(features, "Actor_centroid_x") <= 963.4056396484:
                                                                                                return "OENB"
                                                                                            else:
                                                                                                # if Actor_RR_x <= 1098.0000000000
                                                                                                if _get(features, "Actor_RR_x") <= 1098.0000000000:
                                                                                                    # if Actor_Dist_RT_To_Bbox_BL <= 259.6922607422
                                                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 259.6922607422:
                                                                                                        return "PI_SI"
                                                                                                    else:
                                                                                                        return "OENB"
                                                                                                else:
                                                                                                    return "PI_SI"
                                                                                    else:
                                                                                        # if Actor_Mask_IoU <= 0.9745780826
                                                                                        if _get(features, "Actor_Mask_IoU") <= 0.9745780826:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                        else:
                                                            return "OENB"
                                                else:
                                                    # if Actor_Dist_RL_To_Bbox_TR <= 421.1414642334
                                                    if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 421.1414642334:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                            else:
                                # if Actor_Dist_RB_RL <= 365.2881622314
                                if _get(features, "Actor_Dist_RB_RL") <= 365.2881622314:
                                    # if Actor_Dist_RR_To_Bbox_TR <= 233.5021438599
                                    if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 233.5021438599:
                                        # if Actor_Dist_RB_To_Bbox_TR <= 173.0231170654
                                        if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 173.0231170654:
                                            # if Actor_orientation <= 82.7391433716
                                            if _get(features, "Actor_orientation") <= 82.7391433716:
                                                # if Actor_hu_5 <= 0.0000850000
                                                if _get(features, "Actor_hu_5") <= 0.0000850000:
                                                    # if Actor_hu_1 <= 0.0216775462
                                                    if _get(features, "Actor_hu_1") <= 0.0216775462:
                                                        # if c3_Rat_Distance <= 287.7378845215
                                                        if _get(features, "c3_Rat_Distance") <= 287.7378845215:
                                                            # if Actor_RT_y <= 461.5000000000
                                                            if _get(features, "Actor_RT_y") <= 461.5000000000:
                                                                # if Actor_solidity <= 0.9098249078
                                                                if _get(features, "Actor_solidity") <= 0.9098249078:
                                                                    return "OENB"
                                                                else:
                                                                    # if Actor_area <= 28943.5000000000
                                                                    if _get(features, "Actor_area") <= 28943.5000000000:
                                                                        return "OENB"
                                                                    else:
                                                                        return "PI_SI"
                                                            else:
                                                                return "PI_SI"
                                                        else:
                                                            return "PI_SI"
                                                    else:
                                                        return "OENB"
                                                else:
                                                    # if Actor_RB_y <= 607.5000000000
                                                    if _get(features, "Actor_RB_y") <= 607.5000000000:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                            else:
                                                # if Actor_Centroid_To_Bbox_TL <= 207.1580734253
                                                if _get(features, "Actor_Centroid_To_Bbox_TL") <= 207.1580734253:
                                                    # if Actor_RL_y <= 586.5000000000
                                                    if _get(features, "Actor_RL_y") <= 586.5000000000:
                                                        # if Actor_orientation <= 84.3137931824
                                                        if _get(features, "Actor_orientation") <= 84.3137931824:
                                                            # if Actor_hu_3 <= 0.0005628510
                                                            if _get(features, "Actor_hu_3") <= 0.0005628510:
                                                                # if foodhopperMid_Rat_Distance <= 488.0583953857
                                                                if _get(features, "foodhopperMid_Rat_Distance") <= 488.0583953857:
                                                                    # if Actor_Dist_RT_To_Bbox_TL <= 216.5000000000
                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 216.5000000000:
                                                                        return "OENB"
                                                                    else:
                                                                        return "PI_SI"
                                                                else:
                                                                    return "PI_SI"
                                                            else:
                                                                # if Actor_Dist_RR_To_Bbox_TL <= 333.4290466309
                                                                if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 333.4290466309:
                                                                    # if Actor_Dist_RT_To_Bbox_TR <= 77.0000000000
                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 77.0000000000:
                                                                        return "OENB"
                                                                    else:
                                                                        # if Actor_Dist_RB_To_Bbox_BR <= 40.5123443604
                                                                        if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 40.5123443604:
                                                                            # if Actor_Dist_RL_To_Bbox_TR <= 325.6431884766
                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 325.6431884766:
                                                                                return "OENB"
                                                                            else:
                                                                                # if Actor_orientation <= 82.9321861267
                                                                                if _get(features, "Actor_orientation") <= 82.9321861267:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                        else:
                                                                            return "PI_SI"
                                                                else:
                                                                    # if Actor_solidity <= 0.8757824600
                                                                    if _get(features, "Actor_solidity") <= 0.8757824600:
                                                                        return "PI_SI"
                                                                    else:
                                                                        return "OENB"
                                                        else:
                                                            # if c2_Rat_Distance <= 525.3481140137
                                                            if _get(features, "c2_Rat_Distance") <= 525.3481140137:
                                                                # if Actor_RT_x <= 1035.0000000000
                                                                if _get(features, "Actor_RT_x") <= 1035.0000000000:
                                                                    return "OENB"
                                                                else:
                                                                    return "PI_SI"
                                                            else:
                                                                # if Actor_RR_y <= 617.5000000000
                                                                if _get(features, "Actor_RR_y") <= 617.5000000000:
                                                                    # if Actor_Centroid_To_Bbox_TL <= 204.5849685669
                                                                    if _get(features, "Actor_Centroid_To_Bbox_TL") <= 204.5849685669:
                                                                        # if Actor_Dist_RL_To_Bbox_BL <= 105.0000000000
                                                                        if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 105.0000000000:
                                                                            # if Actor_Area_Diff_Abs <= 7965.0000000000
                                                                            if _get(features, "Actor_Area_Diff_Abs") <= 7965.0000000000:
                                                                                return "PI_SI"
                                                                            else:
                                                                                # if c3_Rat_Distance <= 277.7404632568
                                                                                if _get(features, "c3_Rat_Distance") <= 277.7404632568:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                        else:
                                                                            # if Actor_hu_3 <= 0.0000479000
                                                                            if _get(features, "Actor_hu_3") <= 0.0000479000:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                    else:
                                                                        # if Actor_eccentricity <= 0.9083690047
                                                                        if _get(features, "Actor_eccentricity") <= 0.9083690047:
                                                                            return "PI_SI"
                                                                        else:
                                                                            # if Actor_Dist_RR_To_Bbox_TR <= 105.0048141479
                                                                            if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 105.0048141479:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                else:
                                                                    return "OENB"
                                                    else:
                                                        # if Actor_RT_x <= 1053.5000000000
                                                        if _get(features, "Actor_RT_x") <= 1053.5000000000:
                                                            # if Actor_Dist_RR_RB <= 53.1506099701
                                                            if _get(features, "Actor_Dist_RR_RB") <= 53.1506099701:
                                                                return "OENB"
                                                            else:
                                                                return "PI_SI"
                                                        else:
                                                            # if Actor_Centroid_To_Bbox_TL <= 172.2600860596
                                                            if _get(features, "Actor_Centroid_To_Bbox_TL") <= 172.2600860596:
                                                                return "PI_SI"
                                                            else:
                                                                return "OENB"
                                                else:
                                                    # if Actor_Dist_RL_To_Bbox_BR <= 322.7436981201
                                                    if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 322.7436981201:
                                                        # if c1_Rat_Distance <= 1150.2153930664
                                                        if _get(features, "c1_Rat_Distance") <= 1150.2153930664:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        # if Actor_centroid_x <= 1050.7406616211
                                                        if _get(features, "Actor_centroid_x") <= 1050.7406616211:
                                                            return "OENB"
                                                        else:
                                                            return "PI_SI"
                                        else:
                                            # if Nest_Mask_IoU <= 0.8169920146
                                            if _get(features, "Nest_Mask_IoU") <= 0.8169920146:
                                                # if Actor_bbox_h <= 249.5000000000
                                                if _get(features, "Actor_bbox_h") <= 249.5000000000:
                                                    # if Nest_solidity <= 0.5563362539
                                                    if _get(features, "Nest_solidity") <= 0.5563362539:
                                                        # if Nest_area <= 9248.7500000000
                                                        if _get(features, "Nest_area") <= 9248.7500000000:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        # if pipeStart_Rat_Distance <= 343.4961395264
                                                        if _get(features, "pipeStart_Rat_Distance") <= 343.4961395264:
                                                            return "OENB"
                                                        else:
                                                            # if Actor_Dist_RT_To_Bbox_TL <= 200.5000000000
                                                            if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 200.5000000000:
                                                                # if Nest_Mask_IoU <= 0.8168281913
                                                                if _get(features, "Nest_Mask_IoU") <= 0.8168281913:
                                                                    # if Nest_hu_1 <= 0.0005138415
                                                                    if _get(features, "Nest_hu_1") <= 0.0005138415:
                                                                        # if Actor_RB_y <= 609.0000000000
                                                                        if _get(features, "Actor_RB_y") <= 609.0000000000:
                                                                            return "OENB"
                                                                        else:
                                                                            return "PI_SI"
                                                                    else:
                                                                        # if Actor_To_Nest_Dist_Change <= -70.9096298218
                                                                        if _get(features, "Actor_To_Nest_Dist_Change") <= -70.9096298218:
                                                                            # if Actor_Dist_RR_To_Bbox_BR <= 72.0070304871
                                                                            if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 72.0070304871:
                                                                                return "PI_SI"
                                                                            else:
                                                                                return "OENB"
                                                                        else:
                                                                            return "PI_SI"
                                                                else:
                                                                    return "OENB"
                                                            else:
                                                                # if foodhopperRight_Nest_Distance <= 492.3339385986
                                                                if _get(features, "foodhopperRight_Nest_Distance") <= 492.3339385986:
                                                                    # if Nest_RB_y <= 628.0000000000
                                                                    if _get(features, "Nest_RB_y") <= 628.0000000000:
                                                                        # if Actor_bbox_x <= 828.0000000000
                                                                        if _get(features, "Actor_bbox_x") <= 828.0000000000:
                                                                            return "OENB"
                                                                        else:
                                                                            return "PI_SI"
                                                                    else:
                                                                        # if Nest_Dist_RT_To_Bbox_BL <= 143.2380523682
                                                                        if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 143.2380523682:
                                                                            return "OENB"
                                                                        else:
                                                                            return "PI_SI"
                                                                else:
                                                                    # if Nest_hu_0 <= 1.3253242970
                                                                    if _get(features, "Nest_hu_0") <= 1.3253242970:
                                                                        return "PI_SI"
                                                                    else:
                                                                        return "OENB"
                                                else:
                                                    # if Nest_Dist_RL_To_Bbox_BL <= 32.5000000000
                                                    if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 32.5000000000:
                                                        # if Actor_Centroid_To_Bbox_BR <= 227.7317199707
                                                        if _get(features, "Actor_Centroid_To_Bbox_BR") <= 227.7317199707:
                                                            # if Nest_RR_y <= 577.0000000000
                                                            if _get(features, "Nest_RR_y") <= 577.0000000000:
                                                                return "OENB"
                                                            else:
                                                                return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        # if Actor_Dist_RT_To_Bbox_TR <= 182.5000000000
                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 182.5000000000:
                                                            return "OENB"
                                                        else:
                                                            # if Actor_Centroid_To_Bbox_TL <= 218.0382766724
                                                            if _get(features, "Actor_Centroid_To_Bbox_TL") <= 218.0382766724:
                                                                return "PI_SI"
                                                            else:
                                                                return "OENB"
                                            else:
                                                # if Nest_orientation <= 154.4545364380
                                                if _get(features, "Nest_orientation") <= 154.4545364380:
                                                    # if Actor_Dist_RR_To_Bbox_TL <= 465.1257476807
                                                    if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 465.1257476807:
                                                        # if Nest_Dist_RT_To_Bbox_TR <= 423.0000000000
                                                        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 423.0000000000:
                                                            # if Actor_Dist_RB_To_Bbox_BL <= 187.5026626587
                                                            if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 187.5026626587:
                                                                # if Nest_solidity <= 0.5631156862
                                                                if _get(features, "Nest_solidity") <= 0.5631156862:
                                                                    return "OENB"
                                                                else:
                                                                    # if Actor_centroid_y <= 477.7134246826
                                                                    if _get(features, "Actor_centroid_y") <= 477.7134246826:
                                                                        # if Nest_Centroid_To_Bbox_BR <= 149.6446228027
                                                                        if _get(features, "Nest_Centroid_To_Bbox_BR") <= 149.6446228027:
                                                                            # if Actor_Dist_RL_RT <= 216.6266632080
                                                                            if _get(features, "Actor_Dist_RL_RT") <= 216.6266632080:
                                                                                # if Nest_Area_Diff_Abs <= 35.7500000000
                                                                                if _get(features, "Nest_Area_Diff_Abs") <= 35.7500000000:
                                                                                    # if Nest_centroid_y <= 576.7919311523
                                                                                    if _get(features, "Nest_centroid_y") <= 576.7919311523:
                                                                                        return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    # if Actor_aspect_ratio <= 1.2229729891
                                                                                    if _get(features, "Actor_aspect_ratio") <= 1.2229729891:
                                                                                        # if Actor_Dist_RT_RB <= 231.7143936157
                                                                                        if _get(features, "Actor_Dist_RT_RB") <= 231.7143936157:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                            else:
                                                                                # if Nest_Dist_RB_To_Bbox_TR <= 166.6878852844
                                                                                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 166.6878852844:
                                                                                    return "PI_SI"
                                                                                else:
                                                                                    return "OENB"
                                                                        else:
                                                                            # if Nest_Dist_RL_RT <= 330.9785003662
                                                                            if _get(features, "Nest_Dist_RL_RT") <= 330.9785003662:
                                                                                # if Nest_bbox_h <= 98.5000000000
                                                                                if _get(features, "Nest_bbox_h") <= 98.5000000000:
                                                                                    return "OENB"
                                                                                else:
                                                                                    # if Actor_Dist_RT_To_Bbox_TL <= 106.5000000000
                                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 106.5000000000:
                                                                                        # if Actor_RT_x <= 213.0000000000
                                                                                        if _get(features, "Actor_RT_x") <= 213.0000000000:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            # if Actor_aspect_ratio <= 1.7167948484
                                                                                            if _get(features, "Actor_aspect_ratio") <= 1.7167948484:
                                                                                                # if Actor_RT_x <= 1100.0000000000
                                                                                                if _get(features, "Actor_RT_x") <= 1100.0000000000:
                                                                                                    return "PI_SI"
                                                                                                else:
                                                                                                    return "OENB"
                                                                                            else:
                                                                                                return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                            else:
                                                                                # if Nest_Centroid_To_Bbox_BR <= 160.6124649048
                                                                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 160.6124649048:
                                                                                    return "PI_SI"
                                                                                else:
                                                                                    # if Nest_centroid_y <= 571.6618957520
                                                                                    if _get(features, "Nest_centroid_y") <= 571.6618957520:
                                                                                        # if Nest_Dist_RT_To_Bbox_TL <= 325.5000000000
                                                                                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 325.5000000000:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                    else:
                                                                        # if Nest_area <= 26402.5000000000
                                                                        if _get(features, "Nest_area") <= 26402.5000000000:
                                                                            # if Actor_hu_0 <= 0.1610492319
                                                                            if _get(features, "Actor_hu_0") <= 0.1610492319:
                                                                                return "OENB"
                                                                            else:
                                                                                # if Actor_perimeter <= 1662.0012207031
                                                                                if _get(features, "Actor_perimeter") <= 1662.0012207031:
                                                                                    # if Actor_RB_y <= 547.5000000000
                                                                                    if _get(features, "Actor_RB_y") <= 547.5000000000:
                                                                                        # if Nest_RT_x <= 622.0000000000
                                                                                        if _get(features, "Nest_RT_x") <= 622.0000000000:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                    else:
                                                                                        # if foodhopperRight_Nest_Distance <= 948.3886413574
                                                                                        if _get(features, "foodhopperRight_Nest_Distance") <= 948.3886413574:
                                                                                            # if Nest_RR_y <= 633.5000000000
                                                                                            if _get(features, "Nest_RR_y") <= 633.5000000000:
                                                                                                # if Nest_area <= 26074.7500000000
                                                                                                if _get(features, "Nest_area") <= 26074.7500000000:
                                                                                                    # if Actor_Dist_RR_RB <= 116.0280151367
                                                                                                    if _get(features, "Actor_Dist_RR_RB") <= 116.0280151367:
                                                                                                        # if c2_Rat_Distance <= 586.2542724609
                                                                                                        if _get(features, "c2_Rat_Distance") <= 586.2542724609:
                                                                                                            # if foodhopperRight_Nest_Distance <= 461.3366699219
                                                                                                            if _get(features, "foodhopperRight_Nest_Distance") <= 461.3366699219:
                                                                                                                return "OENB"
                                                                                                            else:
                                                                                                                # if Actor_Dist_RR_RB <= 115.9956893921
                                                                                                                if _get(features, "Actor_Dist_RR_RB") <= 115.9956893921:
                                                                                                                    # if Actor_Dist_RR_To_Bbox_BR <= 93.0053787231
                                                                                                                    if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 93.0053787231:
                                                                                                                        return "PI_SI"
                                                                                                                    else:
                                                                                                                        # if pipeMid_Rat_Distance <= 531.5817871094
                                                                                                                        if _get(features, "pipeMid_Rat_Distance") <= 531.5817871094:
                                                                                                                            return "OENB"
                                                                                                                        else:
                                                                                                                            return "PI_SI"
                                                                                                                else:
                                                                                                                    return "OENB"
                                                                                                        else:
                                                                                                            # if Actor_Dist_RT_RB <= 196.4545974731
                                                                                                            if _get(features, "Actor_Dist_RT_RB") <= 196.4545974731:
                                                                                                                # if Actor_RB_x <= 1036.0000000000
                                                                                                                if _get(features, "Actor_RB_x") <= 1036.0000000000:
                                                                                                                    # if Nest_Dist_RL_RR <= 283.0541915894
                                                                                                                    if _get(features, "Nest_Dist_RL_RR") <= 283.0541915894:
                                                                                                                        return "PI_SI"
                                                                                                                    else:
                                                                                                                        return "OENB"
                                                                                                                else:
                                                                                                                    return "PI_SI"
                                                                                                            else:
                                                                                                                return "OENB"
                                                                                                    else:
                                                                                                        # if Actor_Dist_RR_To_Bbox_TR <= 228.0021896362
                                                                                                        if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 228.0021896362:
                                                                                                            # if Actor_Dist_RB_To_Bbox_TL <= 331.9506835938
                                                                                                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 331.9506835938:
                                                                                                                # if Nest_Dist_RT_RB <= 76.9837532043
                                                                                                                if _get(features, "Nest_Dist_RT_RB") <= 76.9837532043:
                                                                                                                    # if Nest_aspect_ratio <= 9.1447372437
                                                                                                                    if _get(features, "Nest_aspect_ratio") <= 9.1447372437:
                                                                                                                        # if Actor_Direction_deg <= -173.0363845825
                                                                                                                        if _get(features, "Actor_Direction_deg") <= -173.0363845825:
                                                                                                                            # if Actor_Mask_IoU <= 0.9750589430
                                                                                                                            if _get(features, "Actor_Mask_IoU") <= 0.9750589430:
                                                                                                                                return "PI_SI"
                                                                                                                            else:
                                                                                                                                return "OENB"
                                                                                                                        else:
                                                                                                                            return "PI_SI"
                                                                                                                    else:
                                                                                                                        # if Actor_Dist_RT_To_Bbox_BR <= 279.8397674561
                                                                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 279.8397674561:
                                                                                                                            return "PI_SI"
                                                                                                                        else:
                                                                                                                            return "OENB"
                                                                                                                else:
                                                                                                                    # if Actor_Dist_RR_To_Bbox_TR <= 223.5022354126
                                                                                                                    if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 223.5022354126:
                                                                                                                        # if Nest_solidity <= 0.9369860888
                                                                                                                        if _get(features, "Nest_solidity") <= 0.9369860888:
                                                                                                                            # if Actor_Area_Diff_Abs <= 8895.7500000000
                                                                                                                            if _get(features, "Actor_Area_Diff_Abs") <= 8895.7500000000:
                                                                                                                                # if Actor_centroid_y <= 478.3236999512
                                                                                                                                if _get(features, "Actor_centroid_y") <= 478.3236999512:
                                                                                                                                    # if Actor_centroid_y <= 478.3230133057
                                                                                                                                    if _get(features, "Actor_centroid_y") <= 478.3230133057:
                                                                                                                                        return "PI_SI"
                                                                                                                                    else:
                                                                                                                                        return "OENB"
                                                                                                                                else:
                                                                                                                                    # if Actor_RR_y <= 608.5000000000
                                                                                                                                    if _get(features, "Actor_RR_y") <= 608.5000000000:
                                                                                                                                        # if Actor_Centroid_To_Bbox_BR <= 150.6057052612
                                                                                                                                        if _get(features, "Actor_Centroid_To_Bbox_BR") <= 150.6057052612:
                                                                                                                                            # if Actor_Dist_RL_To_Bbox_TR <= 331.0585479736
                                                                                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 331.0585479736:
                                                                                                                                                # if Actor_Dist_RB_To_Bbox_BR <= 97.5051307678
                                                                                                                                                if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 97.5051307678:
                                                                                                                                                    # if Actor_Dist_RB_RL <= 145.4627227783
                                                                                                                                                    if _get(features, "Actor_Dist_RB_RL") <= 145.4627227783:
                                                                                                                                                        # if Actor_Centroid_To_Bbox_BR <= 146.1643447876
                                                                                                                                                        if _get(features, "Actor_Centroid_To_Bbox_BR") <= 146.1643447876:
                                                                                                                                                            return "PI_SI"
                                                                                                                                                        else:
                                                                                                                                                            return "OENB"
                                                                                                                                                    else:
                                                                                                                                                        return "PI_SI"
                                                                                                                                                else:
                                                                                                                                                    return "PI_SI"
                                                                                                                                            else:
                                                                                                                                                return "OENB"
                                                                                                                                        else:
                                                                                                                                            return "PI_SI"
                                                                                                                                    else:
                                                                                                                                        # if Actor_Dist_RT_RR <= 193.9276657104
                                                                                                                                        if _get(features, "Actor_Dist_RT_RR") <= 193.9276657104:
                                                                                                                                            return "OENB"
                                                                                                                                        else:
                                                                                                                                            return "PI_SI"
                                                                                                                            else:
                                                                                                                                # if Actor_Direction_deg <= -165.3641281128
                                                                                                                                if _get(features, "Actor_Direction_deg") <= -165.3641281128:
                                                                                                                                    return "OENB"
                                                                                                                                else:
                                                                                                                                    return "PI_SI"
                                                                                                                        else:
                                                                                                                            # if Nest_bbox_w <= 211.0000000000
                                                                                                                            if _get(features, "Nest_bbox_w") <= 211.0000000000:
                                                                                                                                return "PI_SI"
                                                                                                                            else:
                                                                                                                                return "OENB"
                                                                                                                    else:
                                                                                                                        # if Nest_Dist_RT_To_Bbox_BL <= 92.9458732605
                                                                                                                        if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 92.9458732605:
                                                                                                                            return "OENB"
                                                                                                                        else:
                                                                                                                            return "PI_SI"
                                                                                                            else:
                                                                                                                # if Nest_RL_x <= 797.0000000000
                                                                                                                if _get(features, "Nest_RL_x") <= 797.0000000000:
                                                                                                                    return "PI_SI"
                                                                                                                else:
                                                                                                                    return "OENB"
                                                                                                        else:
                                                                                                            # if foodhopperLeft_Nest_Distance <= 622.2589416504
                                                                                                            if _get(features, "foodhopperLeft_Nest_Distance") <= 622.2589416504:
                                                                                                                return "PI_SI"
                                                                                                            else:
                                                                                                                return "OENB"
                                                                                                else:
                                                                                                    # if Actor_Dist_RB_To_Bbox_TL <= 263.5583343506
                                                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 263.5583343506:
                                                                                                        return "PI_SI"
                                                                                                    else:
                                                                                                        # if Pups_Location_Rat_Distance <= 114.8335037231
                                                                                                        if _get(features, "Pups_Location_Rat_Distance") <= 114.8335037231:
                                                                                                            # if Pups_Location_Rat_Distance <= 113.0457458496
                                                                                                            if _get(features, "Pups_Location_Rat_Distance") <= 113.0457458496:
                                                                                                                return "PI_SI"
                                                                                                            else:
                                                                                                                return "OENB"
                                                                                                        else:
                                                                                                            return "PI_SI"
                                                                                            else:
                                                                                                # if Nest_hu_1 <= 0.1045668311
                                                                                                if _get(features, "Nest_hu_1") <= 0.1045668311:
                                                                                                    return "OENB"
                                                                                                else:
                                                                                                    return "PI_SI"
                                                                                        else:
                                                                                            # if Nest_Dist_RL_To_Bbox_BL <= 55.0000000000
                                                                                            if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 55.0000000000:
                                                                                                return "PI_SI"
                                                                                            else:
                                                                                                # if Nest_hu_5 <= 0.0002919388
                                                                                                if _get(features, "Nest_hu_5") <= 0.0002919388:
                                                                                                    return "PI_SI"
                                                                                                else:
                                                                                                    return "OENB"
                                                                                else:
                                                                                    return "OENB"
                                                                        else:
                                                                            # if Nest_centroid_y <= 582.3794555664
                                                                            if _get(features, "Nest_centroid_y") <= 582.3794555664:
                                                                                return "PI_SI"
                                                                            else:
                                                                                # if Actor_To_Nest_Distance <= 135.9330863953
                                                                                if _get(features, "Actor_To_Nest_Distance") <= 135.9330863953:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                            else:
                                                                # if Actor_Dist_RB_To_Bbox_TL <= 304.4191131592
                                                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 304.4191131592:
                                                                    # if Actor_hu_0 <= 0.1679250747
                                                                    if _get(features, "Actor_hu_0") <= 0.1679250747:
                                                                        # if Actor_extent <= 0.7489563823
                                                                        if _get(features, "Actor_extent") <= 0.7489563823:
                                                                            # if Actor_Dist_RL_To_Bbox_BR <= 278.5775604248
                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 278.5775604248:
                                                                                # if c3_Rat_Distance <= 284.2127685547
                                                                                if _get(features, "c3_Rat_Distance") <= 284.2127685547:
                                                                                    # if Actor_Dist_RT_To_Bbox_BR <= 271.4709625244
                                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 271.4709625244:
                                                                                        # if Actor_Area_Diff_Abs <= 1324.0000000000
                                                                                        if _get(features, "Actor_Area_Diff_Abs") <= 1324.0000000000:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                    else:
                                                                                        # if c3_Rat_Distance <= 278.9028625488
                                                                                        if _get(features, "c3_Rat_Distance") <= 278.9028625488:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            # if c4_Rat_Distance <= 1058.1952514648
                                                                                            if _get(features, "c4_Rat_Distance") <= 1058.1952514648:
                                                                                                return "PI_SI"
                                                                                            else:
                                                                                                return "OENB"
                                                                                else:
                                                                                    return "OENB"
                                                                            else:
                                                                                # if pipeMid_Rat_Distance <= 543.9030761719
                                                                                if _get(features, "pipeMid_Rat_Distance") <= 543.9030761719:
                                                                                    # if Actor_Dist_RL_RR <= 257.3507232666
                                                                                    if _get(features, "Actor_Dist_RL_RR") <= 257.3507232666:
                                                                                        return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    # if Actor_hu_1 <= 0.0009862635
                                                                                    if _get(features, "Actor_hu_1") <= 0.0009862635:
                                                                                        # if Actor_RT_y <= 397.5000000000
                                                                                        if _get(features, "Actor_RT_y") <= 397.5000000000:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                    else:
                                                                                        return "OENB"
                                                                        else:
                                                                            # if Actor_hu_2 <= 0.0003873355
                                                                            if _get(features, "Actor_hu_2") <= 0.0003873355:
                                                                                # if Actor_Dist_RT_RB <= 229.5518264771
                                                                                if _get(features, "Actor_Dist_RT_RB") <= 229.5518264771:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                            else:
                                                                                return "OENB"
                                                                    else:
                                                                        # if Actor_hu_1 <= 0.0292048287
                                                                        if _get(features, "Actor_hu_1") <= 0.0292048287:
                                                                            # if c2_Rat_Distance <= 598.9412536621
                                                                            if _get(features, "c2_Rat_Distance") <= 598.9412536621:
                                                                                # if Actor_RB_x <= 1123.0000000000
                                                                                if _get(features, "Actor_RB_x") <= 1123.0000000000:
                                                                                    # if Actor_RT_y <= 397.5000000000
                                                                                    if _get(features, "Actor_RT_y") <= 397.5000000000:
                                                                                        # if Actor_bbox_y <= 395.5000000000
                                                                                        if _get(features, "Actor_bbox_y") <= 395.5000000000:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            # if Actor_Dist_RT_RB <= 242.8682708740
                                                                                            if _get(features, "Actor_Dist_RT_RB") <= 242.8682708740:
                                                                                                # if Actor_Dist_RL_To_Bbox_BR <= 261.9632568359
                                                                                                if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 261.9632568359:
                                                                                                    return "PI_SI"
                                                                                                else:
                                                                                                    return "OENB"
                                                                                            else:
                                                                                                return "PI_SI"
                                                                                    else:
                                                                                        # if Actor_Dist_RB_To_Bbox_BR <= 142.5035095215
                                                                                        if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 142.5035095215:
                                                                                            # if Actor_centroid_y <= 514.3244934082
                                                                                            if _get(features, "Actor_centroid_y") <= 514.3244934082:
                                                                                                # if Actor_Dist_RR_RB <= 71.8034515381
                                                                                                if _get(features, "Actor_Dist_RR_RB") <= 71.8034515381:
                                                                                                    # if pipeStart_Rat_Distance <= 497.8735046387
                                                                                                    if _get(features, "pipeStart_Rat_Distance") <= 497.8735046387:
                                                                                                        return "OENB"
                                                                                                    else:
                                                                                                        return "PI_SI"
                                                                                                else:
                                                                                                    # if Actor_Dist_RR_To_Bbox_BR <= 88.5056495667
                                                                                                    if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 88.5056495667:
                                                                                                        # if foodhopperRight_Rat_Distance <= 390.7379608154
                                                                                                        if _get(features, "foodhopperRight_Rat_Distance") <= 390.7379608154:
                                                                                                            # if Actor_hu_1 <= 0.0029971460
                                                                                                            if _get(features, "Actor_hu_1") <= 0.0029971460:
                                                                                                                return "OENB"
                                                                                                            else:
                                                                                                                return "PI_SI"
                                                                                                        else:
                                                                                                            return "PI_SI"
                                                                                                    else:
                                                                                                        return "OENB"
                                                                                            else:
                                                                                                # if Actor_hu_1 <= 0.0263047218
                                                                                                if _get(features, "Actor_hu_1") <= 0.0263047218:
                                                                                                    # if Actor_Dist_RB_To_Bbox_BR <= 135.5036926270
                                                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 135.5036926270:
                                                                                                        return "PI_SI"
                                                                                                    else:
                                                                                                        # if Actor_Dist_RT_RB <= 162.3603668213
                                                                                                        if _get(features, "Actor_Dist_RT_RB") <= 162.3603668213:
                                                                                                            return "OENB"
                                                                                                        else:
                                                                                                            return "PI_SI"
                                                                                                else:
                                                                                                    # if Actor_Dist_RT_To_Bbox_BL <= 267.5185546875
                                                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 267.5185546875:
                                                                                                        return "OENB"
                                                                                                    else:
                                                                                                        return "PI_SI"
                                                                                        else:
                                                                                            # if Actor_Dist_RT_To_Bbox_BL <= 266.2370605469
                                                                                            if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 266.2370605469:
                                                                                                return "OENB"
                                                                                            else:
                                                                                                return "PI_SI"
                                                                                else:
                                                                                    # if Actor_solidity <= 0.9489347637
                                                                                    if _get(features, "Actor_solidity") <= 0.9489347637:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        # if Actor_Dist_RT_RB <= 237.8339767456
                                                                                        if _get(features, "Actor_Dist_RT_RB") <= 237.8339767456:
                                                                                            # if Actor_RR_x <= 1186.5000000000
                                                                                            if _get(features, "Actor_RR_x") <= 1186.5000000000:
                                                                                                return "OENB"
                                                                                            else:
                                                                                                return "PI_SI"
                                                                                        else:
                                                                                            # if Actor_Direction_deg <= 114.8981742859
                                                                                            if _get(features, "Actor_Direction_deg") <= 114.8981742859:
                                                                                                return "OENB"
                                                                                            else:
                                                                                                return "PI_SI"
                                                                            else:
                                                                                # if Actor_Dist_RT_RB <= 171.2644119263
                                                                                if _get(features, "Actor_Dist_RT_RB") <= 171.2644119263:
                                                                                    # if foodhopperMid_Rat_Distance <= 490.2149047852
                                                                                    if _get(features, "foodhopperMid_Rat_Distance") <= 490.2149047852:
                                                                                        # if Actor_Dist_RT_To_Bbox_TL <= 216.5000000000
                                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 216.5000000000:
                                                                                            # if foodhopperMid_Rat_Distance <= 490.0243530273
                                                                                            if _get(features, "foodhopperMid_Rat_Distance") <= 490.0243530273:
                                                                                                return "PI_SI"
                                                                                            else:
                                                                                                return "OENB"
                                                                                        else:
                                                                                            # if Actor_Dist_RT_To_Bbox_BL <= 283.7080383301
                                                                                            if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 283.7080383301:
                                                                                                return "OENB"
                                                                                            else:
                                                                                                return "PI_SI"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    # if foodhopperLeft_Rat_Distance <= 689.7435302734
                                                                                    if _get(features, "foodhopperLeft_Rat_Distance") <= 689.7435302734:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        # if Actor_hu_1 <= 0.0120721729
                                                                                        if _get(features, "Actor_hu_1") <= 0.0120721729:
                                                                                            # if foodhopperBottom_Rat_Distance <= 447.5696411133
                                                                                            if _get(features, "foodhopperBottom_Rat_Distance") <= 447.5696411133:
                                                                                                return "PI_SI"
                                                                                            else:
                                                                                                return "OENB"
                                                                                        else:
                                                                                            # if Actor_Dist_RB_To_Bbox_TL <= 257.1166687012
                                                                                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 257.1166687012:
                                                                                                return "PI_SI"
                                                                                            else:
                                                                                                return "OENB"
                                                                        else:
                                                                            # if Actor_hu_3 <= 0.0007837780
                                                                            if _get(features, "Actor_hu_3") <= 0.0007837780:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                else:
                                                                    # if Actor_RT_x <= 269.0000000000
                                                                    if _get(features, "Actor_RT_x") <= 269.0000000000:
                                                                        # if Nest_RT_x <= 495.5000000000
                                                                        if _get(features, "Nest_RT_x") <= 495.5000000000:
                                                                            return "PI_SI"
                                                                        else:
                                                                            return "OENB"
                                                                    else:
                                                                        # if Nest_Dist_RT_To_Bbox_TR <= 350.0000000000
                                                                        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 350.0000000000:
                                                                            # if Actor_Dist_RL_To_Bbox_TL <= 209.5000000000
                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 209.5000000000:
                                                                                # if Actor_centroid_y <= 466.5294952393
                                                                                if _get(features, "Actor_centroid_y") <= 466.5294952393:
                                                                                    return "OENB"
                                                                                else:
                                                                                    # if Nest_solidity <= 0.8076772392
                                                                                    if _get(features, "Nest_solidity") <= 0.8076772392:
                                                                                        # if Nest_bbox_w <= 469.0000000000
                                                                                        if _get(features, "Nest_bbox_w") <= 469.0000000000:
                                                                                            # if Actor_Dist_RL_To_Bbox_BR <= 265.9990692139
                                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 265.9990692139:
                                                                                                # if Actor_centroid_x <= 1051.1577148438
                                                                                                if _get(features, "Actor_centroid_x") <= 1051.1577148438:
                                                                                                    return "OENB"
                                                                                                else:
                                                                                                    return "PI_SI"
                                                                                            else:
                                                                                                # if Actor_Dist_RB_To_Bbox_TL <= 305.0024566650
                                                                                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 305.0024566650:
                                                                                                    # if Actor_Centroid_To_Bbox_BL <= 171.0182037354
                                                                                                    if _get(features, "Actor_Centroid_To_Bbox_BL") <= 171.0182037354:
                                                                                                        # if Actor_Dist_RT_RR <= 197.3617324829
                                                                                                        if _get(features, "Actor_Dist_RT_RR") <= 197.3617324829:
                                                                                                            return "PI_SI"
                                                                                                        else:
                                                                                                            return "OENB"
                                                                                                    else:
                                                                                                        return "PI_SI"
                                                                                                else:
                                                                                                    # if Actor_Dist_RB_To_Bbox_TL <= 306.5044860840
                                                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 306.5044860840:
                                                                                                        # if Actor_Dist_RB_To_Bbox_TL <= 306.4579925537
                                                                                                        if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 306.4579925537:
                                                                                                            # if Actor_Dist_RR_To_Bbox_TL <= 293.4518737793
                                                                                                            if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 293.4518737793:
                                                                                                                # if Actor_RT_x <= 1036.0000000000
                                                                                                                if _get(features, "Actor_RT_x") <= 1036.0000000000:
                                                                                                                    return "OENB"
                                                                                                                else:
                                                                                                                    return "PI_SI"
                                                                                                            else:
                                                                                                                return "PI_SI"
                                                                                                        else:
                                                                                                            # if Actor_perimeter <= 875.4858703613
                                                                                                            if _get(features, "Actor_perimeter") <= 875.4858703613:
                                                                                                                return "PI_SI"
                                                                                                            else:
                                                                                                                return "OENB"
                                                                                                    else:
                                                                                                        # if Actor_Dist_RB_To_Bbox_TL <= 308.3228759766
                                                                                                        if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 308.3228759766:
                                                                                                            # if Actor_Dist_RB_To_Bbox_TL <= 308.2296142578
                                                                                                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 308.2296142578:
                                                                                                                return "PI_SI"
                                                                                                            else:
                                                                                                                # if pipeMid_Rat_Distance <= 547.8054504395
                                                                                                                if _get(features, "pipeMid_Rat_Distance") <= 547.8054504395:
                                                                                                                    return "PI_SI"
                                                                                                                else:
                                                                                                                    return "OENB"
                                                                                                        else:
                                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                    else:
                                                                                        # if Actor_Dist_RT_RB <= 288.1473693848
                                                                                        if _get(features, "Actor_Dist_RT_RB") <= 288.1473693848:
                                                                                            # if Actor_hu_2 <= 0.0002485290
                                                                                            if _get(features, "Actor_hu_2") <= 0.0002485290:
                                                                                                # if Nest_RR_y <= 616.5000000000
                                                                                                if _get(features, "Nest_RR_y") <= 616.5000000000:
                                                                                                    # if Nest_solidity <= 0.8100128472
                                                                                                    if _get(features, "Nest_solidity") <= 0.8100128472:
                                                                                                        return "OENB"
                                                                                                    else:
                                                                                                        # if Actor_hu_2 <= 0.0002456070
                                                                                                        if _get(features, "Actor_hu_2") <= 0.0002456070:
                                                                                                            # if Actor_Mask_IoU <= 0.9885175824
                                                                                                            if _get(features, "Actor_Mask_IoU") <= 0.9885175824:
                                                                                                                # if Actor_hu_3 <= 0.0000185000
                                                                                                                if _get(features, "Actor_hu_3") <= 0.0000185000:
                                                                                                                    # if Nest_hu_3 <= 0.0000042200
                                                                                                                    if _get(features, "Nest_hu_3") <= 0.0000042200:
                                                                                                                        # if Actor_Dist_RL_RR <= 296.4203186035
                                                                                                                        if _get(features, "Actor_Dist_RL_RR") <= 296.4203186035:
                                                                                                                            return "PI_SI"
                                                                                                                        else:
                                                                                                                            return "OENB"
                                                                                                                    else:
                                                                                                                        return "PI_SI"
                                                                                                                else:
                                                                                                                    return "OENB"
                                                                                                            else:
                                                                                                                return "OENB"
                                                                                                        else:
                                                                                                            # if Actor_To_Nest_Distance <= 125.3928756714
                                                                                                            if _get(features, "Actor_To_Nest_Distance") <= 125.3928756714:
                                                                                                                return "OENB"
                                                                                                            else:
                                                                                                                return "PI_SI"
                                                                                                else:
                                                                                                    # if c3_Rat_Distance <= 253.0402679443
                                                                                                    if _get(features, "c3_Rat_Distance") <= 253.0402679443:
                                                                                                        # if c4_Rat_Distance <= 1088.4741821289
                                                                                                        if _get(features, "c4_Rat_Distance") <= 1088.4741821289:
                                                                                                            return "PI_SI"
                                                                                                        else:
                                                                                                            return "OENB"
                                                                                                    else:
                                                                                                        return "OENB"
                                                                                            else:
                                                                                                # if Nest_RL_y <= 545.5000000000
                                                                                                if _get(features, "Nest_RL_y") <= 545.5000000000:
                                                                                                    return "OENB"
                                                                                                else:
                                                                                                    # if Nest_hu_1 <= 0.0045617190
                                                                                                    if _get(features, "Nest_hu_1") <= 0.0045617190:
                                                                                                        # if c1_Rat_Distance <= 1165.9252319336
                                                                                                        if _get(features, "c1_Rat_Distance") <= 1165.9252319336:
                                                                                                            return "PI_SI"
                                                                                                        else:
                                                                                                            return "OENB"
                                                                                                    else:
                                                                                                        # if Actor_Dist_RR_To_Bbox_BR <= 99.0050506592
                                                                                                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 99.0050506592:
                                                                                                            return "PI_SI"
                                                                                                        else:
                                                                                                            # if Actor_Dist_RT_To_Bbox_BL <= 265.3415985107
                                                                                                            if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 265.3415985107:
                                                                                                                return "OENB"
                                                                                                            else:
                                                                                                                return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                            else:
                                                                                # if c3_Rat_Distance <= 277.7538452148
                                                                                if _get(features, "c3_Rat_Distance") <= 277.7538452148:
                                                                                    # if Actor_hu_3 <= 0.0000066050
                                                                                    if _get(features, "Actor_hu_3") <= 0.0000066050:
                                                                                        # if c2_Rat_Distance <= 556.0592956543
                                                                                        if _get(features, "c2_Rat_Distance") <= 556.0592956543:
                                                                                            # if Actor_orientation <= 82.8144836426
                                                                                            if _get(features, "Actor_orientation") <= 82.8144836426:
                                                                                                # if Actor_solidity <= 0.9533118010
                                                                                                if _get(features, "Actor_solidity") <= 0.9533118010:
                                                                                                    return "OENB"
                                                                                                else:
                                                                                                    return "PI_SI"
                                                                                            else:
                                                                                                return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    return "PI_SI"
                                                                        else:
                                                                            # if Nest_Dist_RL_To_Bbox_TR <= 436.0056457520
                                                                            if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 436.0056457520:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        # if c1_Nest_Distance <= 1207.4409179688
                                                        if _get(features, "c1_Nest_Distance") <= 1207.4409179688:
                                                            return "OENB"
                                                        else:
                                                            return "PI_SI"
                                                else:
                                                    # if Actor_Dist_RR_To_Bbox_TL <= 358.1869659424
                                                    if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 358.1869659424:
                                                        return "PI_SI"
                                                    else:
                                                        # if Nest_bbox_x <= 821.5000000000
                                                        if _get(features, "Nest_bbox_x") <= 821.5000000000:
                                                            return "OENB"
                                                        else:
                                                            # if Actor_RL_y <= 535.5000000000
                                                            if _get(features, "Actor_RL_y") <= 535.5000000000:
                                                                return "OENB"
                                                            else:
                                                                return "PI_SI"
                                    else:
                                        # if Nest_RT_y <= 542.0000000000
                                        if _get(features, "Nest_RT_y") <= 542.0000000000:
                                            return "PI_SI"
                                        else:
                                            # if Nest_solidity <= 0.8624867499
                                            if _get(features, "Nest_solidity") <= 0.8624867499:
                                                # if Nest_aspect_ratio <= 3.5174934864
                                                if _get(features, "Nest_aspect_ratio") <= 3.5174934864:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                            else:
                                                return "PI_SI"
                                else:
                                    # if Actor_Dist_RT_To_Bbox_BR <= 249.9806518555
                                    if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 249.9806518555:
                                        # if Nest_Dist_RL_RR <= 174.5771484375
                                        if _get(features, "Nest_Dist_RL_RR") <= 174.5771484375:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        # if Nest_Dist_RT_RR <= 48.9666976929
                                        if _get(features, "Nest_Dist_RT_RR") <= 48.9666976929:
                                            return "OENB"
                                        else:
                                            # if Actor_Centroid_To_Bbox_TL <= 230.8691635132
                                            if _get(features, "Actor_Centroid_To_Bbox_TL") <= 230.8691635132:
                                                # if Actor_RR_x <= 1219.5000000000
                                                if _get(features, "Actor_RR_x") <= 1219.5000000000:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                            else:
                                                return "PI_SI"
                    else:
                        # if c2_Nest_Distance <= 677.6032104492
                        if _get(features, "c2_Nest_Distance") <= 677.6032104492:
                            # if Nest_RT_x <= 833.0000000000
                            if _get(features, "Nest_RT_x") <= 833.0000000000:
                                # if Actor_orientation <= 73.3808555603
                                if _get(features, "Actor_orientation") <= 73.3808555603:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                            else:
                                # if Nest_Dist_RL_RR <= 459.6757202148
                                if _get(features, "Nest_Dist_RL_RR") <= 459.6757202148:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                        else:
                            # if Nest_hu_5 <= 0.1564559937
                            if _get(features, "Nest_hu_5") <= 0.1564559937:
                                # if Actor_Dist_RT_To_Bbox_BR <= 374.2127532959
                                if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 374.2127532959:
                                    # if Actor_RT_x <= 1121.0000000000
                                    if _get(features, "Actor_RT_x") <= 1121.0000000000:
                                        # if Nest_RB_y <= 618.5000000000
                                        if _get(features, "Nest_RB_y") <= 618.5000000000:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    # if Actor_Dist_RL_To_Bbox_BL <= 81.5000000000
                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 81.5000000000:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                            else:
                                return "PI_SI"
            else:
                # if Nest_Dist_RL_To_Bbox_BL <= 35.0000000000
                if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 35.0000000000:
                    # if Actor_RT_x <= 1091.0000000000
                    if _get(features, "Actor_RT_x") <= 1091.0000000000:
                        # if Actor_Dist_RL_To_Bbox_BR <= 304.9895477295
                        if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 304.9895477295:
                            return "OENB"
                        else:
                            # if Nest_Dist_RT_RB <= 335.7784729004
                            if _get(features, "Nest_Dist_RT_RB") <= 335.7784729004:
                                return "PI_SI"
                            else:
                                return "OENB"
                    else:
                        return "OENB"
                else:
                    # if Actor_Dist_RT_To_Bbox_BL <= 253.7452316284
                    if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 253.7452316284:
                        # if Nest_centroid_y <= 584.8220825195
                        if _get(features, "Nest_centroid_y") <= 584.8220825195:
                            # if Nest_hu_6 <= -0.0000007180
                            if _get(features, "Nest_hu_6") <= -0.0000007180:
                                return "PI_SI"
                            else:
                                return "OENB"
                        else:
                            # if Nest_Dist_RR_To_Bbox_BL <= 452.1932983398
                            if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 452.1932983398:
                                return "PI_SI"
                            else:
                                return "OENB"
                    else:
                        # if Nest_RT_x <= 1088.5000000000
                        if _get(features, "Nest_RT_x") <= 1088.5000000000:
                            # if Nest_RT_y <= 506.5000000000
                            if _get(features, "Nest_RT_y") <= 506.5000000000:
                                # if Actor_RL_y <= 517.0000000000
                                if _get(features, "Actor_RL_y") <= 517.0000000000:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                            else:
                                return "OENB"
                        else:
                            # if Actor_Dist_RR_To_Bbox_TR <= 169.0029983521
                            if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 169.0029983521:
                                return "PI_SI"
                            else:
                                return "OENB"
        else:
            # if Nest_hu_6 <= 0.0000010380
            if _get(features, "Nest_hu_6") <= 0.0000010380:
                # if Nest_hu_0 <= 0.5292384177
                if _get(features, "Nest_hu_0") <= 0.5292384177:
                    # if Actor_hu_6 <= -0.0000025250
                    if _get(features, "Actor_hu_6") <= -0.0000025250:
                        # if Nest_perimeter <= 480.9188232422
                        if _get(features, "Nest_perimeter") <= 480.9188232422:
                            return "OENB"
                        else:
                            return "PI_SI"
                    else:
                        # if Nest_Dist_RR_To_Bbox_TR <= 113.0044250488
                        if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 113.0044250488:
                            # if Actor_RL_y <= 640.0000000000
                            if _get(features, "Actor_RL_y") <= 640.0000000000:
                                # if c3_Rat_Distance <= 248.0383987427
                                if _get(features, "c3_Rat_Distance") <= 248.0383987427:
                                    # if Nest_RL_x <= 799.0000000000
                                    if _get(features, "Nest_RL_x") <= 799.0000000000:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    # if Actor_aspect_ratio <= 2.4622411728
                                    if _get(features, "Actor_aspect_ratio") <= 2.4622411728:
                                        # if Nest_area <= 1227.5000000000
                                        if _get(features, "Nest_area") <= 1227.5000000000:
                                            return "OENB"
                                        else:
                                            # if Pups_Location_Rat_Distance <= 116.9026107788
                                            if _get(features, "Pups_Location_Rat_Distance") <= 116.9026107788:
                                                # if Actor_Centroid_To_Bbox_BR <= 239.0398330688
                                                if _get(features, "Actor_Centroid_To_Bbox_BR") <= 239.0398330688:
                                                    # if Pups_Location_Nest_Distance <= 131.3172912598
                                                    if _get(features, "Pups_Location_Nest_Distance") <= 131.3172912598:
                                                        return "OENB"
                                                    else:
                                                        # if foodhopperLeft_Rat_Distance <= 731.2085266113
                                                        if _get(features, "foodhopperLeft_Rat_Distance") <= 731.2085266113:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                else:
                                                    # if Actor_To_Nest_Dist_Change <= 2.0799313784
                                                    if _get(features, "Actor_To_Nest_Dist_Change") <= 2.0799313784:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                                            else:
                                                # if Actor_Direction_deg <= -178.0659408569
                                                if _get(features, "Actor_Direction_deg") <= -178.0659408569:
                                                    # if Nest_Centroid_To_Bbox_BR <= 81.6223030090
                                                    if _get(features, "Nest_Centroid_To_Bbox_BR") <= 81.6223030090:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                                else:
                                                    # if Nest_Area_Diff_Abs <= 5064.0000000000
                                                    if _get(features, "Nest_Area_Diff_Abs") <= 5064.0000000000:
                                                        # if Actor_hu_2 <= 0.0000144500
                                                        if _get(features, "Actor_hu_2") <= 0.0000144500:
                                                            # if Actor_bbox_w <= 398.5000000000
                                                            if _get(features, "Actor_bbox_w") <= 398.5000000000:
                                                                return "OENB"
                                                            else:
                                                                return "PI_SI"
                                                        else:
                                                            return "PI_SI"
                                                    else:
                                                        # if Nest_Dist_RL_To_Bbox_BR <= 188.3322601318
                                                        if _get(features, "Nest_Dist_RL_To_Bbox_BR") <= 188.3322601318:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                    else:
                                        # if Nest_Dist_RR_To_Bbox_TR <= 74.0067672729
                                        if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 74.0067672729:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
                            else:
                                return "OENB"
                        else:
                            return "OENB"
                else:
                    # if Nest_Dist_RT_RR <= 99.1061744690
                    if _get(features, "Nest_Dist_RT_RR") <= 99.1061744690:
                        return "PI_SI"
                    else:
                        return "OENB"
            else:
                # if c2_Nest_Distance <= 659.0289916992
                if _get(features, "c2_Nest_Distance") <= 659.0289916992:
                    # if pipeStart_Rat_Distance <= 208.5758743286
                    if _get(features, "pipeStart_Rat_Distance") <= 208.5758743286:
                        return "OENB"
                    else:
                        return "PI_SI"
                else:
                    # if Nest_RR_y <= 609.5000000000
                    if _get(features, "Nest_RR_y") <= 609.5000000000:
                        # if Actor_eccentricity <= 0.8128882647
                        if _get(features, "Actor_eccentricity") <= 0.8128882647:
                            return "PI_SI"
                        else:
                            return "OENB"
                    else:
                        # if Actor_Dist_RB_To_Bbox_BR <= 458.0010833740
                        if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 458.0010833740:
                            # if Nest_solidity <= 0.8755539358
                            if _get(features, "Nest_solidity") <= 0.8755539358:
                                return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            return "PI_SI"
    else:
        # if Nest_Centroid_To_Bbox_BL <= 150.1401748657
        if _get(features, "Nest_Centroid_To_Bbox_BL") <= 150.1401748657:
            # if Nest_Dist_RT_To_Bbox_BL <= 197.9772644043
            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 197.9772644043:
                # if Actor_solidity <= 0.8593095541
                if _get(features, "Actor_solidity") <= 0.8593095541:
                    # if Nest_Dist_RT_RB <= 169.9293823242
                    if _get(features, "Nest_Dist_RT_RB") <= 169.9293823242:
                        # if pipeStart_Rat_Distance <= 308.3318786621
                        if _get(features, "pipeStart_Rat_Distance") <= 308.3318786621:
                            return "PI_SI"
                        else:
                            return "OENB"
                    else:
                        # if Nest_solidity <= 0.6310548484
                        if _get(features, "Nest_solidity") <= 0.6310548484:
                            # if Actor_RT_y <= 435.5000000000
                            if _get(features, "Actor_RT_y") <= 435.5000000000:
                                return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            # if Actor_bbox_h <= 127.5000000000
                            if _get(features, "Actor_bbox_h") <= 127.5000000000:
                                # if Nest_bbox_x <= 72.5000000000
                                if _get(features, "Nest_bbox_x") <= 72.5000000000:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                            else:
                                # if Actor_Dist_RL_RT <= 263.7802124023
                                if _get(features, "Actor_Dist_RL_RT") <= 263.7802124023:
                                    # if Actor_Dist_RT_To_Bbox_BR <= 176.5545806885
                                    if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 176.5545806885:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    return "OENB"
                else:
                    # if pipeMid_Rat_Distance <= 281.4829711914
                    if _get(features, "pipeMid_Rat_Distance") <= 281.4829711914:
                        # if Actor_Dist_RB_To_Bbox_BR <= 240.0020828247
                        if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 240.0020828247:
                            return "PI_SI"
                        else:
                            return "OENB"
                    else:
                        # if Actor_Dist_RL_To_Bbox_BL <= 125.5000000000
                        if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 125.5000000000:
                            # if Actor_bbox_x <= 952.0000000000
                            if _get(features, "Actor_bbox_x") <= 952.0000000000:
                                # if Nest_extent <= 0.3273887485
                                if _get(features, "Nest_extent") <= 0.3273887485:
                                    # if Actor_hu_3 <= 0.0000082400
                                    if _get(features, "Actor_hu_3") <= 0.0000082400:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    # if Pups_Location_Rat_Distance <= 49.2045707703
                                    if _get(features, "Pups_Location_Rat_Distance") <= 49.2045707703:
                                        return "OENB"
                                    else:
                                        # if Nest_Centroid_To_Bbox_BR <= 104.6542358398
                                        if _get(features, "Nest_Centroid_To_Bbox_BR") <= 104.6542358398:
                                            # if pipeMid_Rat_Distance <= 299.5789031982
                                            if _get(features, "pipeMid_Rat_Distance") <= 299.5789031982:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                                        else:
                                            return "PI_SI"
                            else:
                                # if Nest_RT_x <= 861.5000000000
                                if _get(features, "Nest_RT_x") <= 861.5000000000:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                        else:
                            # if Actor_hu_3 <= 0.0000204000
                            if _get(features, "Actor_hu_3") <= 0.0000204000:
                                # if Actor_hu_0 <= 0.1652647406
                                if _get(features, "Actor_hu_0") <= 0.1652647406:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                            else:
                                return "OENB"
            else:
                # if Nest_hu_5 <= 0.0003053690
                if _get(features, "Nest_hu_5") <= 0.0003053690:
                    # if Nest_RR_x <= 524.5000000000
                    if _get(features, "Nest_RR_x") <= 524.5000000000:
                        # if Actor_RT_x <= 388.0000000000
                        if _get(features, "Actor_RT_x") <= 388.0000000000:
                            # if Actor_Dist_RB_To_Bbox_BL <= 36.5136985779
                            if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 36.5136985779:
                                # if Nest_orientation <= 52.1388988495
                                if _get(features, "Nest_orientation") <= 52.1388988495:
                                    return "OENB"
                                else:
                                    # if Nest_hu_2 <= 0.0068539942
                                    if _get(features, "Nest_hu_2") <= 0.0068539942:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                            else:
                                # if c4_Nest_Distance <= 480.0796966553
                                if _get(features, "c4_Nest_Distance") <= 480.0796966553:
                                    # if c1_Rat_Distance <= 521.1951904297
                                    if _get(features, "c1_Rat_Distance") <= 521.1951904297:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    return "OENB"
                        else:
                            return "OENB"
                    else:
                        # if Nest_Dist_RT_RR <= 223.0949859619
                        if _get(features, "Nest_Dist_RT_RR") <= 223.0949859619:
                            # if Nest_Centroid_To_Bbox_TL <= 106.7275924683
                            if _get(features, "Nest_Centroid_To_Bbox_TL") <= 106.7275924683:
                                return "PI_SI"
                            else:
                                return "OENB"
                        else:
                            return "PI_SI"
                else:
                    # if Nest_aspect_ratio <= 1.0790950060
                    if _get(features, "Nest_aspect_ratio") <= 1.0790950060:
                        return "OENB"
                    else:
                        # if Actor_orientation <= 80.6570358276
                        if _get(features, "Actor_orientation") <= 80.6570358276:
                            return "PI_SI"
                        else:
                            return "OENB"
        else:
            # if Nest_area <= 36090.7500000000
            if _get(features, "Nest_area") <= 36090.7500000000:
                # if c2_Nest_Distance <= 658.1289672852
                if _get(features, "c2_Nest_Distance") <= 658.1289672852:
                    # if Nest_Centroid_To_Bbox_BL <= 151.1207199097
                    if _get(features, "Nest_Centroid_To_Bbox_BL") <= 151.1207199097:
                        # if Actor_hu_0 <= 0.1903786585
                        if _get(features, "Actor_hu_0") <= 0.1903786585:
                            return "PI_SI"
                        else:
                            return "OENB"
                    else:
                        # if Nest_orientation <= 84.0413894653
                        if _get(features, "Nest_orientation") <= 84.0413894653:
                            # if Actor_Centroid_To_Bbox_TL <= 234.5061721802
                            if _get(features, "Actor_Centroid_To_Bbox_TL") <= 234.5061721802:
                                return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            # if Actor_solidity <= 0.9399529397
                            if _get(features, "Actor_solidity") <= 0.9399529397:
                                # if c2_Nest_Distance <= 658.0721130371
                                if _get(features, "c2_Nest_Distance") <= 658.0721130371:
                                    # if Actor_Area_Diff_Abs <= 14.7500000000
                                    if _get(features, "Actor_Area_Diff_Abs") <= 14.7500000000:
                                        # if Nest_Area_Diff_Abs <= 162.2500000000
                                        if _get(features, "Nest_Area_Diff_Abs") <= 162.2500000000:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    # if Nest_RR_y <= 607.0000000000
                                    if _get(features, "Nest_RR_y") <= 607.0000000000:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                            else:
                                # if Nest_Dist_RL_RR <= 351.3574218750
                                if _get(features, "Nest_Dist_RL_RR") <= 351.3574218750:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                else:
                    # if Nest_RB_y <= 618.5000000000
                    if _get(features, "Nest_RB_y") <= 618.5000000000:
                        # if Actor_orientation <= 72.4015502930
                        if _get(features, "Actor_orientation") <= 72.4015502930:
                            # if Actor_Area_Diff_Abs <= 1960.2500000000
                            if _get(features, "Actor_Area_Diff_Abs") <= 1960.2500000000:
                                return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            # if Nest_solidity <= 0.5357858837
                            if _get(features, "Nest_solidity") <= 0.5357858837:
                                return "OENB"
                            else:
                                return "PI_SI"
                    else:
                        # if Actor_area <= 60923.7500000000
                        if _get(features, "Actor_area") <= 60923.7500000000:
                            # if Nest_Dist_RT_To_Bbox_BR <= 469.9319152832
                            if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 469.9319152832:
                                # if Actor_Dist_RL_To_Bbox_TL <= 35.5000000000
                                if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 35.5000000000:
                                    # if Actor_bbox_y <= 436.5000000000
                                    if _get(features, "Actor_bbox_y") <= 436.5000000000:
                                        # if Nest_RT_y <= 453.5000000000
                                        if _get(features, "Nest_RT_y") <= 453.5000000000:
                                            # if Actor_hu_0 <= 0.1696899012
                                            if _get(features, "Actor_hu_0") <= 0.1696899012:
                                                # if Actor_centroid_x <= 1004.3482055664
                                                if _get(features, "Actor_centroid_x") <= 1004.3482055664:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                            else:
                                                # if Nest_Dist_RT_RR <= 102.1113891602
                                                if _get(features, "Nest_Dist_RT_RR") <= 102.1113891602:
                                                    return "OENB"
                                                else:
                                                    # if Nest_Centroid_To_Bbox_TR <= 194.0357513428
                                                    if _get(features, "Nest_Centroid_To_Bbox_TR") <= 194.0357513428:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                                        else:
                                            # if Nest_bbox_h <= 165.0000000000
                                            if _get(features, "Nest_bbox_h") <= 165.0000000000:
                                                # if c3_Rat_Distance <= 1027.9290466309
                                                if _get(features, "c3_Rat_Distance") <= 1027.9290466309:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                            else:
                                                # if Actor_eccentricity <= 0.5153432786
                                                if _get(features, "Actor_eccentricity") <= 0.5153432786:
                                                    # if Actor_Dist_RB_RL <= 183.7447433472
                                                    if _get(features, "Actor_Dist_RB_RL") <= 183.7447433472:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                                                else:
                                                    # if Actor_Dist_RL_RT <= 244.8439788818
                                                    if _get(features, "Actor_Dist_RL_RT") <= 244.8439788818:
                                                        # if Nest_RR_x <= 533.5000000000
                                                        if _get(features, "Nest_RR_x") <= 533.5000000000:
                                                            return "OENB"
                                                        else:
                                                            # if Actor_Dist_RL_To_Bbox_TR <= 237.9291458130
                                                            if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 237.9291458130:
                                                                return "OENB"
                                                            else:
                                                                return "PI_SI"
                                                    else:
                                                        return "PI_SI"
                                    else:
                                        # if Nest_RL_y <= 618.5000000000
                                        if _get(features, "Nest_RL_y") <= 618.5000000000:
                                            return "PI_SI"
                                        else:
                                            # if Nest_perimeter <= 1054.9453125000
                                            if _get(features, "Nest_perimeter") <= 1054.9453125000:
                                                # if Actor_bbox_y <= 490.5000000000
                                                if _get(features, "Actor_bbox_y") <= 490.5000000000:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                            else:
                                                # if Actor_To_Nest_Distance <= 550.8485412598
                                                if _get(features, "Actor_To_Nest_Distance") <= 550.8485412598:
                                                    # if Nest_Dist_RT_To_Bbox_BL <= 368.2153320312
                                                    if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 368.2153320312:
                                                        # if Nest_Dist_RL_To_Bbox_BR <= 371.1057586670
                                                        if _get(features, "Nest_Dist_RL_To_Bbox_BR") <= 371.1057586670:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        return "PI_SI"
                                                else:
                                                    return "OENB"
                                else:
                                    # if Actor_RL_x <= 39.5000000000
                                    if _get(features, "Actor_RL_x") <= 39.5000000000:
                                        # if foodhopperRight_Nest_Distance <= 745.5090026855
                                        if _get(features, "foodhopperRight_Nest_Distance") <= 745.5090026855:
                                            return "OENB"
                                        else:
                                            # if Nest_Dist_RB_To_Bbox_BL <= 113.0044593811
                                            if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 113.0044593811:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                    else:
                                        # if Nest_Centroid_To_Bbox_BR <= 141.2044219971
                                        if _get(features, "Nest_Centroid_To_Bbox_BR") <= 141.2044219971:
                                            # if c1_Rat_Distance <= 602.5621948242
                                            if _get(features, "c1_Rat_Distance") <= 602.5621948242:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                        else:
                                            # if Actor_Dist_RB_To_Bbox_TL <= 432.2160797119
                                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 432.2160797119:
                                                # if Nest_RL_x <= 754.5000000000
                                                if _get(features, "Nest_RL_x") <= 754.5000000000:
                                                    # if Actor_RL_x <= 910.5000000000
                                                    if _get(features, "Actor_RL_x") <= 910.5000000000:
                                                        # if Nest_RR_y <= 429.0000000000
                                                        if _get(features, "Nest_RR_y") <= 429.0000000000:
                                                            return "PI_SI"
                                                        else:
                                                            # if Nest_RB_x <= 103.5000000000
                                                            if _get(features, "Nest_RB_x") <= 103.5000000000:
                                                                return "PI_SI"
                                                            else:
                                                                # if Actor_Dist_RB_To_Bbox_TR <= 345.2318115234
                                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 345.2318115234:
                                                                    # if c1_Nest_Distance <= 582.2543334961
                                                                    if _get(features, "c1_Nest_Distance") <= 582.2543334961:
                                                                        # if Nest_Dist_RL_To_Bbox_BL <= 48.5000000000
                                                                        if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 48.5000000000:
                                                                            # if Nest_hu_5 <= 0.0001548046
                                                                            if _get(features, "Nest_hu_5") <= 0.0001548046:
                                                                                # if Nest_hu_5 <= 0.0001113170
                                                                                if _get(features, "Nest_hu_5") <= 0.0001113170:
                                                                                    return "OENB"
                                                                                else:
                                                                                    # if Actor_bbox_y <= 471.5000000000
                                                                                    if _get(features, "Actor_bbox_y") <= 471.5000000000:
                                                                                        return "OENB"
                                                                                    else:
                                                                                        # if Nest_perimeter <= 974.7909851074
                                                                                        if _get(features, "Nest_perimeter") <= 974.7909851074:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            # if Actor_Dist_RL_To_Bbox_BL <= 32.0000000000
                                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 32.0000000000:
                                                                                                return "OENB"
                                                                                            else:
                                                                                                return "PI_SI"
                                                                            else:
                                                                                # if Nest_hu_0 <= 0.3820223957
                                                                                if _get(features, "Nest_hu_0") <= 0.3820223957:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                        else:
                                                                            # if Actor_aspect_ratio <= 2.6886146069
                                                                            if _get(features, "Actor_aspect_ratio") <= 2.6886146069:
                                                                                # if Actor_Dist_RR_To_Bbox_TR <= 144.0034713745
                                                                                if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 144.0034713745:
                                                                                    # if Nest_Dist_RR_RB <= 226.8169250488
                                                                                    if _get(features, "Nest_Dist_RR_RB") <= 226.8169250488:
                                                                                        # if Nest_area <= 23183.5000000000
                                                                                        if _get(features, "Nest_area") <= 23183.5000000000:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            # if Nest_area <= 23280.7500000000
                                                                                            if _get(features, "Nest_area") <= 23280.7500000000:
                                                                                                # if Nest_Dist_RL_To_Bbox_BL <= 59.0000000000
                                                                                                if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 59.0000000000:
                                                                                                    return "PI_SI"
                                                                                                else:
                                                                                                    return "OENB"
                                                                                            else:
                                                                                                # if c2_Rat_Distance <= 620.0571289062
                                                                                                if _get(features, "c2_Rat_Distance") <= 620.0571289062:
                                                                                                    return "OENB"
                                                                                                else:
                                                                                                    # if Nest_Centroid_To_Bbox_BR <= 173.3597183228
                                                                                                    if _get(features, "Nest_Centroid_To_Bbox_BR") <= 173.3597183228:
                                                                                                        return "PI_SI"
                                                                                                    else:
                                                                                                        return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    return "PI_SI"
                                                                            else:
                                                                                return "PI_SI"
                                                                    else:
                                                                        # if pipeStart_Rat_Distance <= 100.8391456604
                                                                        if _get(features, "pipeStart_Rat_Distance") <= 100.8391456604:
                                                                            # if Nest_extent <= 0.4651328623
                                                                            if _get(features, "Nest_extent") <= 0.4651328623:
                                                                                # if Nest_hu_1 <= 0.0406710897
                                                                                if _get(features, "Nest_hu_1") <= 0.0406710897:
                                                                                    # if Actor_centroid_x <= 521.5079956055
                                                                                    if _get(features, "Actor_centroid_x") <= 521.5079956055:
                                                                                        # if Actor_Dist_RL_RT <= 111.4038696289
                                                                                        if _get(features, "Actor_Dist_RL_RT") <= 111.4038696289:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                    else:
                                                                                        # if Nest_bbox_y <= 465.0000000000
                                                                                        if _get(features, "Nest_bbox_y") <= 465.0000000000:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                else:
                                                                                    return "OENB"
                                                                            else:
                                                                                # if Actor_Dist_RR_To_Bbox_TR <= 55.5090084076
                                                                                if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 55.5090084076:
                                                                                    return "OENB"
                                                                                else:
                                                                                    # if Nest_Dist_RT_RR <= 69.7731552124
                                                                                    if _get(features, "Nest_Dist_RT_RR") <= 69.7731552124:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                        else:
                                                                            # if Actor_centroid_y <= 572.6836242676
                                                                            if _get(features, "Actor_centroid_y") <= 572.6836242676:
                                                                                # if c2_Nest_Distance <= 658.2550659180
                                                                                if _get(features, "c2_Nest_Distance") <= 658.2550659180:
                                                                                    # if Actor_RL_y <= 458.0000000000
                                                                                    if _get(features, "Actor_RL_y") <= 458.0000000000:
                                                                                        return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    # if Nest_Mask_IoU <= 0.6689687371
                                                                                    if _get(features, "Nest_Mask_IoU") <= 0.6689687371:
                                                                                        # if Nest_RT_y <= 455.0000000000
                                                                                        if _get(features, "Nest_RT_y") <= 455.0000000000:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                    else:
                                                                                        # if Actor_To_Nest_Dist_Change <= -306.0699691772
                                                                                        if _get(features, "Actor_To_Nest_Dist_Change") <= -306.0699691772:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            # if Nest_extent <= 0.5571362972
                                                                                            if _get(features, "Nest_extent") <= 0.5571362972:
                                                                                                # if Actor_Centroid_To_Bbox_BL <= 292.1333923340
                                                                                                if _get(features, "Actor_Centroid_To_Bbox_BL") <= 292.1333923340:
                                                                                                    # if Actor_extent <= 0.7869952917
                                                                                                    if _get(features, "Actor_extent") <= 0.7869952917:
                                                                                                        # if Nest_Dist_RB_RL <= 338.9136962891
                                                                                                        if _get(features, "Nest_Dist_RB_RL") <= 338.9136962891:
                                                                                                            # if Actor_RB_x <= 122.5000000000
                                                                                                            if _get(features, "Actor_RB_x") <= 122.5000000000:
                                                                                                                # if foodhopperLeft_Rat_Distance <= 470.1804504395
                                                                                                                if _get(features, "foodhopperLeft_Rat_Distance") <= 470.1804504395:
                                                                                                                    return "PI_SI"
                                                                                                                else:
                                                                                                                    return "OENB"
                                                                                                            else:
                                                                                                                # if Nest_Dist_RT_RR <= 20.5768728256
                                                                                                                if _get(features, "Nest_Dist_RT_RR") <= 20.5768728256:
                                                                                                                    # if Nest_Dist_RR_To_Bbox_BL <= 383.2313232422
                                                                                                                    if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 383.2313232422:
                                                                                                                        return "PI_SI"
                                                                                                                    else:
                                                                                                                        return "OENB"
                                                                                                                else:
                                                                                                                    # if Nest_Centroid_To_Bbox_TL <= 152.2982330322
                                                                                                                    if _get(features, "Nest_Centroid_To_Bbox_TL") <= 152.2982330322:
                                                                                                                        # if pipeStart_Nest_Distance <= 267.2426986694
                                                                                                                        if _get(features, "pipeStart_Nest_Distance") <= 267.2426986694:
                                                                                                                            return "OENB"
                                                                                                                        else:
                                                                                                                            return "PI_SI"
                                                                                                                    else:
                                                                                                                        # if Nest_Dist_RT_To_Bbox_BR <= 170.8639755249
                                                                                                                        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 170.8639755249:
                                                                                                                            # if Nest_area <= 23579.5000000000
                                                                                                                            if _get(features, "Nest_area") <= 23579.5000000000:
                                                                                                                                # if Actor_Dist_RT_RB <= 155.7160873413
                                                                                                                                if _get(features, "Actor_Dist_RT_RB") <= 155.7160873413:
                                                                                                                                    # if Nest_Dist_RL_To_Bbox_BR <= 309.2327575684
                                                                                                                                    if _get(features, "Nest_Dist_RL_To_Bbox_BR") <= 309.2327575684:
                                                                                                                                        return "PI_SI"
                                                                                                                                    else:
                                                                                                                                        return "OENB"
                                                                                                                                else:
                                                                                                                                    return "OENB"
                                                                                                                            else:
                                                                                                                                # if Actor_Mask_IoU <= 0.9831088483
                                                                                                                                if _get(features, "Actor_Mask_IoU") <= 0.9831088483:
                                                                                                                                    return "PI_SI"
                                                                                                                                else:
                                                                                                                                    return "OENB"
                                                                                                                        else:
                                                                                                                            # if Actor_Dist_RR_To_Bbox_BR <= 10.5476179123
                                                                                                                            if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 10.5476179123:
                                                                                                                                # if Nest_Dist_RT_To_Bbox_BR <= 461.8522186279
                                                                                                                                if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 461.8522186279:
                                                                                                                                    return "OENB"
                                                                                                                                else:
                                                                                                                                    return "PI_SI"
                                                                                                                            else:
                                                                                                                                # if Actor_Dist_RB_To_Bbox_TR <= 343.8648071289
                                                                                                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 343.8648071289:
                                                                                                                                    # if c1_Rat_Distance <= 548.8679199219
                                                                                                                                    if _get(features, "c1_Rat_Distance") <= 548.8679199219:
                                                                                                                                        # if pipeMid_Rat_Distance <= 322.0113067627
                                                                                                                                        if _get(features, "pipeMid_Rat_Distance") <= 322.0113067627:
                                                                                                                                            return "PI_SI"
                                                                                                                                        else:
                                                                                                                                            return "OENB"
                                                                                                                                    else:
                                                                                                                                        # if pipeStart_Rat_Distance <= 103.0132446289
                                                                                                                                        if _get(features, "pipeStart_Rat_Distance") <= 103.0132446289:
                                                                                                                                            # if pipeStart_Rat_Distance <= 102.9601478577
                                                                                                                                            if _get(features, "pipeStart_Rat_Distance") <= 102.9601478577:
                                                                                                                                                return "OENB"
                                                                                                                                            else:
                                                                                                                                                return "PI_SI"
                                                                                                                                        else:
                                                                                                                                            return "OENB"
                                                                                                                                else:
                                                                                                                                    # if Actor_Centroid_To_Bbox_BR <= 223.0158386230
                                                                                                                                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 223.0158386230:
                                                                                                                                        return "PI_SI"
                                                                                                                                    else:
                                                                                                                                        return "OENB"
                                                                                                        else:
                                                                                                            # if Nest_hu_2 <= 0.0187198278
                                                                                                            if _get(features, "Nest_hu_2") <= 0.0187198278:
                                                                                                                return "PI_SI"
                                                                                                            else:
                                                                                                                # if Nest_eccentricity <= 0.9636175334
                                                                                                                if _get(features, "Nest_eccentricity") <= 0.9636175334:
                                                                                                                    return "PI_SI"
                                                                                                                else:
                                                                                                                    # if Nest_RB_x <= 1046.5000000000
                                                                                                                    if _get(features, "Nest_RB_x") <= 1046.5000000000:
                                                                                                                        # if c3_Nest_Distance <= 341.9140625000
                                                                                                                        if _get(features, "c3_Nest_Distance") <= 341.9140625000:
                                                                                                                            return "OENB"
                                                                                                                        else:
                                                                                                                            return "PI_SI"
                                                                                                                    else:
                                                                                                                        return "OENB"
                                                                                                    else:
                                                                                                        # if Nest_Dist_RR_To_Bbox_BR <= 135.0037231445
                                                                                                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 135.0037231445:
                                                                                                            return "PI_SI"
                                                                                                        else:
                                                                                                            return "OENB"
                                                                                                else:
                                                                                                    # if Nest_Dist_RL_To_Bbox_TL <= 161.5000000000
                                                                                                    if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 161.5000000000:
                                                                                                        return "PI_SI"
                                                                                                    else:
                                                                                                        return "OENB"
                                                                                            else:
                                                                                                # if Nest_RL_x <= 233.0000000000
                                                                                                if _get(features, "Nest_RL_x") <= 233.0000000000:
                                                                                                    return "PI_SI"
                                                                                                else:
                                                                                                    return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                else:
                                                                    # if Actor_Dist_RR_RB <= 281.8306274414
                                                                    if _get(features, "Actor_Dist_RR_RB") <= 281.8306274414:
                                                                        # if Nest_RT_y <= 456.5000000000
                                                                        if _get(features, "Nest_RT_y") <= 456.5000000000:
                                                                            return "PI_SI"
                                                                        else:
                                                                            # if Actor_Centroid_To_Bbox_BL <= 198.0845794678
                                                                            if _get(features, "Actor_Centroid_To_Bbox_BL") <= 198.0845794678:
                                                                                # if Actor_Area_Diff_Abs <= 93.5000000000
                                                                                if _get(features, "Actor_Area_Diff_Abs") <= 93.5000000000:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                            else:
                                                                                return "OENB"
                                                                    else:
                                                                        # if Actor_Dist_RL_To_Bbox_TR <= 344.3998718262
                                                                        if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 344.3998718262:
                                                                            # if Actor_Dist_RT_To_Bbox_BL <= 285.3175354004
                                                                            if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 285.3175354004:
                                                                                return "PI_SI"
                                                                            else:
                                                                                return "OENB"
                                                                        else:
                                                                            # if Nest_Centroid_To_Bbox_TL <= 192.7490158081
                                                                            if _get(features, "Nest_Centroid_To_Bbox_TL") <= 192.7490158081:
                                                                                # if Actor_Area_Diff_Abs <= 8.0000000000
                                                                                if _get(features, "Actor_Area_Diff_Abs") <= 8.0000000000:
                                                                                    # if Actor_Dist_RR_To_Bbox_BR <= 155.0032272339
                                                                                    if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 155.0032272339:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                                else:
                                                                                    return "OENB"
                                                                            else:
                                                                                # if Nest_Area_Diff_Abs <= 116.5000000000
                                                                                if _get(features, "Nest_Area_Diff_Abs") <= 116.5000000000:
                                                                                    # if Nest_perimeter <= 975.2138061523
                                                                                    if _get(features, "Nest_perimeter") <= 975.2138061523:
                                                                                        return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    # if Nest_Centroid_To_Bbox_TL <= 192.8480606079
                                                                                    if _get(features, "Nest_Centroid_To_Bbox_TL") <= 192.8480606079:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        # if Actor_Dist_RB_RL <= 18.9559316635
                                                                                        if _get(features, "Actor_Dist_RB_RL") <= 18.9559316635:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            # if Actor_Direction_deg <= 174.0230560303
                                                                                            if _get(features, "Actor_Direction_deg") <= 174.0230560303:
                                                                                                return "OENB"
                                                                                            else:
                                                                                                return "PI_SI"
                                                    else:
                                                        # if Nest_RT_y <= 455.0000000000
                                                        if _get(features, "Nest_RT_y") <= 455.0000000000:
                                                            return "PI_SI"
                                                        else:
                                                            # if Nest_Dist_RR_To_Bbox_TR <= 35.5142192841
                                                            if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 35.5142192841:
                                                                return "PI_SI"
                                                            else:
                                                                return "OENB"
                                                else:
                                                    # if foodhopperRight_Nest_Distance <= 467.2161102295
                                                    if _get(features, "foodhopperRight_Nest_Distance") <= 467.2161102295:
                                                        # if Actor_perimeter <= 1112.5640869141
                                                        if _get(features, "Actor_perimeter") <= 1112.5640869141:
                                                            return "PI_SI"
                                                        else:
                                                            # if Nest_Centroid_To_Bbox_BR <= 233.8305435181
                                                            if _get(features, "Nest_Centroid_To_Bbox_BR") <= 233.8305435181:
                                                                return "OENB"
                                                            else:
                                                                # if Actor_bbox_h <= 150.5000000000
                                                                if _get(features, "Actor_bbox_h") <= 150.5000000000:
                                                                    return "OENB"
                                                                else:
                                                                    return "PI_SI"
                                                    else:
                                                        # if Nest_Dist_RB_To_Bbox_BL <= 257.0019454956
                                                        if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 257.0019454956:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                            else:
                                                # if Actor_RB_x <= 1063.5000000000
                                                if _get(features, "Actor_RB_x") <= 1063.5000000000:
                                                    # if Actor_bbox_h <= 180.0000000000
                                                    if _get(features, "Actor_bbox_h") <= 180.0000000000:
                                                        # if Nest_Dist_RR_RB <= 330.0356140137
                                                        if _get(features, "Nest_Dist_RR_RB") <= 330.0356140137:
                                                            return "OENB"
                                                        else:
                                                            return "PI_SI"
                                                    else:
                                                        return "PI_SI"
                                                else:
                                                    return "OENB"
                            else:
                                # if Nest_Centroid_To_Bbox_TR <= 296.7076721191
                                if _get(features, "Nest_Centroid_To_Bbox_TR") <= 296.7076721191:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                        else:
                            # if Nest_RB_y <= 634.5000000000
                            if _get(features, "Nest_RB_y") <= 634.5000000000:
                                return "PI_SI"
                            else:
                                # if Nest_perimeter <= 778.7371520996
                                if _get(features, "Nest_perimeter") <= 778.7371520996:
                                    return "PI_SI"
                                else:
                                    return "OENB"
            else:
                # if Actor_RT_y <= 435.5000000000
                if _get(features, "Actor_RT_y") <= 435.5000000000:
                    # if Nest_RL_x <= 116.5000000000
                    if _get(features, "Nest_RL_x") <= 116.5000000000:
                        # if Nest_Mask_IoU <= 0.7223642468
                        if _get(features, "Nest_Mask_IoU") <= 0.7223642468:
                            # if Actor_RT_x <= 217.5000000000
                            if _get(features, "Actor_RT_x") <= 217.5000000000:
                                return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            # if Nest_Dist_RT_To_Bbox_BL <= 246.4237899780
                            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 246.4237899780:
                                # if c2_Rat_Distance <= 1159.9935913086
                                if _get(features, "c2_Rat_Distance") <= 1159.9935913086:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                            else:
                                # if Nest_eccentricity <= 0.8030514717
                                if _get(features, "Nest_eccentricity") <= 0.8030514717:
                                    # if pipeStart_Nest_Distance <= 350.4108276367
                                    if _get(features, "pipeStart_Nest_Distance") <= 350.4108276367:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    # if Nest_RB_y <= 637.5000000000
                                    if _get(features, "Nest_RB_y") <= 637.5000000000:
                                        # if Nest_Dist_RB_To_Bbox_TL <= 269.0388336182
                                        if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 269.0388336182:
                                            return "OENB"
                                        else:
                                            # if Nest_Dist_RR_To_Bbox_BR <= 120.5041503906
                                            if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 120.5041503906:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                                    else:
                                        return "OENB"
                    else:
                        # if Actor_To_Nest_Distance <= 122.5345344543
                        if _get(features, "Actor_To_Nest_Distance") <= 122.5345344543:
                            # if Nest_Dist_RB_To_Bbox_BL <= 135.5036926270
                            if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 135.5036926270:
                                # if Actor_hu_2 <= 0.0012418836
                                if _get(features, "Actor_hu_2") <= 0.0012418836:
                                    return "PI_SI"
                                else:
                                    # if Actor_solidity <= 0.8602088988
                                    if _get(features, "Actor_solidity") <= 0.8602088988:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                            else:
                                return "OENB"
                        else:
                            # if Nest_Centroid_To_Bbox_BL <= 241.2696075439
                            if _get(features, "Nest_Centroid_To_Bbox_BL") <= 241.2696075439:
                                # if Actor_To_Nest_Dist_Change <= 22.9958829880
                                if _get(features, "Actor_To_Nest_Dist_Change") <= 22.9958829880:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                            else:
                                # if Actor_orientation <= 70.9781188965
                                if _get(features, "Actor_orientation") <= 70.9781188965:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                else:
                    # if Nest_RT_y <= 470.5000000000
                    if _get(features, "Nest_RT_y") <= 470.5000000000:
                        # if Nest_Dist_RT_To_Bbox_TR <= 241.5000000000
                        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 241.5000000000:
                            # if Actor_Dist_RL_To_Bbox_BR <= 90.0962867737
                            if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 90.0962867737:
                                return "OENB"
                            else:
                                # if Nest_bbox_h <= 186.5000000000
                                if _get(features, "Nest_bbox_h") <= 186.5000000000:
                                    # if Nest_orientation <= 71.7341957092
                                    if _get(features, "Nest_orientation") <= 71.7341957092:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    # if Actor_RT_y <= 436.5000000000
                                    if _get(features, "Actor_RT_y") <= 436.5000000000:
                                        # if c4_Rat_Distance <= 852.5795898438
                                        if _get(features, "c4_Rat_Distance") <= 852.5795898438:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        # if Actor_To_Nest_Dist_Change <= 13.6312294006
                                        if _get(features, "Actor_To_Nest_Dist_Change") <= 13.6312294006:
                                            return "PI_SI"
                                        else:
                                            # if Nest_centroid_x <= 312.4522399902
                                            if _get(features, "Nest_centroid_x") <= 312.4522399902:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                        else:
                            # if Actor_Dist_RT_To_Bbox_TL <= 127.0000000000
                            if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 127.0000000000:
                                return "PI_SI"
                            else:
                                return "OENB"
                    else:
                        # if Actor_eccentricity <= 0.9606508613
                        if _get(features, "Actor_eccentricity") <= 0.9606508613:
                            return "PI_SI"
                        else:
                            return "OENB"



def oenb_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Actor_RB_y <= 644.5000000000
    if _get(features, "Actor_RB_y") <= 644.5000000000:
        # if Actor_To_Nest_Distance <= 210.5930709839
        if _get(features, "Actor_To_Nest_Distance") <= 210.5930709839:
            # if foodhopperMid_Nest_Distance <= 474.6971740723
            if _get(features, "foodhopperMid_Nest_Distance") <= 474.6971740723:
                # if Nest_hu_1 <= 0.0445297770
                if _get(features, "Nest_hu_1") <= 0.0445297770:
                    # if Nest_Dist_RB_To_Bbox_BR <= 44.5112361908
                    if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 44.5112361908:
                        # if foodhopperRight_Rat_Distance <= 371.5654296875
                        if _get(features, "foodhopperRight_Rat_Distance") <= 371.5654296875:
                            # if Nest_RB_x <= 1000.0000000000
                            if _get(features, "Nest_RB_x") <= 1000.0000000000:
                                return "ONE"
                            else:
                                return "NB"
                        else:
                            # if Nest_bbox_x <= 812.0000000000
                            if _get(features, "Nest_bbox_x") <= 812.0000000000:
                                return "OE"
                            else:
                                return "ONE"
                    else:
                        # if Actor_RT_y <= 386.5000000000
                        if _get(features, "Actor_RT_y") <= 386.5000000000:
                            # if Pups_Location_Rat_Distance <= 140.7471389771
                            if _get(features, "Pups_Location_Rat_Distance") <= 140.7471389771:
                                # if Actor_Dist_RB_To_Bbox_BR <= 21.0246896744
                                if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 21.0246896744:
                                    return "ONE"
                                else:
                                    return "OE"
                            else:
                                # if foodhopperMid_Rat_Distance <= 487.3775787354
                                if _get(features, "foodhopperMid_Rat_Distance") <= 487.3775787354:
                                    return "OE"
                                else:
                                    # if Nest_Dist_RB_To_Bbox_BL <= 81.5068607330
                                    if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 81.5068607330:
                                        return "OE"
                                    else:
                                        # if Nest_Mask_IoU <= 0.9849462509
                                        if _get(features, "Nest_Mask_IoU") <= 0.9849462509:
                                            return "NB"
                                        else:
                                            return "OE"
                        else:
                            # if foodhopperLeft_Rat_Distance <= 456.1959686279
                            if _get(features, "foodhopperLeft_Rat_Distance") <= 456.1959686279:
                                return "OE"
                            else:
                                # if Nest_Centroid_To_Bbox_BR <= 121.1069869995
                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 121.1069869995:
                                    return "OE"
                                else:
                                    # if c3_Nest_Distance <= 966.8326721191
                                    if _get(features, "c3_Nest_Distance") <= 966.8326721191:
                                        # if Nest_Dist_RR_To_Bbox_BR <= 7.5666627884
                                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 7.5666627884:
                                            return "ONE"
                                        else:
                                            # if Actor_orientation <= 49.8581314087
                                            if _get(features, "Actor_orientation") <= 49.8581314087:
                                                return "OE"
                                            else:
                                                return "NB"
                                    else:
                                        return "OE"
                else:
                    # if Nest_RR_y <= 491.5000000000
                    if _get(features, "Nest_RR_y") <= 491.5000000000:
                        # if Actor_RR_x <= 429.5000000000
                        if _get(features, "Actor_RR_x") <= 429.5000000000:
                            # if foodhopperMid_Rat_Distance <= 541.7830200195
                            if _get(features, "foodhopperMid_Rat_Distance") <= 541.7830200195:
                                return "NB"
                            else:
                                # if Nest_Dist_RB_To_Bbox_BR <= 337.5015106201
                                if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 337.5015106201:
                                    return "OE"
                                else:
                                    return "ONE"
                        else:
                            # if Actor_Dist_RR_To_Bbox_BR <= 72.5069122314
                            if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 72.5069122314:
                                return "ONE"
                            else:
                                return "OE"
                    else:
                        # if Nest_centroid_y <= 575.7283020020
                        if _get(features, "Nest_centroid_y") <= 575.7283020020:
                            # if Actor_Dist_RB_To_Bbox_TR <= 342.4799194336
                            if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 342.4799194336:
                                # if Nest_RL_x <= 784.5000000000
                                if _get(features, "Nest_RL_x") <= 784.5000000000:
                                    # if Actor_To_Nest_Distance <= 63.0976619720
                                    if _get(features, "Actor_To_Nest_Distance") <= 63.0976619720:
                                        return "ONE"
                                    else:
                                        # if Nest_Centroid_To_Bbox_BL <= 138.0411911011
                                        if _get(features, "Nest_Centroid_To_Bbox_BL") <= 138.0411911011:
                                            return "NB"
                                        else:
                                            # if Nest_eccentricity <= 0.9822785854
                                            if _get(features, "Nest_eccentricity") <= 0.9822785854:
                                                # if Actor_extent <= 0.7253347039
                                                if _get(features, "Actor_extent") <= 0.7253347039:
                                                    # if Nest_extent <= 0.2874857634
                                                    if _get(features, "Nest_extent") <= 0.2874857634:
                                                        return "NB"
                                                    else:
                                                        # if Actor_hu_0 <= 0.1678178757
                                                        if _get(features, "Actor_hu_0") <= 0.1678178757:
                                                            return "NB"
                                                        else:
                                                            # if Nest_hu_0 <= 0.2712052464
                                                            if _get(features, "Nest_hu_0") <= 0.2712052464:
                                                                # if Nest_Centroid_To_Bbox_BR <= 178.9821014404
                                                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 178.9821014404:
                                                                    return "OE"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                # if Actor_Mask_IoU <= 0.5145683438
                                                                if _get(features, "Actor_Mask_IoU") <= 0.5145683438:
                                                                    # if Actor_hu_1 <= 0.0521396911
                                                                    if _get(features, "Actor_hu_1") <= 0.0521396911:
                                                                        return "ONE"
                                                                    else:
                                                                        return "OE"
                                                                else:
                                                                    # if Actor_Dist_RB_To_Bbox_TR <= 341.7206420898
                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 341.7206420898:
                                                                        # if Nest_hu_3 <= 0.0000083100
                                                                        if _get(features, "Nest_hu_3") <= 0.0000083100:
                                                                            # if Actor_RL_y <= 475.5000000000
                                                                            if _get(features, "Actor_RL_y") <= 475.5000000000:
                                                                                return "ONE"
                                                                            else:
                                                                                return "OE"
                                                                        else:
                                                                            return "OE"
                                                                    else:
                                                                        # if Actor_Dist_RT_RB <= 275.2192535400
                                                                        if _get(features, "Actor_Dist_RT_RB") <= 275.2192535400:
                                                                            return "ONE"
                                                                        else:
                                                                            return "OE"
                                                else:
                                                    # if Nest_Centroid_To_Bbox_TR <= 181.6158828735
                                                    if _get(features, "Nest_Centroid_To_Bbox_TR") <= 181.6158828735:
                                                        return "OE"
                                                    else:
                                                        return "ONE"
                                            else:
                                                return "ONE"
                                else:
                                    # if Actor_Dist_RT_RR <= 213.3668823242
                                    if _get(features, "Actor_Dist_RT_RR") <= 213.3668823242:
                                        return "NB"
                                    else:
                                        # if Nest_perimeter <= 823.3695983887
                                        if _get(features, "Nest_perimeter") <= 823.3695983887:
                                            return "ONE"
                                        else:
                                            return "OE"
                            else:
                                # if Actor_orientation <= 63.7761363983
                                if _get(features, "Actor_orientation") <= 63.7761363983:
                                    # if Nest_perimeter <= 951.9503479004
                                    if _get(features, "Nest_perimeter") <= 951.9503479004:
                                        # if Actor_Area_Diff_Abs <= 66.2500000000
                                        if _get(features, "Actor_Area_Diff_Abs") <= 66.2500000000:
                                            return "ONE"
                                        else:
                                            # if Nest_solidity <= 0.8553139865
                                            if _get(features, "Nest_solidity") <= 0.8553139865:
                                                return "OE"
                                            else:
                                                return "ONE"
                                    else:
                                        # if Actor_centroid_y <= 506.1529693604
                                        if _get(features, "Actor_centroid_y") <= 506.1529693604:
                                            # if Actor_Mask_IoU <= 0.7383709252
                                            if _get(features, "Actor_Mask_IoU") <= 0.7383709252:
                                                return "NB"
                                            else:
                                                return "ONE"
                                        else:
                                            return "OE"
                                else:
                                    # if Nest_extent <= 0.3520888388
                                    if _get(features, "Nest_extent") <= 0.3520888388:
                                        # if Actor_bbox_x <= 69.0000000000
                                        if _get(features, "Actor_bbox_x") <= 69.0000000000:
                                            # if Actor_solidity <= 0.8872199655
                                            if _get(features, "Actor_solidity") <= 0.8872199655:
                                                return "NB"
                                            else:
                                                return "OE"
                                        else:
                                            return "ONE"
                                    else:
                                        # if foodhopperRight_Nest_Distance <= 789.3693237305
                                        if _get(features, "foodhopperRight_Nest_Distance") <= 789.3693237305:
                                            # if Nest_solidity <= 0.8392189145
                                            if _get(features, "Nest_solidity") <= 0.8392189145:
                                                # if Nest_solidity <= 0.8294848502
                                                if _get(features, "Nest_solidity") <= 0.8294848502:
                                                    return "OE"
                                                else:
                                                    # if Nest_Centroid_To_Bbox_TR <= 184.0651702881
                                                    if _get(features, "Nest_Centroid_To_Bbox_TR") <= 184.0651702881:
                                                        return "OE"
                                                    else:
                                                        return "ONE"
                                            else:
                                                # if Actor_hu_2 <= 0.0005744445
                                                if _get(features, "Actor_hu_2") <= 0.0005744445:
                                                    return "ONE"
                                                else:
                                                    return "OE"
                                        else:
                                            # if foodhopperMid_Nest_Distance <= 452.2732849121
                                            if _get(features, "foodhopperMid_Nest_Distance") <= 452.2732849121:
                                                return "ONE"
                                            else:
                                                return "OE"
                        else:
                            # if Actor_hu_1 <= 0.1057334170
                            if _get(features, "Actor_hu_1") <= 0.1057334170:
                                # if Actor_Dist_RR_To_Bbox_BL <= 333.7026672363
                                if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 333.7026672363:
                                    # if Nest_Dist_RT_To_Bbox_TL <= 66.5000000000
                                    if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 66.5000000000:
                                        # if Nest_hu_3 <= 0.0214534309
                                        if _get(features, "Nest_hu_3") <= 0.0214534309:
                                            # if Nest_RB_y <= 623.5000000000
                                            if _get(features, "Nest_RB_y") <= 623.5000000000:
                                                # if Nest_Dist_RL_RR <= 360.5078430176
                                                if _get(features, "Nest_Dist_RL_RR") <= 360.5078430176:
                                                    return "NB"
                                                else:
                                                    return "ONE"
                                            else:
                                                return "OE"
                                        else:
                                            # if Actor_Dist_RL_To_Bbox_TR <= 355.8600311279
                                            if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 355.8600311279:
                                                # if Nest_Mask_IoU <= 0.9729278088
                                                if _get(features, "Nest_Mask_IoU") <= 0.9729278088:
                                                    return "ONE"
                                                else:
                                                    return "OE"
                                            else:
                                                return "NB"
                                    else:
                                        # if Nest_RB_y <= 632.0000000000
                                        if _get(features, "Nest_RB_y") <= 632.0000000000:
                                            # if Nest_eccentricity <= 0.9721913636
                                            if _get(features, "Nest_eccentricity") <= 0.9721913636:
                                                # if Nest_hu_1 <= 0.7573364079
                                                if _get(features, "Nest_hu_1") <= 0.7573364079:
                                                    # if Actor_RB_x <= 916.5000000000
                                                    if _get(features, "Actor_RB_x") <= 916.5000000000:
                                                        return "OE"
                                                    else:
                                                        return "NB"
                                                else:
                                                    # if Actor_Dist_RL_To_Bbox_TL <= 70.0000000000
                                                    if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 70.0000000000:
                                                        return "OE"
                                                    else:
                                                        return "NB"
                                            else:
                                                # if Nest_Mask_IoU <= 0.9331113994
                                                if _get(features, "Nest_Mask_IoU") <= 0.9331113994:
                                                    return "ONE"
                                                else:
                                                    return "OE"
                                        else:
                                            return "OE"
                                else:
                                    # if Actor_Dist_RB_RL <= 388.0662231445
                                    if _get(features, "Actor_Dist_RB_RL") <= 388.0662231445:
                                        # if foodhopperRight_Rat_Distance <= 365.5852050781
                                        if _get(features, "foodhopperRight_Rat_Distance") <= 365.5852050781:
                                            # if Actor_Direction_deg <= 14.9919238091
                                            if _get(features, "Actor_Direction_deg") <= 14.9919238091:
                                                return "ONE"
                                            else:
                                                # if Nest_Centroid_To_Bbox_TL <= 132.7548255920
                                                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 132.7548255920:
                                                    return "OE"
                                                else:
                                                    return "NB"
                                        else:
                                            # if pipeEnd_Rat_Distance <= 664.8896179199
                                            if _get(features, "pipeEnd_Rat_Distance") <= 664.8896179199:
                                                # if Nest_area <= 24429.7500000000
                                                if _get(features, "Nest_area") <= 24429.7500000000:
                                                    # if Actor_Area_Diff_Abs <= 13666.0000000000
                                                    if _get(features, "Actor_Area_Diff_Abs") <= 13666.0000000000:
                                                        # if Actor_eccentricity <= 0.9668252468
                                                        if _get(features, "Actor_eccentricity") <= 0.9668252468:
                                                            # if Actor_Centroid_To_Bbox_BR <= 175.4075393677
                                                            if _get(features, "Actor_Centroid_To_Bbox_BR") <= 175.4075393677:
                                                                # if Nest_RR_x <= 1218.5000000000
                                                                if _get(features, "Nest_RR_x") <= 1218.5000000000:
                                                                    return "OE"
                                                                else:
                                                                    return "NB"
                                                            else:
                                                                # if Actor_Dist_RB_To_Bbox_TR <= 706.0058593750
                                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 706.0058593750:
                                                                    return "OE"
                                                                else:
                                                                    # if Nest_Dist_RR_To_Bbox_TL <= 221.0655899048
                                                                    if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 221.0655899048:
                                                                        return "OE"
                                                                    else:
                                                                        return "ONE"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    return "ONE"
                                            else:
                                                return "NB"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_BR <= 119.0042190552
                                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 119.0042190552:
                                            return "ONE"
                                        else:
                                            return "OE"
                            else:
                                # if Nest_Centroid_To_Bbox_BR <= 133.4640197754
                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 133.4640197754:
                                    return "OE"
                                else:
                                    # if foodhopperRight_Rat_Distance <= 410.3961486816
                                    if _get(features, "foodhopperRight_Rat_Distance") <= 410.3961486816:
                                        # if Nest_RT_y <= 532.5000000000
                                        if _get(features, "Nest_RT_y") <= 532.5000000000:
                                            return "OE"
                                        else:
                                            return "ONE"
                                    else:
                                        return "ONE"
            else:
                # if foodhopperRight_Rat_Distance <= 412.0635833740
                if _get(features, "foodhopperRight_Rat_Distance") <= 412.0635833740:
                    # if Actor_Dist_RB_To_Bbox_TR <= 240.2842025757
                    if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 240.2842025757:
                        # if Actor_hu_1 <= 0.0019116195
                        if _get(features, "Actor_hu_1") <= 0.0019116195:
                            # if pipeMid_Nest_Distance <= 438.4406738281
                            if _get(features, "pipeMid_Nest_Distance") <= 438.4406738281:
                                return "NB"
                            else:
                                return "OE"
                        else:
                            # if Actor_RT_x <= 1063.5000000000
                            if _get(features, "Actor_RT_x") <= 1063.5000000000:
                                # if Actor_RR_x <= 1077.0000000000
                                if _get(features, "Actor_RR_x") <= 1077.0000000000:
                                    return "OE"
                                else:
                                    # if Actor_solidity <= 0.9465212226
                                    if _get(features, "Actor_solidity") <= 0.9465212226:
                                        # if Nest_RR_y <= 628.5000000000
                                        if _get(features, "Nest_RR_y") <= 628.5000000000:
                                            # if Nest_Mask_IoU <= 0.6764084697
                                            if _get(features, "Nest_Mask_IoU") <= 0.6764084697:
                                                # if Actor_orientation <= 95.2422828674
                                                if _get(features, "Actor_orientation") <= 95.2422828674:
                                                    return "OE"
                                                else:
                                                    return "ONE"
                                            else:
                                                # if Nest_Dist_RR_RB <= 188.6274642944
                                                if _get(features, "Nest_Dist_RR_RB") <= 188.6274642944:
                                                    # if Actor_aspect_ratio <= 1.1285361648
                                                    if _get(features, "Actor_aspect_ratio") <= 1.1285361648:
                                                        # if Actor_aspect_ratio <= 1.1255505681
                                                        if _get(features, "Actor_aspect_ratio") <= 1.1255505681:
                                                            return "ONE"
                                                        else:
                                                            return "NB"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    return "OE"
                                        else:
                                            return "OE"
                                    else:
                                        # if c4_Rat_Distance <= 1018.7172851562
                                        if _get(features, "c4_Rat_Distance") <= 1018.7172851562:
                                            return "ONE"
                                        else:
                                            return "NB"
                            else:
                                # if Actor_Dist_RB_To_Bbox_TR <= 219.8642501831
                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 219.8642501831:
                                    return "ONE"
                                else:
                                    # if Actor_To_Nest_Dist_Change <= 5.1554594040
                                    if _get(features, "Actor_To_Nest_Dist_Change") <= 5.1554594040:
                                        # if Nest_RL_y <= 602.5000000000
                                        if _get(features, "Nest_RL_y") <= 602.5000000000:
                                            return "OE"
                                        else:
                                            # if Actor_Dist_RT_To_Bbox_BR <= 274.5726013184
                                            if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 274.5726013184:
                                                return "ONE"
                                            else:
                                                return "OE"
                                    else:
                                        return "ONE"
                    else:
                        # if Actor_solidity <= 0.8710614443
                        if _get(features, "Actor_solidity") <= 0.8710614443:
                            # if Actor_bbox_x <= 851.0000000000
                            if _get(features, "Actor_bbox_x") <= 851.0000000000:
                                # if Actor_Dist_RB_To_Bbox_TL <= 333.1626281738
                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 333.1626281738:
                                    # if Actor_RT_x <= 1059.0000000000
                                    if _get(features, "Actor_RT_x") <= 1059.0000000000:
                                        # if Actor_RR_y <= 560.5000000000
                                        if _get(features, "Actor_RR_y") <= 560.5000000000:
                                            return "ONE"
                                        else:
                                            # if Actor_RB_y <= 610.0000000000
                                            if _get(features, "Actor_RB_y") <= 610.0000000000:
                                                return "ONE"
                                            else:
                                                return "OE"
                                    else:
                                        return "NB"
                                else:
                                    # if Actor_Dist_RT_To_Bbox_TR <= 198.5000000000
                                    if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 198.5000000000:
                                        # if Actor_To_Nest_Distance <= 120.1528701782
                                        if _get(features, "Actor_To_Nest_Distance") <= 120.1528701782:
                                            return "ONE"
                                        else:
                                            return "OE"
                                    else:
                                        return "ONE"
                            else:
                                # if Nest_Dist_RL_RT <= 94.8913650513
                                if _get(features, "Nest_Dist_RL_RT") <= 94.8913650513:
                                    # if Actor_Dist_RL_To_Bbox_BL <= 82.5000000000
                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 82.5000000000:
                                        return "ONE"
                                    else:
                                        return "OE"
                                else:
                                    # if Nest_Dist_RT_RB <= 137.8448638916
                                    if _get(features, "Nest_Dist_RT_RB") <= 137.8448638916:
                                        return "ONE"
                                    else:
                                        return "NB"
                        else:
                            # if Nest_Dist_RL_To_Bbox_BL <= 25.0000000000
                            if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 25.0000000000:
                                return "ONE"
                            else:
                                # if Actor_Dist_RT_To_Bbox_TR <= 116.5000000000
                                if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 116.5000000000:
                                    # if Actor_Centroid_To_Bbox_BL <= 162.2197189331
                                    if _get(features, "Actor_Centroid_To_Bbox_BL") <= 162.2197189331:
                                        return "NB"
                                    else:
                                        return "ONE"
                                else:
                                    # if Actor_Dist_RT_To_Bbox_TL <= 97.5000000000
                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 97.5000000000:
                                        # if Actor_Dist_RL_To_Bbox_TL <= 146.5000000000
                                        if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 146.5000000000:
                                            # if Actor_perimeter <= 949.2138061523
                                            if _get(features, "Actor_perimeter") <= 949.2138061523:
                                                # if Actor_Area_Diff_Abs <= 259.7500000000
                                                if _get(features, "Actor_Area_Diff_Abs") <= 259.7500000000:
                                                    # if Actor_Centroid_To_Bbox_TR <= 168.5030441284
                                                    if _get(features, "Actor_Centroid_To_Bbox_TR") <= 168.5030441284:
                                                        # if Actor_Centroid_To_Bbox_TL <= 157.5893554688
                                                        if _get(features, "Actor_Centroid_To_Bbox_TL") <= 157.5893554688:
                                                            return "NB"
                                                        else:
                                                            return "OE"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    # if Actor_perimeter <= 948.3351440430
                                                    if _get(features, "Actor_perimeter") <= 948.3351440430:
                                                        return "OE"
                                                    else:
                                                        return "ONE"
                                            else:
                                                # if Nest_Dist_RL_To_Bbox_BR <= 458.7524414062
                                                if _get(features, "Nest_Dist_RL_To_Bbox_BR") <= 458.7524414062:
                                                    return "OE"
                                                else:
                                                    return "ONE"
                                        else:
                                            return "ONE"
                                    else:
                                        # if Nest_Dist_RB_To_Bbox_TL <= 413.6068420410
                                        if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 413.6068420410:
                                            # if pipeEnd_Rat_Distance <= 517.9934387207
                                            if _get(features, "pipeEnd_Rat_Distance") <= 517.9934387207:
                                                # if Actor_eccentricity <= 0.6758790314
                                                if _get(features, "Actor_eccentricity") <= 0.6758790314:
                                                    # if Actor_Dist_RL_RR <= 232.8062438965
                                                    if _get(features, "Actor_Dist_RL_RR") <= 232.8062438965:
                                                        return "OE"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    return "OE"
                                            else:
                                                # if foodhopperRight_Nest_Distance <= 456.2838897705
                                                if _get(features, "foodhopperRight_Nest_Distance") <= 456.2838897705:
                                                    return "NB"
                                                else:
                                                    # if Actor_area <= 31566.0000000000
                                                    if _get(features, "Actor_area") <= 31566.0000000000:
                                                        return "NB"
                                                    else:
                                                        # if Actor_RB_y <= 570.5000000000
                                                        if _get(features, "Actor_RB_y") <= 570.5000000000:
                                                            return "NB"
                                                        else:
                                                            # if Actor_Mask_IoU <= 0.9928132296
                                                            if _get(features, "Actor_Mask_IoU") <= 0.9928132296:
                                                                # if Actor_RL_y <= 587.5000000000
                                                                if _get(features, "Actor_RL_y") <= 587.5000000000:
                                                                    # if Actor_Dist_RB_To_Bbox_TR <= 241.5481262207
                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 241.5481262207:
                                                                        # if Actor_RB_y <= 628.0000000000
                                                                        if _get(features, "Actor_RB_y") <= 628.0000000000:
                                                                            return "OE"
                                                                        else:
                                                                            return "ONE"
                                                                    else:
                                                                        # if Actor_Dist_RT_To_Bbox_TL <= 99.5000000000
                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 99.5000000000:
                                                                            # if Actor_RL_y <= 534.0000000000
                                                                            if _get(features, "Actor_RL_y") <= 534.0000000000:
                                                                                return "ONE"
                                                                            else:
                                                                                # if Actor_Dist_RL_To_Bbox_TR <= 287.0178985596
                                                                                if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 287.0178985596:
                                                                                    return "OE"
                                                                                else:
                                                                                    # if Actor_extent <= 0.6903742254
                                                                                    if _get(features, "Actor_extent") <= 0.6903742254:
                                                                                        return "OE"
                                                                                    else:
                                                                                        return "ONE"
                                                                        else:
                                                                            # if Actor_area <= 32010.7500000000
                                                                            if _get(features, "Actor_area") <= 32010.7500000000:
                                                                                # if Actor_Centroid_To_Bbox_TR <= 158.2806320190
                                                                                if _get(features, "Actor_Centroid_To_Bbox_TR") <= 158.2806320190:
                                                                                    return "OE"
                                                                                else:
                                                                                    return "NB"
                                                                            else:
                                                                                return "OE"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                return "ONE"
                                        else:
                                            return "ONE"
                else:
                    # if Nest_RB_y <= 617.5000000000
                    if _get(features, "Nest_RB_y") <= 617.5000000000:
                        # if Actor_bbox_x <= 76.5000000000
                        if _get(features, "Actor_bbox_x") <= 76.5000000000:
                            return "ONE"
                        else:
                            return "NB"
                    else:
                        # if Actor_Dist_RL_To_Bbox_TR <= 327.1253356934
                        if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 327.1253356934:
                            # if Nest_RR_y <= 524.5000000000
                            if _get(features, "Nest_RR_y") <= 524.5000000000:
                                # if Actor_Dist_RL_To_Bbox_BL <= 37.0000000000
                                if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 37.0000000000:
                                    # if Nest_Dist_RL_To_Bbox_BL <= 35.5000000000
                                    if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 35.5000000000:
                                        # if Actor_Dist_RR_To_Bbox_BL <= 294.5997161865
                                        if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 294.5997161865:
                                            return "ONE"
                                        else:
                                            return "OE"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_BR <= 109.5045661926
                                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 109.5045661926:
                                            # if Nest_centroid_y <= 536.8908691406
                                            if _get(features, "Nest_centroid_y") <= 536.8908691406:
                                                return "ONE"
                                            else:
                                                return "NB"
                                        else:
                                            return "OE"
                                else:
                                    # if Actor_Dist_RT_RB <= 243.0549545288
                                    if _get(features, "Actor_Dist_RT_RB") <= 243.0549545288:
                                        return "OE"
                                    else:
                                        return "ONE"
                            else:
                                # if Actor_RT_x <= 1059.5000000000
                                if _get(features, "Actor_RT_x") <= 1059.5000000000:
                                    # if Nest_hu_0 <= 0.2555862069
                                    if _get(features, "Nest_hu_0") <= 0.2555862069:
                                        return "OE"
                                    else:
                                        # if Actor_area <= 35341.5000000000
                                        if _get(features, "Actor_area") <= 35341.5000000000:
                                            # if Actor_Dist_RR_RB <= 50.3884563446
                                            if _get(features, "Actor_Dist_RR_RB") <= 50.3884563446:
                                                # if Actor_extent <= 0.6627372801
                                                if _get(features, "Actor_extent") <= 0.6627372801:
                                                    return "ONE"
                                                else:
                                                    return "NB"
                                            else:
                                                # if Actor_Dist_RB_To_Bbox_BL <= 267.5018615723
                                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 267.5018615723:
                                                    # if Actor_RL_y <= 587.0000000000
                                                    if _get(features, "Actor_RL_y") <= 587.0000000000:
                                                        return "ONE"
                                                    else:
                                                        # if Actor_bbox_w <= 288.0000000000
                                                        if _get(features, "Actor_bbox_w") <= 288.0000000000:
                                                            return "ONE"
                                                        else:
                                                            return "NB"
                                                else:
                                                    # if Actor_Dist_RR_To_Bbox_TR <= 88.5056800842
                                                    if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 88.5056800842:
                                                        return "ONE"
                                                    else:
                                                        return "NB"
                                        else:
                                            return "NB"
                                else:
                                    # if Actor_hu_5 <= 0.0000527500
                                    if _get(features, "Actor_hu_5") <= 0.0000527500:
                                        return "NB"
                                    else:
                                        return "ONE"
                        else:
                            # if Actor_perimeter <= 1065.7493286133
                            if _get(features, "Actor_perimeter") <= 1065.7493286133:
                                # if Actor_extent <= 0.5992330909
                                if _get(features, "Actor_extent") <= 0.5992330909:
                                    # if Nest_RL_y <= 609.5000000000
                                    if _get(features, "Nest_RL_y") <= 609.5000000000:
                                        return "ONE"
                                    else:
                                        # if Nest_bbox_w <= 442.0000000000
                                        if _get(features, "Nest_bbox_w") <= 442.0000000000:
                                            return "OE"
                                        else:
                                            return "NB"
                                else:
                                    # if Actor_centroid_y <= 555.7179870605
                                    if _get(features, "Actor_centroid_y") <= 555.7179870605:
                                        # if Actor_Dist_RT_To_Bbox_BR <= 182.5335464478
                                        if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 182.5335464478:
                                            return "ONE"
                                        else:
                                            # if Actor_Dist_RL_To_Bbox_TR <= 400.4301605225
                                            if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 400.4301605225:
                                                # if Actor_Dist_RL_RR <= 320.0132751465
                                                if _get(features, "Actor_Dist_RL_RR") <= 320.0132751465:
                                                    # if Actor_Dist_RB_To_Bbox_TL <= 320.5065460205
                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 320.5065460205:
                                                        # if Actor_area <= 36816.0000000000
                                                        if _get(features, "Actor_area") <= 36816.0000000000:
                                                            # if c2_Rat_Distance <= 601.7926025391
                                                            if _get(features, "c2_Rat_Distance") <= 601.7926025391:
                                                                # if Actor_extent <= 0.6382584572
                                                                if _get(features, "Actor_extent") <= 0.6382584572:
                                                                    return "NB"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                # if Actor_Dist_RB_To_Bbox_TR <= 163.7482757568
                                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 163.7482757568:
                                                                    # if Actor_Dist_RL_To_Bbox_TR <= 337.5149230957
                                                                    if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 337.5149230957:
                                                                        return "NB"
                                                                    else:
                                                                        return "ONE"
                                                                else:
                                                                    # if Actor_Dist_RL_To_Bbox_TL <= 115.5000000000
                                                                    if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 115.5000000000:
                                                                        # if Actor_Dist_RR_To_Bbox_BL <= 310.8333435059
                                                                        if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 310.8333435059:
                                                                            return "ONE"
                                                                        else:
                                                                            return "NB"
                                                                    else:
                                                                        return "NB"
                                                        else:
                                                            # if Actor_Dist_RR_RB <= 143.7898597717
                                                            if _get(features, "Actor_Dist_RR_RB") <= 143.7898597717:
                                                                return "ONE"
                                                            else:
                                                                return "OE"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    # if Actor_Dist_RT_RB <= 162.5238189697
                                                    if _get(features, "Actor_Dist_RT_RB") <= 162.5238189697:
                                                        # if Actor_RR_y <= 599.5000000000
                                                        if _get(features, "Actor_RR_y") <= 599.5000000000:
                                                            return "ONE"
                                                        else:
                                                            return "NB"
                                                    else:
                                                        return "NB"
                                            else:
                                                return "ONE"
                                    else:
                                        return "ONE"
                            else:
                                # if pipeMid_Nest_Distance <= 323.6409606934
                                if _get(features, "pipeMid_Nest_Distance") <= 323.6409606934:
                                    # if Nest_RR_y <= 513.0000000000
                                    if _get(features, "Nest_RR_y") <= 513.0000000000:
                                        # if c2_Nest_Distance <= 1107.8635253906
                                        if _get(features, "c2_Nest_Distance") <= 1107.8635253906:
                                            return "ONE"
                                        else:
                                            return "NB"
                                    else:
                                        return "OE"
                                else:
                                    # if pipeEnd_Rat_Distance <= 618.9777221680
                                    if _get(features, "pipeEnd_Rat_Distance") <= 618.9777221680:
                                        # if c3_Rat_Distance <= 254.2545776367
                                        if _get(features, "c3_Rat_Distance") <= 254.2545776367:
                                            # if Actor_centroid_y <= 556.2276306152
                                            if _get(features, "Actor_centroid_y") <= 556.2276306152:
                                                return "ONE"
                                            else:
                                                return "NB"
                                        else:
                                            return "ONE"
                                    else:
                                        return "NB"
        else:
            # if Nest_RL_y <= 645.5000000000
            if _get(features, "Nest_RL_y") <= 645.5000000000:
                # if Actor_To_Nest_Distance <= 836.6520385742
                if _get(features, "Actor_To_Nest_Distance") <= 836.6520385742:
                    # if Nest_RB_x <= 1139.0000000000
                    if _get(features, "Nest_RB_x") <= 1139.0000000000:
                        # if Nest_area <= 36422.7500000000
                        if _get(features, "Nest_area") <= 36422.7500000000:
                            # if Actor_hu_6 <= -0.0000653500
                            if _get(features, "Actor_hu_6") <= -0.0000653500:
                                # if foodhopperMid_Nest_Distance <= 475.6659851074
                                if _get(features, "foodhopperMid_Nest_Distance") <= 475.6659851074:
                                    # if Actor_Centroid_To_Bbox_BR <= 214.1024093628
                                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 214.1024093628:
                                        return "ONE"
                                    else:
                                        return "OE"
                                else:
                                    return "OE"
                            else:
                                # if Nest_hu_5 <= 0.0086705941
                                if _get(features, "Nest_hu_5") <= 0.0086705941:
                                    # if Actor_hu_5 <= 0.0350434761
                                    if _get(features, "Actor_hu_5") <= 0.0350434761:
                                        # if Actor_Dist_RB_RL <= 262.7784118652
                                        if _get(features, "Actor_Dist_RB_RL") <= 262.7784118652:
                                            # if Nest_Dist_RT_RR <= 71.5751342773
                                            if _get(features, "Nest_Dist_RT_RR") <= 71.5751342773:
                                                # if Actor_solidity <= 0.6508905292
                                                if _get(features, "Actor_solidity") <= 0.6508905292:
                                                    # if Actor_Dist_RT_To_Bbox_TL <= 65.0000000000
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 65.0000000000:
                                                        return "OE"
                                                    else:
                                                        # if Nest_RR_x <= 510.5000000000
                                                        if _get(features, "Nest_RR_x") <= 510.5000000000:
                                                            return "OE"
                                                        else:
                                                            return "ONE"
                                                else:
                                                    # if Nest_orientation <= 64.6379241943
                                                    if _get(features, "Nest_orientation") <= 64.6379241943:
                                                        return "ONE"
                                                    else:
                                                        # if Nest_Dist_RT_RR <= 71.5576705933
                                                        if _get(features, "Nest_Dist_RT_RR") <= 71.5576705933:
                                                            # if c4_Rat_Distance <= 554.9430847168
                                                            if _get(features, "c4_Rat_Distance") <= 554.9430847168:
                                                                return "ONE"
                                                            else:
                                                                # if Nest_Centroid_To_Bbox_BL <= 243.2268981934
                                                                if _get(features, "Nest_Centroid_To_Bbox_BL") <= 243.2268981934:
                                                                    # if Actor_RL_y <= 561.5000000000
                                                                    if _get(features, "Actor_RL_y") <= 561.5000000000:
                                                                        # if Actor_Dist_RT_To_Bbox_TL <= 0.5000000000
                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 0.5000000000:
                                                                            # if Nest_Dist_RL_RR <= 350.1537628174
                                                                            if _get(features, "Nest_Dist_RL_RR") <= 350.1537628174:
                                                                                return "ONE"
                                                                            else:
                                                                                return "OE"
                                                                        else:
                                                                            # if Nest_Area_Diff_Abs <= 3135.2500000000
                                                                            if _get(features, "Nest_Area_Diff_Abs") <= 3135.2500000000:
                                                                                return "OE"
                                                                            else:
                                                                                # if Actor_Dist_RR_To_Bbox_BR <= 160.5031204224
                                                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 160.5031204224:
                                                                                    return "OE"
                                                                                else:
                                                                                    return "ONE"
                                                                    else:
                                                                        # if Actor_perimeter <= 286.1284637451
                                                                        if _get(features, "Actor_perimeter") <= 286.1284637451:
                                                                            return "OE"
                                                                        else:
                                                                            return "ONE"
                                                                else:
                                                                    return "ONE"
                                                        else:
                                                            return "ONE"
                                            else:
                                                # if Actor_RB_x <= 145.5000000000
                                                if _get(features, "Actor_RB_x") <= 145.5000000000:
                                                    return "ONE"
                                                else:
                                                    # if Actor_bbox_y <= 487.0000000000
                                                    if _get(features, "Actor_bbox_y") <= 487.0000000000:
                                                        # if Actor_solidity <= 0.4971318990
                                                        if _get(features, "Actor_solidity") <= 0.4971318990:
                                                            # if Nest_RL_x <= 464.5000000000
                                                            if _get(features, "Nest_RL_x") <= 464.5000000000:
                                                                return "OE"
                                                            else:
                                                                return "ONE"
                                                        else:
                                                            # if Actor_Dist_RL_To_Bbox_TL <= 3.5000000000
                                                            if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 3.5000000000:
                                                                # if c4_Rat_Distance <= 912.3089294434
                                                                if _get(features, "c4_Rat_Distance") <= 912.3089294434:
                                                                    return "ONE"
                                                                else:
                                                                    return "OE"
                                                            else:
                                                                # if Nest_hu_6 <= 0.0001318380
                                                                if _get(features, "Nest_hu_6") <= 0.0001318380:
                                                                    # if Actor_hu_0 <= 0.5167745948
                                                                    if _get(features, "Actor_hu_0") <= 0.5167745948:
                                                                        return "OE"
                                                                    else:
                                                                        # if Nest_bbox_w <= 349.0000000000
                                                                        if _get(features, "Nest_bbox_w") <= 349.0000000000:
                                                                            return "ONE"
                                                                        else:
                                                                            return "OE"
                                                                else:
                                                                    # if Actor_Dist_RR_To_Bbox_TR <= 28.0190391541
                                                                    if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 28.0190391541:
                                                                        return "ONE"
                                                                    else:
                                                                        # if Actor_To_Nest_Dist_Change <= -53.3718013763
                                                                        if _get(features, "Actor_To_Nest_Dist_Change") <= -53.3718013763:
                                                                            return "ONE"
                                                                        else:
                                                                            return "OE"
                                                    else:
                                                        # if Actor_aspect_ratio <= 0.8695652187
                                                        if _get(features, "Actor_aspect_ratio") <= 0.8695652187:
                                                            return "ONE"
                                                        else:
                                                            return "OE"
                                        else:
                                            # if Nest_RT_x <= 473.0000000000
                                            if _get(features, "Nest_RT_x") <= 473.0000000000:
                                                # if Actor_hu_0 <= 0.4019902647
                                                if _get(features, "Actor_hu_0") <= 0.4019902647:
                                                    # if Nest_Dist_RT_To_Bbox_TL <= 209.5000000000
                                                    if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 209.5000000000:
                                                        # if Actor_Dist_RT_To_Bbox_BL <= 268.1444854736
                                                        if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 268.1444854736:
                                                            # if Nest_Dist_RB_RL <= 78.3916320801
                                                            if _get(features, "Nest_Dist_RB_RL") <= 78.3916320801:
                                                                # if Actor_Centroid_To_Bbox_TR <= 149.2511520386
                                                                if _get(features, "Actor_Centroid_To_Bbox_TR") <= 149.2511520386:
                                                                    return "ONE"
                                                                else:
                                                                    return "OE"
                                                            else:
                                                                return "OE"
                                                        else:
                                                            return "OE"
                                                    else:
                                                        # if Actor_Dist_RL_To_Bbox_BL <= 22.0000000000
                                                        if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 22.0000000000:
                                                            return "ONE"
                                                        else:
                                                            # if Actor_Dist_RL_RR <= 241.0701370239
                                                            if _get(features, "Actor_Dist_RL_RR") <= 241.0701370239:
                                                                # if Actor_bbox_y <= 343.5000000000
                                                                if _get(features, "Actor_bbox_y") <= 343.5000000000:
                                                                    return "OE"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                return "OE"
                                                else:
                                                    # if Nest_Dist_RB_To_Bbox_BL <= 64.0079708099
                                                    if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 64.0079708099:
                                                        return "OE"
                                                    else:
                                                        return "ONE"
                                            else:
                                                # if Actor_aspect_ratio <= 0.5447491407
                                                if _get(features, "Actor_aspect_ratio") <= 0.5447491407:
                                                    # if Actor_Centroid_To_Bbox_BR <= 297.5288085938
                                                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 297.5288085938:
                                                        # if Actor_aspect_ratio <= 0.5408543050
                                                        if _get(features, "Actor_aspect_ratio") <= 0.5408543050:
                                                            return "OE"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        # if Actor_centroid_x <= 127.6584434509
                                                        if _get(features, "Actor_centroid_x") <= 127.6584434509:
                                                            # if Nest_Dist_RR_To_Bbox_TL <= 241.2133789062
                                                            if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 241.2133789062:
                                                                return "ONE"
                                                            else:
                                                                return "OE"
                                                        else:
                                                            return "ONE"
                                                else:
                                                    # if Actor_Dist_RT_To_Bbox_TL <= 430.5000000000
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 430.5000000000:
                                                        # if Actor_Mask_IoU <= 0.2270213068
                                                        if _get(features, "Actor_Mask_IoU") <= 0.2270213068:
                                                            # if Actor_Dist_RL_To_Bbox_BL <= 113.5000000000
                                                            if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 113.5000000000:
                                                                return "OE"
                                                            else:
                                                                return "ONE"
                                                        else:
                                                            # if c2_Nest_Distance <= 712.2463073730
                                                            if _get(features, "c2_Nest_Distance") <= 712.2463073730:
                                                                # if c2_Nest_Distance <= 711.9151000977
                                                                if _get(features, "c2_Nest_Distance") <= 711.9151000977:
                                                                    # if Actor_bbox_y <= 375.5000000000
                                                                    if _get(features, "Actor_bbox_y") <= 375.5000000000:
                                                                        # if Nest_Centroid_To_Bbox_TR <= 136.7100830078
                                                                        if _get(features, "Nest_Centroid_To_Bbox_TR") <= 136.7100830078:
                                                                            # if Actor_hu_5 <= 0.0000881112
                                                                            if _get(features, "Actor_hu_5") <= 0.0000881112:
                                                                                return "OE"
                                                                            else:
                                                                                return "ONE"
                                                                        else:
                                                                            return "OE"
                                                                    else:
                                                                        return "ONE"
                                                                else:
                                                                    # if pipeMid_Nest_Distance <= 405.7074127197
                                                                    if _get(features, "pipeMid_Nest_Distance") <= 405.7074127197:
                                                                        return "OE"
                                                                    else:
                                                                        return "ONE"
                                                            else:
                                                                # if Actor_hu_0 <= 0.4913807809
                                                                if _get(features, "Actor_hu_0") <= 0.4913807809:
                                                                    # if Actor_Dist_RT_To_Bbox_TR <= 342.5000000000
                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 342.5000000000:
                                                                        # if Nest_Centroid_To_Bbox_TL <= 254.1548538208
                                                                        if _get(features, "Nest_Centroid_To_Bbox_TL") <= 254.1548538208:
                                                                            return "OE"
                                                                        else:
                                                                            # if c3_Nest_Distance <= 947.9724121094
                                                                            if _get(features, "c3_Nest_Distance") <= 947.9724121094:
                                                                                return "ONE"
                                                                            else:
                                                                                return "OE"
                                                                    else:
                                                                        # if Actor_Centroid_To_Bbox_BR <= 151.2993087769
                                                                        if _get(features, "Actor_Centroid_To_Bbox_BR") <= 151.2993087769:
                                                                            return "ONE"
                                                                        else:
                                                                            # if Nest_Dist_RL_To_Bbox_BL <= 48.5000000000
                                                                            if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 48.5000000000:
                                                                                # if Actor_centroid_y <= 514.1199340820
                                                                                if _get(features, "Actor_centroid_y") <= 514.1199340820:
                                                                                    return "OE"
                                                                                else:
                                                                                    # if c4_Rat_Distance <= 863.3888244629
                                                                                    if _get(features, "c4_Rat_Distance") <= 863.3888244629:
                                                                                        return "ONE"
                                                                                    else:
                                                                                        return "OE"
                                                                            else:
                                                                                return "ONE"
                                                                else:
                                                                    # if Actor_Dist_RL_To_Bbox_TL <= 36.0000000000
                                                                    if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 36.0000000000:
                                                                        return "OE"
                                                                    else:
                                                                        return "ONE"
                                                    else:
                                                        # if foodhopperLeft_Rat_Distance <= 360.7525939941
                                                        if _get(features, "foodhopperLeft_Rat_Distance") <= 360.7525939941:
                                                            # if Actor_hu_5 <= 0.0002433730
                                                            if _get(features, "Actor_hu_5") <= 0.0002433730:
                                                                return "OE"
                                                            else:
                                                                return "ONE"
                                                        else:
                                                            # if Actor_Dist_RR_To_Bbox_BL <= 564.0215759277
                                                            if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 564.0215759277:
                                                                # if Nest_Centroid_To_Bbox_TR <= 137.0970764160
                                                                if _get(features, "Nest_Centroid_To_Bbox_TR") <= 137.0970764160:
                                                                    return "ONE"
                                                                else:
                                                                    return "OE"
                                                            else:
                                                                return "ONE"
                                    else:
                                        # if Actor_extent <= 0.3221880943
                                        if _get(features, "Actor_extent") <= 0.3221880943:
                                            return "OE"
                                        else:
                                            # if Actor_RR_y <= 532.0000000000
                                            if _get(features, "Actor_RR_y") <= 532.0000000000:
                                                return "OE"
                                            else:
                                                return "ONE"
                                else:
                                    # if Actor_bbox_x <= 376.0000000000
                                    if _get(features, "Actor_bbox_x") <= 376.0000000000:
                                        # if Actor_bbox_y <= 262.0000000000
                                        if _get(features, "Actor_bbox_y") <= 262.0000000000:
                                            return "OE"
                                        else:
                                            # if Nest_area <= 15681.0000000000
                                            if _get(features, "Nest_area") <= 15681.0000000000:
                                                return "ONE"
                                            else:
                                                return "OE"
                                    else:
                                        # if Actor_Dist_RB_To_Bbox_BL <= 403.0012359619
                                        if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 403.0012359619:
                                            # if Actor_centroid_x <= 1081.0578002930
                                            if _get(features, "Actor_centroid_x") <= 1081.0578002930:
                                                # if Actor_solidity <= 0.7381038368
                                                if _get(features, "Actor_solidity") <= 0.7381038368:
                                                    # if Nest_RB_x <= 791.5000000000
                                                    if _get(features, "Nest_RB_x") <= 791.5000000000:
                                                        return "ONE"
                                                    else:
                                                        return "OE"
                                                else:
                                                    return "OE"
                                            else:
                                                # if Actor_bbox_h <= 187.5000000000
                                                if _get(features, "Actor_bbox_h") <= 187.5000000000:
                                                    # if Nest_Area_Diff_Abs <= 35.2500000000
                                                    if _get(features, "Nest_Area_Diff_Abs") <= 35.2500000000:
                                                        # if Actor_To_Nest_Distance <= 254.0151443481
                                                        if _get(features, "Actor_To_Nest_Distance") <= 254.0151443481:
                                                            return "ONE"
                                                        else:
                                                            return "OE"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    # if Actor_hu_0 <= 0.1826955974
                                                    if _get(features, "Actor_hu_0") <= 0.1826955974:
                                                        return "OE"
                                                    else:
                                                        return "ONE"
                                        else:
                                            # if Actor_RT_x <= 961.5000000000
                                            if _get(features, "Actor_RT_x") <= 961.5000000000:
                                                return "ONE"
                                            else:
                                                return "OE"
                        else:
                            # if Actor_RL_y <= 474.5000000000
                            if _get(features, "Actor_RL_y") <= 474.5000000000:
                                # if Nest_aspect_ratio <= 2.0196208954
                                if _get(features, "Nest_aspect_ratio") <= 2.0196208954:
                                    # if Nest_hu_3 <= 0.0000910500
                                    if _get(features, "Nest_hu_3") <= 0.0000910500:
                                        # if foodhopperBottom_Rat_Distance <= 116.2195701599
                                        if _get(features, "foodhopperBottom_Rat_Distance") <= 116.2195701599:
                                            return "OE"
                                        else:
                                            return "ONE"
                                    else:
                                        # if Nest_Mask_IoU <= 0.9773958921
                                        if _get(features, "Nest_Mask_IoU") <= 0.9773958921:
                                            return "OE"
                                        else:
                                            # if foodhopperRight_Nest_Distance <= 827.6168823242
                                            if _get(features, "foodhopperRight_Nest_Distance") <= 827.6168823242:
                                                return "OE"
                                            else:
                                                return "ONE"
                                else:
                                    # if Actor_Centroid_To_Bbox_BL <= 293.5713500977
                                    if _get(features, "Actor_Centroid_To_Bbox_BL") <= 293.5713500977:
                                        # if Nest_Centroid_To_Bbox_BL <= 245.4164199829
                                        if _get(features, "Nest_Centroid_To_Bbox_BL") <= 245.4164199829:
                                            return "ONE"
                                        else:
                                            return "OE"
                                    else:
                                        return "OE"
                            else:
                                # if Nest_RR_y <= 525.0000000000
                                if _get(features, "Nest_RR_y") <= 525.0000000000:
                                    return "OE"
                                else:
                                    return "ONE"
                    else:
                        # if Actor_centroid_y <= 454.9903717041
                        if _get(features, "Actor_centroid_y") <= 454.9903717041:
                            return "OE"
                        else:
                            return "ONE"
                else:
                    # if Actor_aspect_ratio <= 2.2633981705
                    if _get(features, "Actor_aspect_ratio") <= 2.2633981705:
                        # if Nest_RL_x <= 3.5000000000
                        if _get(features, "Nest_RL_x") <= 3.5000000000:
                            return "ONE"
                        else:
                            return "OE"
                    else:
                        return "ONE"
            else:
                # if pipeMid_Rat_Distance <= 59.3530464172
                if _get(features, "pipeMid_Rat_Distance") <= 59.3530464172:
                    # if Actor_perimeter <= 561.4162902832
                    if _get(features, "Actor_perimeter") <= 561.4162902832:
                        return "OE"
                    else:
                        # if Nest_Dist_RL_To_Bbox_TR <= 401.2607269287
                        if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 401.2607269287:
                            return "OE"
                        else:
                            # if Actor_orientation <= 33.2642345428
                            if _get(features, "Actor_orientation") <= 33.2642345428:
                                return "ONE"
                            else:
                                # if Actor_Mask_IoU <= 0.9561573267
                                if _get(features, "Actor_Mask_IoU") <= 0.9561573267:
                                    return "OE"
                                else:
                                    return "ONE"
                else:
                    # if Nest_solidity <= 0.8703053594
                    if _get(features, "Nest_solidity") <= 0.8703053594:
                        # if Nest_eccentricity <= 0.9266214669
                        if _get(features, "Nest_eccentricity") <= 0.9266214669:
                            # if Actor_Dist_RB_To_Bbox_TL <= 194.3244781494
                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 194.3244781494:
                                return "ONE"
                            else:
                                return "OE"
                        else:
                            # if Nest_RB_y <= 655.5000000000
                            if _get(features, "Nest_RB_y") <= 655.5000000000:
                                return "ONE"
                            else:
                                return "OE"
                    else:
                        return "ONE"
    else:
        # if pipeStart_Rat_Distance <= 439.6889343262
        if _get(features, "pipeStart_Rat_Distance") <= 439.6889343262:
            # if Nest_eccentricity <= 0.9618000984
            if _get(features, "Nest_eccentricity") <= 0.9618000984:
                # if Nest_Dist_RT_To_Bbox_TR <= 12.0000000000
                if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 12.0000000000:
                    # if Nest_Dist_RR_To_Bbox_BR <= 134.0037574768
                    if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 134.0037574768:
                        return "OE"
                    else:
                        # if Nest_Centroid_To_Bbox_TL <= 235.7050399780
                        if _get(features, "Nest_Centroid_To_Bbox_TL") <= 235.7050399780:
                            return "NB"
                        else:
                            return "ONE"
                else:
                    # if c1_Rat_Distance <= 533.2679748535
                    if _get(features, "c1_Rat_Distance") <= 533.2679748535:
                        return "ONE"
                    else:
                        # if Actor_area <= 37562.0000000000
                        if _get(features, "Actor_area") <= 37562.0000000000:
                            return "OE"
                        else:
                            # if Nest_Dist_RT_To_Bbox_TR <= 16.5000000000
                            if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 16.5000000000:
                                # if Actor_Dist_RT_To_Bbox_TR <= 166.5000000000
                                if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 166.5000000000:
                                    return "NB"
                                else:
                                    return "OE"
                            else:
                                return "NB"
            else:
                # if Actor_Dist_RR_To_Bbox_TL <= 322.3756408691
                if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 322.3756408691:
                    # if Actor_Area_Diff_Abs <= 1178.0000000000
                    if _get(features, "Actor_Area_Diff_Abs") <= 1178.0000000000:
                        return "ONE"
                    else:
                        return "NB"
                else:
                    return "OE"
        else:
            # if foodhopperLeft_Nest_Distance <= 517.6102447510
            if _get(features, "foodhopperLeft_Nest_Distance") <= 517.6102447510:
                return "ONE"
            else:
                return "OE"


def _gate_pi_si_from_ratio(x):
    # flip=False: x <= t -> PI, else SI
    # flip=True : x <= t -> SI, else PI
    if x != x:  # NaN
        return "PI"
    if not RATIO_FLIP:
        return "PI" if x <= RATIO_THRESH else "SI"
    else:
        return "SI" if x <= RATIO_THRESH else "PI"

def predict_row(features: dict):
    """Return one of: 'PI','SI','OE','ONE','NB'"""
    route = router_tree_predict(features)   # 'PI_SI' or 'OENB'
    if route == "PI_SI":
        ar = _get(features, RATIO_FEATURE)
        return _gate_pi_si_from_ratio(ar)
    else:
        return oenb_tree_predict(features)

def predict_df(df, gt_col=None, unify=True, print_report=True):
    import pandas as _pd
    import numpy as _np

    def _unify_cols(cols):
        out = []
        for c in cols:
            c = str(c)
            if c.startswith("Mouse_"):
                out.append("Actor_" + c[len("Mouse_"):])
            elif c.startswith("Rat_"):
                out.append("Actor_" + c[len("Rat_"):])
            else:
                out.append(c)
        return out

    work = df.copy()
    if unify:
        work.columns = _unify_cols(work.columns)

    need = set(ROUTER_COLS) | set(OENB_COLS) | {RATIO_FEATURE}
    preds = []
    for _, row in work.iterrows():
        feat_map = {k: row[k] for k in need if k in work.columns}
        preds.append(predict_row(feat_map))

    out = df.copy()
    out["Predicted_Activity"] = preds

    # Ground-truth accuracy (optional)
    if print_report:
        if gt_col is None:
            for c in df.columns:
                if "activity" in str(c).lower():
                    gt_col = c
                    break
        if gt_col is not None and gt_col in df.columns:
            try:
                from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
                y_true = df[gt_col].astype(str).str.strip()
                y_pred = _pd.Series(preds, index=df.index)
                acc = accuracy_score(y_true, y_pred)
                print(f"Accuracy: {acc:.4f}")
                labs = ["PI","SI","OE","ONE","NB"]
                print(classification_report(y_true, y_pred, labels=labs, digits=3))
                print("Confusion Matrix (PI,SI,OE,ONE,NB):\n", confusion_matrix(y_true, y_pred, labels=labs))
            except Exception:
                pass

    return out
