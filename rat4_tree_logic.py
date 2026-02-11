# THIS FILE IS AUTO-GENERATED: pure if/else logic for your hierarchical classifier.
# Requires only Python + numpy/pandas at runtime (sklearn not required).
# Do not edit by hand; regenerate after retraining.

import numpy as np

# --- constants learned at training time ---
ROUTER_COLS = ["Nest_Dist_RL_RT", "Nest_Dist_RL_To_Bbox_TR", "Nest_Dist_RT_To_Bbox_BL", "Nest_Dist_RB_To_Bbox_TR", "Nest_eccentricity", "Actor_bbox_y", "Nest_Dist_RL_RR", "Nest_Dist_RT_RB", "Actor_RT_y", "Nest_Dist_RB_To_Bbox_BR", "Nest_Dist_RT_To_Bbox_TL", "Nest_area", "Nest_hu_1", "Nest_Centroid_To_Bbox_TR", "Nest_Dist_RR_RB", "Nest_RB_x", "Nest_Dist_RR_To_Bbox_BL", "Nest_perimeter", "Nest_Centroid_To_Bbox_BR", "Nest_Dist_RB_To_Bbox_TL", "Nest_Centroid_To_Bbox_TL", "Nest_bbox_w", "Nest_extent", "Nest_RB_y", "Nest_Centroid_To_Bbox_BL", "Actor_aspect_ratio", "Nest_Dist_RL_To_Bbox_BR", "Actor_centroid_y", "Actor_RR_y", "c1_Nest_Distance", "Nest_bbox_h", "Actor_To_Nest_Distance", "Nest_hu_5", "Nest_RT_y", "Nest_Dist_RR_To_Bbox_BR", "Nest_bbox_y", "Nest_RT_x", "Actor_Dist_RL_To_Bbox_BR", "Nest_centroid_x", "Nest_Dist_RR_To_Bbox_TL", "Nest_Dist_RL_To_Bbox_TL", "Nest_orientation", "Nest_hu_3", "Actor_orientation", "Nest_centroid_y", "pipeStart_Nest_Distance", "foodhopperRight_Nest_Distance", "Nest_Dist_RT_To_Bbox_TR", "c4_Nest_Distance", "Nest_hu_0", "Actor_bbox_w", "Nest_hu_4", "Actor_bbox_h", "Actor_Dist_RL_RR", "c1_Rat_Distance", "Nest_bbox_x", "Actor_Dist_RR_To_Bbox_TL", "Actor_bbox_x", "Actor_Dist_RR_To_Bbox_BL", "Actor_Dist_RR_To_Bbox_BR", "Nest_Dist_RT_RR", "Nest_Dist_RT_To_Bbox_BR", "Actor_RL_x", "Actor_Dist_RL_To_Bbox_TL", "foodhopperLeft_Nest_Distance", "c3_Nest_Distance", "Actor_Centroid_To_Bbox_TL", "Pups_Location_Nest_Distance", "pipeEnd_Nest_Distance", "Pups_Location_Rat_Distance", "c2_Nest_Distance", "foodhopperBottom_Rat_Distance", "foodhopperMid_Nest_Distance", "foodhopperRight_Rat_Distance", "foodhopperBottom_Nest_Distance", "c3_Rat_Distance", "Nest_Mask_IoU", "foodhopperMid_Rat_Distance", "Actor_Dist_RT_To_Bbox_TR", "Nest_RR_x", "Actor_Centroid_To_Bbox_BL", "Nest_aspect_ratio", "Actor_Dist_RL_To_Bbox_TR", "Nest_RL_x", "foodhopperLeft_Rat_Distance", "Actor_RB_y", "pipeStart_Rat_Distance", "c2_Rat_Distance", "Actor_Dist_RB_To_Bbox_BR", "Actor_centroid_x", "Actor_area", "Actor_RB_x", "Actor_Dist_RT_RR", "pipeMid_Rat_Distance", "Nest_hu_2", "c4_Rat_Distance", "Actor_extent", "Nest_solidity", "Actor_RT_x", "Actor_Centroid_To_Bbox_BR", "Actor_Dist_RR_To_Bbox_TR", "Nest_RL_y", "Actor_Centroid_To_Bbox_TR", "Nest_Dist_RR_To_Bbox_TR", "Actor_eccentricity", "pipeMid_Nest_Distance", "Nest_Dist_RL_To_Bbox_BL", "Actor_Dist_RR_RB", "Actor_perimeter", "Actor_solidity", "Nest_RR_y", "pipeEnd_Rat_Distance", "Actor_Dist_RB_To_Bbox_TR", "Actor_RR_x", "Actor_RL_y", "Actor_hu_1", "Actor_hu_0", "Nest_Dist_RB_RL", "Actor_Dist_RT_To_Bbox_BL", "Actor_Dist_RT_To_Bbox_BR", "Actor_Dist_RL_To_Bbox_BL", "Actor_Dist_RB_To_Bbox_BL", "Actor_Dist_RB_RL", "Actor_Dist_RT_To_Bbox_TL", "Actor_Dist_RL_RT", "Actor_hu_2", "Actor_hu_3", "Actor_Dist_RT_RB", "Nest_Dist_RB_To_Bbox_BL", "Actor_hu_5", "Actor_Mask_IoU", "Actor_Dist_RB_To_Bbox_TL", "Nest_Area_Diff_Abs", "Nest_hu_6", "Actor_Area_Diff_Abs", "Actor_To_Nest_Dist_Change", "Actor_hu_4", "Actor_hu_6", "Actor_Direction_deg"]
OENB_COLS   = ["Actor_area", "Actor_perimeter", "Actor_centroid_x", "Actor_centroid_y", "Actor_bbox_x", "Actor_bbox_y", "Actor_bbox_w", "Actor_bbox_h", "Actor_aspect_ratio", "Actor_extent", "Actor_solidity", "Actor_orientation", "Actor_eccentricity", "Actor_RL_x", "Actor_RL_y", "Actor_RR_x", "Actor_RR_y", "Actor_RT_x", "Actor_RT_y", "Actor_RB_x", "Actor_RB_y", "Actor_hu_0", "Actor_hu_1", "Actor_hu_2", "Actor_hu_3", "Actor_hu_4", "Actor_hu_5", "Actor_hu_6", "Actor_Dist_RL_RR", "Actor_Dist_RT_RB", "Actor_Dist_RL_RT", "Actor_Dist_RT_RR", "Actor_Dist_RR_RB", "Actor_Dist_RB_RL", "Actor_Centroid_To_Bbox_TL", "Actor_Centroid_To_Bbox_TR", "Actor_Centroid_To_Bbox_BR", "Actor_Centroid_To_Bbox_BL", "Actor_Dist_RL_To_Bbox_TL", "Actor_Dist_RL_To_Bbox_TR", "Actor_Dist_RL_To_Bbox_BR", "Actor_Dist_RL_To_Bbox_BL", "Actor_Dist_RR_To_Bbox_TL", "Actor_Dist_RR_To_Bbox_TR", "Actor_Dist_RR_To_Bbox_BR", "Actor_Dist_RR_To_Bbox_BL", "Actor_Dist_RT_To_Bbox_TL", "Actor_Dist_RT_To_Bbox_TR", "Actor_Dist_RT_To_Bbox_BR", "Actor_Dist_RT_To_Bbox_BL", "Actor_Dist_RB_To_Bbox_TL", "Actor_Dist_RB_To_Bbox_TR", "Actor_Dist_RB_To_Bbox_BR", "Actor_Dist_RB_To_Bbox_BL", "Nest_area", "Nest_perimeter", "Nest_centroid_x", "Nest_centroid_y", "Nest_bbox_x", "Nest_bbox_y", "Nest_bbox_w", "Nest_bbox_h", "Nest_aspect_ratio", "Nest_extent", "Nest_solidity", "Nest_orientation", "Nest_eccentricity", "Nest_RL_x", "Nest_RL_y", "Nest_RR_x", "Nest_RR_y", "Nest_RT_x", "Nest_RT_y", "Nest_RB_x", "Nest_RB_y", "Nest_hu_0", "Nest_hu_1", "Nest_hu_2", "Nest_hu_3", "Nest_hu_4", "Nest_hu_5", "Nest_hu_6", "Nest_Dist_RL_RR", "Nest_Dist_RT_RB", "Nest_Dist_RL_RT", "Nest_Dist_RT_RR", "Nest_Dist_RR_RB", "Nest_Dist_RB_RL", "Nest_Centroid_To_Bbox_TL", "Nest_Centroid_To_Bbox_TR", "Nest_Centroid_To_Bbox_BR", "Nest_Centroid_To_Bbox_BL", "Nest_Dist_RL_To_Bbox_TL", "Nest_Dist_RL_To_Bbox_TR", "Nest_Dist_RL_To_Bbox_BR", "Nest_Dist_RL_To_Bbox_BL", "Nest_Dist_RR_To_Bbox_TL", "Nest_Dist_RR_To_Bbox_TR", "Nest_Dist_RR_To_Bbox_BR", "Nest_Dist_RR_To_Bbox_BL", "Nest_Dist_RT_To_Bbox_TL", "Nest_Dist_RT_To_Bbox_TR", "Nest_Dist_RT_To_Bbox_BR", "Nest_Dist_RT_To_Bbox_BL", "Nest_Dist_RB_To_Bbox_TL", "Nest_Dist_RB_To_Bbox_TR", "Nest_Dist_RB_To_Bbox_BR", "Nest_Dist_RB_To_Bbox_BL", "Actor_Area_Diff_Abs", "Actor_Mask_IoU", "Nest_Area_Diff_Abs", "Nest_Mask_IoU", "Actor_To_Nest_Distance", "Actor_Direction_deg", "Actor_To_Nest_Dist_Change", "c1_Rat_Distance", "c1_Nest_Distance", "c2_Rat_Distance", "c2_Nest_Distance", "c3_Rat_Distance", "c3_Nest_Distance", "c4_Rat_Distance", "c4_Nest_Distance", "pipeEnd_Rat_Distance", "pipeEnd_Nest_Distance", "pipeMid_Rat_Distance", "pipeMid_Nest_Distance", "pipeStart_Rat_Distance", "pipeStart_Nest_Distance", "foodhopperBottom_Rat_Distance", "foodhopperBottom_Nest_Distance", "foodhopperLeft_Rat_Distance", "foodhopperLeft_Nest_Distance", "foodhopperRight_Rat_Distance", "foodhopperRight_Nest_Distance", "foodhopperMid_Rat_Distance", "foodhopperMid_Nest_Distance", "Pups_Location_Rat_Distance", "Pups_Location_Nest_Distance"]
RATIO_FEATURE = "Actor_aspect_ratio"
RATIO_THRESH  = 0.5552475975
RATIO_FLIP    = True

def _get(d, k):
    try:
        return float(d.get(k, float("nan")))
    except Exception:
        return float("nan")


def router_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Nest_Dist_RT_To_Bbox_BL <= 197.8786849976
    if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 197.8786849976:
        # if Actor_Dist_RL_To_Bbox_BL <= 20.0000000000
        if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 20.0000000000:
            # if Actor_Dist_RL_To_Bbox_TR <= 399.5298309326
            if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 399.5298309326:
                return "OENB"
            else:
                return "PI_SI"
        else:
            # if Actor_aspect_ratio <= 1.0512542129
            if _get(features, "Actor_aspect_ratio") <= 1.0512542129:
                return "OENB"
            else:
                # if Nest_extent <= 0.3262846023
                if _get(features, "Nest_extent") <= 0.3262846023:
                    # if Nest_Dist_RR_To_Bbox_BR <= 116.0043830872
                    if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 116.0043830872:
                        return "OENB"
                    else:
                        return "PI_SI"
                else:
                    # if Actor_RB_x <= 265.5000000000
                    if _get(features, "Actor_RB_x") <= 265.5000000000:
                        # if Nest_extent <= 0.3506082147
                        if _get(features, "Nest_extent") <= 0.3506082147:
                            # if Actor_bbox_w <= 332.0000000000
                            if _get(features, "Actor_bbox_w") <= 332.0000000000:
                                return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            # if Actor_Direction_deg <= -169.1172332764
                            if _get(features, "Actor_Direction_deg") <= -169.1172332764:
                                # if Actor_Direction_deg <= -169.5112152100
                                if _get(features, "Actor_Direction_deg") <= -169.5112152100:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                            else:
                                return "PI_SI"
                    else:
                        # if Actor_To_Nest_Dist_Change <= 1.4366008043
                        if _get(features, "Actor_To_Nest_Dist_Change") <= 1.4366008043:
                            return "PI_SI"
                        else:
                            return "OENB"
    else:
        # if Actor_RT_y <= 436.5000000000
        if _get(features, "Actor_RT_y") <= 436.5000000000:
            # if Nest_Mask_IoU <= 0.8829551935
            if _get(features, "Nest_Mask_IoU") <= 0.8829551935:
                # if Nest_Dist_RR_To_Bbox_BR <= 127.5039215088
                if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 127.5039215088:
                    # if Nest_eccentricity <= 0.9474068582
                    if _get(features, "Nest_eccentricity") <= 0.9474068582:
                        # if Nest_bbox_x <= 360.5000000000
                        if _get(features, "Nest_bbox_x") <= 360.5000000000:
                            # if Nest_bbox_h <= 225.5000000000
                            if _get(features, "Nest_bbox_h") <= 225.5000000000:
                                # if c2_Nest_Distance <= 976.6277465820
                                if _get(features, "c2_Nest_Distance") <= 976.6277465820:
                                    # if Actor_Dist_RL_To_Bbox_BR <= 357.6738891602
                                    if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 357.6738891602:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    # if Nest_RB_y <= 648.5000000000
                                    if _get(features, "Nest_RB_y") <= 648.5000000000:
                                        # if Nest_RT_x <= 499.5000000000
                                        if _get(features, "Nest_RT_x") <= 499.5000000000:
                                            return "PI_SI"
                                        else:
                                            # if Actor_perimeter <= 1019.4981079102
                                            if _get(features, "Actor_perimeter") <= 1019.4981079102:
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
                        # if Actor_hu_0 <= 0.1768456548
                        if _get(features, "Actor_hu_0") <= 0.1768456548:
                            return "PI_SI"
                        else:
                            return "OENB"
                else:
                    # if Actor_Dist_RR_RB <= 362.4805450439
                    if _get(features, "Actor_Dist_RR_RB") <= 362.4805450439:
                        # if Actor_bbox_x <= 36.5000000000
                        if _get(features, "Actor_bbox_x") <= 36.5000000000:
                            # if Actor_RR_y <= 514.5000000000
                            if _get(features, "Actor_RR_y") <= 514.5000000000:
                                return "PI_SI"
                            else:
                                return "OENB"
                        else:
                            # if Actor_To_Nest_Distance <= 53.5598068237
                            if _get(features, "Actor_To_Nest_Distance") <= 53.5598068237:
                                # if Actor_centroid_x <= 225.2895660400
                                if _get(features, "Actor_centroid_x") <= 225.2895660400:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                            else:
                                # if Actor_Dist_RB_To_Bbox_TL <= 165.0229034424
                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 165.0229034424:
                                    return "PI_SI"
                                else:
                                    # if Actor_RB_y <= 671.5000000000
                                    if _get(features, "Actor_RB_y") <= 671.5000000000:
                                        # if Actor_Dist_RT_RR <= 43.6830806732
                                        if _get(features, "Actor_Dist_RT_RR") <= 43.6830806732:
                                            return "PI_SI"
                                        else:
                                            # if Actor_orientation <= 9.8524141312
                                            if _get(features, "Actor_orientation") <= 9.8524141312:
                                                return "PI_SI"
                                            else:
                                                # if Actor_Dist_RT_To_Bbox_TR <= 19.0000000000
                                                if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 19.0000000000:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                    else:
                                        # if Nest_Dist_RT_To_Bbox_TL <= 207.0000000000
                                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 207.0000000000:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                    else:
                        # if Actor_aspect_ratio <= 1.3557077050
                        if _get(features, "Actor_aspect_ratio") <= 1.3557077050:
                            # if Nest_RB_x <= 215.0000000000
                            if _get(features, "Nest_RB_x") <= 215.0000000000:
                                return "PI_SI"
                            else:
                                return "OENB"
                        else:
                            return "PI_SI"
            else:
                # if Nest_RT_y <= 453.5000000000
                if _get(features, "Nest_RT_y") <= 453.5000000000:
                    # if Pups_Location_Rat_Distance <= 103.6159095764
                    if _get(features, "Pups_Location_Rat_Distance") <= 103.6159095764:
                        # if pipeMid_Nest_Distance <= 228.4140930176
                        if _get(features, "pipeMid_Nest_Distance") <= 228.4140930176:
                            # if Nest_eccentricity <= 0.9455868304
                            if _get(features, "Nest_eccentricity") <= 0.9455868304:
                                return "PI_SI"
                            else:
                                return "OENB"
                        else:
                            # if Nest_RB_y <= 643.0000000000
                            if _get(features, "Nest_RB_y") <= 643.0000000000:
                                return "PI_SI"
                            else:
                                return "OENB"
                    else:
                        # if Actor_Dist_RL_To_Bbox_TL <= 27.5000000000
                        if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 27.5000000000:
                            # if Actor_area <= 27877.0000000000
                            if _get(features, "Actor_area") <= 27877.0000000000:
                                # if Nest_centroid_y <= 550.2182312012
                                if _get(features, "Nest_centroid_y") <= 550.2182312012:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                            else:
                                return "OENB"
                        else:
                            # if Nest_Dist_RL_RT <= 210.5215682983
                            if _get(features, "Nest_Dist_RL_RT") <= 210.5215682983:
                                # if c1_Nest_Distance <= 605.9964294434
                                if _get(features, "c1_Nest_Distance") <= 605.9964294434:
                                    # if Actor_Dist_RT_To_Bbox_TL <= 121.5000000000
                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 121.5000000000:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    return "PI_SI"
                            else:
                                # if Actor_eccentricity <= 0.8445782065
                                if _get(features, "Actor_eccentricity") <= 0.8445782065:
                                    # if Nest_hu_2 <= 0.0001008130
                                    if _get(features, "Nest_hu_2") <= 0.0001008130:
                                        return "PI_SI"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_TR <= 151.0033111572
                                        if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 151.0033111572:
                                            # if Nest_Dist_RB_To_Bbox_BL <= 155.0032272339
                                            if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 155.0032272339:
                                                # if Actor_RR_y <= 554.5000000000
                                                if _get(features, "Actor_RR_y") <= 554.5000000000:
                                                    # if Actor_Dist_RT_RB <= 317.2015533447
                                                    if _get(features, "Actor_Dist_RT_RB") <= 317.2015533447:
                                                        return "OENB"
                                                    else:
                                                        # if Actor_Dist_RT_To_Bbox_TL <= 210.5000000000
                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 210.5000000000:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                else:
                                                    # if foodhopperBottom_Nest_Distance <= 301.0077362061
                                                    if _get(features, "foodhopperBottom_Nest_Distance") <= 301.0077362061:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                                            else:
                                                # if Nest_Dist_RT_RB <= 231.6851348877
                                                if _get(features, "Nest_Dist_RT_RB") <= 231.6851348877:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                        else:
                                            # if Nest_RT_y <= 452.0000000000
                                            if _get(features, "Nest_RT_y") <= 452.0000000000:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                else:
                                    # if Actor_RL_x <= 47.0000000000
                                    if _get(features, "Actor_RL_x") <= 47.0000000000:
                                        return "PI_SI"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_TR <= 97.5051307678
                                        if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 97.5051307678:
                                            # if Nest_aspect_ratio <= 1.8870281577
                                            if _get(features, "Nest_aspect_ratio") <= 1.8870281577:
                                                # if Nest_Mask_IoU <= 0.8922349811
                                                if _get(features, "Nest_Mask_IoU") <= 0.8922349811:
                                                    # if Nest_Dist_RB_To_Bbox_BL <= 57.0091781616
                                                    if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 57.0091781616:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                                else:
                                                    return "OENB"
                                            else:
                                                # if Nest_Dist_RL_To_Bbox_TL <= 185.5000000000
                                                if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 185.5000000000:
                                                    return "OENB"
                                                else:
                                                    # if Nest_centroid_y <= 555.3767395020
                                                    if _get(features, "Nest_centroid_y") <= 555.3767395020:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                        else:
                                            # if Actor_solidity <= 0.9032180011
                                            if _get(features, "Actor_solidity") <= 0.9032180011:
                                                return "OENB"
                                            else:
                                                # if Actor_solidity <= 0.9104259312
                                                if _get(features, "Actor_solidity") <= 0.9104259312:
                                                    # if Actor_RB_y <= 632.5000000000
                                                    if _get(features, "Actor_RB_y") <= 632.5000000000:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                                                else:
                                                    # if c1_Nest_Distance <= 652.9074707031
                                                    if _get(features, "c1_Nest_Distance") <= 652.9074707031:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                else:
                    # if Nest_perimeter <= 559.4787292480
                    if _get(features, "Nest_perimeter") <= 559.4787292480:
                        # if Nest_Centroid_To_Bbox_BR <= 115.0308189392
                        if _get(features, "Nest_Centroid_To_Bbox_BR") <= 115.0308189392:
                            return "PI_SI"
                        else:
                            # if Actor_Dist_RT_RR <= 135.6408004761
                            if _get(features, "Actor_Dist_RT_RR") <= 135.6408004761:
                                return "PI_SI"
                            else:
                                return "OENB"
                    else:
                        # if Actor_RL_x <= 44.5000000000
                        if _get(features, "Actor_RL_x") <= 44.5000000000:
                            # if Nest_hu_2 <= 0.0062198739
                            if _get(features, "Nest_hu_2") <= 0.0062198739:
                                return "PI_SI"
                            else:
                                return "OENB"
                        else:
                            # if Nest_hu_1 <= 0.0180418612
                            if _get(features, "Nest_hu_1") <= 0.0180418612:
                                return "PI_SI"
                            else:
                                # if Nest_hu_6 <= -0.0000034600
                                if _get(features, "Nest_hu_6") <= -0.0000034600:
                                    # if Nest_hu_1 <= 0.0923130400
                                    if _get(features, "Nest_hu_1") <= 0.0923130400:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    # if Actor_Centroid_To_Bbox_BL <= 292.0261383057
                                    if _get(features, "Actor_Centroid_To_Bbox_BL") <= 292.0261383057:
                                        # if pipeStart_Rat_Distance <= 100.8391456604
                                        if _get(features, "pipeStart_Rat_Distance") <= 100.8391456604:
                                            # if c2_Nest_Distance <= 1094.9866333008
                                            if _get(features, "c2_Nest_Distance") <= 1094.9866333008:
                                                # if Nest_area <= 32936.0000000000
                                                if _get(features, "Nest_area") <= 32936.0000000000:
                                                    # if Actor_bbox_x <= 472.5000000000
                                                    if _get(features, "Actor_bbox_x") <= 472.5000000000:
                                                        # if Actor_Direction_deg <= -56.1431198120
                                                        if _get(features, "Actor_Direction_deg") <= -56.1431198120:
                                                            # if Nest_RR_x <= 511.5000000000
                                                            if _get(features, "Nest_RR_x") <= 511.5000000000:
                                                                return "OENB"
                                                            else:
                                                                return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        # if Nest_RL_y <= 624.5000000000
                                                        if _get(features, "Nest_RL_y") <= 624.5000000000:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                else:
                                                    return "PI_SI"
                                            else:
                                                # if Actor_Mask_IoU <= 0.9720745683
                                                if _get(features, "Actor_Mask_IoU") <= 0.9720745683:
                                                    # if Actor_Direction_deg <= -160.5929489136
                                                    if _get(features, "Actor_Direction_deg") <= -160.5929489136:
                                                        # if c3_Nest_Distance <= 942.4360046387
                                                        if _get(features, "c3_Nest_Distance") <= 942.4360046387:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        return "OENB"
                                                else:
                                                    return "PI_SI"
                                        else:
                                            # if Actor_Mask_IoU <= 0.1635503173
                                            if _get(features, "Actor_Mask_IoU") <= 0.1635503173:
                                                # if Nest_RL_y <= 616.5000000000
                                                if _get(features, "Nest_RL_y") <= 616.5000000000:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                            else:
                                                # if Nest_Dist_RR_To_Bbox_TR <= 68.5073013306
                                                if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 68.5073013306:
                                                    # if Actor_RR_x <= 325.5000000000
                                                    if _get(features, "Actor_RR_x") <= 325.5000000000:
                                                        return "PI_SI"
                                                    else:
                                                        # if Actor_Dist_RL_To_Bbox_BL <= 240.5000000000
                                                        if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 240.5000000000:
                                                            # if c1_Nest_Distance <= 699.8799438477
                                                            if _get(features, "c1_Nest_Distance") <= 699.8799438477:
                                                                # if Nest_extent <= 0.5678086877
                                                                if _get(features, "Nest_extent") <= 0.5678086877:
                                                                    # if Actor_RL_x <= 909.5000000000
                                                                    if _get(features, "Actor_RL_x") <= 909.5000000000:
                                                                        # if Nest_Dist_RT_RR <= 20.5768728256
                                                                        if _get(features, "Nest_Dist_RT_RR") <= 20.5768728256:
                                                                            # if Nest_aspect_ratio <= 1.9189196825
                                                                            if _get(features, "Nest_aspect_ratio") <= 1.9189196825:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                        else:
                                                                            # if Actor_RR_x <= 1146.5000000000
                                                                            if _get(features, "Actor_RR_x") <= 1146.5000000000:
                                                                                # if Actor_RT_y <= 435.5000000000
                                                                                if _get(features, "Actor_RT_y") <= 435.5000000000:
                                                                                    # if pipeStart_Rat_Distance <= 102.9935531616
                                                                                    if _get(features, "pipeStart_Rat_Distance") <= 102.9935531616:
                                                                                        # if Actor_Dist_RT_To_Bbox_TL <= 69.0000000000
                                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 69.0000000000:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                    else:
                                                                                        # if Actor_eccentricity <= 0.5153432786
                                                                                        if _get(features, "Actor_eccentricity") <= 0.5153432786:
                                                                                            # if Actor_Centroid_To_Bbox_TR <= 155.8330230713
                                                                                            if _get(features, "Actor_Centroid_To_Bbox_TR") <= 155.8330230713:
                                                                                                return "OENB"
                                                                                            else:
                                                                                                return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                else:
                                                                                    # if c1_Nest_Distance <= 661.8530273438
                                                                                    if _get(features, "c1_Nest_Distance") <= 661.8530273438:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                            else:
                                                                                # if foodhopperRight_Rat_Distance <= 347.0852508545
                                                                                if _get(features, "foodhopperRight_Rat_Distance") <= 347.0852508545:
                                                                                    return "PI_SI"
                                                                                else:
                                                                                    return "OENB"
                                                                    else:
                                                                        # if Nest_Dist_RT_To_Bbox_BR <= 198.5581436157
                                                                        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 198.5581436157:
                                                                            return "PI_SI"
                                                                        else:
                                                                            # if Nest_solidity <= 0.8575079739
                                                                            if _get(features, "Nest_solidity") <= 0.8575079739:
                                                                                # if Actor_perimeter <= 1034.9711608887
                                                                                if _get(features, "Actor_perimeter") <= 1034.9711608887:
                                                                                    # if Nest_Dist_RR_To_Bbox_BR <= 121.5041160583
                                                                                    if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 121.5041160583:
                                                                                        # if foodhopperMid_Nest_Distance <= 452.0180053711
                                                                                        if _get(features, "foodhopperMid_Nest_Distance") <= 452.0180053711:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                            else:
                                                                                # if Actor_Dist_RR_To_Bbox_BL <= 134.7035522461
                                                                                if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 134.7035522461:
                                                                                    return "OENB"
                                                                                else:
                                                                                    return "PI_SI"
                                                                else:
                                                                    return "PI_SI"
                                                            else:
                                                                return "PI_SI"
                                                        else:
                                                            return "PI_SI"
                                                else:
                                                    # if Actor_RR_x <= 405.5000000000
                                                    if _get(features, "Actor_RR_x") <= 405.5000000000:
                                                        # if Nest_hu_5 <= 0.0002563945
                                                        if _get(features, "Nest_hu_5") <= 0.0002563945:
                                                            return "OENB"
                                                        else:
                                                            return "PI_SI"
                                                    else:
                                                        # if Nest_eccentricity <= 0.9575167596
                                                        if _get(features, "Nest_eccentricity") <= 0.9575167596:
                                                            # if Actor_RB_x <= 167.5000000000
                                                            if _get(features, "Actor_RB_x") <= 167.5000000000:
                                                                return "PI_SI"
                                                            else:
                                                                # if Nest_Dist_RL_RT <= 294.1382904053
                                                                if _get(features, "Nest_Dist_RL_RT") <= 294.1382904053:
                                                                    # if Nest_RR_x <= 521.0000000000
                                                                    if _get(features, "Nest_RR_x") <= 521.0000000000:
                                                                        return "OENB"
                                                                    else:
                                                                        return "PI_SI"
                                                                else:
                                                                    return "OENB"
                                                        else:
                                                            return "PI_SI"
                                    else:
                                        # if Nest_Dist_RB_To_Bbox_TR <= 352.6112976074
                                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 352.6112976074:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
        else:
            # if Nest_extent <= 0.4534643888
            if _get(features, "Nest_extent") <= 0.4534643888:
                # if pipeStart_Rat_Distance <= 377.5732421875
                if _get(features, "pipeStart_Rat_Distance") <= 377.5732421875:
                    # if Nest_hu_2 <= 0.0007109185
                    if _get(features, "Nest_hu_2") <= 0.0007109185:
                        # if Actor_Dist_RR_To_Bbox_BL <= 362.8106384277
                        if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 362.8106384277:
                            return "OENB"
                        else:
                            return "PI_SI"
                    else:
                        # if Actor_hu_0 <= 0.1881270930
                        if _get(features, "Actor_hu_0") <= 0.1881270930:
                            return "OENB"
                        else:
                            return "PI_SI"
                else:
                    # if Nest_bbox_y <= 467.0000000000
                    if _get(features, "Nest_bbox_y") <= 467.0000000000:
                        # if Nest_Dist_RR_To_Bbox_TR <= 22.5227613449
                        if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 22.5227613449:
                            return "PI_SI"
                        else:
                            # if Nest_Area_Diff_Abs <= 7169.7500000000
                            if _get(features, "Nest_Area_Diff_Abs") <= 7169.7500000000:
                                return "OENB"
                            else:
                                return "PI_SI"
                    else:
                        # if Nest_Dist_RT_To_Bbox_BR <= 185.9759292603
                        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 185.9759292603:
                            return "PI_SI"
                        else:
                            return "OENB"
            else:
                # if Nest_bbox_y <= 470.5000000000
                if _get(features, "Nest_bbox_y") <= 470.5000000000:
                    # if Actor_Dist_RR_To_Bbox_BL <= 89.0617675781
                    if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 89.0617675781:
                        return "OENB"
                    else:
                        # if Nest_Centroid_To_Bbox_BR <= 277.4882049561
                        if _get(features, "Nest_Centroid_To_Bbox_BR") <= 277.4882049561:
                            # if Actor_hu_6 <= -0.0000356000
                            if _get(features, "Actor_hu_6") <= -0.0000356000:
                                return "OENB"
                            else:
                                # if Nest_Dist_RT_To_Bbox_BL <= 369.4873809814
                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 369.4873809814:
                                    # if Actor_Dist_RT_To_Bbox_TL <= 94.0000000000
                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 94.0000000000:
                                        # if foodhopperMid_Nest_Distance <= 463.3785247803
                                        if _get(features, "foodhopperMid_Nest_Distance") <= 463.3785247803:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        # if Actor_Centroid_To_Bbox_BL <= 291.3421020508
                                        if _get(features, "Actor_Centroid_To_Bbox_BL") <= 291.3421020508:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                else:
                                    # if Nest_RT_y <= 469.5000000000
                                    if _get(features, "Nest_RT_y") <= 469.5000000000:
                                        # if Actor_To_Nest_Dist_Change <= -16.6908445358
                                        if _get(features, "Actor_To_Nest_Dist_Change") <= -16.6908445358:
                                            # if Actor_Dist_RL_RR <= 428.2687072754
                                            if _get(features, "Actor_Dist_RL_RR") <= 428.2687072754:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                        else:
                                            return "PI_SI"
                                    else:
                                        # if Nest_Dist_RT_To_Bbox_TR <= 68.5000000000
                                        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 68.5000000000:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                        else:
                            return "OENB"
                else:
                    # if Nest_Dist_RT_RR <= 79.9092636108
                    if _get(features, "Nest_Dist_RT_RR") <= 79.9092636108:
                        # if Actor_perimeter <= 384.5218505859
                        if _get(features, "Actor_perimeter") <= 384.5218505859:
                            return "OENB"
                        else:
                            return "PI_SI"
                    else:
                        return "OENB"



def oenb_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Actor_RB_y <= 642.5000000000
    if _get(features, "Actor_RB_y") <= 642.5000000000:
        # if Nest_centroid_y <= 549.7604675293
        if _get(features, "Nest_centroid_y") <= 549.7604675293:
            # if Nest_Dist_RT_To_Bbox_BR <= 300.2298736572
            if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 300.2298736572:
                # if Nest_Dist_RT_To_Bbox_TR <= 16.5000000000
                if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 16.5000000000:
                    return "OE"
                else:
                    # if foodhopperRight_Rat_Distance <= 734.8137817383
                    if _get(features, "foodhopperRight_Rat_Distance") <= 734.8137817383:
                        return "OE"
                    else:
                        # if pipeMid_Rat_Distance <= 356.2449493408
                        if _get(features, "pipeMid_Rat_Distance") <= 356.2449493408:
                            # if Nest_Dist_RR_To_Bbox_BR <= 122.5040855408
                            if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 122.5040855408:
                                return "OE"
                            else:
                                return "NB"
                        else:
                            return "OE"
            else:
                # if Actor_RB_x <= 134.5000000000
                if _get(features, "Actor_RB_x") <= 134.5000000000:
                    # if Actor_Centroid_To_Bbox_TL <= 175.4132003784
                    if _get(features, "Actor_Centroid_To_Bbox_TL") <= 175.4132003784:
                        # if Nest_Dist_RT_To_Bbox_TR <= 304.5000000000
                        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 304.5000000000:
                            return "ONE"
                        else:
                            return "OE"
                    else:
                        return "NB"
                else:
                    # if Actor_eccentricity <= 0.7213634551
                    if _get(features, "Actor_eccentricity") <= 0.7213634551:
                        return "ONE"
                    else:
                        return "OE"
        else:
            # if Nest_RL_y <= 645.5000000000
            if _get(features, "Nest_RL_y") <= 645.5000000000:
                # if Actor_aspect_ratio <= 2.6807771921
                if _get(features, "Actor_aspect_ratio") <= 2.6807771921:
                    # if Nest_RT_y <= 438.5000000000
                    if _get(features, "Nest_RT_y") <= 438.5000000000:
                        # if Pups_Location_Rat_Distance <= 766.8681945801
                        if _get(features, "Pups_Location_Rat_Distance") <= 766.8681945801:
                            return "OE"
                        else:
                            # if Nest_Dist_RT_To_Bbox_BL <= 464.4088592529
                            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 464.4088592529:
                                return "NB"
                            else:
                                return "ONE"
                    else:
                        # if Actor_Dist_RB_To_Bbox_TR <= 345.1275177002
                        if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 345.1275177002:
                            # if Actor_hu_6 <= -0.0000233500
                            if _get(features, "Actor_hu_6") <= -0.0000233500:
                                # if foodhopperBottom_Nest_Distance <= 348.4085845947
                                if _get(features, "foodhopperBottom_Nest_Distance") <= 348.4085845947:
                                    return "ONE"
                                else:
                                    return "OE"
                            else:
                                # if Nest_hu_5 <= -0.0000034800
                                if _get(features, "Nest_hu_5") <= -0.0000034800:
                                    # if Actor_Dist_RL_To_Bbox_TL <= 37.5000000000
                                    if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 37.5000000000:
                                        # if Actor_Centroid_To_Bbox_TR <= 148.0744628906
                                        if _get(features, "Actor_Centroid_To_Bbox_TR") <= 148.0744628906:
                                            return "ONE"
                                        else:
                                            # if Nest_Dist_RR_To_Bbox_BR <= 119.5041847229
                                            if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 119.5041847229:
                                                return "ONE"
                                            else:
                                                return "OE"
                                    else:
                                        # if Actor_hu_4 <= 0.0075967819
                                        if _get(features, "Actor_hu_4") <= 0.0075967819:
                                            # if Actor_centroid_y <= 420.6081848145
                                            if _get(features, "Actor_centroid_y") <= 420.6081848145:
                                                return "ONE"
                                            else:
                                                # if Actor_eccentricity <= 0.9592491388
                                                if _get(features, "Actor_eccentricity") <= 0.9592491388:
                                                    return "OE"
                                                else:
                                                    # if Nest_area <= 35961.7500000000
                                                    if _get(features, "Nest_area") <= 35961.7500000000:
                                                        return "ONE"
                                                    else:
                                                        return "OE"
                                        else:
                                            return "ONE"
                                else:
                                    # if Actor_hu_4 <= -0.0000014250
                                    if _get(features, "Actor_hu_4") <= -0.0000014250:
                                        # if pipeEnd_Rat_Distance <= 66.1948585510
                                        if _get(features, "pipeEnd_Rat_Distance") <= 66.1948585510:
                                            return "ONE"
                                        else:
                                            # if Nest_Dist_RR_To_Bbox_TR <= 68.0073547363
                                            if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 68.0073547363:
                                                # if Actor_Dist_RL_RT <= 172.2831192017
                                                if _get(features, "Actor_Dist_RL_RT") <= 172.2831192017:
                                                    return "OE"
                                                else:
                                                    return "ONE"
                                            else:
                                                return "ONE"
                                    else:
                                        # if Actor_Dist_RL_To_Bbox_BR <= 83.9463081360
                                        if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 83.9463081360:
                                            # if Actor_Dist_RB_To_Bbox_TL <= 130.6120071411
                                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 130.6120071411:
                                                # if Actor_RB_y <= 588.5000000000
                                                if _get(features, "Actor_RB_y") <= 588.5000000000:
                                                    return "OE"
                                                else:
                                                    # if Nest_centroid_x <= 332.3167114258
                                                    if _get(features, "Nest_centroid_x") <= 332.3167114258:
                                                        return "OE"
                                                    else:
                                                        return "ONE"
                                            else:
                                                return "ONE"
                                        else:
                                            # if Actor_Dist_RT_RB <= 347.6555023193
                                            if _get(features, "Actor_Dist_RT_RB") <= 347.6555023193:
                                                # if Actor_To_Nest_Distance <= 110.7360954285
                                                if _get(features, "Actor_To_Nest_Distance") <= 110.7360954285:
                                                    return "ONE"
                                                else:
                                                    # if Actor_hu_3 <= 0.0985210240
                                                    if _get(features, "Actor_hu_3") <= 0.0985210240:
                                                        # if Nest_hu_5 <= 0.0438605975
                                                        if _get(features, "Nest_hu_5") <= 0.0438605975:
                                                            # if Nest_RR_x <= 535.5000000000
                                                            if _get(features, "Nest_RR_x") <= 535.5000000000:
                                                                # if Actor_Centroid_To_Bbox_BR <= 225.2759704590
                                                                if _get(features, "Actor_Centroid_To_Bbox_BR") <= 225.2759704590:
                                                                    # if pipeEnd_Rat_Distance <= 33.3467807770
                                                                    if _get(features, "pipeEnd_Rat_Distance") <= 33.3467807770:
                                                                        # if Nest_bbox_y <= 472.5000000000
                                                                        if _get(features, "Nest_bbox_y") <= 472.5000000000:
                                                                            return "ONE"
                                                                        else:
                                                                            return "OE"
                                                                    else:
                                                                        # if Actor_To_Nest_Dist_Change <= -19.7875423431
                                                                        if _get(features, "Actor_To_Nest_Dist_Change") <= -19.7875423431:
                                                                            # if Actor_Dist_RT_RR <= 352.9601745605
                                                                            if _get(features, "Actor_Dist_RT_RR") <= 352.9601745605:
                                                                                # if Nest_area <= 37185.7500000000
                                                                                if _get(features, "Nest_area") <= 37185.7500000000:
                                                                                    # if Nest_Dist_RT_RR <= 163.7610092163
                                                                                    if _get(features, "Nest_Dist_RT_RR") <= 163.7610092163:
                                                                                        # if Actor_orientation <= 12.9167327881
                                                                                        if _get(features, "Actor_orientation") <= 12.9167327881:
                                                                                            return "ONE"
                                                                                        else:
                                                                                            return "OE"
                                                                                    else:
                                                                                        return "ONE"
                                                                                else:
                                                                                    return "ONE"
                                                                            else:
                                                                                return "ONE"
                                                                        else:
                                                                            # if pipeStart_Rat_Distance <= 99.2616920471
                                                                            if _get(features, "pipeStart_Rat_Distance") <= 99.2616920471:
                                                                                # if Nest_perimeter <= 1071.2884521484
                                                                                if _get(features, "Nest_perimeter") <= 1071.2884521484:
                                                                                    # if Nest_RL_y <= 611.5000000000
                                                                                    if _get(features, "Nest_RL_y") <= 611.5000000000:
                                                                                        return "ONE"
                                                                                    else:
                                                                                        return "OE"
                                                                                else:
                                                                                    # if Actor_RR_y <= 380.0000000000
                                                                                    if _get(features, "Actor_RR_y") <= 380.0000000000:
                                                                                        return "ONE"
                                                                                    else:
                                                                                        return "OE"
                                                                            else:
                                                                                # if Actor_hu_6 <= -0.0000152000
                                                                                if _get(features, "Actor_hu_6") <= -0.0000152000:
                                                                                    # if Nest_centroid_x <= 324.5490570068
                                                                                    if _get(features, "Nest_centroid_x") <= 324.5490570068:
                                                                                        return "OE"
                                                                                    else:
                                                                                        return "ONE"
                                                                                else:
                                                                                    # if Nest_aspect_ratio <= 1.5786893964
                                                                                    if _get(features, "Nest_aspect_ratio") <= 1.5786893964:
                                                                                        # if Actor_Dist_RT_RB <= 190.9716720581
                                                                                        if _get(features, "Actor_Dist_RT_RB") <= 190.9716720581:
                                                                                            return "ONE"
                                                                                        else:
                                                                                            return "OE"
                                                                                    else:
                                                                                        # if Actor_hu_5 <= 0.0338661838
                                                                                        if _get(features, "Actor_hu_5") <= 0.0338661838:
                                                                                            # if Actor_Dist_RT_To_Bbox_BR <= 392.9872283936
                                                                                            if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 392.9872283936:
                                                                                                # if foodhopperLeft_Nest_Distance <= 492.1067352295
                                                                                                if _get(features, "foodhopperLeft_Nest_Distance") <= 492.1067352295:
                                                                                                    # if Actor_Dist_RB_RL <= 262.4689331055
                                                                                                    if _get(features, "Actor_Dist_RB_RL") <= 262.4689331055:
                                                                                                        return "OE"
                                                                                                    else:
                                                                                                        # if Actor_Dist_RB_RL <= 263.3077850342
                                                                                                        if _get(features, "Actor_Dist_RB_RL") <= 263.3077850342:
                                                                                                            return "ONE"
                                                                                                        else:
                                                                                                            # if Actor_Dist_RB_To_Bbox_TL <= 276.3769989014
                                                                                                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 276.3769989014:
                                                                                                                return "ONE"
                                                                                                            else:
                                                                                                                # if Actor_Dist_RL_To_Bbox_BL <= 102.0000000000
                                                                                                                if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 102.0000000000:
                                                                                                                    # if Actor_Centroid_To_Bbox_TL <= 245.6408157349
                                                                                                                    if _get(features, "Actor_Centroid_To_Bbox_TL") <= 245.6408157349:
                                                                                                                        return "OE"
                                                                                                                    else:
                                                                                                                        return "ONE"
                                                                                                                else:
                                                                                                                    # if Actor_Dist_RL_To_Bbox_TL <= 7.5000000000
                                                                                                                    if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 7.5000000000:
                                                                                                                        # if c3_Rat_Distance <= 434.1877593994
                                                                                                                        if _get(features, "c3_Rat_Distance") <= 434.1877593994:
                                                                                                                            return "OE"
                                                                                                                        else:
                                                                                                                            return "ONE"
                                                                                                                    else:
                                                                                                                        # if Actor_hu_0 <= 0.4773539454
                                                                                                                        if _get(features, "Actor_hu_0") <= 0.4773539454:
                                                                                                                            # if Nest_Dist_RT_To_Bbox_TR <= 39.5000000000
                                                                                                                            if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 39.5000000000:
                                                                                                                                # if Actor_orientation <= 106.5210266113
                                                                                                                                if _get(features, "Actor_orientation") <= 106.5210266113:
                                                                                                                                    return "OE"
                                                                                                                                else:
                                                                                                                                    return "ONE"
                                                                                                                            else:
                                                                                                                                return "OE"
                                                                                                                        else:
                                                                                                                            # if Actor_extent <= 0.3269055933
                                                                                                                            if _get(features, "Actor_extent") <= 0.3269055933:
                                                                                                                                return "OE"
                                                                                                                            else:
                                                                                                                                return "ONE"
                                                                                                else:
                                                                                                    # if Nest_Centroid_To_Bbox_BR <= 221.4431152344
                                                                                                    if _get(features, "Nest_Centroid_To_Bbox_BR") <= 221.4431152344:
                                                                                                        return "ONE"
                                                                                                    else:
                                                                                                        return "OE"
                                                                                            else:
                                                                                                # if Nest_bbox_y <= 461.5000000000
                                                                                                if _get(features, "Nest_bbox_y") <= 461.5000000000:
                                                                                                    return "ONE"
                                                                                                else:
                                                                                                    return "OE"
                                                                                        else:
                                                                                            # if Actor_area <= 20081.2500000000
                                                                                            if _get(features, "Actor_area") <= 20081.2500000000:
                                                                                                return "OE"
                                                                                            else:
                                                                                                return "ONE"
                                                                else:
                                                                    # if foodhopperLeft_Rat_Distance <= 462.0324096680
                                                                    if _get(features, "foodhopperLeft_Rat_Distance") <= 462.0324096680:
                                                                        # if Nest_Centroid_To_Bbox_BL <= 171.2956924438
                                                                        if _get(features, "Nest_Centroid_To_Bbox_BL") <= 171.2956924438:
                                                                            return "OE"
                                                                        else:
                                                                            return "ONE"
                                                                    else:
                                                                        return "OE"
                                                            else:
                                                                return "ONE"
                                                        else:
                                                            return "NB"
                                                    else:
                                                        # if Nest_bbox_h <= 191.5000000000
                                                        if _get(features, "Nest_bbox_h") <= 191.5000000000:
                                                            return "OE"
                                                        else:
                                                            return "ONE"
                                            else:
                                                return "ONE"
                        else:
                            # if Actor_orientation <= 63.8299789429
                            if _get(features, "Actor_orientation") <= 63.8299789429:
                                # if Nest_Dist_RB_To_Bbox_TR <= 336.8545532227
                                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 336.8545532227:
                                    # if Actor_Centroid_To_Bbox_BL <= 200.0366058350
                                    if _get(features, "Actor_Centroid_To_Bbox_BL") <= 200.0366058350:
                                        return "OE"
                                    else:
                                        # if foodhopperBottom_Rat_Distance <= 404.6971435547
                                        if _get(features, "foodhopperBottom_Rat_Distance") <= 404.6971435547:
                                            return "OE"
                                        else:
                                            return "ONE"
                                else:
                                    return "ONE"
                            else:
                                # if Actor_Dist_RB_To_Bbox_BL <= 95.5052375793
                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 95.5052375793:
                                    return "OE"
                                else:
                                    # if Pups_Location_Rat_Distance <= 796.8511962891
                                    if _get(features, "Pups_Location_Rat_Distance") <= 796.8511962891:
                                        # if Actor_RL_x <= 75.5000000000
                                        if _get(features, "Actor_RL_x") <= 75.5000000000:
                                            return "ONE"
                                        else:
                                            return "OE"
                                    else:
                                        return "OE"
                else:
                    # if Actor_area <= 23375.7500000000
                    if _get(features, "Actor_area") <= 23375.7500000000:
                        # if Actor_Mask_IoU <= 0.9634583592
                        if _get(features, "Actor_Mask_IoU") <= 0.9634583592:
                            # if Nest_Dist_RR_To_Bbox_BR <= 148.5033645630
                            if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 148.5033645630:
                                # if c2_Rat_Distance <= 667.7499389648
                                if _get(features, "c2_Rat_Distance") <= 667.7499389648:
                                    return "ONE"
                                else:
                                    return "OE"
                            else:
                                return "OE"
                        else:
                            # if Nest_hu_1 <= 0.0801251046
                            if _get(features, "Nest_hu_1") <= 0.0801251046:
                                return "ONE"
                            else:
                                return "OE"
                    else:
                        return "OE"
            else:
                # if Nest_hu_0 <= 0.2693002224
                if _get(features, "Nest_hu_0") <= 0.2693002224:
                    # if Nest_Centroid_To_Bbox_TL <= 204.2137145996
                    if _get(features, "Nest_Centroid_To_Bbox_TL") <= 204.2137145996:
                        # if Actor_area <= 11478.7500000000
                        if _get(features, "Actor_area") <= 11478.7500000000:
                            return "OE"
                        else:
                            # if Actor_RB_y <= 567.0000000000
                            if _get(features, "Actor_RB_y") <= 567.0000000000:
                                return "ONE"
                            else:
                                return "OE"
                    else:
                        # if c3_Nest_Distance <= 951.6295776367
                        if _get(features, "c3_Nest_Distance") <= 951.6295776367:
                            # if Nest_Mask_IoU <= 0.9923439026
                            if _get(features, "Nest_Mask_IoU") <= 0.9923439026:
                                # if Nest_Dist_RT_RR <= 44.2142667770
                                if _get(features, "Nest_Dist_RT_RR") <= 44.2142667770:
                                    return "OE"
                                else:
                                    return "ONE"
                            else:
                                return "OE"
                        else:
                            return "OE"
                else:
                    # if Nest_solidity <= 0.8752641082
                    if _get(features, "Nest_solidity") <= 0.8752641082:
                        # if Nest_RR_y <= 494.5000000000
                        if _get(features, "Nest_RR_y") <= 494.5000000000:
                            return "NB"
                        else:
                            # if Nest_Dist_RT_To_Bbox_BR <= 199.4513626099
                            if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 199.4513626099:
                                return "ONE"
                            else:
                                # if Nest_solidity <= 0.8627046645
                                if _get(features, "Nest_solidity") <= 0.8627046645:
                                    return "OE"
                                else:
                                    # if Actor_Dist_RL_To_Bbox_BL <= 145.5000000000
                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 145.5000000000:
                                        return "OE"
                                    else:
                                        return "ONE"
                    else:
                        return "ONE"
    else:
        # if Nest_Dist_RT_To_Bbox_TR <= 12.0000000000
        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 12.0000000000:
            # if Nest_Dist_RR_To_Bbox_BR <= 134.0037574768
            if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 134.0037574768:
                return "OE"
            else:
                # if Actor_To_Nest_Dist_Change <= 4.8605563641
                if _get(features, "Actor_To_Nest_Dist_Change") <= 4.8605563641:
                    return "ONE"
                else:
                    return "NB"
        else:
            # if Actor_Centroid_To_Bbox_TL <= 160.8755111694
            if _get(features, "Actor_Centroid_To_Bbox_TL") <= 160.8755111694:
                # if Actor_centroid_x <= 201.8019256592
                if _get(features, "Actor_centroid_x") <= 201.8019256592:
                    return "NB"
                else:
                    return "OE"
            else:
                # if Nest_eccentricity <= 0.9618000984
                if _get(features, "Nest_eccentricity") <= 0.9618000984:
                    # if c3_Rat_Distance <= 1103.0532226562
                    if _get(features, "c3_Rat_Distance") <= 1103.0532226562:
                        # if Nest_Dist_RT_To_Bbox_TR <= 16.5000000000
                        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 16.5000000000:
                            # if Nest_Dist_RT_To_Bbox_BR <= 194.0511779785
                            if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 194.0511779785:
                                return "OE"
                            else:
                                return "NB"
                        else:
                            # if Actor_RB_x <= 71.5000000000
                            if _get(features, "Actor_RB_x") <= 71.5000000000:
                                # if Actor_Mask_IoU <= 0.9294822216
                                if _get(features, "Actor_Mask_IoU") <= 0.9294822216:
                                    return "NB"
                                else:
                                    return "OE"
                            else:
                                return "NB"
                    else:
                        # if Actor_area <= 54924.5000000000
                        if _get(features, "Actor_area") <= 54924.5000000000:
                            return "ONE"
                        else:
                            return "NB"
                else:
                    # if Nest_perimeter <= 870.0214233398
                    if _get(features, "Nest_perimeter") <= 870.0214233398:
                        return "OE"
                    else:
                        # if Nest_hu_2 <= 0.0162282602
                        if _get(features, "Nest_hu_2") <= 0.0162282602:
                            return "ONE"
                        else:
                            return "NB"


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
