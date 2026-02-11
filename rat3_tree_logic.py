# THIS FILE IS AUTO-GENERATED: pure if/else logic for your hierarchical classifier.
# Requires only Python + numpy/pandas at runtime (sklearn not required).
# Do not edit by hand; regenerate after retraining.

import numpy as np

# --- constants learned at training time ---
ROUTER_COLS = ["Pups_Location_Rat_Distance", "Actor_bbox_x", "pipeEnd_Rat_Distance", "Actor_RL_x", "Actor_Dist_RT_To_Bbox_TL", "foodhopperBottom_Rat_Distance", "c1_Rat_Distance", "Actor_centroid_x", "pipeStart_Rat_Distance", "c3_Rat_Distance", "pipeMid_Rat_Distance", "c2_Rat_Distance", "foodhopperLeft_Rat_Distance", "Nest_bbox_x", "c4_Rat_Distance", "foodhopperMid_Rat_Distance", "Actor_RL_y", "Nest_RL_x", "Nest_Dist_RB_RL", "Nest_Dist_RB_To_Bbox_BL", "Actor_RB_y", "Nest_Dist_RB_To_Bbox_TL", "foodhopperRight_Nest_Distance", "Actor_Dist_RL_To_Bbox_TL", "Actor_centroid_y", "Nest_Centroid_To_Bbox_TL", "Actor_Dist_RL_To_Bbox_BL", "Nest_Dist_RT_RB", "Nest_Dist_RT_To_Bbox_BR", "Actor_Dist_RT_To_Bbox_BL", "Nest_RL_y", "Actor_RT_x", "Actor_RT_y", "c2_Nest_Distance", "Actor_To_Nest_Distance", "Nest_RT_x", "Actor_bbox_y", "Nest_RB_x", "Nest_extent", "c4_Nest_Distance", "Nest_Dist_RB_To_Bbox_BR", "foodhopperRight_Rat_Distance", "Nest_Dist_RT_To_Bbox_TR", "Actor_RR_x", "Nest_Dist_RT_RR", "Nest_Dist_RR_RB", "Nest_Centroid_To_Bbox_BL", "Nest_Dist_RL_To_Bbox_BL", "Nest_Dist_RB_To_Bbox_TR", "Nest_Dist_RR_To_Bbox_TL", "Nest_centroid_x", "Nest_Dist_RL_RR", "Nest_hu_1", "Nest_Centroid_To_Bbox_TR", "Pups_Location_Nest_Distance", "Nest_area", "Actor_Centroid_To_Bbox_TR", "c3_Nest_Distance", "Nest_Dist_RL_To_Bbox_TR", "pipeEnd_Nest_Distance", "Nest_hu_0", "Actor_Dist_RL_To_Bbox_BR", "Nest_centroid_y", "Nest_RR_x", "Nest_solidity", "Nest_Dist_RR_To_Bbox_BL", "pipeStart_Nest_Distance", "Actor_Dist_RL_RR", "Actor_Centroid_To_Bbox_TL", "Nest_Dist_RL_To_Bbox_BR", "pipeMid_Nest_Distance", "Actor_area", "Actor_Centroid_To_Bbox_BR", "foodhopperLeft_Nest_Distance", "Actor_Dist_RB_RL", "Nest_Centroid_To_Bbox_BR", "Nest_perimeter", "Actor_Centroid_To_Bbox_BL", "Actor_Dist_RL_To_Bbox_TR", "Actor_bbox_w", "Nest_Dist_RR_To_Bbox_BR", "c1_Nest_Distance", "Nest_hu_5", "Nest_RR_y", "Nest_Dist_RL_RT", "Actor_perimeter", "Nest_RB_y", "Actor_Dist_RR_To_Bbox_TL", "Actor_Dist_RL_RT", "foodhopperBottom_Nest_Distance", "Actor_Mask_IoU", "Nest_RT_y", "Nest_bbox_h", "Actor_Dist_RB_To_Bbox_TR", "Nest_Dist_RT_To_Bbox_BL", "Actor_RR_y", "Nest_hu_3", "Nest_bbox_w", "Actor_solidity", "Nest_Dist_RL_To_Bbox_TL", "Actor_Dist_RR_To_Bbox_BL", "Nest_bbox_y", "Nest_hu_6", "foodhopperMid_Nest_Distance", "Nest_aspect_ratio", "Actor_aspect_ratio", "Nest_Dist_RT_To_Bbox_TL", "Actor_eccentricity", "Nest_Dist_RR_To_Bbox_TR", "Nest_hu_2", "Actor_RB_x", "Actor_bbox_h", "Nest_orientation", "Actor_Dist_RT_To_Bbox_TR", "Actor_Dist_RT_RR", "Nest_eccentricity", "Actor_hu_0", "Actor_hu_2", "Actor_Dist_RT_To_Bbox_BR", "Actor_Dist_RB_To_Bbox_BL", "Nest_hu_4", "Nest_Mask_IoU", "Actor_Dist_RT_RB", "Actor_hu_3", "Actor_hu_1", "Actor_orientation", "Actor_hu_5", "Actor_extent", "Actor_Dist_RB_To_Bbox_TL", "Actor_Dist_RR_RB", "Actor_Dist_RR_To_Bbox_TR", "Actor_Dist_RB_To_Bbox_BR", "Nest_Area_Diff_Abs", "Actor_Area_Diff_Abs", "Actor_To_Nest_Dist_Change", "Actor_Dist_RR_To_Bbox_BR", "Actor_hu_6", "Actor_Direction_deg", "Actor_hu_4"]
OENB_COLS   = ["Actor_area", "Actor_perimeter", "Actor_centroid_x", "Actor_centroid_y", "Actor_bbox_x", "Actor_bbox_y", "Actor_bbox_w", "Actor_bbox_h", "Actor_aspect_ratio", "Actor_extent", "Actor_solidity", "Actor_orientation", "Actor_eccentricity", "Actor_RL_x", "Actor_RL_y", "Actor_RR_x", "Actor_RR_y", "Actor_RT_x", "Actor_RT_y", "Actor_RB_x", "Actor_RB_y", "Actor_hu_0", "Actor_hu_1", "Actor_hu_2", "Actor_hu_3", "Actor_hu_4", "Actor_hu_5", "Actor_hu_6", "Actor_Dist_RL_RR", "Actor_Dist_RT_RB", "Actor_Dist_RL_RT", "Actor_Dist_RT_RR", "Actor_Dist_RR_RB", "Actor_Dist_RB_RL", "Actor_Centroid_To_Bbox_TL", "Actor_Centroid_To_Bbox_TR", "Actor_Centroid_To_Bbox_BR", "Actor_Centroid_To_Bbox_BL", "Actor_Dist_RL_To_Bbox_TL", "Actor_Dist_RL_To_Bbox_TR", "Actor_Dist_RL_To_Bbox_BR", "Actor_Dist_RL_To_Bbox_BL", "Actor_Dist_RR_To_Bbox_TL", "Actor_Dist_RR_To_Bbox_TR", "Actor_Dist_RR_To_Bbox_BR", "Actor_Dist_RR_To_Bbox_BL", "Actor_Dist_RT_To_Bbox_TL", "Actor_Dist_RT_To_Bbox_TR", "Actor_Dist_RT_To_Bbox_BR", "Actor_Dist_RT_To_Bbox_BL", "Actor_Dist_RB_To_Bbox_TL", "Actor_Dist_RB_To_Bbox_TR", "Actor_Dist_RB_To_Bbox_BR", "Actor_Dist_RB_To_Bbox_BL", "Nest_area", "Nest_perimeter", "Nest_centroid_x", "Nest_centroid_y", "Nest_bbox_x", "Nest_bbox_y", "Nest_bbox_w", "Nest_bbox_h", "Nest_aspect_ratio", "Nest_extent", "Nest_solidity", "Nest_orientation", "Nest_eccentricity", "Nest_RL_x", "Nest_RL_y", "Nest_RR_x", "Nest_RR_y", "Nest_RT_x", "Nest_RT_y", "Nest_RB_x", "Nest_RB_y", "Nest_hu_0", "Nest_hu_1", "Nest_hu_2", "Nest_hu_3", "Nest_hu_4", "Nest_hu_5", "Nest_hu_6", "Nest_Dist_RL_RR", "Nest_Dist_RT_RB", "Nest_Dist_RL_RT", "Nest_Dist_RT_RR", "Nest_Dist_RR_RB", "Nest_Dist_RB_RL", "Nest_Centroid_To_Bbox_TL", "Nest_Centroid_To_Bbox_TR", "Nest_Centroid_To_Bbox_BR", "Nest_Centroid_To_Bbox_BL", "Nest_Dist_RL_To_Bbox_TL", "Nest_Dist_RL_To_Bbox_TR", "Nest_Dist_RL_To_Bbox_BR", "Nest_Dist_RL_To_Bbox_BL", "Nest_Dist_RR_To_Bbox_TL", "Nest_Dist_RR_To_Bbox_TR", "Nest_Dist_RR_To_Bbox_BR", "Nest_Dist_RR_To_Bbox_BL", "Nest_Dist_RT_To_Bbox_TL", "Nest_Dist_RT_To_Bbox_TR", "Nest_Dist_RT_To_Bbox_BR", "Nest_Dist_RT_To_Bbox_BL", "Nest_Dist_RB_To_Bbox_TL", "Nest_Dist_RB_To_Bbox_TR", "Nest_Dist_RB_To_Bbox_BR", "Nest_Dist_RB_To_Bbox_BL", "Actor_Area_Diff_Abs", "Actor_Mask_IoU", "Nest_Area_Diff_Abs", "Nest_Mask_IoU", "Actor_To_Nest_Distance", "Actor_Direction_deg", "Actor_To_Nest_Dist_Change", "c1_Rat_Distance", "c1_Nest_Distance", "c2_Rat_Distance", "c2_Nest_Distance", "c3_Rat_Distance", "c3_Nest_Distance", "c4_Rat_Distance", "c4_Nest_Distance", "pipeEnd_Rat_Distance", "pipeEnd_Nest_Distance", "pipeMid_Rat_Distance", "pipeMid_Nest_Distance", "pipeStart_Rat_Distance", "pipeStart_Nest_Distance", "foodhopperBottom_Rat_Distance", "foodhopperBottom_Nest_Distance", "foodhopperLeft_Rat_Distance", "foodhopperLeft_Nest_Distance", "foodhopperRight_Rat_Distance", "foodhopperRight_Nest_Distance", "foodhopperMid_Rat_Distance", "foodhopperMid_Nest_Distance", "Pups_Location_Rat_Distance", "Pups_Location_Nest_Distance"]
RATIO_FEATURE = "Actor_aspect_ratio"
RATIO_THRESH  = 0.8272003535
RATIO_FLIP    = True

def _get(d, k):
    try:
        return float(d.get(k, float("nan")))
    except Exception:
        return float("nan")


def router_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if c3_Rat_Distance <= 372.1563415527
    if _get(features, "c3_Rat_Distance") <= 372.1563415527:
        # if Actor_RL_y <= 454.5000000000
        if _get(features, "Actor_RL_y") <= 454.5000000000:
            # if Actor_perimeter <= 907.8670654297
            if _get(features, "Actor_perimeter") <= 907.8670654297:
                # if c2_Nest_Distance <= 658.0043945312
                if _get(features, "c2_Nest_Distance") <= 658.0043945312:
                    # if Actor_solidity <= 0.9334671199
                    if _get(features, "Actor_solidity") <= 0.9334671199:
                        # if Actor_hu_1 <= 0.0002239200
                        if _get(features, "Actor_hu_1") <= 0.0002239200:
                            # if Nest_RT_y <= 521.0000000000
                            if _get(features, "Nest_RT_y") <= 521.0000000000:
                                return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            return "PI_SI"
                    else:
                        # if Actor_Centroid_To_Bbox_TR <= 146.2350463867
                        if _get(features, "Actor_Centroid_To_Bbox_TR") <= 146.2350463867:
                            # if Nest_Dist_RB_RL <= 258.2931594849
                            if _get(features, "Nest_Dist_RB_RL") <= 258.2931594849:
                                return "PI_SI"
                            else:
                                return "OENB"
                        else:
                            return "OENB"
                else:
                    # if Actor_RT_x <= 1020.5000000000
                    if _get(features, "Actor_RT_x") <= 1020.5000000000:
                        return "OENB"
                    else:
                        return "PI_SI"
            else:
                # if Actor_area <= 48866.7500000000
                if _get(features, "Actor_area") <= 48866.7500000000:
                    # if Nest_hu_0 <= 0.8724102974
                    if _get(features, "Nest_hu_0") <= 0.8724102974:
                        # if Actor_perimeter <= 1274.4341430664
                        if _get(features, "Actor_perimeter") <= 1274.4341430664:
                            return "OENB"
                        else:
                            return "PI_SI"
                    else:
                        return "PI_SI"
                else:
                    # if Nest_RT_y <= 538.0000000000
                    if _get(features, "Nest_RT_y") <= 538.0000000000:
                        # if Nest_hu_6 <= -0.0000019960
                        if _get(features, "Nest_hu_6") <= -0.0000019960:
                            return "OENB"
                        else:
                            return "PI_SI"
                    else:
                        return "OENB"
        else:
            # if Nest_RB_x <= 1125.0000000000
            if _get(features, "Nest_RB_x") <= 1125.0000000000:
                # if foodhopperRight_Nest_Distance <= 445.9980163574
                if _get(features, "foodhopperRight_Nest_Distance") <= 445.9980163574:
                    # if Nest_area <= 20792.0000000000
                    if _get(features, "Nest_area") <= 20792.0000000000:
                        return "OENB"
                    else:
                        # if Actor_centroid_y <= 488.0038909912
                        if _get(features, "Actor_centroid_y") <= 488.0038909912:
                            return "PI_SI"
                        else:
                            return "OENB"
                else:
                    # if Actor_RB_x <= 854.5000000000
                    if _get(features, "Actor_RB_x") <= 854.5000000000:
                        # if Actor_To_Nest_Dist_Change <= -4.1586410999
                        if _get(features, "Actor_To_Nest_Dist_Change") <= -4.1586410999:
                            return "PI_SI"
                        else:
                            return "OENB"
                    else:
                        # if Nest_RT_y <= 543.5000000000
                        if _get(features, "Nest_RT_y") <= 543.5000000000:
                            # if Nest_hu_6 <= 0.0002300860
                            if _get(features, "Nest_hu_6") <= 0.0002300860:
                                # if Nest_hu_6 <= -0.0000025350
                                if _get(features, "Nest_hu_6") <= -0.0000025350:
                                    # if Nest_RB_x <= 1039.5000000000
                                    if _get(features, "Nest_RB_x") <= 1039.5000000000:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    # if Nest_aspect_ratio <= 4.2963223457
                                    if _get(features, "Nest_aspect_ratio") <= 4.2963223457:
                                        # if Pups_Location_Rat_Distance <= 165.0750808716
                                        if _get(features, "Pups_Location_Rat_Distance") <= 165.0750808716:
                                            # if Actor_To_Nest_Dist_Change <= 29.9952011108
                                            if _get(features, "Actor_To_Nest_Dist_Change") <= 29.9952011108:
                                                # if Actor_bbox_x <= 996.5000000000
                                                if _get(features, "Actor_bbox_x") <= 996.5000000000:
                                                    # if Actor_Mask_IoU <= 0.8974884152
                                                    if _get(features, "Actor_Mask_IoU") <= 0.8974884152:
                                                        # if Nest_RL_x <= 829.5000000000
                                                        if _get(features, "Nest_RL_x") <= 829.5000000000:
                                                            # if Nest_Dist_RB_To_Bbox_TL <= 154.8596572876
                                                            if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 154.8596572876:
                                                                # if Nest_extent <= 0.6701990068
                                                                if _get(features, "Nest_extent") <= 0.6701990068:
                                                                    return "OENB"
                                                                else:
                                                                    return "PI_SI"
                                                            else:
                                                                # if Nest_solidity <= 0.9005512297
                                                                if _get(features, "Nest_solidity") <= 0.9005512297:
                                                                    # if Nest_RB_x <= 1041.5000000000
                                                                    if _get(features, "Nest_RB_x") <= 1041.5000000000:
                                                                        # if Actor_bbox_x <= 994.5000000000
                                                                        if _get(features, "Actor_bbox_x") <= 994.5000000000:
                                                                            # if Actor_RL_x <= 812.0000000000
                                                                            if _get(features, "Actor_RL_x") <= 812.0000000000:
                                                                                # if Actor_aspect_ratio <= 1.9525361061
                                                                                if _get(features, "Actor_aspect_ratio") <= 1.9525361061:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                            else:
                                                                                # if Nest_Dist_RR_To_Bbox_TR <= 74.0067596436
                                                                                if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 74.0067596436:
                                                                                    # if Nest_hu_5 <= 0.0000440800
                                                                                    if _get(features, "Nest_hu_5") <= 0.0000440800:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                        else:
                                                                            # if Actor_Mask_IoU <= 0.8450624943
                                                                            if _get(features, "Actor_Mask_IoU") <= 0.8450624943:
                                                                                return "PI_SI"
                                                                            else:
                                                                                return "OENB"
                                                                    else:
                                                                        # if Nest_Centroid_To_Bbox_TL <= 144.9020843506
                                                                        if _get(features, "Nest_Centroid_To_Bbox_TL") <= 144.9020843506:
                                                                            # if Nest_Dist_RT_To_Bbox_BL <= 115.5666809082
                                                                            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 115.5666809082:
                                                                                return "PI_SI"
                                                                            else:
                                                                                return "OENB"
                                                                        else:
                                                                            # if Nest_orientation <= 87.4736442566
                                                                            if _get(features, "Nest_orientation") <= 87.4736442566:
                                                                                return "OENB"
                                                                            else:
                                                                                # if Actor_Dist_RR_To_Bbox_TR <= 230.5021743774
                                                                                if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 230.5021743774:
                                                                                    # if Nest_Dist_RL_To_Bbox_BL <= 25.5000000000
                                                                                    if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 25.5000000000:
                                                                                        # if Actor_Centroid_To_Bbox_TL <= 150.0420570374
                                                                                        if _get(features, "Actor_Centroid_To_Bbox_TL") <= 150.0420570374:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    return "OENB"
                                                                else:
                                                                    # if Nest_Dist_RL_RR <= 267.2986297607
                                                                    if _get(features, "Nest_Dist_RL_RR") <= 267.2986297607:
                                                                        return "OENB"
                                                                    else:
                                                                        return "PI_SI"
                                                        else:
                                                            # if Nest_Dist_RT_To_Bbox_BL <= 147.9320297241
                                                            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 147.9320297241:
                                                                return "PI_SI"
                                                            else:
                                                                return "OENB"
                                                    else:
                                                        # if Actor_Dist_RL_To_Bbox_TL <= 37.5000000000
                                                        if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 37.5000000000:
                                                            return "OENB"
                                                        else:
                                                            # if Nest_area <= 26074.7500000000
                                                            if _get(features, "Nest_area") <= 26074.7500000000:
                                                                # if Actor_Dist_RL_To_Bbox_BR <= 408.9132232666
                                                                if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 408.9132232666:
                                                                    # if Nest_hu_3 <= 0.0000819000
                                                                    if _get(features, "Nest_hu_3") <= 0.0000819000:
                                                                        # if Nest_bbox_x <= 831.5000000000
                                                                        if _get(features, "Nest_bbox_x") <= 831.5000000000:
                                                                            # if Nest_Dist_RT_To_Bbox_TL <= 64.5000000000
                                                                            if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 64.5000000000:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                        else:
                                                                            return "OENB"
                                                                    else:
                                                                        # if foodhopperRight_Nest_Distance <= 446.5347290039
                                                                        if _get(features, "foodhopperRight_Nest_Distance") <= 446.5347290039:
                                                                            # if Actor_Dist_RT_To_Bbox_TR <= 131.0000000000
                                                                            if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 131.0000000000:
                                                                                return "PI_SI"
                                                                            else:
                                                                                return "OENB"
                                                                        else:
                                                                            # if Nest_RL_y <= 536.5000000000
                                                                            if _get(features, "Nest_RL_y") <= 536.5000000000:
                                                                                # if Nest_RL_y <= 523.0000000000
                                                                                if _get(features, "Nest_RL_y") <= 523.0000000000:
                                                                                    return "PI_SI"
                                                                                else:
                                                                                    return "OENB"
                                                                            else:
                                                                                # if Nest_Dist_RL_To_Bbox_BL <= 28.5000000000
                                                                                if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 28.5000000000:
                                                                                    # if Nest_Dist_RB_To_Bbox_TR <= 149.0916061401
                                                                                    if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 149.0916061401:
                                                                                        return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    # if Nest_Dist_RR_RB <= 8.7441377640
                                                                                    if _get(features, "Nest_Dist_RR_RB") <= 8.7441377640:
                                                                                        # if Nest_RB_x <= 1011.5000000000
                                                                                        if _get(features, "Nest_RB_x") <= 1011.5000000000:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                else:
                                                                    # if Nest_Dist_RB_To_Bbox_BR <= 48.0222158432
                                                                    if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 48.0222158432:
                                                                        return "OENB"
                                                                    else:
                                                                        return "PI_SI"
                                                            else:
                                                                # if Actor_Dist_RL_To_Bbox_TL <= 124.5000000000
                                                                if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 124.5000000000:
                                                                    return "PI_SI"
                                                                else:
                                                                    # if Pups_Location_Rat_Distance <= 114.8363418579
                                                                    if _get(features, "Pups_Location_Rat_Distance") <= 114.8363418579:
                                                                        # if Actor_extent <= 0.5758497417
                                                                        if _get(features, "Actor_extent") <= 0.5758497417:
                                                                            return "PI_SI"
                                                                        else:
                                                                            return "OENB"
                                                                    else:
                                                                        return "PI_SI"
                                                else:
                                                    # if Actor_Dist_RT_To_Bbox_TL <= 97.0000000000
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 97.0000000000:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                            else:
                                                # if Actor_bbox_w <= 356.0000000000
                                                if _get(features, "Actor_bbox_w") <= 356.0000000000:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                        else:
                                            # if Nest_perimeter <= 916.1391906738
                                            if _get(features, "Nest_perimeter") <= 916.1391906738:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                                    else:
                                        return "OENB"
                            else:
                                return "OENB"
                        else:
                            # if Actor_RB_x <= 1072.0000000000
                            if _get(features, "Actor_RB_x") <= 1072.0000000000:
                                return "PI_SI"
                            else:
                                return "OENB"
            else:
                # if Nest_RT_x <= 1088.5000000000
                if _get(features, "Nest_RT_x") <= 1088.5000000000:
                    # if Actor_Dist_RL_To_Bbox_TL <= 85.0000000000
                    if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 85.0000000000:
                        return "PI_SI"
                    else:
                        return "OENB"
                else:
                    # if Nest_Dist_RL_To_Bbox_BR <= 404.2310943604
                    if _get(features, "Nest_Dist_RL_To_Bbox_BR") <= 404.2310943604:
                        return "OENB"
                    else:
                        return "PI_SI"
    else:
        # if Nest_Dist_RT_To_Bbox_BR <= 467.8680114746
        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 467.8680114746:
            # if Nest_aspect_ratio <= 2.5941708088
            if _get(features, "Nest_aspect_ratio") <= 2.5941708088:
                # if Nest_Dist_RT_To_Bbox_BL <= 160.7404708862
                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 160.7404708862:
                    # if Nest_Dist_RB_To_Bbox_BR <= 121.5041160583
                    if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 121.5041160583:
                        # if Actor_Dist_RB_To_Bbox_BR <= 18.5280056000
                        if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 18.5280056000:
                            return "OENB"
                        else:
                            return "PI_SI"
                    else:
                        return "OENB"
                else:
                    # if Nest_orientation <= 101.0313796997
                    if _get(features, "Nest_orientation") <= 101.0313796997:
                        # if Nest_RB_y <= 616.5000000000
                        if _get(features, "Nest_RB_y") <= 616.5000000000:
                            return "PI_SI"
                        else:
                            return "OENB"
                    else:
                        # if Actor_hu_4 <= 0.0000622500
                        if _get(features, "Actor_hu_4") <= 0.0000622500:
                            return "PI_SI"
                        else:
                            return "OENB"
            else:
                # if Actor_centroid_x <= 409.3853302002
                if _get(features, "Actor_centroid_x") <= 409.3853302002:
                    return "PI_SI"
                else:
                    # if Actor_Dist_RL_To_Bbox_TR <= 281.3341674805
                    if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 281.3341674805:
                        # if Nest_bbox_y <= 490.0000000000
                        if _get(features, "Nest_bbox_y") <= 490.0000000000:
                            return "OENB"
                        else:
                            return "PI_SI"
                    else:
                        # if Nest_RR_y <= 606.5000000000
                        if _get(features, "Nest_RR_y") <= 606.5000000000:
                            # if c2_Nest_Distance <= 657.9418640137
                            if _get(features, "c2_Nest_Distance") <= 657.9418640137:
                                # if Nest_Dist_RT_To_Bbox_BR <= 202.0961761475
                                if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 202.0961761475:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                            else:
                                # if Nest_Dist_RR_RB <= 194.0919876099
                                if _get(features, "Nest_Dist_RR_RB") <= 194.0919876099:
                                    # if Nest_bbox_w <= 357.5000000000
                                    if _get(features, "Nest_bbox_w") <= 357.5000000000:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    return "PI_SI"
                        else:
                            # if Actor_bbox_w <= 275.5000000000
                            if _get(features, "Actor_bbox_w") <= 275.5000000000:
                                return "PI_SI"
                            else:
                                # if Nest_eccentricity <= 0.9402104914
                                if _get(features, "Nest_eccentricity") <= 0.9402104914:
                                    # if Actor_RB_y <= 583.5000000000
                                    if _get(features, "Actor_RB_y") <= 583.5000000000:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    # if Actor_Dist_RR_To_Bbox_BL <= 285.6807403564
                                    if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 285.6807403564:
                                        # if Actor_Dist_RB_To_Bbox_TR <= 166.0795059204
                                        if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 166.0795059204:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
                                    else:
                                        # if Nest_Dist_RL_RR <= 376.8799591064
                                        if _get(features, "Nest_Dist_RL_RR") <= 376.8799591064:
                                            # if Nest_centroid_y <= 574.8723754883
                                            if _get(features, "Nest_centroid_y") <= 574.8723754883:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                        else:
                                            # if Actor_Dist_RT_To_Bbox_BL <= 236.2160034180
                                            if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 236.2160034180:
                                                # if Actor_To_Nest_Dist_Change <= -1.8069283962
                                                if _get(features, "Actor_To_Nest_Dist_Change") <= -1.8069283962:
                                                    return "PI_SI"
                                                else:
                                                    # if Actor_solidity <= 0.7821397185
                                                    if _get(features, "Actor_solidity") <= 0.7821397185:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                            else:
                                                return "OENB"
        else:
            # if Nest_hu_1 <= 0.6531865895
            if _get(features, "Nest_hu_1") <= 0.6531865895:
                return "OENB"
            else:
                # if Nest_Dist_RB_To_Bbox_TR <= 224.4156723022
                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 224.4156723022:
                    return "OENB"
                else:
                    return "PI_SI"



def oenb_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Nest_RL_x <= 784.5000000000
    if _get(features, "Nest_RL_x") <= 784.5000000000:
        # if Nest_centroid_y <= 577.6940307617
        if _get(features, "Nest_centroid_y") <= 577.6940307617:
            # if foodhopperRight_Rat_Distance <= 346.6043090820
            if _get(features, "foodhopperRight_Rat_Distance") <= 346.6043090820:
                # if Nest_Centroid_To_Bbox_TR <= 229.9353561401
                if _get(features, "Nest_Centroid_To_Bbox_TR") <= 229.9353561401:
                    return "NB"
                else:
                    # if Nest_RT_x <= 778.5000000000
                    if _get(features, "Nest_RT_x") <= 778.5000000000:
                        return "OE"
                    else:
                        return "ONE"
            else:
                # if foodhopperRight_Rat_Distance <= 412.8952789307
                if _get(features, "foodhopperRight_Rat_Distance") <= 412.8952789307:
                    # if Nest_Dist_RR_To_Bbox_TR <= 92.5054054260
                    if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 92.5054054260:
                        return "NB"
                    else:
                        # if Actor_bbox_y <= 443.0000000000
                        if _get(features, "Actor_bbox_y") <= 443.0000000000:
                            # if Actor_Centroid_To_Bbox_BL <= 144.9222335815
                            if _get(features, "Actor_Centroid_To_Bbox_BL") <= 144.9222335815:
                                return "ONE"
                            else:
                                return "OE"
                        else:
                            return "ONE"
                else:
                    # if Nest_Dist_RL_To_Bbox_BL <= 57.0000000000
                    if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 57.0000000000:
                        return "OE"
                    else:
                        return "ONE"
        else:
            # if Nest_extent <= 0.3101563156
            if _get(features, "Nest_extent") <= 0.3101563156:
                # if c4_Rat_Distance <= 913.7525329590
                if _get(features, "c4_Rat_Distance") <= 913.7525329590:
                    return "OE"
                else:
                    # if Actor_centroid_y <= 490.4973449707
                    if _get(features, "Actor_centroid_y") <= 490.4973449707:
                        return "OE"
                    else:
                        return "NB"
            else:
                # if Nest_eccentricity <= 0.9762020409
                if _get(features, "Nest_eccentricity") <= 0.9762020409:
                    # if Nest_area <= 18103.7500000000
                    if _get(features, "Nest_area") <= 18103.7500000000:
                        # if Actor_Dist_RR_To_Bbox_TR <= 157.5031738281
                        if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 157.5031738281:
                            return "ONE"
                        else:
                            # if Actor_hu_1 <= 0.1323086210
                            if _get(features, "Actor_hu_1") <= 0.1323086210:
                                return "NB"
                            else:
                                return "OE"
                    else:
                        # if c2_Nest_Distance <= 663.6565551758
                        if _get(features, "c2_Nest_Distance") <= 663.6565551758:
                            return "OE"
                        else:
                            return "ONE"
                else:
                    # if Nest_Mask_IoU <= 0.9727432132
                    if _get(features, "Nest_Mask_IoU") <= 0.9727432132:
                        # if Nest_RL_y <= 577.0000000000
                        if _get(features, "Nest_RL_y") <= 577.0000000000:
                            # if Actor_To_Nest_Dist_Change <= -120.3363952637
                            if _get(features, "Actor_To_Nest_Dist_Change") <= -120.3363952637:
                                return "OE"
                            else:
                                return "ONE"
                        else:
                            return "NB"
                    else:
                        # if Actor_Dist_RR_To_Bbox_TL <= 551.2130432129
                        if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 551.2130432129:
                            return "OE"
                        else:
                            return "ONE"
    else:
        # if Nest_hu_0 <= 0.4745147228
        if _get(features, "Nest_hu_0") <= 0.4745147228:
            # if Nest_Dist_RR_To_Bbox_TR <= 134.5037231445
            if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 134.5037231445:
                # if foodhopperLeft_Nest_Distance <= 651.1413879395
                if _get(features, "foodhopperLeft_Nest_Distance") <= 651.1413879395:
                    # if Nest_Dist_RL_RR <= 273.4820556641
                    if _get(features, "Nest_Dist_RL_RR") <= 273.4820556641:
                        # if Nest_extent <= 0.5748926997
                        if _get(features, "Nest_extent") <= 0.5748926997:
                            # if Nest_Dist_RB_To_Bbox_TL <= 152.7095489502
                            if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 152.7095489502:
                                return "NB"
                            else:
                                return "ONE"
                        else:
                            return "NB"
                    else:
                        # if Nest_Centroid_To_Bbox_TR <= 155.3169631958
                        if _get(features, "Nest_Centroid_To_Bbox_TR") <= 155.3169631958:
                            # if Actor_solidity <= 0.9042820632
                            if _get(features, "Actor_solidity") <= 0.9042820632:
                                return "OE"
                            else:
                                return "NB"
                        else:
                            # if Nest_orientation <= 90.0146369934
                            if _get(features, "Nest_orientation") <= 90.0146369934:
                                # if Actor_Dist_RB_RL <= 125.3388204575
                                if _get(features, "Actor_Dist_RB_RL") <= 125.3388204575:
                                    return "NB"
                                else:
                                    return "ONE"
                            else:
                                return "NB"
                else:
                    # if pipeEnd_Nest_Distance <= 510.5974426270
                    if _get(features, "pipeEnd_Nest_Distance") <= 510.5974426270:
                        return "ONE"
                    else:
                        return "NB"
            else:
                # if Nest_aspect_ratio <= 2.0497564077
                if _get(features, "Nest_aspect_ratio") <= 2.0497564077:
                    return "ONE"
                else:
                    return "OE"
        else:
            # if Nest_Mask_IoU <= 0.7234582007
            if _get(features, "Nest_Mask_IoU") <= 0.7234582007:
                # if Nest_hu_1 <= 0.3500901163
                if _get(features, "Nest_hu_1") <= 0.3500901163:
                    return "ONE"
                else:
                    return "NB"
            else:
                return "ONE"


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
