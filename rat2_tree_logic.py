# THIS FILE IS AUTO-GENERATED: pure if/else logic for your hierarchical classifier.
# Requires only Python + numpy/pandas at runtime (sklearn not required).
# Do not edit by hand; regenerate after retraining.

import numpy as np

# --- constants learned at training time ---
ROUTER_COLS = ["c2_Rat_Distance", "Actor_Dist_RL_To_Bbox_TL", "Actor_RT_y", "Actor_area", "Actor_bbox_y", "Actor_bbox_h", "Actor_centroid_y", "Actor_RL_x", "Actor_bbox_x", "Actor_Dist_RL_RR", "Actor_Dist_RL_To_Bbox_BR", "Actor_Dist_RT_RB", "Actor_solidity", "Actor_Dist_RB_RL", "Actor_Dist_RR_To_Bbox_BL", "foodhopperRight_Rat_Distance", "Actor_Dist_RB_To_Bbox_TR", "c4_Rat_Distance", "Actor_RT_x", "Actor_Dist_RB_To_Bbox_BL", "Actor_Centroid_To_Bbox_BR", "Actor_Dist_RT_To_Bbox_BR", "Actor_Dist_RR_To_Bbox_TL", "Actor_hu_1", "Actor_extent", "Actor_aspect_ratio", "foodhopperMid_Rat_Distance", "Actor_RR_x", "Actor_hu_0", "Actor_Dist_RR_To_Bbox_TR", "Actor_Dist_RB_To_Bbox_TL", "Actor_bbox_w", "Actor_Centroid_To_Bbox_TL", "Actor_hu_3", "Actor_Dist_RT_To_Bbox_TR", "Actor_Dist_RT_To_Bbox_BL", "foodhopperLeft_Rat_Distance", "Actor_RB_y", "c3_Rat_Distance", "Actor_Dist_RT_To_Bbox_TL", "pipeMid_Rat_Distance", "Actor_centroid_x", "Actor_eccentricity", "foodhopperBottom_Rat_Distance", "pipeEnd_Rat_Distance", "c1_Rat_Distance", "Actor_hu_2", "pipeStart_Rat_Distance", "Actor_Centroid_To_Bbox_TR", "Actor_RB_x", "Actor_Dist_RB_To_Bbox_BR", "Actor_Dist_RL_RT", "Actor_Centroid_To_Bbox_BL", "Actor_Dist_RL_To_Bbox_TR", "Actor_Dist_RT_RR", "Actor_perimeter", "Actor_Dist_RL_To_Bbox_BL", "Actor_orientation", "Actor_Dist_RR_RB", "Actor_RL_y", "Actor_Dist_RR_To_Bbox_BR", "Actor_RR_y", "Actor_Mask_IoU", "Actor_Area_Diff_Abs", "Actor_hu_5", "Actor_Direction_deg", "Actor_hu_4", "Actor_hu_6"]
OENB_COLS   = ["Actor_area", "Actor_perimeter", "Actor_centroid_x", "Actor_centroid_y", "Actor_bbox_x", "Actor_bbox_y", "Actor_bbox_w", "Actor_bbox_h", "Actor_aspect_ratio", "Actor_extent", "Actor_solidity", "Actor_orientation", "Actor_eccentricity", "Actor_RL_x", "Actor_RL_y", "Actor_RR_x", "Actor_RR_y", "Actor_RT_x", "Actor_RT_y", "Actor_RB_x", "Actor_RB_y", "Actor_hu_0", "Actor_hu_1", "Actor_hu_2", "Actor_hu_3", "Actor_hu_4", "Actor_hu_5", "Actor_hu_6", "Actor_Dist_RL_RR", "Actor_Dist_RT_RB", "Actor_Dist_RL_RT", "Actor_Dist_RT_RR", "Actor_Dist_RR_RB", "Actor_Dist_RB_RL", "Actor_Centroid_To_Bbox_TL", "Actor_Centroid_To_Bbox_TR", "Actor_Centroid_To_Bbox_BR", "Actor_Centroid_To_Bbox_BL", "Actor_Dist_RL_To_Bbox_TL", "Actor_Dist_RL_To_Bbox_TR", "Actor_Dist_RL_To_Bbox_BR", "Actor_Dist_RL_To_Bbox_BL", "Actor_Dist_RR_To_Bbox_TL", "Actor_Dist_RR_To_Bbox_TR", "Actor_Dist_RR_To_Bbox_BR", "Actor_Dist_RR_To_Bbox_BL", "Actor_Dist_RT_To_Bbox_TL", "Actor_Dist_RT_To_Bbox_TR", "Actor_Dist_RT_To_Bbox_BR", "Actor_Dist_RT_To_Bbox_BL", "Actor_Dist_RB_To_Bbox_TL", "Actor_Dist_RB_To_Bbox_TR", "Actor_Dist_RB_To_Bbox_BR", "Actor_Dist_RB_To_Bbox_BL", "Actor_Area_Diff_Abs", "Actor_Mask_IoU", "Actor_Direction_deg", "c1_Rat_Distance", "c2_Rat_Distance", "c3_Rat_Distance", "c4_Rat_Distance", "pipeEnd_Rat_Distance", "pipeMid_Rat_Distance", "pipeStart_Rat_Distance", "foodhopperBottom_Rat_Distance", "foodhopperLeft_Rat_Distance", "foodhopperRight_Rat_Distance", "foodhopperMid_Rat_Distance"]
RATIO_FEATURE = "Actor_aspect_ratio"
RATIO_THRESH  = 0.8059144245000001
RATIO_FLIP    = True

def _get(d, k):
    try:
        return float(d.get(k, float("nan")))
    except Exception:
        return float("nan")


def router_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Actor_Dist_RL_To_Bbox_BR <= 256.8618316650
    if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 256.8618316650:
        # if Actor_Dist_RT_To_Bbox_BR <= 245.9898300171
        if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 245.9898300171:
            # if foodhopperMid_Rat_Distance <= 430.6146087646
            if _get(features, "foodhopperMid_Rat_Distance") <= 430.6146087646:
                # if Actor_area <= 30753.7500000000
                if _get(features, "Actor_area") <= 30753.7500000000:
                    # if pipeStart_Rat_Distance <= 421.1229400635
                    if _get(features, "pipeStart_Rat_Distance") <= 421.1229400635:
                        # if Actor_centroid_y <= 543.0687561035
                        if _get(features, "Actor_centroid_y") <= 543.0687561035:
                            return "PI_SI"
                        else:
                            # if Actor_hu_3 <= 0.0000580000
                            if _get(features, "Actor_hu_3") <= 0.0000580000:
                                # if Actor_Dist_RR_To_Bbox_TL <= 256.3615875244
                                if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 256.3615875244:
                                    # if Actor_Direction_deg <= 164.3383712769
                                    if _get(features, "Actor_Direction_deg") <= 164.3383712769:
                                        return "PI_SI"
                                    else:
                                        # if Actor_Centroid_To_Bbox_BL <= 141.7808303833
                                        if _get(features, "Actor_Centroid_To_Bbox_BL") <= 141.7808303833:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
                                else:
                                    # if Actor_area <= 24067.5000000000
                                    if _get(features, "Actor_area") <= 24067.5000000000:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                            else:
                                # if Actor_Dist_RT_To_Bbox_BL <= 158.1482849121
                                if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 158.1482849121:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                    else:
                        # if Actor_RT_y <= 413.0000000000
                        if _get(features, "Actor_RT_y") <= 413.0000000000:
                            return "PI_SI"
                        else:
                            return "OENB"
                else:
                    # if foodhopperLeft_Rat_Distance <= 634.1853332520
                    if _get(features, "foodhopperLeft_Rat_Distance") <= 634.1853332520:
                        # if Actor_Dist_RB_To_Bbox_TR <= 262.7040100098
                        if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 262.7040100098:
                            return "OENB"
                        else:
                            # if Actor_Dist_RT_To_Bbox_TL <= 105.5000000000
                            if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 105.5000000000:
                                return "OENB"
                            else:
                                return "PI_SI"
                    else:
                        # if foodhopperLeft_Rat_Distance <= 635.5974731445
                        if _get(features, "foodhopperLeft_Rat_Distance") <= 635.5974731445:
                            # if Actor_aspect_ratio <= 1.1442785859
                            if _get(features, "Actor_aspect_ratio") <= 1.1442785859:
                                return "OENB"
                            else:
                                # if Actor_centroid_x <= 965.4434204102
                                if _get(features, "Actor_centroid_x") <= 965.4434204102:
                                    # if Actor_Direction_deg <= -178.5119934082
                                    if _get(features, "Actor_Direction_deg") <= -178.5119934082:
                                        return "OENB"
                                    else:
                                        # if Actor_Centroid_To_Bbox_TR <= 154.3174743652
                                        if _get(features, "Actor_Centroid_To_Bbox_TR") <= 154.3174743652:
                                            return "OENB"
                                        else:
                                            # if Actor_Direction_deg <= 174.1806793213
                                            if _get(features, "Actor_Direction_deg") <= 174.1806793213:
                                                # if Actor_orientation <= 74.3159828186
                                                if _get(features, "Actor_orientation") <= 74.3159828186:
                                                    return "OENB"
                                                else:
                                                    # if Actor_Dist_RL_RT <= 167.6200408936
                                                    if _get(features, "Actor_Dist_RL_RT") <= 167.6200408936:
                                                        # if Actor_orientation <= 77.1761207581
                                                        if _get(features, "Actor_orientation") <= 77.1761207581:
                                                            return "OENB"
                                                        else:
                                                            return "PI_SI"
                                                    else:
                                                        return "PI_SI"
                                            else:
                                                return "OENB"
                                else:
                                    return "OENB"
                        else:
                            # if Actor_Dist_RB_RL <= 148.6648445129
                            if _get(features, "Actor_Dist_RB_RL") <= 148.6648445129:
                                return "OENB"
                            else:
                                return "PI_SI"
            else:
                # if Actor_solidity <= 0.9759745002
                if _get(features, "Actor_solidity") <= 0.9759745002:
                    # if Actor_Centroid_To_Bbox_BR <= 160.7240295410
                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 160.7240295410:
                        # if Actor_hu_0 <= 0.1662016883
                        if _get(features, "Actor_hu_0") <= 0.1662016883:
                            # if foodhopperLeft_Rat_Distance <= 639.6777954102
                            if _get(features, "foodhopperLeft_Rat_Distance") <= 639.6777954102:
                                return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            # if Actor_Centroid_To_Bbox_TR <= 170.0831298828
                            if _get(features, "Actor_Centroid_To_Bbox_TR") <= 170.0831298828:
                                # if Actor_solidity <= 0.9522595108
                                if _get(features, "Actor_solidity") <= 0.9522595108:
                                    # if Actor_Mask_IoU <= 0.9872753918
                                    if _get(features, "Actor_Mask_IoU") <= 0.9872753918:
                                        # if Actor_orientation <= 65.4027366638
                                        if _get(features, "Actor_orientation") <= 65.4027366638:
                                            # if Actor_Dist_RT_To_Bbox_BL <= 245.7772140503
                                            if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 245.7772140503:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                                        else:
                                            # if c1_Rat_Distance <= 1094.4342041016
                                            if _get(features, "c1_Rat_Distance") <= 1094.4342041016:
                                                # if foodhopperBottom_Rat_Distance <= 385.9986877441
                                                if _get(features, "foodhopperBottom_Rat_Distance") <= 385.9986877441:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                            else:
                                                return "PI_SI"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_BL <= 258.4588165283
                                        if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 258.4588165283:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                else:
                                    # if Actor_Dist_RR_RB <= 117.0679130554
                                    if _get(features, "Actor_Dist_RR_RB") <= 117.0679130554:
                                        # if Actor_hu_3 <= 0.0000175000
                                        if _get(features, "Actor_hu_3") <= 0.0000175000:
                                            return "PI_SI"
                                        else:
                                            # if foodhopperMid_Rat_Distance <= 478.3030395508
                                            if _get(features, "foodhopperMid_Rat_Distance") <= 478.3030395508:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                    else:
                                        # if Actor_Dist_RT_To_Bbox_BR <= 235.2083282471
                                        if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 235.2083282471:
                                            # if c4_Rat_Distance <= 1031.7246704102
                                            if _get(features, "c4_Rat_Distance") <= 1031.7246704102:
                                                return "PI_SI"
                                            else:
                                                # if Actor_Dist_RB_To_Bbox_TL <= 234.1327743530
                                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 234.1327743530:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                        else:
                                            # if c2_Rat_Distance <= 616.6358947754
                                            if _get(features, "c2_Rat_Distance") <= 616.6358947754:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                            else:
                                return "OENB"
                    else:
                        # if Actor_Centroid_To_Bbox_TL <= 148.9159088135
                        if _get(features, "Actor_Centroid_To_Bbox_TL") <= 148.9159088135:
                            return "PI_SI"
                        else:
                            return "OENB"
                else:
                    # if Actor_area <= 37126.5000000000
                    if _get(features, "Actor_area") <= 37126.5000000000:
                        return "OENB"
                    else:
                        return "PI_SI"
        else:
            # if Actor_Dist_RL_RT <= 195.1450119019
            if _get(features, "Actor_Dist_RL_RT") <= 195.1450119019:
                # if Actor_Dist_RR_To_Bbox_BR <= 75.5066223145
                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 75.5066223145:
                    # if Actor_Dist_RR_To_Bbox_TL <= 303.2190704346
                    if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 303.2190704346:
                        return "OENB"
                    else:
                        return "PI_SI"
                else:
                    # if c4_Rat_Distance <= 976.7137756348
                    if _get(features, "c4_Rat_Distance") <= 976.7137756348:
                        return "OENB"
                    else:
                        return "PI_SI"
            else:
                # if Actor_solidity <= 0.9766671658
                if _get(features, "Actor_solidity") <= 0.9766671658:
                    return "PI_SI"
                else:
                    return "OENB"
    else:
        # if Actor_Dist_RL_To_Bbox_BR <= 375.3411560059
        if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 375.3411560059:
            # if Actor_Dist_RT_To_Bbox_TR <= 91.5000000000
            if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 91.5000000000:
                # if Actor_Centroid_To_Bbox_TL <= 184.8683547974
                if _get(features, "Actor_Centroid_To_Bbox_TL") <= 184.8683547974:
                    # if Actor_hu_5 <= -0.0000005435
                    if _get(features, "Actor_hu_5") <= -0.0000005435:
                        # if Actor_area <= 34176.5000000000
                        if _get(features, "Actor_area") <= 34176.5000000000:
                            return "PI_SI"
                        else:
                            # if Actor_Centroid_To_Bbox_TR <= 171.2541961670
                            if _get(features, "Actor_Centroid_To_Bbox_TR") <= 171.2541961670:
                                return "OENB"
                            else:
                                return "PI_SI"
                    else:
                        # if Actor_RB_x <= 1101.5000000000
                        if _get(features, "Actor_RB_x") <= 1101.5000000000:
                            return "PI_SI"
                        else:
                            return "OENB"
                else:
                    # if Actor_bbox_y <= 461.5000000000
                    if _get(features, "Actor_bbox_y") <= 461.5000000000:
                        # if Actor_bbox_y <= 457.5000000000
                        if _get(features, "Actor_bbox_y") <= 457.5000000000:
                            # if Actor_RR_x <= 1134.5000000000
                            if _get(features, "Actor_RR_x") <= 1134.5000000000:
                                # if Actor_Dist_RR_To_Bbox_TL <= 320.4717254639
                                if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 320.4717254639:
                                    return "OENB"
                                else:
                                    # if Actor_orientation <= 76.6590232849
                                    if _get(features, "Actor_orientation") <= 76.6590232849:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                            else:
                                # if Actor_RB_x <= 1006.5000000000
                                if _get(features, "Actor_RB_x") <= 1006.5000000000:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                        else:
                            # if pipeEnd_Rat_Distance <= 579.8656311035
                            if _get(features, "pipeEnd_Rat_Distance") <= 579.8656311035:
                                # if Actor_Dist_RB_RL <= 284.5398254395
                                if _get(features, "Actor_Dist_RB_RL") <= 284.5398254395:
                                    return "OENB"
                                else:
                                    # if Actor_Dist_RR_RB <= 62.1221351624
                                    if _get(features, "Actor_Dist_RR_RB") <= 62.1221351624:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                            else:
                                # if pipeStart_Rat_Distance <= 479.8685607910
                                if _get(features, "pipeStart_Rat_Distance") <= 479.8685607910:
                                    # if Actor_solidity <= 0.8840406835
                                    if _get(features, "Actor_solidity") <= 0.8840406835:
                                        # if Actor_Mask_IoU <= 0.9820088446
                                        if _get(features, "Actor_Mask_IoU") <= 0.9820088446:
                                            # if Actor_Dist_RT_RB <= 165.1208724976
                                            if _get(features, "Actor_Dist_RT_RB") <= 165.1208724976:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                        else:
                                            # if foodhopperBottom_Rat_Distance <= 444.7916564941
                                            if _get(features, "foodhopperBottom_Rat_Distance") <= 444.7916564941:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                    else:
                                        # if Actor_perimeter <= 875.5117492676
                                        if _get(features, "Actor_perimeter") <= 875.5117492676:
                                            # if Actor_hu_5 <= 0.0000813500
                                            if _get(features, "Actor_hu_5") <= 0.0000813500:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                        else:
                                            # if Actor_orientation <= 79.8588142395
                                            if _get(features, "Actor_orientation") <= 79.8588142395:
                                                return "OENB"
                                            else:
                                                # if Actor_Dist_RL_RT <= 256.2877044678
                                                if _get(features, "Actor_Dist_RL_RT") <= 256.2877044678:
                                                    # if Actor_solidity <= 0.8849919140
                                                    if _get(features, "Actor_solidity") <= 0.8849919140:
                                                        # if Actor_centroid_x <= 1013.1234130859
                                                        if _get(features, "Actor_centroid_x") <= 1013.1234130859:
                                                            return "PI_SI"
                                                        else:
                                                            return "OENB"
                                                    else:
                                                        return "PI_SI"
                                                else:
                                                    # if Actor_Direction_deg <= -76.2232108116
                                                    if _get(features, "Actor_Direction_deg") <= -76.2232108116:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                else:
                                    return "OENB"
                    else:
                        # if Actor_Dist_RT_To_Bbox_BL <= 269.3009338379
                        if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 269.3009338379:
                            # if pipeEnd_Rat_Distance <= 584.6006164551
                            if _get(features, "pipeEnd_Rat_Distance") <= 584.6006164551:
                                return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            # if Actor_Dist_RL_To_Bbox_TR <= 325.5595245361
                            if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 325.5595245361:
                                # if Actor_solidity <= 0.8792793751
                                if _get(features, "Actor_solidity") <= 0.8792793751:
                                    # if Actor_orientation <= 84.3359603882
                                    if _get(features, "Actor_orientation") <= 84.3359603882:
                                        # if Actor_aspect_ratio <= 1.8742331266
                                        if _get(features, "Actor_aspect_ratio") <= 1.8742331266:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    return "OENB"
                            else:
                                return "PI_SI"
            else:
                # if Actor_hu_3 <= 0.0000113500
                if _get(features, "Actor_hu_3") <= 0.0000113500:
                    # if Actor_bbox_y <= 396.5000000000
                    if _get(features, "Actor_bbox_y") <= 396.5000000000:
                        # if Actor_Dist_RL_To_Bbox_TL <= 209.5000000000
                        if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 209.5000000000:
                            # if Actor_centroid_y <= 515.9358825684
                            if _get(features, "Actor_centroid_y") <= 515.9358825684:
                                # if Actor_Dist_RL_To_Bbox_BR <= 265.0443267822
                                if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 265.0443267822:
                                    # if Actor_Dist_RR_To_Bbox_BL <= 276.9501037598
                                    if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 276.9501037598:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    return "PI_SI"
                            else:
                                # if Actor_perimeter <= 885.3143310547
                                if _get(features, "Actor_perimeter") <= 885.3143310547:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                        else:
                            # if Actor_solidity <= 0.9522350132
                            if _get(features, "Actor_solidity") <= 0.9522350132:
                                # if Actor_Area_Diff_Abs <= 21.7500000000
                                if _get(features, "Actor_Area_Diff_Abs") <= 21.7500000000:
                                    return "OENB"
                                else:
                                    # if Actor_Direction_deg <= -159.8351135254
                                    if _get(features, "Actor_Direction_deg") <= -159.8351135254:
                                        # if foodhopperMid_Rat_Distance <= 491.9079132080
                                        if _get(features, "foodhopperMid_Rat_Distance") <= 491.9079132080:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        return "PI_SI"
                            else:
                                # if Actor_Centroid_To_Bbox_TL <= 180.1700973511
                                if _get(features, "Actor_Centroid_To_Bbox_TL") <= 180.1700973511:
                                    # if Actor_Direction_deg <= -130.8523139954
                                    if _get(features, "Actor_Direction_deg") <= -130.8523139954:
                                        # if foodhopperBottom_Rat_Distance <= 466.4387817383
                                        if _get(features, "foodhopperBottom_Rat_Distance") <= 466.4387817383:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    return "PI_SI"
                    else:
                        # if Actor_hu_0 <= 0.1678903326
                        if _get(features, "Actor_hu_0") <= 0.1678903326:
                            # if Actor_RT_y <= 398.5000000000
                            if _get(features, "Actor_RT_y") <= 398.5000000000:
                                # if c1_Rat_Distance <= 1165.3062133789
                                if _get(features, "c1_Rat_Distance") <= 1165.3062133789:
                                    return "PI_SI"
                                else:
                                    # if Actor_centroid_y <= 518.4056701660
                                    if _get(features, "Actor_centroid_y") <= 518.4056701660:
                                        # if Actor_aspect_ratio <= 1.1132902503
                                        if _get(features, "Actor_aspect_ratio") <= 1.1132902503:
                                            # if Actor_area <= 43878.7500000000
                                            if _get(features, "Actor_area") <= 43878.7500000000:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                                        else:
                                            # if Actor_eccentricity <= 0.4701194316
                                            if _get(features, "Actor_eccentricity") <= 0.4701194316:
                                                # if c2_Rat_Distance <= 563.6495971680
                                                if _get(features, "c2_Rat_Distance") <= 563.6495971680:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                            else:
                                                # if Actor_Area_Diff_Abs <= 560.5000000000
                                                if _get(features, "Actor_Area_Diff_Abs") <= 560.5000000000:
                                                    return "OENB"
                                                else:
                                                    # if pipeEnd_Rat_Distance <= 607.9421386719
                                                    if _get(features, "pipeEnd_Rat_Distance") <= 607.9421386719:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                    else:
                                        return "PI_SI"
                            else:
                                # if foodhopperLeft_Rat_Distance <= 694.2751770020
                                if _get(features, "foodhopperLeft_Rat_Distance") <= 694.2751770020:
                                    return "OENB"
                                else:
                                    # if Actor_aspect_ratio <= 1.0948086381
                                    if _get(features, "Actor_aspect_ratio") <= 1.0948086381:
                                        # if c1_Rat_Distance <= 1164.2318725586
                                        if _get(features, "c1_Rat_Distance") <= 1164.2318725586:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
                                    else:
                                        return "PI_SI"
                        else:
                            # if Actor_centroid_y <= 518.2752685547
                            if _get(features, "Actor_centroid_y") <= 518.2752685547:
                                # if foodhopperRight_Rat_Distance <= 397.2380065918
                                if _get(features, "foodhopperRight_Rat_Distance") <= 397.2380065918:
                                    # if Actor_aspect_ratio <= 1.1233695745
                                    if _get(features, "Actor_aspect_ratio") <= 1.1233695745:
                                        # if Actor_RR_y <= 548.5000000000
                                        if _get(features, "Actor_RR_y") <= 548.5000000000:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        # if Actor_solidity <= 0.9592890739
                                        if _get(features, "Actor_solidity") <= 0.9592890739:
                                            # if Actor_Area_Diff_Abs <= 19.7500000000
                                            if _get(features, "Actor_Area_Diff_Abs") <= 19.7500000000:
                                                return "OENB"
                                            else:
                                                # if Actor_RL_x <= 920.5000000000
                                                if _get(features, "Actor_RL_x") <= 920.5000000000:
                                                    return "PI_SI"
                                                else:
                                                    # if Actor_RB_x <= 1126.0000000000
                                                    if _get(features, "Actor_RB_x") <= 1126.0000000000:
                                                        return "PI_SI"
                                                    else:
                                                        return "OENB"
                                        else:
                                            return "OENB"
                                else:
                                    # if Actor_RT_y <= 432.5000000000
                                    if _get(features, "Actor_RT_y") <= 432.5000000000:
                                        # if Actor_Dist_RT_To_Bbox_BL <= 269.5367584229
                                        if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 269.5367584229:
                                            # if Actor_centroid_y <= 513.0201416016
                                            if _get(features, "Actor_centroid_y") <= 513.0201416016:
                                                return "PI_SI"
                                            else:
                                                return "OENB"
                                        else:
                                            return "PI_SI"
                                    else:
                                        return "PI_SI"
                            else:
                                # if Actor_Dist_RB_To_Bbox_BL <= 65.5076866150
                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 65.5076866150:
                                    return "OENB"
                                else:
                                    # if Actor_Centroid_To_Bbox_BR <= 147.2766189575
                                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 147.2766189575:
                                        # if Actor_Dist_RT_To_Bbox_BR <= 248.0828628540
                                        if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 248.0828628540:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        return "PI_SI"
                else:
                    # if Actor_centroid_y <= 546.0706176758
                    if _get(features, "Actor_centroid_y") <= 546.0706176758:
                        # if Actor_centroid_y <= 492.9863281250
                        if _get(features, "Actor_centroid_y") <= 492.9863281250:
                            # if Actor_bbox_x <= 823.0000000000
                            if _get(features, "Actor_bbox_x") <= 823.0000000000:
                                # if Actor_Dist_RR_To_Bbox_BR <= 39.5126571655
                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 39.5126571655:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                            else:
                                return "PI_SI"
                        else:
                            # if Actor_hu_3 <= 0.0000138500
                            if _get(features, "Actor_hu_3") <= 0.0000138500:
                                # if Actor_RB_x <= 926.5000000000
                                if _get(features, "Actor_RB_x") <= 926.5000000000:
                                    # if Actor_RT_y <= 432.5000000000
                                    if _get(features, "Actor_RT_y") <= 432.5000000000:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
                                else:
                                    # if Actor_Dist_RL_To_Bbox_BL <= 30.5000000000
                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 30.5000000000:
                                        # if Actor_centroid_x <= 1046.5726318359
                                        if _get(features, "Actor_centroid_x") <= 1046.5726318359:
                                            return "PI_SI"
                                        else:
                                            return "OENB"
                                    else:
                                        # if Actor_Centroid_To_Bbox_TR <= 172.4550781250
                                        if _get(features, "Actor_Centroid_To_Bbox_TR") <= 172.4550781250:
                                            # if Actor_area <= 44006.0000000000
                                            if _get(features, "Actor_area") <= 44006.0000000000:
                                                # if c2_Rat_Distance <= 554.4524536133
                                                if _get(features, "c2_Rat_Distance") <= 554.4524536133:
                                                    # if Actor_Dist_RT_To_Bbox_TL <= 116.5000000000
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 116.5000000000:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                                                else:
                                                    return "PI_SI"
                                            else:
                                                # if Actor_Dist_RT_To_Bbox_BL <= 266.4234619141
                                                if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 266.4234619141:
                                                    return "OENB"
                                                else:
                                                    return "PI_SI"
                                        else:
                                            return "PI_SI"
                            else:
                                # if Actor_Dist_RL_RR <= 248.1310119629
                                if _get(features, "Actor_Dist_RL_RR") <= 248.1310119629:
                                    # if Actor_area <= 36288.2500000000
                                    if _get(features, "Actor_area") <= 36288.2500000000:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    # if Actor_RR_y <= 486.5000000000
                                    if _get(features, "Actor_RR_y") <= 486.5000000000:
                                        # if Actor_hu_0 <= 0.1762692556
                                        if _get(features, "Actor_hu_0") <= 0.1762692556:
                                            return "OENB"
                                        else:
                                            return "PI_SI"
                                    else:
                                        # if Actor_Direction_deg <= -178.6414718628
                                        if _get(features, "Actor_Direction_deg") <= -178.6414718628:
                                            # if c4_Rat_Distance <= 927.7171020508
                                            if _get(features, "c4_Rat_Distance") <= 927.7171020508:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                                        else:
                                            # if Actor_orientation <= 105.4674682617
                                            if _get(features, "Actor_orientation") <= 105.4674682617:
                                                # if Actor_bbox_x <= 762.5000000000
                                                if _get(features, "Actor_bbox_x") <= 762.5000000000:
                                                    # if Actor_hu_3 <= 0.0007105220
                                                    if _get(features, "Actor_hu_3") <= 0.0007105220:
                                                        # if Actor_Centroid_To_Bbox_TL <= 167.9242706299
                                                        if _get(features, "Actor_Centroid_To_Bbox_TL") <= 167.9242706299:
                                                            return "OENB"
                                                        else:
                                                            return "PI_SI"
                                                    else:
                                                        return "OENB"
                                                else:
                                                    # if Actor_Dist_RR_To_Bbox_BL <= 251.4188613892
                                                    if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 251.4188613892:
                                                        # if foodhopperMid_Rat_Distance <= 458.7041320801
                                                        if _get(features, "foodhopperMid_Rat_Distance") <= 458.7041320801:
                                                            return "OENB"
                                                        else:
                                                            return "PI_SI"
                                                    else:
                                                        return "PI_SI"
                                            else:
                                                # if Actor_orientation <= 105.4724349976
                                                if _get(features, "Actor_orientation") <= 105.4724349976:
                                                    return "OENB"
                                                else:
                                                    # if Actor_Mask_IoU <= 0.9888069332
                                                    if _get(features, "Actor_Mask_IoU") <= 0.9888069332:
                                                        # if Actor_Dist_RR_To_Bbox_TR <= 147.5033874512
                                                        if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 147.5033874512:
                                                            # if Actor_hu_5 <= -0.0000006920
                                                            if _get(features, "Actor_hu_5") <= -0.0000006920:
                                                                return "PI_SI"
                                                            else:
                                                                return "OENB"
                                                        else:
                                                            return "PI_SI"
                                                    else:
                                                        # if Actor_Centroid_To_Bbox_BL <= 175.7093429565
                                                        if _get(features, "Actor_Centroid_To_Bbox_BL") <= 175.7093429565:
                                                            return "PI_SI"
                                                        else:
                                                            # if Actor_orientation <= 106.6519737244
                                                            if _get(features, "Actor_orientation") <= 106.6519737244:
                                                                return "OENB"
                                                            else:
                                                                return "PI_SI"
                    else:
                        # if Actor_Dist_RB_RL <= 273.5379180908
                        if _get(features, "Actor_Dist_RB_RL") <= 273.5379180908:
                            # if Actor_Dist_RB_To_Bbox_TR <= 230.6720886230
                            if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 230.6720886230:
                                # if foodhopperRight_Rat_Distance <= 424.9965362549
                                if _get(features, "foodhopperRight_Rat_Distance") <= 424.9965362549:
                                    # if Actor_extent <= 0.6517377198
                                    if _get(features, "Actor_extent") <= 0.6517377198:
                                        return "PI_SI"
                                    else:
                                        return "OENB"
                                else:
                                    # if Actor_Dist_RL_RR <= 353.6311645508
                                    if _get(features, "Actor_Dist_RL_RR") <= 353.6311645508:
                                        # if Actor_Dist_RT_To_Bbox_TL <= 221.5000000000
                                        if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 221.5000000000:
                                            # if foodhopperRight_Rat_Distance <= 425.5207519531
                                            if _get(features, "foodhopperRight_Rat_Distance") <= 425.5207519531:
                                                # if foodhopperRight_Rat_Distance <= 425.4728088379
                                                if _get(features, "foodhopperRight_Rat_Distance") <= 425.4728088379:
                                                    return "PI_SI"
                                                else:
                                                    return "OENB"
                                            else:
                                                # if Actor_Centroid_To_Bbox_BR <= 172.4060745239
                                                if _get(features, "Actor_Centroid_To_Bbox_BR") <= 172.4060745239:
                                                    return "PI_SI"
                                                else:
                                                    # if Actor_Centroid_To_Bbox_BR <= 172.5452651978
                                                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 172.5452651978:
                                                        return "OENB"
                                                    else:
                                                        return "PI_SI"
                                        else:
                                            # if Actor_Dist_RL_RT <= 257.2755355835
                                            if _get(features, "Actor_Dist_RL_RT") <= 257.2755355835:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                                    else:
                                        # if Actor_Direction_deg <= -6.5876972675
                                        if _get(features, "Actor_Direction_deg") <= -6.5876972675:
                                            # if Actor_extent <= 0.6434111893
                                            if _get(features, "Actor_extent") <= 0.6434111893:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                                        else:
                                            # if Actor_Dist_RB_To_Bbox_TL <= 269.5382843018
                                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 269.5382843018:
                                                return "OENB"
                                            else:
                                                return "PI_SI"
                            else:
                                # if Actor_hu_1 <= 0.0095771742
                                if _get(features, "Actor_hu_1") <= 0.0095771742:
                                    return "PI_SI"
                                else:
                                    return "OENB"
                        else:
                            # if Actor_centroid_y <= 547.7150268555
                            if _get(features, "Actor_centroid_y") <= 547.7150268555:
                                # if foodhopperMid_Rat_Distance <= 487.8930206299
                                if _get(features, "foodhopperMid_Rat_Distance") <= 487.8930206299:
                                    return "OENB"
                                else:
                                    return "PI_SI"
                            else:
                                # if Actor_extent <= 0.6868166625
                                if _get(features, "Actor_extent") <= 0.6868166625:
                                    return "PI_SI"
                                else:
                                    # if Actor_perimeter <= 971.0178527832
                                    if _get(features, "Actor_perimeter") <= 971.0178527832:
                                        return "OENB"
                                    else:
                                        return "PI_SI"
        else:
            # if foodhopperLeft_Rat_Distance <= 720.0023803711
            if _get(features, "foodhopperLeft_Rat_Distance") <= 720.0023803711:
                # if Actor_RL_y <= 583.0000000000
                if _get(features, "Actor_RL_y") <= 583.0000000000:
                    return "PI_SI"
                else:
                    # if foodhopperMid_Rat_Distance <= 511.5294342041
                    if _get(features, "foodhopperMid_Rat_Distance") <= 511.5294342041:
                        return "OENB"
                    else:
                        return "PI_SI"
            else:
                # if Actor_Dist_RR_To_Bbox_BR <= 62.5080051422
                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 62.5080051422:
                    return "OENB"
                else:
                    return "PI_SI"



def oenb_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Actor_RT_x <= 967.5000000000
    if _get(features, "Actor_RT_x") <= 967.5000000000:
        # if Actor_extent <= 0.6719707251
        if _get(features, "Actor_extent") <= 0.6719707251:
            # if Actor_eccentricity <= 0.6276718080
            if _get(features, "Actor_eccentricity") <= 0.6276718080:
                return "NB"
            else:
                return "ONE"
        else:
            # if c2_Rat_Distance <= 612.8623352051
            if _get(features, "c2_Rat_Distance") <= 612.8623352051:
                # if Actor_Dist_RT_To_Bbox_TR <= 147.5000000000
                if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 147.5000000000:
                    # if pipeMid_Rat_Distance <= 458.6481475830
                    if _get(features, "pipeMid_Rat_Distance") <= 458.6481475830:
                        # if Actor_aspect_ratio <= 1.1924062967
                        if _get(features, "Actor_aspect_ratio") <= 1.1924062967:
                            # if pipeStart_Rat_Distance <= 413.1551666260
                            if _get(features, "pipeStart_Rat_Distance") <= 413.1551666260:
                                return "OE"
                            else:
                                return "ONE"
                        else:
                            return "ONE"
                    else:
                        # if Actor_Dist_RB_To_Bbox_BL <= 60.5082645416
                        if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 60.5082645416:
                            # if Actor_RR_x <= 1077.0000000000
                            if _get(features, "Actor_RR_x") <= 1077.0000000000:
                                return "OE"
                            else:
                                return "NB"
                        else:
                            # if Actor_RL_y <= 531.5000000000
                            if _get(features, "Actor_RL_y") <= 531.5000000000:
                                # if Actor_extent <= 0.7259769440
                                if _get(features, "Actor_extent") <= 0.7259769440:
                                    return "ONE"
                                else:
                                    return "OE"
                            else:
                                # if Actor_Dist_RT_To_Bbox_TR <= 146.5000000000
                                if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 146.5000000000:
                                    return "OE"
                                else:
                                    # if Actor_Direction_deg <= -81.0993080139
                                    if _get(features, "Actor_Direction_deg") <= -81.0993080139:
                                        return "ONE"
                                    else:
                                        return "OE"
                else:
                    # if Actor_solidity <= 0.9214241207
                    if _get(features, "Actor_solidity") <= 0.9214241207:
                        # if Actor_Direction_deg <= 170.1818542480
                        if _get(features, "Actor_Direction_deg") <= 170.1818542480:
                            return "OE"
                        else:
                            # if Actor_Dist_RL_To_Bbox_TL <= 147.0000000000
                            if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 147.0000000000:
                                return "OE"
                            else:
                                return "ONE"
                    else:
                        # if Actor_Dist_RR_RB <= 159.0235748291
                        if _get(features, "Actor_Dist_RR_RB") <= 159.0235748291:
                            # if Actor_centroid_y <= 520.2062072754
                            if _get(features, "Actor_centroid_y") <= 520.2062072754:
                                # if Actor_Dist_RB_RL <= 118.4331932068
                                if _get(features, "Actor_Dist_RB_RL") <= 118.4331932068:
                                    return "OE"
                                else:
                                    return "ONE"
                            else:
                                return "ONE"
                        else:
                            # if Actor_Centroid_To_Bbox_BL <= 154.6142425537
                            if _get(features, "Actor_Centroid_To_Bbox_BL") <= 154.6142425537:
                                return "OE"
                            else:
                                # if Actor_RT_x <= 950.5000000000
                                if _get(features, "Actor_RT_x") <= 950.5000000000:
                                    # if Actor_Direction_deg <= 64.5387382507
                                    if _get(features, "Actor_Direction_deg") <= 64.5387382507:
                                        return "ONE"
                                    else:
                                        return "OE"
                                else:
                                    return "OE"
            else:
                return "ONE"
    else:
        # if Actor_eccentricity <= 0.6430219114
        if _get(features, "Actor_eccentricity") <= 0.6430219114:
            # if Actor_RB_y <= 628.5000000000
            if _get(features, "Actor_RB_y") <= 628.5000000000:
                return "NB"
            else:
                return "ONE"
        else:
            # if Actor_hu_0 <= 0.2292189077
            if _get(features, "Actor_hu_0") <= 0.2292189077:
                # if Actor_solidity <= 0.9417616725
                if _get(features, "Actor_solidity") <= 0.9417616725:
                    # if Actor_Dist_RT_To_Bbox_TL <= 246.0000000000
                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 246.0000000000:
                        # if Actor_RL_y <= 592.5000000000
                        if _get(features, "Actor_RL_y") <= 592.5000000000:
                            # if Actor_RR_x <= 1085.5000000000
                            if _get(features, "Actor_RR_x") <= 1085.5000000000:
                                return "NB"
                            else:
                                # if Actor_RT_x <= 1060.0000000000
                                if _get(features, "Actor_RT_x") <= 1060.0000000000:
                                    # if Actor_bbox_h <= 161.5000000000
                                    if _get(features, "Actor_bbox_h") <= 161.5000000000:
                                        # if Actor_Dist_RL_To_Bbox_BR <= 302.0584411621
                                        if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 302.0584411621:
                                            return "NB"
                                        else:
                                            return "ONE"
                                    else:
                                        return "ONE"
                                else:
                                    # if Actor_Mask_IoU <= 0.9287956059
                                    if _get(features, "Actor_Mask_IoU") <= 0.9287956059:
                                        return "NB"
                                    else:
                                        return "ONE"
                        else:
                            return "NB"
                    else:
                        return "NB"
                else:
                    # if Actor_Dist_RB_To_Bbox_TR <= 219.4853820801
                    if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 219.4853820801:
                        return "NB"
                    else:
                        return "ONE"
            else:
                # if Actor_aspect_ratio <= 2.3252985477
                if _get(features, "Actor_aspect_ratio") <= 2.3252985477:
                    # if Actor_RT_x <= 1047.5000000000
                    if _get(features, "Actor_RT_x") <= 1047.5000000000:
                        return "ONE"
                    else:
                        # if Actor_Dist_RT_To_Bbox_BR <= 182.5335464478
                        if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 182.5335464478:
                            # if Actor_Dist_RB_To_Bbox_TL <= 323.1807098389
                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 323.1807098389:
                                return "ONE"
                            else:
                                return "NB"
                        else:
                            # if Actor_Centroid_To_Bbox_TR <= 193.3194808960
                            if _get(features, "Actor_Centroid_To_Bbox_TR") <= 193.3194808960:
                                # if c2_Rat_Distance <= 593.7979736328
                                if _get(features, "c2_Rat_Distance") <= 593.7979736328:
                                    # if Actor_Direction_deg <= -8.7449970245
                                    if _get(features, "Actor_Direction_deg") <= -8.7449970245:
                                        return "ONE"
                                    else:
                                        return "NB"
                                else:
                                    # if Actor_Centroid_To_Bbox_TR <= 153.5008010864
                                    if _get(features, "Actor_Centroid_To_Bbox_TR") <= 153.5008010864:
                                        # if Actor_Centroid_To_Bbox_TL <= 202.9944839478
                                        if _get(features, "Actor_Centroid_To_Bbox_TL") <= 202.9944839478:
                                            return "ONE"
                                        else:
                                            return "NB"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_TR <= 156.5031967163
                                        if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 156.5031967163:
                                            # if Actor_Dist_RT_RB <= 162.5622863770
                                            if _get(features, "Actor_Dist_RT_RB") <= 162.5622863770:
                                                # if Actor_Dist_RT_RB <= 162.2975006104
                                                if _get(features, "Actor_Dist_RT_RB") <= 162.2975006104:
                                                    return "NB"
                                                else:
                                                    return "ONE"
                                            else:
                                                # if Actor_Dist_RL_To_Bbox_TL <= 130.5000000000
                                                if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 130.5000000000:
                                                    return "NB"
                                                else:
                                                    # if Actor_Dist_RL_To_Bbox_TR <= 343.0023040771
                                                    if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 343.0023040771:
                                                        return "NB"
                                                    else:
                                                        return "ONE"
                                        else:
                                            return "ONE"
                            else:
                                # if Actor_eccentricity <= 0.9020607769
                                if _get(features, "Actor_eccentricity") <= 0.9020607769:
                                    return "NB"
                                else:
                                    return "ONE"
                else:
                    # if Actor_Dist_RT_To_Bbox_TL <= 211.5000000000
                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 211.5000000000:
                        return "NB"
                    else:
                        # if Actor_Area_Diff_Abs <= 44.0000000000
                        if _get(features, "Actor_Area_Diff_Abs") <= 44.0000000000:
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
