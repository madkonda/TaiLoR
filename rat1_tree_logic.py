# THIS FILE IS AUTO-GENERATED: pure if/else logic for your hierarchical classifier.
# Requires only Python + numpy/pandas at runtime (sklearn not required).
# Do not edit by hand; regenerate after retraining.

import numpy as np

# --- constants learned at training time ---
ROUTER_COLS = ["Nest_RT_x", "Nest_orientation", "Nest_bbox_x", "Nest_RL_x", "c3_Nest_Distance", "Nest_centroid_x", "c2_Nest_Distance", "c4_Nest_Distance", "c1_Nest_Distance", "pipeEnd_Nest_Distance", "pipeMid_Nest_Distance", "Pups_Location_Nest_Distance", "foodhopperLeft_Nest_Distance", "Nest_RR_y", "pipeStart_Nest_Distance", "Nest_extent", "Actor_RR_x", "foodhopperBottom_Nest_Distance", "foodhopperMid_Nest_Distance", "Nest_RR_x", "Nest_hu_6", "Nest_RL_y", "Nest_hu_2", "Nest_Dist_RL_To_Bbox_BL", "Nest_Dist_RR_To_Bbox_TR", "Actor_To_Nest_Distance", "Nest_Dist_RT_To_Bbox_TL", "Actor_RB_x", "Nest_Dist_RT_RR", "Nest_solidity", "Nest_Dist_RL_RT", "Nest_Dist_RT_RB", "Nest_Dist_RT_To_Bbox_BR", "Actor_centroid_x", "Nest_RB_y", "c3_Rat_Distance", "Nest_Dist_RT_To_Bbox_TR", "Nest_hu_3", "pipeEnd_Rat_Distance", "c4_Rat_Distance", "foodhopperLeft_Rat_Distance", "Nest_RB_x", "foodhopperRight_Rat_Distance", "Nest_Dist_RT_To_Bbox_BL", "Nest_centroid_y", "Nest_Centroid_To_Bbox_TR", "c1_Rat_Distance", "foodhopperRight_Nest_Distance", "Nest_Dist_RR_To_Bbox_BL", "Nest_Dist_RL_To_Bbox_TR", "c2_Rat_Distance", "Nest_hu_0", "Pups_Location_Rat_Distance", "Nest_bbox_w", "Nest_Dist_RL_RR", "Nest_Centroid_To_Bbox_BR", "Nest_aspect_ratio", "Nest_Dist_RR_To_Bbox_BR", "Nest_Dist_RR_To_Bbox_TL", "Nest_perimeter", "Nest_Dist_RL_To_Bbox_BR", "Actor_RT_x", "Nest_Dist_RB_RL", "Nest_hu_4", "Nest_bbox_h", "Nest_Dist_RB_To_Bbox_TL", "pipeMid_Rat_Distance", "Actor_Dist_RB_To_Bbox_BR", "foodhopperMid_Rat_Distance", "Nest_Dist_RL_To_Bbox_TL", "Nest_RT_y", "Nest_Centroid_To_Bbox_TL", "Actor_centroid_y", "Actor_RL_x", "foodhopperBottom_Rat_Distance", "Actor_bbox_x", "Nest_Centroid_To_Bbox_BL", "Actor_bbox_h", "Nest_bbox_y", "Actor_Dist_RL_To_Bbox_BR", "Actor_Mask_IoU", "Nest_hu_5", "Nest_hu_1", "pipeStart_Rat_Distance", "Nest_Dist_RB_To_Bbox_BL", "Actor_RB_y", "Actor_Dist_RB_To_Bbox_TL", "Nest_area", "Nest_Mask_IoU", "Actor_Dist_RB_To_Bbox_TR", "Nest_eccentricity", "Actor_Dist_RT_To_Bbox_BL", "Actor_Dist_RR_RB", "Actor_area", "Actor_Dist_RR_To_Bbox_TR", "Actor_Centroid_To_Bbox_TR", "Actor_Dist_RR_To_Bbox_TL", "Actor_Centroid_To_Bbox_BR", "Actor_Centroid_To_Bbox_TL", "Actor_Dist_RR_To_Bbox_BR", "Actor_Centroid_To_Bbox_BL", "Actor_hu_1", "Nest_Dist_RR_RB", "Actor_Dist_RB_RL", "Actor_orientation", "Actor_Dist_RL_RR", "Actor_Dist_RB_To_Bbox_BL", "Actor_aspect_ratio", "Actor_perimeter", "Actor_hu_5", "Actor_eccentricity", "Actor_hu_2", "Actor_bbox_w", "Actor_Dist_RR_To_Bbox_BL", "Actor_Dist_RT_To_Bbox_BR", "Actor_Dist_RL_To_Bbox_TR", "Actor_hu_0", "Actor_bbox_y", "Actor_Dist_RL_RT", "Actor_Dist_RT_To_Bbox_TL", "Nest_Dist_RB_To_Bbox_TR", "Actor_extent", "Nest_Dist_RB_To_Bbox_BR", "Actor_Dist_RT_RR", "Actor_RT_y", "Actor_hu_3", "Actor_solidity", "Actor_Dist_RT_To_Bbox_TR", "Actor_RR_y", "Actor_Dist_RL_To_Bbox_BL", "Actor_hu_6", "Actor_Area_Diff_Abs", "Actor_Dist_RL_To_Bbox_TL", "Actor_RL_y", "Actor_Dist_RT_RB", "Actor_To_Nest_Dist_Change", "Nest_Area_Diff_Abs", "Actor_Direction_deg", "Actor_hu_4"]
OENB_COLS   = ["Actor_area", "Actor_perimeter", "Actor_centroid_x", "Actor_centroid_y", "Actor_bbox_x", "Actor_bbox_y", "Actor_bbox_w", "Actor_bbox_h", "Actor_aspect_ratio", "Actor_extent", "Actor_solidity", "Actor_orientation", "Actor_eccentricity", "Actor_RL_x", "Actor_RL_y", "Actor_RR_x", "Actor_RR_y", "Actor_RT_x", "Actor_RT_y", "Actor_RB_x", "Actor_RB_y", "Actor_hu_0", "Actor_hu_1", "Actor_hu_2", "Actor_hu_3", "Actor_hu_4", "Actor_hu_5", "Actor_hu_6", "Actor_Dist_RL_RR", "Actor_Dist_RT_RB", "Actor_Dist_RL_RT", "Actor_Dist_RT_RR", "Actor_Dist_RR_RB", "Actor_Dist_RB_RL", "Actor_Centroid_To_Bbox_TL", "Actor_Centroid_To_Bbox_TR", "Actor_Centroid_To_Bbox_BR", "Actor_Centroid_To_Bbox_BL", "Actor_Dist_RL_To_Bbox_TL", "Actor_Dist_RL_To_Bbox_TR", "Actor_Dist_RL_To_Bbox_BR", "Actor_Dist_RL_To_Bbox_BL", "Actor_Dist_RR_To_Bbox_TL", "Actor_Dist_RR_To_Bbox_TR", "Actor_Dist_RR_To_Bbox_BR", "Actor_Dist_RR_To_Bbox_BL", "Actor_Dist_RT_To_Bbox_TL", "Actor_Dist_RT_To_Bbox_TR", "Actor_Dist_RT_To_Bbox_BR", "Actor_Dist_RT_To_Bbox_BL", "Actor_Dist_RB_To_Bbox_TL", "Actor_Dist_RB_To_Bbox_TR", "Actor_Dist_RB_To_Bbox_BR", "Actor_Dist_RB_To_Bbox_BL", "Nest_area", "Nest_perimeter", "Nest_centroid_x", "Nest_centroid_y", "Nest_bbox_x", "Nest_bbox_y", "Nest_bbox_w", "Nest_bbox_h", "Nest_aspect_ratio", "Nest_extent", "Nest_solidity", "Nest_orientation", "Nest_eccentricity", "Nest_RL_x", "Nest_RL_y", "Nest_RR_x", "Nest_RR_y", "Nest_RT_x", "Nest_RT_y", "Nest_RB_x", "Nest_RB_y", "Nest_hu_0", "Nest_hu_1", "Nest_hu_2", "Nest_hu_3", "Nest_hu_4", "Nest_hu_5", "Nest_hu_6", "Nest_Dist_RL_RR", "Nest_Dist_RT_RB", "Nest_Dist_RL_RT", "Nest_Dist_RT_RR", "Nest_Dist_RR_RB", "Nest_Dist_RB_RL", "Nest_Centroid_To_Bbox_TL", "Nest_Centroid_To_Bbox_TR", "Nest_Centroid_To_Bbox_BR", "Nest_Centroid_To_Bbox_BL", "Nest_Dist_RL_To_Bbox_TL", "Nest_Dist_RL_To_Bbox_TR", "Nest_Dist_RL_To_Bbox_BR", "Nest_Dist_RL_To_Bbox_BL", "Nest_Dist_RR_To_Bbox_TL", "Nest_Dist_RR_To_Bbox_TR", "Nest_Dist_RR_To_Bbox_BR", "Nest_Dist_RR_To_Bbox_BL", "Nest_Dist_RT_To_Bbox_TL", "Nest_Dist_RT_To_Bbox_TR", "Nest_Dist_RT_To_Bbox_BR", "Nest_Dist_RT_To_Bbox_BL", "Nest_Dist_RB_To_Bbox_TL", "Nest_Dist_RB_To_Bbox_TR", "Nest_Dist_RB_To_Bbox_BR", "Nest_Dist_RB_To_Bbox_BL", "Actor_Area_Diff_Abs", "Actor_Mask_IoU", "Nest_Area_Diff_Abs", "Nest_Mask_IoU", "Actor_To_Nest_Distance", "Actor_Direction_deg", "Actor_To_Nest_Dist_Change", "c1_Rat_Distance", "c1_Nest_Distance", "c2_Rat_Distance", "c2_Nest_Distance", "c3_Rat_Distance", "c3_Nest_Distance", "c4_Rat_Distance", "c4_Nest_Distance", "pipeEnd_Rat_Distance", "pipeEnd_Nest_Distance", "pipeMid_Rat_Distance", "pipeMid_Nest_Distance", "pipeStart_Rat_Distance", "pipeStart_Nest_Distance", "foodhopperBottom_Rat_Distance", "foodhopperBottom_Nest_Distance", "foodhopperLeft_Rat_Distance", "foodhopperLeft_Nest_Distance", "foodhopperRight_Rat_Distance", "foodhopperRight_Nest_Distance", "foodhopperMid_Rat_Distance", "foodhopperMid_Nest_Distance", "Pups_Location_Rat_Distance", "Pups_Location_Nest_Distance"]
RATIO_FEATURE = "Actor_aspect_ratio"
RATIO_THRESH  = 0.5378862405
RATIO_FLIP    = True

def _get(d, k):
    try:
        return float(d.get(k, float("nan")))
    except Exception:
        return float("nan")


def router_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Nest_orientation <= 99.3219413757
    if _get(features, "Nest_orientation") <= 99.3219413757:
        # if Nest_RT_x <= 835.5000000000
        if _get(features, "Nest_RT_x") <= 835.5000000000:
            # if Nest_Dist_RT_RB <= 105.1654396057
            if _get(features, "Nest_Dist_RT_RB") <= 105.1654396057:
                # if Nest_Dist_RB_To_Bbox_TR <= 143.9687347412
                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 143.9687347412:
                    # if Nest_Dist_RT_RR <= 37.2226991653
                    if _get(features, "Nest_Dist_RT_RR") <= 37.2226991653:
                        return "OENB"
                    else:
                        return "PI_SI"
                else:
                    return "OENB"
            else:
                # if c2_Nest_Distance <= 675.1291198730
                if _get(features, "c2_Nest_Distance") <= 675.1291198730:
                    # if Nest_Dist_RL_To_Bbox_TR <= 289.0928802490
                    if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 289.0928802490:
                        return "OENB"
                    else:
                        return "PI_SI"
                else:
                    # if Nest_Centroid_To_Bbox_TL <= 88.4757919312
                    if _get(features, "Nest_Centroid_To_Bbox_TL") <= 88.4757919312:
                        return "PI_SI"
                    else:
                        # if Pups_Location_Rat_Distance <= 83.0406608582
                        if _get(features, "Pups_Location_Rat_Distance") <= 83.0406608582:
                            return "PI_SI"
                        else:
                            # if Nest_hu_0 <= 0.2706543356
                            if _get(features, "Nest_hu_0") <= 0.2706543356:
                                return "PI_SI"
                            else:
                                return "OENB"
        else:
            # if Nest_perimeter <= 1252.6660766602
            if _get(features, "Nest_perimeter") <= 1252.6660766602:
                # if Actor_Dist_RL_To_Bbox_BR <= 169.6475982666
                if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 169.6475982666:
                    return "OENB"
                else:
                    # if Nest_Mask_IoU <= 0.7945336699
                    if _get(features, "Nest_Mask_IoU") <= 0.7945336699:
                        # if Nest_Dist_RL_To_Bbox_BL <= 71.0000000000
                        if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 71.0000000000:
                            # if Nest_Dist_RB_To_Bbox_BL <= 335.0014801025
                            if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 335.0014801025:
                                # if Nest_RR_x <= 1107.5000000000
                                if _get(features, "Nest_RR_x") <= 1107.5000000000:
                                    # if Actor_RB_y <= 642.5000000000
                                    if _get(features, "Actor_RB_y") <= 642.5000000000:
                                        # if Pups_Location_Nest_Distance <= 25.4956912994
                                        if _get(features, "Pups_Location_Nest_Distance") <= 25.4956912994:
                                            return "OENB"
                                        else:
                                            # if Actor_Centroid_To_Bbox_BR <= 207.2330398560
                                            if _get(features, "Actor_Centroid_To_Bbox_BR") <= 207.2330398560:
                                                # if Nest_hu_0 <= 0.1819690168
                                                if _get(features, "Nest_hu_0") <= 0.1819690168:
                                                    # if foodhopperBottom_Nest_Distance <= 360.5814971924
                                                    if _get(features, "foodhopperBottom_Nest_Distance") <= 360.5814971924:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                                else:
                                                    # if Nest_RR_y <= 635.0000000000
                                                    if _get(features, "Nest_RR_y") <= 635.0000000000:
                                                        # if Nest_Dist_RR_To_Bbox_BR <= 2.6991728544
                                                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 2.6991728544:
                                                            return "OENB"
                                                        else:
                                                            return "PI_SI"
                                                    else:
                                                        return "OENB"
                                            else:
                                                # if Nest_Dist_RT_RR <= 163.2734298706
                                                if _get(features, "Nest_Dist_RT_RR") <= 163.2734298706:
                                                    # if Actor_Dist_RB_To_Bbox_BR <= 190.5026245117
                                                    if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 190.5026245117:
                                                        # if Actor_Dist_RT_RB <= 257.8421630859
                                                        if _get(features, "Actor_Dist_RT_RB") <= 257.8421630859:
                                                            return "OENB"
                                                        else:
                                                            # if Actor_To_Nest_Distance <= 148.9461975098
                                                            if _get(features, "Actor_To_Nest_Distance") <= 148.9461975098:
                                                                return "OENB"
                                                            else:
                                                                # if Nest_Dist_RR_To_Bbox_TR <= 7.0772025585
                                                                if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 7.0772025585:
                                                                    return "OENB"
                                                                else:
                                                                    # if Actor_Direction_deg <= 156.9176254272
                                                                    if _get(features, "Actor_Direction_deg") <= 156.9176254272:
                                                                        return "PI_SI"
                                                                    else:
                                                                        return "OENB"
                                                    else:
                                                        # if Actor_hu_3 <= 0.0000954145
                                                        if _get(features, "Actor_hu_3") <= 0.0000954145:
                                                            # if Actor_eccentricity <= 0.7274864912
                                                            if _get(features, "Actor_eccentricity") <= 0.7274864912:
                                                                return "PI_SI"
                                                            else:
                                                                return "OENB"
                                                        else:
                                                            return "PI_SI"
                                                else:
                                                    return "OENB"
                                    else:
                                        # if Nest_RL_x <= 798.5000000000
                                        if _get(features, "Nest_RL_x") <= 798.5000000000:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                else:
                                    # if Nest_Centroid_To_Bbox_TL <= 246.2571105957
                                    if _get(features, "Nest_Centroid_To_Bbox_TL") <= 246.2571105957:
                                        # if Nest_extent <= 0.7195552886
                                        if _get(features, "Nest_extent") <= 0.7195552886:
                                            # if Actor_Area_Diff_Abs <= 47.7500000000
                                            if _get(features, "Actor_Area_Diff_Abs") <= 47.7500000000:
                                                # if Actor_RB_y <= 654.5000000000
                                                if _get(features, "Actor_RB_y") <= 654.5000000000:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                            else:
                                                return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        # if foodhopperLeft_Rat_Distance <= 734.1381835938
                                        if _get(features, "foodhopperLeft_Rat_Distance") <= 734.1381835938:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
                            else:
                                # if Nest_Dist_RB_To_Bbox_TL <= 389.6439819336
                                if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 389.6439819336:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                        else:
                            # if Actor_Area_Diff_Abs <= 1961.2500000000
                            if _get(features, "Actor_Area_Diff_Abs") <= 1961.2500000000:
                                return "PI_SI"
                            else:
                                return "OENB"
                    else:
                        # if Nest_solidity <= 0.4222956449
                        if _get(features, "Nest_solidity") <= 0.4222956449:
                            return "OENB"
                        else:
                            # if Actor_centroid_x <= 709.1190795898
                            if _get(features, "Actor_centroid_x") <= 709.1190795898:
                                return "OENB"
                            else:
                                # if Actor_hu_6 <= -0.0000023450
                                if _get(features, "Actor_hu_6") <= -0.0000023450:
                                    # if Nest_Dist_RT_To_Bbox_BL <= 113.0769157410
                                    if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 113.0769157410:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    # if Actor_hu_2 <= 0.0000175000
                                    if _get(features, "Actor_hu_2") <= 0.0000175000:
                                        # if Nest_extent <= 0.4890019596
                                        if _get(features, "Nest_extent") <= 0.4890019596:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
                                    else:
                                        # if Actor_hu_0 <= 0.1611081958
                                        if _get(features, "Actor_hu_0") <= 0.1611081958:
                                            return "OENB"
                                        else:
                                            # if Actor_Dist_RR_To_Bbox_TR <= 237.5021057129
                                            if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 237.5021057129:
                                                # if Actor_Dist_RR_To_Bbox_BR <= 3.6675437689
                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 3.6675437689:
                                                    return "OENB"
                                                else:
                                                    # if Actor_hu_5 <= 0.0035772185
                                                    if _get(features, "Actor_hu_5") <= 0.0035772185:
                                                        # if c2_Nest_Distance <= 687.3169860840
                                                        if _get(features, "c2_Nest_Distance") <= 687.3169860840:
                                                            # if Actor_hu_0 <= 0.1646378785
                                                            if _get(features, "Actor_hu_0") <= 0.1646378785:
                                                                # if c2_Rat_Distance <= 539.9624633789
                                                                if _get(features, "c2_Rat_Distance") <= 539.9624633789:
                                                                    # if Nest_Centroid_To_Bbox_TL <= 247.7252044678
                                                                    if _get(features, "Nest_Centroid_To_Bbox_TL") <= 247.7252044678:
                                                                        return "PI_SI"
                                                                    else:
                                                                        return "OENB"
                                                                else:
                                                                    # if c2_Rat_Distance <= 541.2101440430
                                                                    if _get(features, "c2_Rat_Distance") <= 541.2101440430:
                                                                        # if Actor_Dist_RL_RR <= 264.4544219971
                                                                        if _get(features, "Actor_Dist_RL_RR") <= 264.4544219971:
                                                                            return "PI_SI"
                                                                        else:
                                                                            return "OENB"
                                                                    else:
                                                                        return "PI_SI"
                                                            else:
                                                                # if Nest_Dist_RT_To_Bbox_BL <= 407.1263885498
                                                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 407.1263885498:
                                                                    # if Nest_hu_3 <= 0.0000239500
                                                                    if _get(features, "Nest_hu_3") <= 0.0000239500:
                                                                        # if Actor_Dist_RT_To_Bbox_BL <= 261.7761688232
                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 261.7761688232:
                                                                            # if foodhopperBottom_Rat_Distance <= 497.4400634766
                                                                            if _get(features, "foodhopperBottom_Rat_Distance") <= 497.4400634766:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                        else:
                                                                            # if Nest_perimeter <= 1082.8010864258
                                                                            if _get(features, "Nest_perimeter") <= 1082.8010864258:
                                                                                # if Actor_Direction_deg <= 162.1008071899
                                                                                if _get(features, "Actor_Direction_deg") <= 162.1008071899:
                                                                                    # if Nest_Mask_IoU <= 0.9541677237
                                                                                    if _get(features, "Nest_Mask_IoU") <= 0.9541677237:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        # if c1_Nest_Distance <= 1159.1469726562
                                                                                        if _get(features, "c1_Nest_Distance") <= 1159.1469726562:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                else:
                                                                                    # if c3_Nest_Distance <= 290.4431762695
                                                                                    if _get(features, "c3_Nest_Distance") <= 290.4431762695:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                            else:
                                                                                return "OENB"
                                                                    else:
                                                                        # if Actor_solidity <= 0.9873920679
                                                                        if _get(features, "Actor_solidity") <= 0.9873920679:
                                                                            # if Nest_RR_x <= 1018.5000000000
                                                                            if _get(features, "Nest_RR_x") <= 1018.5000000000:
                                                                                # if Nest_Dist_RT_To_Bbox_BR <= 129.5325546265
                                                                                if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 129.5325546265:
                                                                                    return "PI_SI"
                                                                                else:
                                                                                    return "OENB"
                                                                            else:
                                                                                # if Actor_RB_y <= 655.5000000000
                                                                                if _get(features, "Actor_RB_y") <= 655.5000000000:
                                                                                    # if Actor_area <= 71783.5000000000
                                                                                    if _get(features, "Actor_area") <= 71783.5000000000:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        # if c1_Nest_Distance <= 1139.5953369141
                                                                                        if _get(features, "c1_Nest_Distance") <= 1139.5953369141:
                                                                                            return "OENB"
                                                                                        else:
                                                                                            return "PI_SI"
                                                                                else:
                                                                                    # if pipeStart_Nest_Distance <= 608.7421264648
                                                                                    if _get(features, "pipeStart_Nest_Distance") <= 608.7421264648:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                        else:
                                                                            # if pipeStart_Nest_Distance <= 506.0499420166
                                                                            if _get(features, "pipeStart_Nest_Distance") <= 506.0499420166:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                else:
                                                                    # if Nest_Dist_RR_To_Bbox_BR <= 39.5129051208
                                                                    if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 39.5129051208:
                                                                        return "PI_SI"
                                                                    else:
                                                                        return "OENB"
                                                        else:
                                                            # if Nest_hu_6 <= 0.0000431500
                                                            if _get(features, "Nest_hu_6") <= 0.0000431500:
                                                                # if Nest_Dist_RT_To_Bbox_BR <= 200.7642364502
                                                                if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 200.7642364502:
                                                                    # if Actor_RR_y <= 603.5000000000
                                                                    if _get(features, "Actor_RR_y") <= 603.5000000000:
                                                                        # if Nest_Dist_RT_To_Bbox_TL <= 32.5000000000
                                                                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 32.5000000000:
                                                                            return "OENB"
                                                                        else:
                                                                            # if pipeEnd_Rat_Distance <= 383.7716217041
                                                                            if _get(features, "pipeEnd_Rat_Distance") <= 383.7716217041:
                                                                                # if Nest_perimeter <= 925.5964965820
                                                                                if _get(features, "Nest_perimeter") <= 925.5964965820:
                                                                                    # if pipeMid_Nest_Distance <= 486.0977630615
                                                                                    if _get(features, "pipeMid_Nest_Distance") <= 486.0977630615:
                                                                                        return "OENB"
                                                                                    else:
                                                                                        return "PI_SI"
                                                                                else:
                                                                                    return "PI_SI"
                                                                            else:
                                                                                # if Nest_hu_6 <= 0.0000032550
                                                                                if _get(features, "Nest_hu_6") <= 0.0000032550:
                                                                                    # if Nest_hu_6 <= 0.0000009555
                                                                                    if _get(features, "Nest_hu_6") <= 0.0000009555:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        # if foodhopperLeft_Rat_Distance <= 725.5886230469
                                                                                        if _get(features, "foodhopperLeft_Rat_Distance") <= 725.5886230469:
                                                                                            return "PI_SI"
                                                                                        else:
                                                                                            return "OENB"
                                                                                else:
                                                                                    # if pipeMid_Rat_Distance <= 553.8763122559
                                                                                    if _get(features, "pipeMid_Rat_Distance") <= 553.8763122559:
                                                                                        return "PI_SI"
                                                                                    else:
                                                                                        return "OENB"
                                                                    else:
                                                                        # if Nest_centroid_y <= 591.5462036133
                                                                        if _get(features, "Nest_centroid_y") <= 591.5462036133:
                                                                            # if Nest_Dist_RB_RL <= 167.7959823608
                                                                            if _get(features, "Nest_Dist_RB_RL") <= 167.7959823608:
                                                                                return "PI_SI"
                                                                            else:
                                                                                return "OENB"
                                                                        else:
                                                                            # if foodhopperMid_Nest_Distance <= 453.2963256836
                                                                            if _get(features, "foodhopperMid_Nest_Distance") <= 453.2963256836:
                                                                                return "OENB"
                                                                            else:
                                                                                return "PI_SI"
                                                                else:
                                                                    return "OENB"
                                                            else:
                                                                return "OENB"
                                                    else:
                                                        # if c2_Nest_Distance <= 623.4593200684
                                                        if _get(features, "c2_Nest_Distance") <= 623.4593200684:
                                                            return "PI_SI"
                                                        else:
                                                            # if Nest_Dist_RT_To_Bbox_TL <= 59.0000000000
                                                            if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 59.0000000000:
                                                                return "OENB"
                                                            else:
                                                                return "PI_SI"
                                            else:
                                                # if Nest_bbox_w <= 175.5000000000
                                                if _get(features, "Nest_bbox_w") <= 175.5000000000:
                                                    return "PI_SI"
                                                else:
                                                    # if Nest_hu_3 <= 0.0003415470
                                                    if _get(features, "Nest_hu_3") <= 0.0003415470:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
            else:
                # if Actor_RR_x <= 1237.5000000000
                if _get(features, "Actor_RR_x") <= 1237.5000000000:
                    return "PI_SI"
                else:
                    return "OENB"
    else:
        # if Nest_RL_x <= 793.5000000000
        if _get(features, "Nest_RL_x") <= 793.5000000000:
            # if Nest_extent <= 0.4814090878
            if _get(features, "Nest_extent") <= 0.4814090878:
                # if Nest_hu_6 <= 0.0000008200
                if _get(features, "Nest_hu_6") <= 0.0000008200:
                    # if Actor_bbox_h <= 230.5000000000
                    if _get(features, "Actor_bbox_h") <= 230.5000000000:
                        return "PI_SI"
                    else:
                        return "OENB"
                else:
                    return "OENB"
            else:
                # if Actor_Centroid_To_Bbox_BR <= 231.0606231689
                if _get(features, "Actor_Centroid_To_Bbox_BR") <= 231.0606231689:
                    return "PI_SI"
                else:
                    # if Nest_RR_y <= 588.0000000000
                    if _get(features, "Nest_RR_y") <= 588.0000000000:
                        return "PI_SI"
                    else:
                        return "OENB"
        else:
            # if Actor_RR_x <= 1201.5000000000
            if _get(features, "Actor_RR_x") <= 1201.5000000000:
                # if Actor_Dist_RR_To_Bbox_BR <= 34.0147151947
                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 34.0147151947:
                    # if Nest_Dist_RR_RB <= 33.7018165588
                    if _get(features, "Nest_Dist_RR_RB") <= 33.7018165588:
                        return "OENB"
                    else:
                        return "PI_SI"
                else:
                    return "PI_SI"
            else:
                # if c2_Nest_Distance <= 694.3979492188
                if _get(features, "c2_Nest_Distance") <= 694.3979492188:
                    # if Nest_Centroid_To_Bbox_TR <= 124.6899566650
                    if _get(features, "Nest_Centroid_To_Bbox_TR") <= 124.6899566650:
                        # if Nest_Dist_RT_RB <= 50.8570270538
                        if _get(features, "Nest_Dist_RT_RB") <= 50.8570270538:
                            return "OENB"
                        else:
                            # if Nest_hu_1 <= 0.0009043895
                            if _get(features, "Nest_hu_1") <= 0.0009043895:
                                return "OENB"
                            else:
                                return "PI_SI"
                    else:
                        # if Nest_eccentricity <= 0.9724422395
                        if _get(features, "Nest_eccentricity") <= 0.9724422395:
                            return "OENB"
                        else:
                            return "PI_SI"
                else:
                    # if Actor_RB_y <= 631.5000000000
                    if _get(features, "Actor_RB_y") <= 631.5000000000:
                        # if Actor_Direction_deg <= -108.5571441650
                        if _get(features, "Actor_Direction_deg") <= -108.5571441650:
                            return "OENB"
                        else:
                            # if pipeMid_Rat_Distance <= 586.5164489746
                            if _get(features, "pipeMid_Rat_Distance") <= 586.5164489746:
                                # if Nest_Centroid_To_Bbox_TL <= 33.3005704880
                                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 33.3005704880:
                                    return "OENB"
                                else:
                                    # if Actor_Dist_RR_To_Bbox_BR <= 5.5908911228
                                    if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 5.5908911228:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                            else:
                                return "OENB"
                    else:
                        # if Nest_Dist_RB_To_Bbox_BL <= 40.5126686096
                        if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 40.5126686096:
                            return "PI_SI"
                        else:
                            # if Nest_Area_Diff_Abs <= 63.0000000000
                            if _get(features, "Nest_Area_Diff_Abs") <= 63.0000000000:
                                # if Actor_Dist_RR_To_Bbox_BR <= 54.5091743469
                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 54.5091743469:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                            else:
                                return "OENB"



def oenb_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Nest_RL_y <= 617.0000000000
    if _get(features, "Nest_RL_y") <= 617.0000000000:
        # if Nest_RB_y <= 625.5000000000
        if _get(features, "Nest_RB_y") <= 625.5000000000:
            # if Nest_hu_1 <= 0.0144325341
            if _get(features, "Nest_hu_1") <= 0.0144325341:
                return "ONE"
            else:
                # if Nest_Centroid_To_Bbox_TR <= 100.2082595825
                if _get(features, "Nest_Centroid_To_Bbox_TR") <= 100.2082595825:
                    return "OE"
                else:
                    return "NB"
        else:
            # if Actor_Dist_RB_To_Bbox_TR <= 683.4655456543
            if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 683.4655456543:
                # if Actor_Dist_RB_To_Bbox_TR <= 223.1624908447
                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 223.1624908447:
                    # if Actor_RB_x <= 1193.0000000000
                    if _get(features, "Actor_RB_x") <= 1193.0000000000:
                        # if pipeEnd_Rat_Distance <= 115.2965774536
                        if _get(features, "pipeEnd_Rat_Distance") <= 115.2965774536:
                            return "ONE"
                        else:
                            # if Actor_RR_x <= 1174.0000000000
                            if _get(features, "Actor_RR_x") <= 1174.0000000000:
                                return "OE"
                            else:
                                # if Actor_area <= 34322.5000000000
                                if _get(features, "Actor_area") <= 34322.5000000000:
                                    return "ONE"
                                else:
                                    # if Nest_Dist_RL_To_Bbox_BL <= 40.5000000000
                                    if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 40.5000000000:
                                        # if Nest_centroid_y <= 606.0150756836
                                        if _get(features, "Nest_centroid_y") <= 606.0150756836:
                                            return "ONE"
                                        else:
                                            return "OE"
                                    else:
                                        # if Nest_Area_Diff_Abs <= 6.7500000000
                                        if _get(features, "Nest_Area_Diff_Abs") <= 6.7500000000:
                                            return "ONE"
                                        else:
                                            # if Actor_Dist_RB_To_Bbox_TR <= 181.9986267090
                                            if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 181.9986267090:
                                                return "ONE"
                                            else:
                                                # if Actor_Dist_RT_To_Bbox_TR <= 161.5000000000
                                                if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 161.5000000000:
                                                    # if Actor_Direction_deg <= -162.5930633545
                                                    if _get(features, "Actor_Direction_deg") <= -162.5930633545:
                                                        # if Nest_hu_4 <= 0.0024061725
                                                        if _get(features, "Nest_hu_4") <= 0.0024061725:
                                                            return "ONE"
                                                        else:
                                                            return "OE"
                                                    else:
                                                        return "OE"
                                                else:
                                                    return "ONE"
                    else:
                        # if Pups_Location_Rat_Distance <= 88.8568801880
                        if _get(features, "Pups_Location_Rat_Distance") <= 88.8568801880:
                            return "OE"
                        else:
                            # if Nest_Dist_RR_To_Bbox_BL <= 200.1062240601
                            if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 200.1062240601:
                                return "OE"
                            else:
                                return "ONE"
                else:
                    # if Actor_orientation <= 165.4986724854
                    if _get(features, "Actor_orientation") <= 165.4986724854:
                        # if Nest_Dist_RB_RL <= 37.3444652557
                        if _get(features, "Nest_Dist_RB_RL") <= 37.3444652557:
                            # if Nest_hu_1 <= 0.1679990776
                            if _get(features, "Nest_hu_1") <= 0.1679990776:
                                return "ONE"
                            else:
                                return "OE"
                        else:
                            # if c2_Nest_Distance <= 792.7405395508
                            if _get(features, "c2_Nest_Distance") <= 792.7405395508:
                                # if Actor_RB_x <= 147.5000000000
                                if _get(features, "Actor_RB_x") <= 147.5000000000:
                                    # if Nest_Dist_RL_RR <= 224.9433212280
                                    if _get(features, "Nest_Dist_RL_RR") <= 224.9433212280:
                                        return "ONE"
                                    else:
                                        # if Pups_Location_Nest_Distance <= 159.4968032837
                                        if _get(features, "Pups_Location_Nest_Distance") <= 159.4968032837:
                                            return "OE"
                                        else:
                                            return "ONE"
                                else:
                                    # if Actor_Dist_RR_To_Bbox_TR <= 19.0263700485
                                    if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 19.0263700485:
                                        # if c2_Rat_Distance <= 922.8082275391
                                        if _get(features, "c2_Rat_Distance") <= 922.8082275391:
                                            return "OE"
                                        else:
                                            return "ONE"
                                    else:
                                        # if Actor_Mask_IoU <= 0.3410654664
                                        if _get(features, "Actor_Mask_IoU") <= 0.3410654664:
                                            return "ONE"
                                        else:
                                            # if Actor_solidity <= 0.4940122068
                                            if _get(features, "Actor_solidity") <= 0.4940122068:
                                                # if Nest_Centroid_To_Bbox_BL <= 97.3335990906
                                                if _get(features, "Nest_Centroid_To_Bbox_BL") <= 97.3335990906:
                                                    return "OE"
                                                else:
                                                    return "ONE"
                                            else:
                                                # if Actor_Dist_RT_To_Bbox_TL <= 430.5000000000
                                                if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 430.5000000000:
                                                    # if Actor_To_Nest_Distance <= 462.7615356445
                                                    if _get(features, "Actor_To_Nest_Distance") <= 462.7615356445:
                                                        # if Actor_To_Nest_Dist_Change <= -56.2090873718
                                                        if _get(features, "Actor_To_Nest_Dist_Change") <= -56.2090873718:
                                                            # if Nest_RR_x <= 1067.0000000000
                                                            if _get(features, "Nest_RR_x") <= 1067.0000000000:
                                                                return "ONE"
                                                            else:
                                                                return "OE"
                                                        else:
                                                            # if Actor_Dist_RT_RB <= 516.6202087402
                                                            if _get(features, "Actor_Dist_RT_RB") <= 516.6202087402:
                                                                # if Actor_Dist_RB_To_Bbox_BL <= 17.5285711288
                                                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 17.5285711288:
                                                                    # if Actor_Dist_RT_RR <= 226.8082885742
                                                                    if _get(features, "Actor_Dist_RT_RR") <= 226.8082885742:
                                                                        return "OE"
                                                                    else:
                                                                        return "ONE"
                                                                else:
                                                                    # if foodhopperRight_Nest_Distance <= 549.4149475098
                                                                    if _get(features, "foodhopperRight_Nest_Distance") <= 549.4149475098:
                                                                        # if Nest_Dist_RR_RB <= 171.0992355347
                                                                        if _get(features, "Nest_Dist_RR_RB") <= 171.0992355347:
                                                                            return "OE"
                                                                        else:
                                                                            # if Nest_centroid_y <= 619.2419433594
                                                                            if _get(features, "Nest_centroid_y") <= 619.2419433594:
                                                                                return "OE"
                                                                            else:
                                                                                return "ONE"
                                                                    else:
                                                                        # if Actor_RR_y <= 507.5000000000
                                                                        if _get(features, "Actor_RR_y") <= 507.5000000000:
                                                                            return "ONE"
                                                                        else:
                                                                            return "OE"
                                                            else:
                                                                # if Actor_aspect_ratio <= 1.2516917586
                                                                if _get(features, "Actor_aspect_ratio") <= 1.2516917586:
                                                                    return "OE"
                                                                else:
                                                                    return "ONE"
                                                    else:
                                                        # if Nest_eccentricity <= 0.9245300591
                                                        if _get(features, "Nest_eccentricity") <= 0.9245300591:
                                                            # if Pups_Location_Rat_Distance <= 613.4839172363
                                                            if _get(features, "Pups_Location_Rat_Distance") <= 613.4839172363:
                                                                # if Actor_bbox_y <= 373.5000000000
                                                                if _get(features, "Actor_bbox_y") <= 373.5000000000:
                                                                    return "OE"
                                                                else:
                                                                    # if foodhopperRight_Rat_Distance <= 715.6850585938
                                                                    if _get(features, "foodhopperRight_Rat_Distance") <= 715.6850585938:
                                                                        return "ONE"
                                                                    else:
                                                                        return "OE"
                                                            else:
                                                                # if Nest_eccentricity <= 0.8607462049
                                                                if _get(features, "Nest_eccentricity") <= 0.8607462049:
                                                                    # if Pups_Location_Rat_Distance <= 614.3310546875
                                                                    if _get(features, "Pups_Location_Rat_Distance") <= 614.3310546875:
                                                                        return "ONE"
                                                                    else:
                                                                        return "OE"
                                                                else:
                                                                    return "OE"
                                                        else:
                                                            # if Nest_Dist_RL_To_Bbox_BR <= 221.7797470093
                                                            if _get(features, "Nest_Dist_RL_To_Bbox_BR") <= 221.7797470093:
                                                                return "ONE"
                                                            else:
                                                                return "OE"
                                                else:
                                                    # if foodhopperLeft_Rat_Distance <= 360.7525939941
                                                    if _get(features, "foodhopperLeft_Rat_Distance") <= 360.7525939941:
                                                        # if Actor_orientation <= 55.8465576172
                                                        if _get(features, "Actor_orientation") <= 55.8465576172:
                                                            # if foodhopperMid_Rat_Distance <= 341.5118560791
                                                            if _get(features, "foodhopperMid_Rat_Distance") <= 341.5118560791:
                                                                return "ONE"
                                                            else:
                                                                return "OE"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        # if Nest_Dist_RT_To_Bbox_TR <= 172.5000000000
                                                        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 172.5000000000:
                                                            # if c1_Rat_Distance <= 628.0737304688
                                                            if _get(features, "c1_Rat_Distance") <= 628.0737304688:
                                                                # if Actor_Dist_RT_To_Bbox_BR <= 347.0925903320
                                                                if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 347.0925903320:
                                                                    return "OE"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                return "OE"
                                                        else:
                                                            return "ONE"
                            else:
                                # if Actor_Dist_RB_To_Bbox_BR <= 158.5043640137
                                if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 158.5043640137:
                                    return "ONE"
                                else:
                                    return "OE"
                    else:
                        # if Actor_Centroid_To_Bbox_BR <= 296.0941925049
                        if _get(features, "Actor_Centroid_To_Bbox_BR") <= 296.0941925049:
                            # if Nest_Dist_RL_To_Bbox_TR <= 226.0056457520
                            if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 226.0056457520:
                                return "ONE"
                            else:
                                return "OE"
                        else:
                            # if Nest_Dist_RT_RR <= 188.3945159912
                            if _get(features, "Nest_Dist_RT_RR") <= 188.3945159912:
                                # if Nest_Area_Diff_Abs <= 109.5000000000
                                if _get(features, "Nest_Area_Diff_Abs") <= 109.5000000000:
                                    return "ONE"
                                else:
                                    return "OE"
                            else:
                                # if Actor_Dist_RR_To_Bbox_TR <= 489.0010223389
                                if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 489.0010223389:
                                    return "ONE"
                                else:
                                    return "OE"
            else:
                # if Nest_RR_y <= 628.5000000000
                if _get(features, "Nest_RR_y") <= 628.5000000000:
                    return "ONE"
                else:
                    # if Nest_Dist_RR_RB <= 127.0983963013
                    if _get(features, "Nest_Dist_RR_RB") <= 127.0983963013:
                        return "OE"
                    else:
                        return "ONE"
    else:
        # if Nest_hu_1 <= 0.2765796296
        if _get(features, "Nest_hu_1") <= 0.2765796296:
            # if Actor_Dist_RT_To_Bbox_TR <= 185.5000000000
            if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 185.5000000000:
                return "OE"
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
