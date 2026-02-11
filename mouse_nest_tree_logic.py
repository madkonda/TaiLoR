# AUTO-GENERATED: Pure if/else logic for hierarchical mouse classifier (auto schema).

def _safe_float(v, default=float("nan")):
    try:
        return float(v)
    except Exception:
        return default

def _get(d, k):
    return _safe_float(d.get(k, float("nan")))

# --- Router tree ---
def router_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Actor_RL_x <= 495.5000000000
    if _get(features, "Actor_RL_x") <= 495.5000000000:
        # if foodhopperMid_Nest_Distance <= 447.4561614990
        if _get(features, "foodhopperMid_Nest_Distance") <= 447.4561614990:
            # if Nest_Mask_IoU <= 0.9793692231
            if _get(features, "Nest_Mask_IoU") <= 0.9793692231:
                # if Nest_RT_y <= 605.5000000000
                if _get(features, "Nest_RT_y") <= 605.5000000000:
                    # if Nest_RB_x <= 757.0000000000
                    if _get(features, "Nest_RB_x") <= 757.0000000000:
                        # if Actor_Dist_RR_RB <= 66.5657463074
                        if _get(features, "Actor_Dist_RR_RB") <= 66.5657463074:
                            # if Nest_Dist_RB_To_Bbox_TL <= 398.4564666748
                            if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 398.4564666748:
                                # if Actor_solidity <= 0.8223262131
                                if _get(features, "Actor_solidity") <= 0.8223262131:
                                    # if Nest_RR_x <= 1004.5000000000
                                    if _get(features, "Nest_RR_x") <= 1004.5000000000:
                                        # if Nest_RR_x <= 978.0000000000
                                        if _get(features, "Nest_RR_x") <= 978.0000000000:
                                            return "OTHER4"
                                        else:
                                            # if Nest_Centroid_To_Bbox_TR <= 419.9801483154
                                            if _get(features, "Nest_Centroid_To_Bbox_TR") <= 419.9801483154:
                                                # if Actor_Mask_IoU <= 0.3570931256
                                                if _get(features, "Actor_Mask_IoU") <= 0.3570931256:
                                                    return "OTHER4"
                                                else:
                                                    return "IPI_ISI"
                                            else:
                                                # if Nest_hu_3 <= 0.0000588500
                                                if _get(features, "Nest_hu_3") <= 0.0000588500:
                                                    return "OTHER4"
                                                else:
                                                    return "IPI_ISI"
                                    else:
                                        # if Nest_Dist_RR_To_Bbox_BR <= 179.0027923584
                                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 179.0027923584:
                                            return "OTHER4"
                                        else:
                                            return "IPI_ISI"
                                else:
                                    # if Actor_Dist_RT_To_Bbox_TR <= 115.5000000000
                                    if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 115.5000000000:
                                        # if Actor_RL_y <= 875.0000000000
                                        if _get(features, "Actor_RL_y") <= 875.0000000000:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                    else:
                                        return "OTHER4"
                            else:
                                # if Nest_Dist_RR_To_Bbox_BR <= 89.5055847168
                                if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 89.5055847168:
                                    # if c2_Mouse_Distance <= 457.3477783203
                                    if _get(features, "c2_Mouse_Distance") <= 457.3477783203:
                                        return "OTHER4"
                                    else:
                                        # if Nest_hu_5 <= 0.0000058000
                                        if _get(features, "Nest_hu_5") <= 0.0000058000:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                else:
                                    # if Actor_Direction_deg <= -179.6468887329
                                    if _get(features, "Actor_Direction_deg") <= -179.6468887329:
                                        return "IPI_ISI"
                                    else:
                                        # if Actor_Mask_IoU <= 0.9175929427
                                        if _get(features, "Actor_Mask_IoU") <= 0.9175929427:
                                            # if Actor_hu_5 <= -0.0010417080
                                            if _get(features, "Actor_hu_5") <= -0.0010417080:
                                                # if Nest_RL_x <= 294.5000000000
                                                if _get(features, "Nest_RL_x") <= 294.5000000000:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                            else:
                                                # if Nest_Dist_RT_RB <= 385.9133300781
                                                if _get(features, "Nest_Dist_RT_RB") <= 385.9133300781:
                                                    # if Nest_RL_y <= 729.0000000000
                                                    if _get(features, "Nest_RL_y") <= 729.0000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    return "OTHER4"
                                        else:
                                            # if Actor_hu_5 <= 0.0000003040
                                            if _get(features, "Actor_hu_5") <= 0.0000003040:
                                                return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                        else:
                            # if Actor_bbox_h <= 43.5000000000
                            if _get(features, "Actor_bbox_h") <= 43.5000000000:
                                # if Actor_Area_Diff_Abs <= 136.5000000000
                                if _get(features, "Actor_Area_Diff_Abs") <= 136.5000000000:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                # if Nest_Dist_RR_To_Bbox_BR <= 29.0177631378
                                if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 29.0177631378:
                                    return "IPI_ISI"
                                else:
                                    # if Actor_hu_4 <= -0.0002350935
                                    if _get(features, "Actor_hu_4") <= -0.0002350935:
                                        return "IPI_ISI"
                                    else:
                                        # if Actor_RR_x <= 475.5000000000
                                        if _get(features, "Actor_RR_x") <= 475.5000000000:
                                            # if foodhopperLeft_Nest_Distance <= 123.4954071045
                                            if _get(features, "foodhopperLeft_Nest_Distance") <= 123.4954071045:
                                                return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                        else:
                                            # if Actor_solidity <= 0.4270768613
                                            if _get(features, "Actor_solidity") <= 0.4270768613:
                                                # if Nest_RB_x <= 574.0000000000
                                                if _get(features, "Nest_RB_x") <= 574.0000000000:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                            else:
                                                # if Actor_Dist_RB_To_Bbox_BR <= 24.5204086304
                                                if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 24.5204086304:
                                                    # if Nest_Dist_RL_To_Bbox_TR <= 587.2813720703
                                                    if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 587.2813720703:
                                                        return "OTHER4"
                                                    else:
                                                        return "IPI_ISI"
                                                else:
                                                    # if Actor_aspect_ratio <= 0.7562084794
                                                    if _get(features, "Actor_aspect_ratio") <= 0.7562084794:
                                                        # if foodhopperMid_Mouse_Distance <= 602.0588989258
                                                        if _get(features, "foodhopperMid_Mouse_Distance") <= 602.0588989258:
                                                            return "OTHER4"
                                                        else:
                                                            # if Actor_aspect_ratio <= 0.6921187043
                                                            if _get(features, "Actor_aspect_ratio") <= 0.6921187043:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                    else:
                        # if Nest_Dist_RR_To_Bbox_BR <= 170.5029373169
                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 170.5029373169:
                            # if Nest_Dist_RR_RB <= 363.7523651123
                            if _get(features, "Nest_Dist_RR_RB") <= 363.7523651123:
                                # if Nest_aspect_ratio <= 2.4353040457
                                if _get(features, "Nest_aspect_ratio") <= 2.4353040457:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                return "IPI_ISI"
                        else:
                            # if c4_Nest_Distance <= 511.5601654053
                            if _get(features, "c4_Nest_Distance") <= 511.5601654053:
                                # if Actor_Dist_RL_To_Bbox_BR <= 214.3133392334
                                if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 214.3133392334:
                                    return "OTHER4"
                                else:
                                    # if Actor_bbox_y <= 552.5000000000
                                    if _get(features, "Actor_bbox_y") <= 552.5000000000:
                                        return "OTHER4"
                                    else:
                                        # if Actor_RB_x <= 354.0000000000
                                        if _get(features, "Actor_RB_x") <= 354.0000000000:
                                            # if Actor_Dist_RR_To_Bbox_BR <= 103.5049018860
                                            if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 103.5049018860:
                                                return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                        else:
                                            return "IPI_ISI"
                            else:
                                return "OTHER4"
                else:
                    # if Nest_RT_y <= 645.5000000000
                    if _get(features, "Nest_RT_y") <= 645.5000000000:
                        # if Nest_Dist_RR_To_Bbox_BR <= 199.5025100708
                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 199.5025100708:
                            # if Actor_Mask_IoU <= 0.8768939078
                            if _get(features, "Actor_Mask_IoU") <= 0.8768939078:
                                # if Nest_Mask_IoU <= 0.9280031025
                                if _get(features, "Nest_Mask_IoU") <= 0.9280031025:
                                    # if Actor_RT_x <= 544.5000000000
                                    if _get(features, "Actor_RT_x") <= 544.5000000000:
                                        # if Nest_RB_y <= 898.5000000000
                                        if _get(features, "Nest_RB_y") <= 898.5000000000:
                                            return "OTHER4"
                                        else:
                                            # if Nest_Dist_RT_To_Bbox_BR <= 387.0977020264
                                            if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 387.0977020264:
                                                # if Nest_Dist_RB_To_Bbox_TR <= 278.4968566895
                                                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 278.4968566895:
                                                    # if Actor_Dist_RL_To_Bbox_TL <= 61.0000000000
                                                    if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 61.0000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    # if Actor_Mask_IoU <= 0.0517988876
                                                    if _get(features, "Actor_Mask_IoU") <= 0.0517988876:
                                                        return "OTHER4"
                                                    else:
                                                        return "IPI_ISI"
                                            else:
                                                # if Actor_Dist_RL_To_Bbox_BR <= 315.1895446777
                                                if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 315.1895446777:
                                                    # if Actor_Area_Diff_Abs <= 14205.0000000000
                                                    if _get(features, "Actor_Area_Diff_Abs") <= 14205.0000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    # if Actor_perimeter <= 1356.2833862305
                                                    if _get(features, "Actor_perimeter") <= 1356.2833862305:
                                                        return "OTHER4"
                                                    else:
                                                        return "IPI_ISI"
                                    else:
                                        # if Nest_RB_y <= 956.5000000000
                                        if _get(features, "Nest_RB_y") <= 956.5000000000:
                                            # if Nest_perimeter <= 2391.0621337891
                                            if _get(features, "Nest_perimeter") <= 2391.0621337891:
                                                # if Nest_Dist_RR_To_Bbox_BR <= 23.0217695236
                                                if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 23.0217695236:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                        else:
                                            # if Actor_bbox_h <= 198.5000000000
                                            if _get(features, "Actor_bbox_h") <= 198.5000000000:
                                                return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                else:
                                    # if Nest_hu_5 <= 0.0000821000
                                    if _get(features, "Nest_hu_5") <= 0.0000821000:
                                        # if Nest_Dist_RR_To_Bbox_BL <= 808.5143432617
                                        if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 808.5143432617:
                                            # if Nest_RB_x <= 1039.5000000000
                                            if _get(features, "Nest_RB_x") <= 1039.5000000000:
                                                # if Nest_bbox_y <= 612.5000000000
                                                if _get(features, "Nest_bbox_y") <= 612.5000000000:
                                                    # if Actor_RL_y <= 709.5000000000
                                                    if _get(features, "Actor_RL_y") <= 709.5000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        # if Actor_Dist_RB_RL <= 90.9149436951
                                                        if _get(features, "Actor_Dist_RB_RL") <= 90.9149436951:
                                                            return "IPI_ISI"
                                                        else:
                                                            return "OTHER4"
                                                else:
                                                    # if c2_Nest_Distance <= 274.5445709229
                                                    if _get(features, "c2_Nest_Distance") <= 274.5445709229:
                                                        # if c4_Mouse_Distance <= 448.6626739502
                                                        if _get(features, "c4_Mouse_Distance") <= 448.6626739502:
                                                            # if Nest_hu_2 <= 0.0000600500
                                                            if _get(features, "Nest_hu_2") <= 0.0000600500:
                                                                return "OTHER4"
                                                            else:
                                                                # if Nest_Mask_IoU <= 0.9791963398
                                                                if _get(features, "Nest_Mask_IoU") <= 0.9791963398:
                                                                    # if Actor_To_Nest_Dist_Change <= 192.9201736450
                                                                    if _get(features, "Actor_To_Nest_Dist_Change") <= 192.9201736450:
                                                                        # if Nest_Dist_RR_To_Bbox_BL <= 338.4931030273
                                                                        if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 338.4931030273:
                                                                            return "OTHER4"
                                                                        else:
                                                                            # if foodhopperMid_Nest_Distance <= 389.2021026611
                                                                            if _get(features, "foodhopperMid_Nest_Distance") <= 389.2021026611:
                                                                                # if foodhopperMid_Mouse_Distance <= 507.8432769775
                                                                                if _get(features, "foodhopperMid_Mouse_Distance") <= 507.8432769775:
                                                                                    return "OTHER4"
                                                                                else:
                                                                                    return "IPI_ISI"
                                                                            else:
                                                                                # if Nest_Dist_RT_To_Bbox_BR <= 712.8083801270
                                                                                if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 712.8083801270:
                                                                                    return "IPI_ISI"
                                                                                else:
                                                                                    # if Actor_Area_Diff_Abs <= 3247.7500000000
                                                                                    if _get(features, "Actor_Area_Diff_Abs") <= 3247.7500000000:
                                                                                        return "IPI_ISI"
                                                                                    else:
                                                                                        return "OTHER4"
                                                                    else:
                                                                        return "OTHER4"
                                                                else:
                                                                    return "OTHER4"
                                                        else:
                                                            return "OTHER4"
                                                    else:
                                                        return "OTHER4"
                                            else:
                                                return "OTHER4"
                                        else:
                                            return "OTHER4"
                                    else:
                                        # if Nest_Dist_RT_To_Bbox_BR <= 358.4588470459
                                        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 358.4588470459:
                                            # if Nest_Dist_RB_To_Bbox_TR <= 343.6706542969
                                            if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 343.6706542969:
                                                return "IPI_ISI"
                                            else:
                                                return "OTHER4"
                                        else:
                                            # if Nest_hu_2 <= 0.0007697040
                                            if _get(features, "Nest_hu_2") <= 0.0007697040:
                                                return "IPI_ISI"
                                            else:
                                                # if Actor_Dist_RL_To_Bbox_TL <= 46.5000000000
                                                if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 46.5000000000:
                                                    # if Nest_Centroid_To_Bbox_BL <= 409.4195251465
                                                    if _get(features, "Nest_Centroid_To_Bbox_BL") <= 409.4195251465:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    return "OTHER4"
                            else:
                                # if Nest_RB_x <= 1038.5000000000
                                if _get(features, "Nest_RB_x") <= 1038.5000000000:
                                    # if Nest_Dist_RR_To_Bbox_BL <= 811.5390930176
                                    if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 811.5390930176:
                                        # if Nest_hu_4 <= 0.0000232250
                                        if _get(features, "Nest_hu_4") <= 0.0000232250:
                                            # if Nest_Dist_RB_To_Bbox_BL <= 28.5175437927
                                            if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 28.5175437927:
                                                return "OTHER4"
                                            else:
                                                # if Actor_Dist_RB_To_Bbox_BL <= 329.5015258789
                                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 329.5015258789:
                                                    # if Nest_Dist_RR_To_Bbox_TR <= 258.0019378662
                                                    if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 258.0019378662:
                                                        # if c2_Mouse_Distance <= 228.5229644775
                                                        if _get(features, "c2_Mouse_Distance") <= 228.5229644775:
                                                            # if Nest_RB_y <= 923.5000000000
                                                            if _get(features, "Nest_RB_y") <= 923.5000000000:
                                                                return "IPI_ISI"
                                                            else:
                                                                return "OTHER4"
                                                        else:
                                                            # if Actor_Dist_RT_To_Bbox_TR <= 272.0000000000
                                                            if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 272.0000000000:
                                                                return "IPI_ISI"
                                                            else:
                                                                # if c4_Mouse_Distance <= 414.1730346680
                                                                if _get(features, "c4_Mouse_Distance") <= 414.1730346680:
                                                                    return "IPI_ISI"
                                                                else:
                                                                    return "OTHER4"
                                                    else:
                                                        # if Nest_Dist_RT_To_Bbox_BR <= 546.7590789795
                                                        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 546.7590789795:
                                                            return "OTHER4"
                                                        else:
                                                            return "IPI_ISI"
                                                else:
                                                    # if Actor_To_Nest_Distance <= 137.5049476624
                                                    if _get(features, "Actor_To_Nest_Distance") <= 137.5049476624:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                        else:
                                            return "OTHER4"
                                    else:
                                        return "OTHER4"
                                else:
                                    return "OTHER4"
                        else:
                            # if Nest_RR_x <= 1143.5000000000
                            if _get(features, "Nest_RR_x") <= 1143.5000000000:
                                return "OTHER4"
                            else:
                                # if Nest_Dist_RB_RL <= 426.3361816406
                                if _get(features, "Nest_Dist_RB_RL") <= 426.3361816406:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                    else:
                        # if Actor_perimeter <= 972.7493286133
                        if _get(features, "Actor_perimeter") <= 972.7493286133:
                            # if Actor_Centroid_To_Bbox_TL <= 151.4324493408
                            if _get(features, "Actor_Centroid_To_Bbox_TL") <= 151.4324493408:
                                # if Actor_Dist_RL_To_Bbox_BR <= 290.4827423096
                                if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 290.4827423096:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                return "IPI_ISI"
                        else:
                            # if Actor_Direction_deg <= -179.1057815552
                            if _get(features, "Actor_Direction_deg") <= -179.1057815552:
                                return "IPI_ISI"
                            else:
                                # if Nest_Mask_IoU <= 0.9786334634
                                if _get(features, "Nest_Mask_IoU") <= 0.9786334634:
                                    return "OTHER4"
                                else:
                                    # if Nest_Dist_RR_To_Bbox_TL <= 784.6086730957
                                    if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 784.6086730957:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
            else:
                # if Nest_area <= 174100.5000000000
                if _get(features, "Nest_area") <= 174100.5000000000:
                    # if Nest_Dist_RR_To_Bbox_BR <= 208.0024032593
                    if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 208.0024032593:
                        # if Nest_orientation <= 81.8098220825
                        if _get(features, "Nest_orientation") <= 81.8098220825:
                            # if Nest_Dist_RT_To_Bbox_BR <= 380.0319671631
                            if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 380.0319671631:
                                return "IPI_ISI"
                            else:
                                return "OTHER4"
                        else:
                            # if Nest_RB_y <= 897.5000000000
                            if _get(features, "Nest_RB_y") <= 897.5000000000:
                                return "OTHER4"
                            else:
                                # if Actor_To_Nest_Distance <= 424.7747192383
                                if _get(features, "Actor_To_Nest_Distance") <= 424.7747192383:
                                    # if Actor_RB_x <= 355.5000000000
                                    if _get(features, "Actor_RB_x") <= 355.5000000000:
                                        # if Nest_Centroid_To_Bbox_TR <= 408.6330261230
                                        if _get(features, "Nest_Centroid_To_Bbox_TR") <= 408.6330261230:
                                            # if foodhopperBottom_Mouse_Distance <= 362.1372985840
                                            if _get(features, "foodhopperBottom_Mouse_Distance") <= 362.1372985840:
                                                # if Actor_Dist_RB_To_Bbox_BL <= 34.0147151947
                                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 34.0147151947:
                                                    return "OTHER4"
                                                else:
                                                    return "IPI_ISI"
                                            else:
                                                return "IPI_ISI"
                                        else:
                                            # if Nest_RB_x <= 797.5000000000
                                            if _get(features, "Nest_RB_x") <= 797.5000000000:
                                                # if Actor_Centroid_To_Bbox_BR <= 238.8917388916
                                                if _get(features, "Actor_Centroid_To_Bbox_BR") <= 238.8917388916:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                            else:
                                                # if Nest_hu_5 <= 0.0006642250
                                                if _get(features, "Nest_hu_5") <= 0.0006642250:
                                                    # if Actor_Centroid_To_Bbox_BR <= 244.3379364014
                                                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 244.3379364014:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    # if Nest_perimeter <= 2326.2789306641
                                                    if _get(features, "Nest_perimeter") <= 2326.2789306641:
                                                        # if Actor_Dist_RB_RL <= 88.0159263611
                                                        if _get(features, "Actor_Dist_RB_RL") <= 88.0159263611:
                                                            return "OTHER4"
                                                        else:
                                                            return "IPI_ISI"
                                                    else:
                                                        # if Nest_hu_3 <= 0.0029876131
                                                        if _get(features, "Nest_hu_3") <= 0.0029876131:
                                                            # if Actor_Dist_RB_To_Bbox_TL <= 231.5700378418
                                                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 231.5700378418:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                        else:
                                                            return "IPI_ISI"
                                    else:
                                        # if Nest_bbox_y <= 660.5000000000
                                        if _get(features, "Nest_bbox_y") <= 660.5000000000:
                                            # if Nest_hu_6 <= -0.0000024250
                                            if _get(features, "Nest_hu_6") <= -0.0000024250:
                                                return "OTHER4"
                                            else:
                                                # if Nest_Centroid_To_Bbox_TR <= 452.0232086182
                                                if _get(features, "Nest_Centroid_To_Bbox_TR") <= 452.0232086182:
                                                    # if Nest_RB_x <= 1060.5000000000
                                                    if _get(features, "Nest_RB_x") <= 1060.5000000000:
                                                        # if Actor_RR_y <= 596.5000000000
                                                        if _get(features, "Actor_RR_y") <= 596.5000000000:
                                                            # if Nest_centroid_x <= 659.6343688965
                                                            if _get(features, "Nest_centroid_x") <= 659.6343688965:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                        else:
                                                            # if foodhopperBottom_Mouse_Distance <= 301.1957855225
                                                            if _get(features, "foodhopperBottom_Mouse_Distance") <= 301.1957855225:
                                                                # if c2_Nest_Distance <= 238.8953628540
                                                                if _get(features, "c2_Nest_Distance") <= 238.8953628540:
                                                                    # if Nest_hu_5 <= 0.0000898000
                                                                    if _get(features, "Nest_hu_5") <= 0.0000898000:
                                                                        return "IPI_ISI"
                                                                    else:
                                                                        return "OTHER4"
                                                                else:
                                                                    # if Actor_Dist_RB_To_Bbox_TR <= 305.2687835693
                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 305.2687835693:
                                                                        # if Nest_centroid_y <= 789.2643127441
                                                                        if _get(features, "Nest_centroid_y") <= 789.2643127441:
                                                                            # if Actor_Dist_RT_To_Bbox_TR <= 321.5000000000
                                                                            if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 321.5000000000:
                                                                                return "IPI_ISI"
                                                                            else:
                                                                                # if Actor_perimeter <= 960.1427612305
                                                                                if _get(features, "Actor_perimeter") <= 960.1427612305:
                                                                                    return "OTHER4"
                                                                                else:
                                                                                    return "IPI_ISI"
                                                                        else:
                                                                            # if foodhopperRight_Mouse_Distance <= 664.6405639648
                                                                            if _get(features, "foodhopperRight_Mouse_Distance") <= 664.6405639648:
                                                                                return "OTHER4"
                                                                            else:
                                                                                return "IPI_ISI"
                                                                    else:
                                                                        return "OTHER4"
                                                            else:
                                                                # if Nest_Centroid_To_Bbox_BR <= 358.1875610352
                                                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 358.1875610352:
                                                                    # if Nest_Dist_RL_RR <= 662.1174316406
                                                                    if _get(features, "Nest_Dist_RL_RR") <= 662.1174316406:
                                                                        return "IPI_ISI"
                                                                    else:
                                                                        # if Nest_Dist_RB_To_Bbox_BR <= 545.5009155273
                                                                        if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 545.5009155273:
                                                                            return "OTHER4"
                                                                        else:
                                                                            return "IPI_ISI"
                                                                else:
                                                                    # if Nest_hu_2 <= 0.0001362475
                                                                    if _get(features, "Nest_hu_2") <= 0.0001362475:
                                                                        return "OTHER4"
                                                                    else:
                                                                        # if Nest_Dist_RB_To_Bbox_BR <= 39.5126571655
                                                                        if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 39.5126571655:
                                                                            # if Nest_RR_x <= 1072.5000000000
                                                                            if _get(features, "Nest_RR_x") <= 1072.5000000000:
                                                                                return "IPI_ISI"
                                                                            else:
                                                                                return "OTHER4"
                                                                        else:
                                                                            # if Actor_RB_x <= 356.5000000000
                                                                            if _get(features, "Actor_RB_x") <= 356.5000000000:
                                                                                # if Actor_RB_y <= 820.5000000000
                                                                                if _get(features, "Actor_RB_y") <= 820.5000000000:
                                                                                    # if Nest_Dist_RT_To_Bbox_TL <= 439.5000000000
                                                                                    if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 439.5000000000:
                                                                                        return "IPI_ISI"
                                                                                    else:
                                                                                        return "OTHER4"
                                                                                else:
                                                                                    return "IPI_ISI"
                                                                            else:
                                                                                # if Nest_RL_y <= 662.5000000000
                                                                                if _get(features, "Nest_RL_y") <= 662.5000000000:
                                                                                    return "OTHER4"
                                                                                else:
                                                                                    # if Nest_RB_x <= 404.5000000000
                                                                                    if _get(features, "Nest_RB_x") <= 404.5000000000:
                                                                                        return "OTHER4"
                                                                                    else:
                                                                                        # if Nest_hu_1 <= 0.0141574969
                                                                                        if _get(features, "Nest_hu_1") <= 0.0141574969:
                                                                                            return "OTHER4"
                                                                                        else:
                                                                                            # if Actor_hu_3 <= 0.0130284964
                                                                                            if _get(features, "Actor_hu_3") <= 0.0130284964:
                                                                                                # if Nest_Dist_RT_To_Bbox_BL <= 694.1102294922
                                                                                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 694.1102294922:
                                                                                                    # if Nest_orientation <= 82.4189262390
                                                                                                    if _get(features, "Nest_orientation") <= 82.4189262390:
                                                                                                        # if Actor_Dist_RR_To_Bbox_BR <= 105.5047378540
                                                                                                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 105.5047378540:
                                                                                                            return "OTHER4"
                                                                                                        else:
                                                                                                            return "IPI_ISI"
                                                                                                    else:
                                                                                                        # if Actor_To_Nest_Distance <= 422.3148498535
                                                                                                        if _get(features, "Actor_To_Nest_Distance") <= 422.3148498535:
                                                                                                            # if Actor_RL_y <= 912.0000000000
                                                                                                            if _get(features, "Actor_RL_y") <= 912.0000000000:
                                                                                                                # if Actor_hu_6 <= 0.0000912000
                                                                                                                if _get(features, "Actor_hu_6") <= 0.0000912000:
                                                                                                                    # if foodhopperLeft_Mouse_Distance <= 17.4739551544
                                                                                                                    if _get(features, "foodhopperLeft_Mouse_Distance") <= 17.4739551544:
                                                                                                                        # if foodhopperRight_Mouse_Distance <= 643.0494079590
                                                                                                                        if _get(features, "foodhopperRight_Mouse_Distance") <= 643.0494079590:
                                                                                                                            return "OTHER4"
                                                                                                                        else:
                                                                                                                            # if Actor_hu_4 <= 0.0000382500
                                                                                                                            if _get(features, "Actor_hu_4") <= 0.0000382500:
                                                                                                                                return "IPI_ISI"
                                                                                                                            else:
                                                                                                                                return "OTHER4"
                                                                                                                    else:
                                                                                                                        # if Actor_RR_y <= 598.5000000000
                                                                                                                        if _get(features, "Actor_RR_y") <= 598.5000000000:
                                                                                                                            # if Actor_Dist_RL_To_Bbox_BR <= 132.4527435303
                                                                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 132.4527435303:
                                                                                                                                return "OTHER4"
                                                                                                                            else:
                                                                                                                                return "IPI_ISI"
                                                                                                                        else:
                                                                                                                            # if Actor_Dist_RR_RB <= 13.7649297714
                                                                                                                            if _get(features, "Actor_Dist_RR_RB") <= 13.7649297714:
                                                                                                                                # if foodhopperMid_Nest_Distance <= 420.2356414795
                                                                                                                                if _get(features, "foodhopperMid_Nest_Distance") <= 420.2356414795:
                                                                                                                                    # if foodhopperLeft_Mouse_Distance <= 69.3616409302
                                                                                                                                    if _get(features, "foodhopperLeft_Mouse_Distance") <= 69.3616409302:
                                                                                                                                        return "OTHER4"
                                                                                                                                    else:
                                                                                                                                        return "IPI_ISI"
                                                                                                                                else:
                                                                                                                                    # if Nest_RT_y <= 621.5000000000
                                                                                                                                    if _get(features, "Nest_RT_y") <= 621.5000000000:
                                                                                                                                        # if Actor_Dist_RT_RB <= 300.6764678955
                                                                                                                                        if _get(features, "Actor_Dist_RT_RB") <= 300.6764678955:
                                                                                                                                            return "IPI_ISI"
                                                                                                                                        else:
                                                                                                                                            return "OTHER4"
                                                                                                                                    else:
                                                                                                                                        return "IPI_ISI"
                                                                                                                            else:
                                                                                                                                # if Nest_solidity <= 0.9106019437
                                                                                                                                if _get(features, "Nest_solidity") <= 0.9106019437:
                                                                                                                                    # if Actor_Dist_RB_To_Bbox_BL <= 328.5015258789
                                                                                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 328.5015258789:
                                                                                                                                        return "IPI_ISI"
                                                                                                                                    else:
                                                                                                                                        # if Nest_RR_y <= 868.5000000000
                                                                                                                                        if _get(features, "Nest_RR_y") <= 868.5000000000:
                                                                                                                                            return "OTHER4"
                                                                                                                                        else:
                                                                                                                                            return "IPI_ISI"
                                                                                                                                else:
                                                                                                                                    # if Nest_Dist_RR_To_Bbox_BL <= 778.6985473633
                                                                                                                                    if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 778.6985473633:
                                                                                                                                        return "IPI_ISI"
                                                                                                                                    else:
                                                                                                                                        return "OTHER4"
                                                                                                                else:
                                                                                                                    # if Actor_centroid_y <= 674.1706848145
                                                                                                                    if _get(features, "Actor_centroid_y") <= 674.1706848145:
                                                                                                                        return "IPI_ISI"
                                                                                                                    else:
                                                                                                                        return "OTHER4"
                                                                                                            else:
                                                                                                                # if Nest_hu_1 <= 0.0286861248
                                                                                                                if _get(features, "Nest_hu_1") <= 0.0286861248:
                                                                                                                    return "OTHER4"
                                                                                                                else:
                                                                                                                    return "IPI_ISI"
                                                                                                        else:
                                                                                                            # if c2_Mouse_Distance <= 362.6828002930
                                                                                                            if _get(features, "c2_Mouse_Distance") <= 362.6828002930:
                                                                                                                return "OTHER4"
                                                                                                            else:
                                                                                                                # if Actor_hu_2 <= 0.0018093970
                                                                                                                if _get(features, "Actor_hu_2") <= 0.0018093970:
                                                                                                                    return "IPI_ISI"
                                                                                                                else:
                                                                                                                    return "OTHER4"
                                                                                                else:
                                                                                                    # if c4_Mouse_Distance <= 430.7918090820
                                                                                                    if _get(features, "c4_Mouse_Distance") <= 430.7918090820:
                                                                                                        # if Actor_Mask_IoU <= 0.9257242680
                                                                                                        if _get(features, "Actor_Mask_IoU") <= 0.9257242680:
                                                                                                            # if Actor_aspect_ratio <= 1.9854311347
                                                                                                            if _get(features, "Actor_aspect_ratio") <= 1.9854311347:
                                                                                                                # if Nest_Centroid_To_Bbox_TR <= 418.4795989990
                                                                                                                if _get(features, "Nest_Centroid_To_Bbox_TR") <= 418.4795989990:
                                                                                                                    # if Actor_Mask_IoU <= 0.9254615009
                                                                                                                    if _get(features, "Actor_Mask_IoU") <= 0.9254615009:
                                                                                                                        # if Actor_Area_Diff_Abs <= 204.7500000000
                                                                                                                        if _get(features, "Actor_Area_Diff_Abs") <= 204.7500000000:
                                                                                                                            return "OTHER4"
                                                                                                                        else:
                                                                                                                            return "IPI_ISI"
                                                                                                                    else:
                                                                                                                        return "OTHER4"
                                                                                                                else:
                                                                                                                    # if Nest_Dist_RL_To_Bbox_TR <= 783.1903381348
                                                                                                                    if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 783.1903381348:
                                                                                                                        return "OTHER4"
                                                                                                                    else:
                                                                                                                        return "IPI_ISI"
                                                                                                            else:
                                                                                                                # if Nest_hu_1 <= 0.1198618859
                                                                                                                if _get(features, "Nest_hu_1") <= 0.1198618859:
                                                                                                                    return "OTHER4"
                                                                                                                else:
                                                                                                                    # if Nest_Dist_RL_RT <= 626.5951843262
                                                                                                                    if _get(features, "Nest_Dist_RL_RT") <= 626.5951843262:
                                                                                                                        return "OTHER4"
                                                                                                                    else:
                                                                                                                        return "IPI_ISI"
                                                                                                        else:
                                                                                                            # if Actor_To_Nest_Dist_Change <= -5.4767155647
                                                                                                            if _get(features, "Actor_To_Nest_Dist_Change") <= -5.4767155647:
                                                                                                                # if Nest_aspect_ratio <= 2.3742773533
                                                                                                                if _get(features, "Nest_aspect_ratio") <= 2.3742773533:
                                                                                                                    return "IPI_ISI"
                                                                                                                else:
                                                                                                                    return "OTHER4"
                                                                                                            else:
                                                                                                                # if Actor_RR_x <= 814.5000000000
                                                                                                                if _get(features, "Actor_RR_x") <= 814.5000000000:
                                                                                                                    # if Nest_Mask_IoU <= 0.9835002422
                                                                                                                    if _get(features, "Nest_Mask_IoU") <= 0.9835002422:
                                                                                                                        # if Actor_RL_y <= 692.5000000000
                                                                                                                        if _get(features, "Actor_RL_y") <= 692.5000000000:
                                                                                                                            return "OTHER4"
                                                                                                                        else:
                                                                                                                            return "IPI_ISI"
                                                                                                                    else:
                                                                                                                        return "IPI_ISI"
                                                                                                                else:
                                                                                                                    # if Actor_area <= 36492.0000000000
                                                                                                                    if _get(features, "Actor_area") <= 36492.0000000000:
                                                                                                                        return "OTHER4"
                                                                                                                    else:
                                                                                                                        return "IPI_ISI"
                                                                                                    else:
                                                                                                        # if Nest_Dist_RB_To_Bbox_TR <= 351.1129913330
                                                                                                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 351.1129913330:
                                                                                                            return "IPI_ISI"
                                                                                                        else:
                                                                                                            # if Actor_Direction_deg <= 146.7799377441
                                                                                                            if _get(features, "Actor_Direction_deg") <= 146.7799377441:
                                                                                                                return "OTHER4"
                                                                                                            else:
                                                                                                                return "IPI_ISI"
                                                                                            else:
                                                                                                # if Actor_Dist_RR_To_Bbox_BR <= 105.0047607422
                                                                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 105.0047607422:
                                                                                                    # if c4_Nest_Distance <= 417.8031768799
                                                                                                    if _get(features, "c4_Nest_Distance") <= 417.8031768799:
                                                                                                        return "IPI_ISI"
                                                                                                    else:
                                                                                                        return "OTHER4"
                                                                                                else:
                                                                                                    return "OTHER4"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    return "OTHER4"
                                        else:
                                            return "OTHER4"
                                else:
                                    # if Actor_hu_2 <= 0.0015718165
                                    if _get(features, "Actor_hu_2") <= 0.0015718165:
                                        # if Actor_Dist_RL_To_Bbox_BL <= 141.5000000000
                                        if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 141.5000000000:
                                            return "OTHER4"
                                        else:
                                            # if Actor_eccentricity <= 0.8251172304
                                            if _get(features, "Actor_eccentricity") <= 0.8251172304:
                                                # if Actor_hu_2 <= 0.0015232125
                                                if _get(features, "Actor_hu_2") <= 0.0015232125:
                                                    return "IPI_ISI"
                                                else:
                                                    # if Actor_Dist_RR_To_Bbox_BL <= 311.4795684814
                                                    if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 311.4795684814:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                            else:
                                                # if Actor_RR_x <= 675.5000000000
                                                if _get(features, "Actor_RR_x") <= 675.5000000000:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_BL <= 287.6319732666
                                        if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 287.6319732666:
                                            return "IPI_ISI"
                                        else:
                                            # if foodhopperMid_Nest_Distance <= 387.9352416992
                                            if _get(features, "foodhopperMid_Nest_Distance") <= 387.9352416992:
                                                # if Actor_Dist_RR_To_Bbox_TR <= 267.0018768311
                                                if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 267.0018768311:
                                                    return "OTHER4"
                                                else:
                                                    return "IPI_ISI"
                                            else:
                                                return "IPI_ISI"
                    else:
                        # if Nest_Dist_RT_To_Bbox_TL <= 331.5000000000
                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 331.5000000000:
                            # if Actor_hu_5 <= 0.0000021850
                            if _get(features, "Actor_hu_5") <= 0.0000021850:
                                # if Nest_hu_3 <= 0.0003125500
                                if _get(features, "Nest_hu_3") <= 0.0003125500:
                                    # if Nest_Dist_RL_To_Bbox_TL <= 116.5000000000
                                    if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 116.5000000000:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                # if Actor_hu_2 <= 0.0006086130
                                if _get(features, "Actor_hu_2") <= 0.0006086130:
                                    return "OTHER4"
                                else:
                                    # if Actor_hu_4 <= 0.0000004215
                                    if _get(features, "Actor_hu_4") <= 0.0000004215:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                        else:
                            # if Nest_hu_0 <= 0.3141033500
                            if _get(features, "Nest_hu_0") <= 0.3141033500:
                                # if Nest_Dist_RT_To_Bbox_BR <= 565.9014282227
                                if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 565.9014282227:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                return "IPI_ISI"
                else:
                    # if Actor_Dist_RL_To_Bbox_TL <= 39.5000000000
                    if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 39.5000000000:
                        # if Actor_Dist_RR_To_Bbox_BR <= 28.5175437927
                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 28.5175437927:
                            # if Nest_Dist_RT_To_Bbox_TL <= 362.5000000000
                            if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 362.5000000000:
                                # if Actor_bbox_y <= 893.5000000000
                                if _get(features, "Actor_bbox_y") <= 893.5000000000:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                # if Nest_RT_x <= 672.0000000000
                                if _get(features, "Nest_RT_x") <= 672.0000000000:
                                    # if Actor_RR_y <= 601.5000000000
                                    if _get(features, "Actor_RR_y") <= 601.5000000000:
                                        # if Actor_bbox_x <= 434.0000000000
                                        if _get(features, "Actor_bbox_x") <= 434.0000000000:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                    else:
                                        # if c4_Mouse_Distance <= 419.6315612793
                                        if _get(features, "c4_Mouse_Distance") <= 419.6315612793:
                                            # if c1_Mouse_Distance <= 551.4446716309
                                            if _get(features, "c1_Mouse_Distance") <= 551.4446716309:
                                                # if Actor_Dist_RL_To_Bbox_TR <= 250.2503814697
                                                if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 250.2503814697:
                                                    # if Nest_Dist_RL_To_Bbox_TR <= 709.4920654297
                                                    if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 709.4920654297:
                                                        return "OTHER4"
                                                    else:
                                                        # if Nest_perimeter <= 2081.9581298828
                                                        if _get(features, "Nest_perimeter") <= 2081.9581298828:
                                                            return "OTHER4"
                                                        else:
                                                            # if Nest_extent <= 0.6459436417
                                                            if _get(features, "Nest_extent") <= 0.6459436417:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                            else:
                                                # if Nest_Dist_RB_To_Bbox_BL <= 172.5028991699
                                                if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 172.5028991699:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                        else:
                                            return "OTHER4"
                                else:
                                    # if Actor_area <= 10298.2500000000
                                    if _get(features, "Actor_area") <= 10298.2500000000:
                                        return "OTHER4"
                                    else:
                                        # if Actor_Dist_RL_To_Bbox_TR <= 225.3136672974
                                        if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 225.3136672974:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                        else:
                            # if Nest_Dist_RT_To_Bbox_BL <= 512.7828826904
                            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 512.7828826904:
                                return "IPI_ISI"
                            else:
                                # if Nest_hu_5 <= 0.0000129000
                                if _get(features, "Nest_hu_5") <= 0.0000129000:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                    else:
                        # if Nest_Dist_RB_To_Bbox_TL <= 386.6205444336
                        if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 386.6205444336:
                            return "IPI_ISI"
                        else:
                            # if Nest_Dist_RL_RT <= 133.4012107849
                            if _get(features, "Nest_Dist_RL_RT") <= 133.4012107849:
                                return "IPI_ISI"
                            else:
                                # if Nest_Area_Diff_Abs <= 7269.2500000000
                                if _get(features, "Nest_Area_Diff_Abs") <= 7269.2500000000:
                                    # if Actor_aspect_ratio <= 2.6595360041
                                    if _get(features, "Actor_aspect_ratio") <= 2.6595360041:
                                        return "OTHER4"
                                    else:
                                        # if Actor_aspect_ratio <= 2.6913082600
                                        if _get(features, "Actor_aspect_ratio") <= 2.6913082600:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                else:
                                    return "IPI_ISI"
        else:
            # if c2_Nest_Distance <= 503.9048614502
            if _get(features, "c2_Nest_Distance") <= 503.9048614502:
                # if Actor_To_Nest_Distance <= 84.5685005188
                if _get(features, "Actor_To_Nest_Distance") <= 84.5685005188:
                    # if Nest_RR_x <= 954.5000000000
                    if _get(features, "Nest_RR_x") <= 954.5000000000:
                        return "OTHER4"
                    else:
                        return "IPI_ISI"
                else:
                    # if Nest_Dist_RB_To_Bbox_TR <= 676.5876464844
                    if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 676.5876464844:
                        # if Nest_bbox_h <= 277.5000000000
                        if _get(features, "Nest_bbox_h") <= 277.5000000000:
                            # if Nest_hu_5 <= -0.0000034150
                            if _get(features, "Nest_hu_5") <= -0.0000034150:
                                # if Nest_Area_Diff_Abs <= 1729.7500000000
                                if _get(features, "Nest_Area_Diff_Abs") <= 1729.7500000000:
                                    # if Actor_solidity <= 0.8984458447
                                    if _get(features, "Actor_solidity") <= 0.8984458447:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                                else:
                                    return "OTHER4"
                            else:
                                # if Nest_orientation <= 111.0392646790
                                if _get(features, "Nest_orientation") <= 111.0392646790:
                                    # if Actor_Direction_deg <= -176.4980697632
                                    if _get(features, "Actor_Direction_deg") <= -176.4980697632:
                                        # if Actor_RR_y <= 702.0000000000
                                        if _get(features, "Actor_RR_y") <= 702.0000000000:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                    else:
                                        return "OTHER4"
                                else:
                                    # if Actor_Dist_RL_To_Bbox_BR <= 376.3509521484
                                    if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 376.3509521484:
                                        return "OTHER4"
                                    else:
                                        return "IPI_ISI"
                        else:
                            # if Nest_Area_Diff_Abs <= 62232.7500000000
                            if _get(features, "Nest_Area_Diff_Abs") <= 62232.7500000000:
                                # if Nest_perimeter <= 2818.9687500000
                                if _get(features, "Nest_perimeter") <= 2818.9687500000:
                                    # if foodhopperMid_Nest_Distance <= 611.9639892578
                                    if _get(features, "foodhopperMid_Nest_Distance") <= 611.9639892578:
                                        # if Nest_perimeter <= 1265.3422851562
                                        if _get(features, "Nest_perimeter") <= 1265.3422851562:
                                            # if Actor_bbox_h <= 238.5000000000
                                            if _get(features, "Actor_bbox_h") <= 238.5000000000:
                                                return "IPI_ISI"
                                            else:
                                                # if Actor_Mask_IoU <= 0.9368969202
                                                if _get(features, "Actor_Mask_IoU") <= 0.9368969202:
                                                    # if Nest_Dist_RT_RR <= 400.9887847900
                                                    if _get(features, "Nest_Dist_RT_RR") <= 400.9887847900:
                                                        # if Actor_Centroid_To_Bbox_BL <= 214.8645858765
                                                        if _get(features, "Actor_Centroid_To_Bbox_BL") <= 214.8645858765:
                                                            # if Actor_Centroid_To_Bbox_TL <= 197.5289001465
                                                            if _get(features, "Actor_Centroid_To_Bbox_TL") <= 197.5289001465:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                        else:
                                                            return "OTHER4"
                                                    else:
                                                        # if Nest_Dist_RT_To_Bbox_TL <= 64.0000000000
                                                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 64.0000000000:
                                                            return "OTHER4"
                                                        else:
                                                            return "IPI_ISI"
                                                else:
                                                    return "IPI_ISI"
                                        else:
                                            # if Actor_hu_6 <= -0.0000281500
                                            if _get(features, "Actor_hu_6") <= -0.0000281500:
                                                # if Actor_area <= 9378.5000000000
                                                if _get(features, "Actor_area") <= 9378.5000000000:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                            else:
                                                # if Actor_Dist_RT_To_Bbox_TL <= 1.5000000000
                                                if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 1.5000000000:
                                                    # if Nest_Centroid_To_Bbox_TL <= 394.0231933594
                                                    if _get(features, "Nest_Centroid_To_Bbox_TL") <= 394.0231933594:
                                                        return "OTHER4"
                                                    else:
                                                        return "IPI_ISI"
                                                else:
                                                    # if Actor_hu_5 <= -0.0012492750
                                                    if _get(features, "Actor_hu_5") <= -0.0012492750:
                                                        # if Actor_Centroid_To_Bbox_TL <= 148.0480461121
                                                        if _get(features, "Actor_Centroid_To_Bbox_TL") <= 148.0480461121:
                                                            return "IPI_ISI"
                                                        else:
                                                            return "OTHER4"
                                                    else:
                                                        # if Nest_Dist_RT_To_Bbox_TL <= 607.5000000000
                                                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 607.5000000000:
                                                            # if Nest_bbox_h <= 280.5000000000
                                                            if _get(features, "Nest_bbox_h") <= 280.5000000000:
                                                                # if Nest_RB_x <= 691.0000000000
                                                                if _get(features, "Nest_RB_x") <= 691.0000000000:
                                                                    return "OTHER4"
                                                                else:
                                                                    return "IPI_ISI"
                                                            else:
                                                                # if Actor_hu_6 <= 0.0012053250
                                                                if _get(features, "Actor_hu_6") <= 0.0012053250:
                                                                    # if foodhopperLeft_Mouse_Distance <= 5.2419352531
                                                                    if _get(features, "foodhopperLeft_Mouse_Distance") <= 5.2419352531:
                                                                        # if foodhopperRight_Mouse_Distance <= 647.5388488770
                                                                        if _get(features, "foodhopperRight_Mouse_Distance") <= 647.5388488770:
                                                                            return "IPI_ISI"
                                                                        else:
                                                                            return "OTHER4"
                                                                    else:
                                                                        # if Actor_bbox_x <= 494.5000000000
                                                                        if _get(features, "Actor_bbox_x") <= 494.5000000000:
                                                                            # if Actor_Dist_RR_To_Bbox_BR <= 185.5026931763
                                                                            if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 185.5026931763:
                                                                                # if Nest_Area_Diff_Abs <= 20443.2500000000
                                                                                if _get(features, "Nest_Area_Diff_Abs") <= 20443.2500000000:
                                                                                    return "OTHER4"
                                                                                else:
                                                                                    # if Actor_Dist_RB_To_Bbox_TR <= 139.8449821472
                                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 139.8449821472:
                                                                                        return "IPI_ISI"
                                                                                    else:
                                                                                        return "OTHER4"
                                                                            else:
                                                                                # if Nest_Dist_RT_RB <= 533.4756011963
                                                                                if _get(features, "Nest_Dist_RT_RB") <= 533.4756011963:
                                                                                    return "OTHER4"
                                                                                else:
                                                                                    return "IPI_ISI"
                                                                        else:
                                                                            # if Nest_RR_y <= 789.0000000000
                                                                            if _get(features, "Nest_RR_y") <= 789.0000000000:
                                                                                return "IPI_ISI"
                                                                            else:
                                                                                return "OTHER4"
                                                                else:
                                                                    # if Actor_Dist_RL_To_Bbox_BL <= 63.5000000000
                                                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 63.5000000000:
                                                                        return "IPI_ISI"
                                                                    else:
                                                                        return "OTHER4"
                                                        else:
                                                            # if Nest_Dist_RL_To_Bbox_BL <= 183.0000000000
                                                            if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 183.0000000000:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                    else:
                                        return "IPI_ISI"
                                else:
                                    # if foodhopperLeft_Nest_Distance <= 148.7028884888
                                    if _get(features, "foodhopperLeft_Nest_Distance") <= 148.7028884888:
                                        return "OTHER4"
                                    else:
                                        return "IPI_ISI"
                            else:
                                # if Nest_Dist_RB_RL <= 397.5560150146
                                if _get(features, "Nest_Dist_RB_RL") <= 397.5560150146:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                    else:
                        # if Nest_area <= 191937.0000000000
                        if _get(features, "Nest_area") <= 191937.0000000000:
                            return "OTHER4"
                        else:
                            # if Actor_Dist_RR_To_Bbox_BR <= 26.0192527771
                            if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 26.0192527771:
                                return "IPI_ISI"
                            else:
                                # if Nest_Dist_RB_RL <= 313.0055236816
                                if _get(features, "Nest_Dist_RB_RL") <= 313.0055236816:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
            else:
                # if Actor_Dist_RL_To_Bbox_BL <= 91.5000000000
                if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 91.5000000000:
                    # if Actor_Dist_RT_To_Bbox_BL <= 199.0513916016
                    if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 199.0513916016:
                        return "IPI_ISI"
                    else:
                        return "OTHER4"
                else:
                    # if Actor_perimeter <= 1324.3752441406
                    if _get(features, "Actor_perimeter") <= 1324.3752441406:
                        # if Actor_extent <= 0.7059853375
                        if _get(features, "Actor_extent") <= 0.7059853375:
                            # if Nest_Dist_RT_To_Bbox_BL <= 365.0618591309
                            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 365.0618591309:
                                return "OTHER4"
                            else:
                                # if Actor_Centroid_To_Bbox_BL <= 247.1704864502
                                if _get(features, "Actor_Centroid_To_Bbox_BL") <= 247.1704864502:
                                    return "IPI_ISI"
                                else:
                                    return "OTHER4"
                        else:
                            # if Nest_Centroid_To_Bbox_BR <= 230.8571395874
                            if _get(features, "Nest_Centroid_To_Bbox_BR") <= 230.8571395874:
                                return "OTHER4"
                            else:
                                return "IPI_ISI"
                    else:
                        return "OTHER4"
    else:
        # if Nest_RR_x <= 1257.0000000000
        if _get(features, "Nest_RR_x") <= 1257.0000000000:
            # if Nest_hu_0 <= 0.3806101978
            if _get(features, "Nest_hu_0") <= 0.3806101978:
                # if Nest_Centroid_To_Bbox_TL <= 246.1635665894
                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 246.1635665894:
                    # if Nest_RL_y <= 716.5000000000
                    if _get(features, "Nest_RL_y") <= 716.5000000000:
                        # if foodhopperMid_Nest_Distance <= 439.5938415527
                        if _get(features, "foodhopperMid_Nest_Distance") <= 439.5938415527:
                            return "OTHER4"
                        else:
                            return "IPI_ISI"
                    else:
                        return "OTHER4"
                else:
                    # if Actor_centroid_y <= 803.8483581543
                    if _get(features, "Actor_centroid_y") <= 803.8483581543:
                        # if Nest_Dist_RB_To_Bbox_TR <= 286.1581573486
                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 286.1581573486:
                            # if Actor_Centroid_To_Bbox_TL <= 171.7080230713
                            if _get(features, "Actor_Centroid_To_Bbox_TL") <= 171.7080230713:
                                return "IPI_ISI"
                            else:
                                return "OTHER4"
                        else:
                            # if Nest_RT_y <= 668.5000000000
                            if _get(features, "Nest_RT_y") <= 668.5000000000:
                                # if Actor_Dist_RT_To_Bbox_BR <= 25.7112741470
                                if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 25.7112741470:
                                    # if Nest_Dist_RT_RR <= 436.1735687256
                                    if _get(features, "Nest_Dist_RT_RR") <= 436.1735687256:
                                        return "OTHER4"
                                    else:
                                        return "IPI_ISI"
                                else:
                                    # if Actor_RL_x <= 535.5000000000
                                    if _get(features, "Actor_RL_x") <= 535.5000000000:
                                        # if Nest_Dist_RB_To_Bbox_BL <= 366.5013732910
                                        if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 366.5013732910:
                                            # if Actor_hu_1 <= 0.0000481000
                                            if _get(features, "Actor_hu_1") <= 0.0000481000:
                                                return "IPI_ISI"
                                            else:
                                                # if Nest_RR_x <= 601.5000000000
                                                if _get(features, "Nest_RR_x") <= 601.5000000000:
                                                    return "IPI_ISI"
                                                else:
                                                    # if Nest_Dist_RB_RL <= 98.6393089294
                                                    if _get(features, "Nest_Dist_RB_RL") <= 98.6393089294:
                                                        # if Nest_orientation <= 45.9233798981
                                                        if _get(features, "Nest_orientation") <= 45.9233798981:
                                                            return "OTHER4"
                                                        else:
                                                            return "IPI_ISI"
                                                    else:
                                                        # if Nest_Mask_IoU <= 0.9937746525
                                                        if _get(features, "Nest_Mask_IoU") <= 0.9937746525:
                                                            return "OTHER4"
                                                        else:
                                                            # if Nest_Dist_RL_To_Bbox_TR <= 683.3321228027
                                                            if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 683.3321228027:
                                                                return "IPI_ISI"
                                                            else:
                                                                return "OTHER4"
                                        else:
                                            # if Nest_Centroid_To_Bbox_BL <= 376.7652893066
                                            if _get(features, "Nest_Centroid_To_Bbox_BL") <= 376.7652893066:
                                                # if Nest_Dist_RR_RB <= 289.9333496094
                                                if _get(features, "Nest_Dist_RR_RB") <= 289.9333496094:
                                                    return "OTHER4"
                                                else:
                                                    # if Actor_To_Nest_Distance <= 190.8701629639
                                                    if _get(features, "Actor_To_Nest_Distance") <= 190.8701629639:
                                                        # if c2_Nest_Distance <= 307.2740325928
                                                        if _get(features, "c2_Nest_Distance") <= 307.2740325928:
                                                            # if Nest_Mask_IoU <= 0.9211857915
                                                            if _get(features, "Nest_Mask_IoU") <= 0.9211857915:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                        else:
                                                            return "OTHER4"
                                                    else:
                                                        return "OTHER4"
                                            else:
                                                # if Nest_Centroid_To_Bbox_TL <= 387.0949707031
                                                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 387.0949707031:
                                                    return "IPI_ISI"
                                                else:
                                                    # if Actor_bbox_h <= 28.0000000000
                                                    if _get(features, "Actor_bbox_h") <= 28.0000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        # if Actor_Dist_RR_To_Bbox_BR <= 7.5666627884
                                                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 7.5666627884:
                                                            # if Nest_Mask_IoU <= 0.9774040282
                                                            if _get(features, "Nest_Mask_IoU") <= 0.9774040282:
                                                                return "IPI_ISI"
                                                            else:
                                                                return "OTHER4"
                                                        else:
                                                            return "OTHER4"
                                    else:
                                        # if c1_Nest_Distance <= 601.8191528320
                                        if _get(features, "c1_Nest_Distance") <= 601.8191528320:
                                            # if c4_Mouse_Distance <= 442.1134796143
                                            if _get(features, "c4_Mouse_Distance") <= 442.1134796143:
                                                # if Nest_RL_y <= 678.5000000000
                                                if _get(features, "Nest_RL_y") <= 678.5000000000:
                                                    return "OTHER4"
                                                else:
                                                    return "IPI_ISI"
                                            else:
                                                return "OTHER4"
                                        else:
                                            # if Actor_Direction_deg <= 179.7660369873
                                            if _get(features, "Actor_Direction_deg") <= 179.7660369873:
                                                # if Actor_To_Nest_Distance <= 31.6595344543
                                                if _get(features, "Actor_To_Nest_Distance") <= 31.6595344543:
                                                    # if Actor_Dist_RB_To_Bbox_TR <= 172.9724655151
                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 172.9724655151:
                                                        return "OTHER4"
                                                    else:
                                                        return "IPI_ISI"
                                                else:
                                                    # if Nest_RL_x <= 346.5000000000
                                                    if _get(features, "Nest_RL_x") <= 346.5000000000:
                                                        # if Nest_Dist_RB_To_Bbox_TR <= 736.4010314941
                                                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 736.4010314941:
                                                            # if Actor_Dist_RL_RT <= 1.8251407743
                                                            if _get(features, "Actor_Dist_RL_RT") <= 1.8251407743:
                                                                # if Actor_area <= 6026.5000000000
                                                                if _get(features, "Actor_area") <= 6026.5000000000:
                                                                    return "OTHER4"
                                                                else:
                                                                    return "IPI_ISI"
                                                            else:
                                                                # if Actor_To_Nest_Dist_Change <= 49.4222354889
                                                                if _get(features, "Actor_To_Nest_Dist_Change") <= 49.4222354889:
                                                                    return "OTHER4"
                                                                else:
                                                                    # if Actor_To_Nest_Dist_Change <= 49.4788608551
                                                                    if _get(features, "Actor_To_Nest_Dist_Change") <= 49.4788608551:
                                                                        return "IPI_ISI"
                                                                    else:
                                                                        return "OTHER4"
                                                        else:
                                                            # if Nest_Dist_RR_To_Bbox_TL <= 894.6095886230
                                                            if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 894.6095886230:
                                                                return "IPI_ISI"
                                                            else:
                                                                return "OTHER4"
                                                    else:
                                                        # if Nest_Dist_RB_To_Bbox_BL <= 397.5012512207
                                                        if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 397.5012512207:
                                                            return "OTHER4"
                                                        else:
                                                            # if Nest_solidity <= 0.8613486886
                                                            if _get(features, "Nest_solidity") <= 0.8613486886:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                            else:
                                                # if Actor_hu_2 <= 0.0030187946
                                                if _get(features, "Actor_hu_2") <= 0.0030187946:
                                                    return "OTHER4"
                                                else:
                                                    return "IPI_ISI"
                            else:
                                # if Nest_Centroid_To_Bbox_BL <= 437.3295898438
                                if _get(features, "Nest_Centroid_To_Bbox_BL") <= 437.3295898438:
                                    # if Nest_hu_5 <= -0.0000063500
                                    if _get(features, "Nest_hu_5") <= -0.0000063500:
                                        # if Nest_bbox_h <= 292.0000000000
                                        if _get(features, "Nest_bbox_h") <= 292.0000000000:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                    else:
                                        # if Nest_extent <= 0.8011789620
                                        if _get(features, "Nest_extent") <= 0.8011789620:
                                            return "OTHER4"
                                        else:
                                            return "IPI_ISI"
                                else:
                                    # if foodhopperMid_Nest_Distance <= 426.5288085938
                                    if _get(features, "foodhopperMid_Nest_Distance") <= 426.5288085938:
                                        # if Actor_hu_1 <= 0.0035011180
                                        if _get(features, "Actor_hu_1") <= 0.0035011180:
                                            return "OTHER4"
                                        else:
                                            # if Nest_hu_1 <= 0.0635258518
                                            if _get(features, "Nest_hu_1") <= 0.0635258518:
                                                return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                    else:
                        # if Actor_Dist_RB_RL <= 27.2988471985
                        if _get(features, "Actor_Dist_RB_RL") <= 27.2988471985:
                            # if Nest_Centroid_To_Bbox_BR <= 364.7868957520
                            if _get(features, "Nest_Centroid_To_Bbox_BR") <= 364.7868957520:
                                return "OTHER4"
                            else:
                                # if foodhopperBottom_Mouse_Distance <= 548.9036865234
                                if _get(features, "foodhopperBottom_Mouse_Distance") <= 548.9036865234:
                                    # if c1_Mouse_Distance <= 780.6715698242
                                    if _get(features, "c1_Mouse_Distance") <= 780.6715698242:
                                        return "OTHER4"
                                    else:
                                        # if Nest_Mask_IoU <= 0.9481388330
                                        if _get(features, "Nest_Mask_IoU") <= 0.9481388330:
                                            # if Actor_Dist_RB_RL <= 15.7115740776
                                            if _get(features, "Actor_Dist_RB_RL") <= 15.7115740776:
                                                return "IPI_ISI"
                                            else:
                                                return "OTHER4"
                                        else:
                                            return "IPI_ISI"
                                else:
                                    return "OTHER4"
                        else:
                            # if Nest_RT_y <= 591.0000000000
                            if _get(features, "Nest_RT_y") <= 591.0000000000:
                                # if Nest_solidity <= 0.9193887115
                                if _get(features, "Nest_solidity") <= 0.9193887115:
                                    # if Actor_centroid_y <= 805.7102355957
                                    if _get(features, "Actor_centroid_y") <= 805.7102355957:
                                        return "IPI_ISI"
                                    else:
                                        # if Actor_Dist_RB_To_Bbox_TL <= 59.9716281891
                                        if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 59.9716281891:
                                            # if Nest_Dist_RL_RR <= 676.6692810059
                                            if _get(features, "Nest_Dist_RL_RR") <= 676.6692810059:
                                                return "IPI_ISI"
                                            else:
                                                return "OTHER4"
                                        else:
                                            return "OTHER4"
                                else:
                                    # if Nest_Dist_RB_To_Bbox_BL <= 236.5021133423
                                    if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 236.5021133423:
                                        # if Nest_Dist_RT_To_Bbox_BR <= 512.4838562012
                                        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 512.4838562012:
                                            return "OTHER4"
                                        else:
                                            return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                            else:
                                # if foodhopperRight_Nest_Distance <= 599.2819213867
                                if _get(features, "foodhopperRight_Nest_Distance") <= 599.2819213867:
                                    # if Nest_hu_1 <= 0.0964906998
                                    if _get(features, "Nest_hu_1") <= 0.0964906998:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                                else:
                                    return "OTHER4"
            else:
                # if Nest_Dist_RT_To_Bbox_BR <= 356.1215362549
                if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 356.1215362549:
                    # if Nest_Area_Diff_Abs <= 8518.7500000000
                    if _get(features, "Nest_Area_Diff_Abs") <= 8518.7500000000:
                        # if Actor_bbox_w <= 335.0000000000
                        if _get(features, "Actor_bbox_w") <= 335.0000000000:
                            # if Nest_Dist_RB_To_Bbox_TR <= 349.0669097900
                            if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 349.0669097900:
                                return "IPI_ISI"
                            else:
                                # if Nest_Dist_RB_To_Bbox_BR <= 157.0031890869
                                if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 157.0031890869:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                        else:
                            return "OTHER4"
                    else:
                        return "OTHER4"
                else:
                    return "OTHER4"
        else:
            return "IPI_ISI"

# --- OTHER4 tree ---
def other4_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Nest_Mask_IoU <= 0.9880100489
    if _get(features, "Nest_Mask_IoU") <= 0.9880100489:
        # if Nest_RB_y <= 898.5000000000
        if _get(features, "Nest_RB_y") <= 898.5000000000:
            # if Nest_hu_0 <= 0.2367037758
            if _get(features, "Nest_hu_0") <= 0.2367037758:
                # if Nest_Dist_RL_To_Bbox_TL <= 217.5000000000
                if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 217.5000000000:
                    # if c1_Mouse_Distance <= 568.2575683594
                    if _get(features, "c1_Mouse_Distance") <= 568.2575683594:
                        return "ONE"
                    else:
                        # if Actor_To_Nest_Distance <= 84.8469696045
                        if _get(features, "Actor_To_Nest_Distance") <= 84.8469696045:
                            return "ONE"
                        else:
                            # if Nest_Dist_RB_RL <= 180.6655883789
                            if _get(features, "Nest_Dist_RB_RL") <= 180.6655883789:
                                return "ONE"
                            else:
                                # if Actor_Dist_RT_To_Bbox_TL <= 323.0000000000
                                if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 323.0000000000:
                                    return "INB"
                                else:
                                    # if Actor_Dist_RB_RL <= 397.1942443848
                                    if _get(features, "Actor_Dist_RB_RL") <= 397.1942443848:
                                        return "INB"
                                    else:
                                        return "ONE"
                else:
                    # if Nest_hu_2 <= 0.0004707365
                    if _get(features, "Nest_hu_2") <= 0.0004707365:
                        # if Actor_RR_y <= 904.5000000000
                        if _get(features, "Actor_RR_y") <= 904.5000000000:
                            # if Actor_Dist_RB_To_Bbox_BR <= 222.0022583008
                            if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 222.0022583008:
                                # if Actor_Direction_deg <= -170.4517822266
                                if _get(features, "Actor_Direction_deg") <= -170.4517822266:
                                    # if Actor_Dist_RL_To_Bbox_BL <= 107.0000000000
                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 107.0000000000:
                                        return "ONE"
                                    else:
                                        return "INB"
                                else:
                                    return "INB"
                            else:
                                return "ONE"
                        else:
                            return "ONE"
                    else:
                        # if Nest_Dist_RL_RR <= 345.3687591553
                        if _get(features, "Nest_Dist_RL_RR") <= 345.3687591553:
                            return "INB"
                        else:
                            return "ONE"
            else:
                # if Nest_RT_y <= 606.5000000000
                if _get(features, "Nest_RT_y") <= 606.5000000000:
                    # if Nest_Centroid_To_Bbox_TR <= 282.5733337402
                    if _get(features, "Nest_Centroid_To_Bbox_TR") <= 282.5733337402:
                        return "INB"
                    else:
                        # if foodhopperRight_Mouse_Distance <= 725.9006347656
                        if _get(features, "foodhopperRight_Mouse_Distance") <= 725.9006347656:
                            # if Nest_area <= 157240.0000000000
                            if _get(features, "Nest_area") <= 157240.0000000000:
                                # if Nest_RL_x <= 368.0000000000
                                if _get(features, "Nest_RL_x") <= 368.0000000000:
                                    # if foodhopperBottom_Nest_Distance <= 435.2605590820
                                    if _get(features, "foodhopperBottom_Nest_Distance") <= 435.2605590820:
                                        # if c3_Mouse_Distance <= 1007.5460815430
                                        if _get(features, "c3_Mouse_Distance") <= 1007.5460815430:
                                            # if Nest_RB_y <= 897.5000000000
                                            if _get(features, "Nest_RB_y") <= 897.5000000000:
                                                return "ONE"
                                            else:
                                                # if Actor_Centroid_To_Bbox_BL <= 129.2937774658
                                                if _get(features, "Actor_Centroid_To_Bbox_BL") <= 129.2937774658:
                                                    return "INB"
                                                else:
                                                    return "ONE"
                                        else:
                                            # if Actor_Dist_RR_RB <= 12.5316984653
                                            if _get(features, "Actor_Dist_RR_RB") <= 12.5316984653:
                                                return "ONE"
                                            else:
                                                return "INB"
                                    else:
                                        # if Actor_Dist_RL_To_Bbox_TL <= 110.0000000000
                                        if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 110.0000000000:
                                            return "INB"
                                        else:
                                            return "ONE"
                                else:
                                    # if Actor_eccentricity <= 0.8976081610
                                    if _get(features, "Actor_eccentricity") <= 0.8976081610:
                                        return "INB"
                                    else:
                                        return "ONE"
                            else:
                                return "INB"
                        else:
                            # if Actor_Centroid_To_Bbox_BR <= 127.7906074524
                            if _get(features, "Actor_Centroid_To_Bbox_BR") <= 127.7906074524:
                                return "INB"
                            else:
                                return "ONE"
                else:
                    # if Actor_hu_2 <= 0.0001974690
                    if _get(features, "Actor_hu_2") <= 0.0001974690:
                        return "ONE"
                    else:
                        # if foodhopperRight_Mouse_Distance <= 112.7715110779
                        if _get(features, "foodhopperRight_Mouse_Distance") <= 112.7715110779:
                            return "ONE"
                        else:
                            return "INB"
        else:
            # if c4_Mouse_Distance <= 624.0421142578
            if _get(features, "c4_Mouse_Distance") <= 624.0421142578:
                # if Nest_area <= 167656.0000000000
                if _get(features, "Nest_area") <= 167656.0000000000:
                    # if Nest_Dist_RB_To_Bbox_BL <= 302.5016479492
                    if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 302.5016479492:
                        # if Actor_Dist_RT_RB <= 567.8168334961
                        if _get(features, "Actor_Dist_RT_RB") <= 567.8168334961:
                            # if Nest_RT_x <= 348.5000000000
                            if _get(features, "Nest_RT_x") <= 348.5000000000:
                                # if Nest_Dist_RL_To_Bbox_BL <= 209.0000000000
                                if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 209.0000000000:
                                    # if Nest_RT_x <= 338.5000000000
                                    if _get(features, "Nest_RT_x") <= 338.5000000000:
                                        return "ONE"
                                    else:
                                        return "INB"
                                else:
                                    # if c3_Nest_Distance <= 908.8770141602
                                    if _get(features, "c3_Nest_Distance") <= 908.8770141602:
                                        return "INB"
                                    else:
                                        # if c1_Mouse_Distance <= 716.8008117676
                                        if _get(features, "c1_Mouse_Distance") <= 716.8008117676:
                                            return "ONE"
                                        else:
                                            return "INB"
                            else:
                                # if foodhopperMid_Mouse_Distance <= 297.3259735107
                                if _get(features, "foodhopperMid_Mouse_Distance") <= 297.3259735107:
                                    # if Actor_RT_y <= 638.5000000000
                                    if _get(features, "Actor_RT_y") <= 638.5000000000:
                                        # if Nest_Dist_RR_RB <= 271.1640472412
                                        if _get(features, "Nest_Dist_RR_RB") <= 271.1640472412:
                                            return "ONE"
                                        else:
                                            # if Actor_RT_x <= 863.5000000000
                                            if _get(features, "Actor_RT_x") <= 863.5000000000:
                                                # if Nest_solidity <= 0.9411504865
                                                if _get(features, "Nest_solidity") <= 0.9411504865:
                                                    # if Actor_Area_Diff_Abs <= 427.5000000000
                                                    if _get(features, "Actor_Area_Diff_Abs") <= 427.5000000000:
                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    return "ONE"
                                            else:
                                                return "ONE"
                                    else:
                                        # if Actor_extent <= 0.7435173690
                                        if _get(features, "Actor_extent") <= 0.7435173690:
                                            return "ONE"
                                        else:
                                            # if foodhopperLeft_Nest_Distance <= 166.1117858887
                                            if _get(features, "foodhopperLeft_Nest_Distance") <= 166.1117858887:
                                                return "OE"
                                            else:
                                                return "INB"
                                else:
                                    # if Nest_bbox_x <= 289.5000000000
                                    if _get(features, "Nest_bbox_x") <= 289.5000000000:
                                        # if foodhopperRight_Mouse_Distance <= 692.3497619629
                                        if _get(features, "foodhopperRight_Mouse_Distance") <= 692.3497619629:
                                            # if Nest_Dist_RL_To_Bbox_BL <= 328.0000000000
                                            if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 328.0000000000:
                                                # if Nest_extent <= 0.5081437528
                                                if _get(features, "Nest_extent") <= 0.5081437528:
                                                    # if Actor_solidity <= 0.8610863388
                                                    if _get(features, "Actor_solidity") <= 0.8610863388:
                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    return "INB"
                                            else:
                                                # if Actor_RL_y <= 676.5000000000
                                                if _get(features, "Actor_RL_y") <= 676.5000000000:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                        else:
                                            # if Actor_bbox_x <= 364.5000000000
                                            if _get(features, "Actor_bbox_x") <= 364.5000000000:
                                                return "INB"
                                            else:
                                                return "ONE"
                                    else:
                                        # if Nest_extent <= 0.7459943295
                                        if _get(features, "Nest_extent") <= 0.7459943295:
                                            # if Nest_RR_y <= 566.0000000000
                                            if _get(features, "Nest_RR_y") <= 566.0000000000:
                                                return "ONE"
                                            else:
                                                # if Nest_eccentricity <= 0.4446214139
                                                if _get(features, "Nest_eccentricity") <= 0.4446214139:
                                                    # if Nest_Dist_RT_RB <= 420.3885192871
                                                    if _get(features, "Nest_Dist_RT_RB") <= 420.3885192871:
                                                        return "INB"
                                                    else:
                                                        # if Nest_Dist_RR_RB <= 315.9193725586
                                                        if _get(features, "Nest_Dist_RR_RB") <= 315.9193725586:
                                                            return "ONE"
                                                        else:
                                                            return "INB"
                                                else:
                                                    # if Nest_Dist_RR_To_Bbox_BR <= 5.5908911228
                                                    if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 5.5908911228:
                                                        return "ONE"
                                                    else:
                                                        # if Nest_Dist_RT_To_Bbox_TR <= 673.5000000000
                                                        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 673.5000000000:
                                                            # if Nest_perimeter <= 2555.6307373047
                                                            if _get(features, "Nest_perimeter") <= 2555.6307373047:
                                                                # if Nest_solidity <= 0.9330063462
                                                                if _get(features, "Nest_solidity") <= 0.9330063462:
                                                                    # if Actor_Centroid_To_Bbox_TL <= 382.3980560303
                                                                    if _get(features, "Actor_Centroid_To_Bbox_TL") <= 382.3980560303:
                                                                        # if Actor_eccentricity <= 0.4760665298
                                                                        if _get(features, "Actor_eccentricity") <= 0.4760665298:
                                                                            # if Nest_hu_1 <= 0.0748545043
                                                                            if _get(features, "Nest_hu_1") <= 0.0748545043:
                                                                                # if Nest_perimeter <= 2487.5545654297
                                                                                if _get(features, "Nest_perimeter") <= 2487.5545654297:
                                                                                    # if Nest_Dist_RB_To_Bbox_TL <= 539.8815917969
                                                                                    if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 539.8815917969:
                                                                                        return "INB"
                                                                                    else:
                                                                                        return "ONE"
                                                                                else:
                                                                                    return "ONE"
                                                                            else:
                                                                                # if Nest_hu_3 <= 0.0020482750
                                                                                if _get(features, "Nest_hu_3") <= 0.0020482750:
                                                                                    return "ONE"
                                                                                else:
                                                                                    return "INB"
                                                                        else:
                                                                            # if Actor_Dist_RL_To_Bbox_TR <= 67.2419853210
                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 67.2419853210:
                                                                                # if Actor_RB_x <= 756.5000000000
                                                                                if _get(features, "Actor_RB_x") <= 756.5000000000:
                                                                                    return "INB"
                                                                                else:
                                                                                    return "ONE"
                                                                            else:
                                                                                # if Nest_hu_4 <= -0.0000009110
                                                                                if _get(features, "Nest_hu_4") <= -0.0000009110:
                                                                                    # if Actor_Dist_RT_RB <= 364.4582977295
                                                                                    if _get(features, "Actor_Dist_RT_RB") <= 364.4582977295:
                                                                                        return "INB"
                                                                                    else:
                                                                                        return "ONE"
                                                                                else:
                                                                                    # if Actor_orientation <= 1.7651435137
                                                                                    if _get(features, "Actor_orientation") <= 1.7651435137:
                                                                                        # if Actor_Dist_RT_To_Bbox_TL <= 40.5000000000
                                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 40.5000000000:
                                                                                            return "ONE"
                                                                                        else:
                                                                                            return "INB"
                                                                                    else:
                                                                                        # if Actor_hu_0 <= 0.1667646170
                                                                                        if _get(features, "Actor_hu_0") <= 0.1667646170:
                                                                                            # if Nest_hu_1 <= 0.0758567005
                                                                                            if _get(features, "Nest_hu_1") <= 0.0758567005:
                                                                                                return "INB"
                                                                                            else:
                                                                                                return "ONE"
                                                                                        else:
                                                                                            return "INB"
                                                                    else:
                                                                        # if Actor_bbox_w <= 701.5000000000
                                                                        if _get(features, "Actor_bbox_w") <= 701.5000000000:
                                                                            return "ONE"
                                                                        else:
                                                                            return "INB"
                                                                else:
                                                                    # if Nest_hu_2 <= 0.0000975500
                                                                    if _get(features, "Nest_hu_2") <= 0.0000975500:
                                                                        # if Actor_orientation <= 176.2449722290
                                                                        if _get(features, "Actor_orientation") <= 176.2449722290:
                                                                            return "ONE"
                                                                        else:
                                                                            return "INB"
                                                                    else:
                                                                        # if Nest_centroid_x <= 492.4272460938
                                                                        if _get(features, "Nest_centroid_x") <= 492.4272460938:
                                                                            return "ONE"
                                                                        else:
                                                                            return "INB"
                                                            else:
                                                                # if Actor_RB_x <= 487.5000000000
                                                                if _get(features, "Actor_RB_x") <= 487.5000000000:
                                                                    # if Nest_Dist_RT_RR <= 314.3383178711
                                                                    if _get(features, "Nest_Dist_RT_RR") <= 314.3383178711:
                                                                        return "INB"
                                                                    else:
                                                                        return "ONE"
                                                                else:
                                                                    return "INB"
                                                        else:
                                                            return "ONE"
                                        else:
                                            # if Nest_hu_5 <= 0.0000033550
                                            if _get(features, "Nest_hu_5") <= 0.0000033550:
                                                # if Actor_aspect_ratio <= 2.8324786425
                                                if _get(features, "Actor_aspect_ratio") <= 2.8324786425:
                                                    return "INB"
                                                else:
                                                    return "ONE"
                                            else:
                                                return "ONE"
                        else:
                            # if c4_Nest_Distance <= 284.1097412109
                            if _get(features, "c4_Nest_Distance") <= 284.1097412109:
                                return "ONE"
                            else:
                                return "INB"
                    else:
                        # if Nest_Dist_RB_To_Bbox_BR <= 425.5011749268
                        if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 425.5011749268:
                            # if Actor_RB_y <= 791.5000000000
                            if _get(features, "Actor_RB_y") <= 791.5000000000:
                                # if Nest_Dist_RB_To_Bbox_BR <= 301.5016479492
                                if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 301.5016479492:
                                    # if Actor_Dist_RL_To_Bbox_BL <= 82.5000000000
                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 82.5000000000:
                                        # if Nest_Dist_RB_To_Bbox_TR <= 301.7268066406
                                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 301.7268066406:
                                            return "INB"
                                        else:
                                            # if c1_Nest_Distance <= 704.8817749023
                                            if _get(features, "c1_Nest_Distance") <= 704.8817749023:
                                                # if Actor_Dist_RB_RL <= 234.0320663452
                                                if _get(features, "Actor_Dist_RB_RL") <= 234.0320663452:
                                                    # if c1_Mouse_Distance <= 553.4301452637
                                                    if _get(features, "c1_Mouse_Distance") <= 553.4301452637:
                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    return "ONE"
                                            else:
                                                # if foodhopperBottom_Mouse_Distance <= 281.4899291992
                                                if _get(features, "foodhopperBottom_Mouse_Distance") <= 281.4899291992:
                                                    return "INB"
                                                else:
                                                    # if foodhopperMid_Nest_Distance <= 507.3903198242
                                                    if _get(features, "foodhopperMid_Nest_Distance") <= 507.3903198242:
                                                        # if Nest_Dist_RL_To_Bbox_BL <= 116.0000000000
                                                        if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 116.0000000000:
                                                            return "INB"
                                                        else:
                                                            # if Nest_Mask_IoU <= 0.8340489566
                                                            if _get(features, "Nest_Mask_IoU") <= 0.8340489566:
                                                                # if Nest_Dist_RB_RL <= 370.9829711914
                                                                if _get(features, "Nest_Dist_RB_RL") <= 370.9829711914:
                                                                    return "ONE"
                                                                else:
                                                                    return "INB"
                                                            else:
                                                                # if Actor_bbox_y <= 652.5000000000
                                                                if _get(features, "Actor_bbox_y") <= 652.5000000000:
                                                                    # if Actor_RB_x <= 779.5000000000
                                                                    if _get(features, "Actor_RB_x") <= 779.5000000000:
                                                                        return "ONE"
                                                                    else:
                                                                        # if Nest_Dist_RL_To_Bbox_TL <= 255.5000000000
                                                                        if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 255.5000000000:
                                                                            # if Nest_RL_y <= 710.0000000000
                                                                            if _get(features, "Nest_RL_y") <= 710.0000000000:
                                                                                return "OE"
                                                                            else:
                                                                                # if Nest_Dist_RB_To_Bbox_TR <= 313.0827636719
                                                                                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 313.0827636719:
                                                                                    return "INB"
                                                                                else:
                                                                                    return "ONE"
                                                                        else:
                                                                            return "INB"
                                                                else:
                                                                    # if Nest_solidity <= 0.8823466897
                                                                    if _get(features, "Nest_solidity") <= 0.8823466897:
                                                                        # if Actor_eccentricity <= 0.6973129809
                                                                        if _get(features, "Actor_eccentricity") <= 0.6973129809:
                                                                            return "OE"
                                                                        else:
                                                                            return "INB"
                                                                    else:
                                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                    else:
                                        # if Nest_hu_5 <= -0.0000077000
                                        if _get(features, "Nest_hu_5") <= -0.0000077000:
                                            # if Actor_Dist_RT_To_Bbox_BL <= 278.0133972168
                                            if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 278.0133972168:
                                                return "ONE"
                                            else:
                                                return "INB"
                                        else:
                                            # if Nest_extent <= 0.7260734737
                                            if _get(features, "Nest_extent") <= 0.7260734737:
                                                # if foodhopperMid_Mouse_Distance <= 298.0730285645
                                                if _get(features, "foodhopperMid_Mouse_Distance") <= 298.0730285645:
                                                    # if foodhopperMid_Nest_Distance <= 487.8368530273
                                                    if _get(features, "foodhopperMid_Nest_Distance") <= 487.8368530273:
                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    # if Actor_Dist_RB_To_Bbox_BL <= 31.0195598602
                                                    if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 31.0195598602:
                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                            else:
                                                # if Actor_Dist_RR_To_Bbox_BR <= 152.5032806396
                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 152.5032806396:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                else:
                                    # if Nest_RB_y <= 965.5000000000
                                    if _get(features, "Nest_RB_y") <= 965.5000000000:
                                        # if Nest_Centroid_To_Bbox_BL <= 318.8241577148
                                        if _get(features, "Nest_Centroid_To_Bbox_BL") <= 318.8241577148:
                                            # if Nest_extent <= 0.5069653094
                                            if _get(features, "Nest_extent") <= 0.5069653094:
                                                return "ONE"
                                            else:
                                                return "INB"
                                        else:
                                            # if Nest_Centroid_To_Bbox_BR <= 438.5373992920
                                            if _get(features, "Nest_Centroid_To_Bbox_BR") <= 438.5373992920:
                                                # if Nest_Dist_RB_To_Bbox_TR <= 410.8869628906
                                                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 410.8869628906:
                                                    # if foodhopperLeft_Mouse_Distance <= 102.5293579102
                                                    if _get(features, "foodhopperLeft_Mouse_Distance") <= 102.5293579102:
                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    # if Nest_Dist_RB_To_Bbox_TL <= 558.2590942383
                                                    if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 558.2590942383:
                                                        # if Nest_hu_5 <= -0.0000151000
                                                        if _get(features, "Nest_hu_5") <= -0.0000151000:
                                                            # if Nest_Dist_RB_To_Bbox_BR <= 324.5015411377
                                                            if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 324.5015411377:
                                                                return "ONE"
                                                            else:
                                                                return "INB"
                                                        else:
                                                            # if Actor_Dist_RT_RR <= 20.4729022980
                                                            if _get(features, "Actor_Dist_RT_RR") <= 20.4729022980:
                                                                # if Actor_extent <= 0.4054578394
                                                                if _get(features, "Actor_extent") <= 0.4054578394:
                                                                    return "INB"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                # if Actor_Dist_RB_To_Bbox_BL <= 312.0016174316
                                                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 312.0016174316:
                                                                    return "INB"
                                                                else:
                                                                    # if Actor_RT_x <= 615.5000000000
                                                                    if _get(features, "Actor_RT_x") <= 615.5000000000:
                                                                        return "ONE"
                                                                    else:
                                                                        return "INB"
                                                    else:
                                                        # if Nest_orientation <= 97.4199714661
                                                        if _get(features, "Nest_orientation") <= 97.4199714661:
                                                            return "ONE"
                                                        else:
                                                            return "INB"
                                            else:
                                                # if Nest_bbox_x <= 311.5000000000
                                                if _get(features, "Nest_bbox_x") <= 311.5000000000:
                                                    return "INB"
                                                else:
                                                    return "ONE"
                                    else:
                                        # if Nest_Dist_RB_To_Bbox_TR <= 487.1865539551
                                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 487.1865539551:
                                            return "INB"
                                        else:
                                            # if Nest_aspect_ratio <= 1.9349969625
                                            if _get(features, "Nest_aspect_ratio") <= 1.9349969625:
                                                # if Nest_RL_x <= 366.5000000000
                                                if _get(features, "Nest_RL_x") <= 366.5000000000:
                                                    return "INB"
                                                else:
                                                    return "ONE"
                                            else:
                                                # if Actor_RT_x <= 546.0000000000
                                                if _get(features, "Actor_RT_x") <= 546.0000000000:
                                                    return "INB"
                                                else:
                                                    return "ONE"
                            else:
                                # if Actor_Dist_RB_To_Bbox_TL <= 103.3376846313
                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 103.3376846313:
                                    # if Nest_bbox_y <= 532.5000000000
                                    if _get(features, "Nest_bbox_y") <= 532.5000000000:
                                        return "INB"
                                    else:
                                        return "ONE"
                                else:
                                    # if Nest_Dist_RR_RB <= 424.7084197998
                                    if _get(features, "Nest_Dist_RR_RB") <= 424.7084197998:
                                        # if Nest_extent <= 0.7347203493
                                        if _get(features, "Nest_extent") <= 0.7347203493:
                                            # if Actor_RB_x <= 473.5000000000
                                            if _get(features, "Actor_RB_x") <= 473.5000000000:
                                                # if foodhopperRight_Nest_Distance <= 522.9979858398
                                                if _get(features, "foodhopperRight_Nest_Distance") <= 522.9979858398:
                                                    return "INB"
                                                else:
                                                    # if Actor_Dist_RT_To_Bbox_BR <= 279.6314392090
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 279.6314392090:
                                                        return "INB"
                                                    else:
                                                        return "ONE"
                                            else:
                                                # if Nest_Dist_RT_To_Bbox_BL <= 292.4833068848
                                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 292.4833068848:
                                                    # if Actor_Dist_RL_To_Bbox_BR <= 547.3003540039
                                                    if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 547.3003540039:
                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    # if foodhopperLeft_Nest_Distance <= 118.8082008362
                                                    if _get(features, "foodhopperLeft_Nest_Distance") <= 118.8082008362:
                                                        # if foodhopperMid_Mouse_Distance <= 373.0508270264
                                                        if _get(features, "foodhopperMid_Mouse_Distance") <= 373.0508270264:
                                                            # if foodhopperRight_Mouse_Distance <= 479.3395538330
                                                            if _get(features, "foodhopperRight_Mouse_Distance") <= 479.3395538330:
                                                                return "INB"
                                                            else:
                                                                return "ONE"
                                                        else:
                                                            return "INB"
                                                    else:
                                                        # if foodhopperMid_Mouse_Distance <= 266.5982666016
                                                        if _get(features, "foodhopperMid_Mouse_Distance") <= 266.5982666016:
                                                            return "ONE"
                                                        else:
                                                            # if Actor_Dist_RR_RB <= 492.3885650635
                                                            if _get(features, "Actor_Dist_RR_RB") <= 492.3885650635:
                                                                # if Nest_hu_4 <= -0.0000013250
                                                                if _get(features, "Nest_hu_4") <= -0.0000013250:
                                                                    # if Nest_Dist_RB_RL <= 370.3799438477
                                                                    if _get(features, "Nest_Dist_RB_RL") <= 370.3799438477:
                                                                        return "ONE"
                                                                    else:
                                                                        return "INB"
                                                                else:
                                                                    # if Actor_Area_Diff_Abs <= 30.7500000000
                                                                    if _get(features, "Actor_Area_Diff_Abs") <= 30.7500000000:
                                                                        # if Actor_hu_1 <= 0.0474100751
                                                                        if _get(features, "Actor_hu_1") <= 0.0474100751:
                                                                            return "INB"
                                                                        else:
                                                                            return "ONE"
                                                                    else:
                                                                        # if Actor_RR_x <= 1098.5000000000
                                                                        if _get(features, "Actor_RR_x") <= 1098.5000000000:
                                                                            # if Nest_extent <= 0.6979467273
                                                                            if _get(features, "Nest_extent") <= 0.6979467273:
                                                                                # if Nest_Dist_RT_To_Bbox_BR <= 329.2965545654
                                                                                if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 329.2965545654:
                                                                                    # if Nest_Dist_RR_To_Bbox_TL <= 586.8406982422
                                                                                    if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 586.8406982422:
                                                                                        return "ONE"
                                                                                    else:
                                                                                        return "INB"
                                                                                else:
                                                                                    return "INB"
                                                                            else:
                                                                                # if c2_Nest_Distance <= 330.8166351318
                                                                                if _get(features, "c2_Nest_Distance") <= 330.8166351318:
                                                                                    return "INB"
                                                                                else:
                                                                                    return "ONE"
                                                                        else:
                                                                            # if Actor_bbox_h <= 315.0000000000
                                                                            if _get(features, "Actor_bbox_h") <= 315.0000000000:
                                                                                return "ONE"
                                                                            else:
                                                                                return "INB"
                                                            else:
                                                                # if foodhopperRight_Nest_Distance <= 638.9163818359
                                                                if _get(features, "foodhopperRight_Nest_Distance") <= 638.9163818359:
                                                                    return "ONE"
                                                                else:
                                                                    return "INB"
                                        else:
                                            return "ONE"
                                    else:
                                        # if foodhopperMid_Nest_Distance <= 424.2384643555
                                        if _get(features, "foodhopperMid_Nest_Distance") <= 424.2384643555:
                                            # if foodhopperRight_Nest_Distance <= 470.7655639648
                                            if _get(features, "foodhopperRight_Nest_Distance") <= 470.7655639648:
                                                # if Nest_Centroid_To_Bbox_TL <= 452.4559936523
                                                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 452.4559936523:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                            else:
                                                # if Nest_RT_x <= 649.5000000000
                                                if _get(features, "Nest_RT_x") <= 649.5000000000:
                                                    return "INB"
                                                else:
                                                    # if Nest_Dist_RL_To_Bbox_BR <= 731.7349548340
                                                    if _get(features, "Nest_Dist_RL_To_Bbox_BR") <= 731.7349548340:
                                                        return "INB"
                                                    else:
                                                        # if Nest_Dist_RL_To_Bbox_TR <= 818.4975585938
                                                        if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 818.4975585938:
                                                            # if c4_Nest_Distance <= 468.8006744385
                                                            if _get(features, "c4_Nest_Distance") <= 468.8006744385:
                                                                return "ONE"
                                                            else:
                                                                # if Nest_Dist_RT_To_Bbox_BL <= 515.0705566406
                                                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 515.0705566406:
                                                                    return "INB"
                                                                else:
                                                                    return "ONE"
                                                        else:
                                                            return "INB"
                                        else:
                                            return "INB"
                        else:
                            # if Nest_bbox_x <= 315.5000000000
                            if _get(features, "Nest_bbox_x") <= 315.5000000000:
                                # if Actor_perimeter <= 1099.3889160156
                                if _get(features, "Actor_perimeter") <= 1099.3889160156:
                                    return "INB"
                                else:
                                    return "ONE"
                            else:
                                # if Nest_centroid_y <= 806.5607604980
                                if _get(features, "Nest_centroid_y") <= 806.5607604980:
                                    # if Actor_solidity <= 0.9176737666
                                    if _get(features, "Actor_solidity") <= 0.9176737666:
                                        return "ONE"
                                    else:
                                        return "INB"
                                else:
                                    return "INB"
                else:
                    # if Actor_RL_y <= 563.5000000000
                    if _get(features, "Actor_RL_y") <= 563.5000000000:
                        # if foodhopperBottom_Nest_Distance <= 375.4570465088
                        if _get(features, "foodhopperBottom_Nest_Distance") <= 375.4570465088:
                            return "INB"
                        else:
                            # if Actor_aspect_ratio <= 2.1963766813
                            if _get(features, "Actor_aspect_ratio") <= 2.1963766813:
                                # if Actor_To_Nest_Dist_Change <= 78.5123558044
                                if _get(features, "Actor_To_Nest_Dist_Change") <= 78.5123558044:
                                    return "ONE"
                                else:
                                    return "INB"
                            else:
                                return "INB"
                    else:
                        # if Nest_Dist_RR_To_Bbox_TR <= 174.5028610229
                        if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 174.5028610229:
                            # if Nest_Dist_RL_To_Bbox_TL <= 86.0000000000
                            if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 86.0000000000:
                                return "ONE"
                            else:
                                # if Nest_aspect_ratio <= 2.4398754835
                                if _get(features, "Nest_aspect_ratio") <= 2.4398754835:
                                    # if Nest_Dist_RT_To_Bbox_BL <= 370.1651763916
                                    if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 370.1651763916:
                                        # if Actor_eccentricity <= 0.7778380513
                                        if _get(features, "Actor_eccentricity") <= 0.7778380513:
                                            return "INB"
                                        else:
                                            return "ONE"
                                    else:
                                        # if Actor_extent <= 0.7238601446
                                        if _get(features, "Actor_extent") <= 0.7238601446:
                                            return "INB"
                                        else:
                                            return "ONE"
                                else:
                                    # if Nest_RL_x <= 319.0000000000
                                    if _get(features, "Nest_RL_x") <= 319.0000000000:
                                        return "ONE"
                                    else:
                                        return "INB"
                        else:
                            # if Actor_RB_y <= 606.5000000000
                            if _get(features, "Actor_RB_y") <= 606.5000000000:
                                # if Nest_bbox_x <= 311.5000000000
                                if _get(features, "Nest_bbox_x") <= 311.5000000000:
                                    return "ONE"
                                else:
                                    return "INB"
                            else:
                                # if Nest_Dist_RT_RB <= 348.5275268555
                                if _get(features, "Nest_Dist_RT_RB") <= 348.5275268555:
                                    # if Actor_Centroid_To_Bbox_TR <= 45.0780220032
                                    if _get(features, "Actor_Centroid_To_Bbox_TR") <= 45.0780220032:
                                        return "ONE"
                                    else:
                                        return "INB"
                                else:
                                    # if Actor_Centroid_To_Bbox_TR <= 17.3375101089
                                    if _get(features, "Actor_Centroid_To_Bbox_TR") <= 17.3375101089:
                                        # if Nest_bbox_w <= 636.5000000000
                                        if _get(features, "Nest_bbox_w") <= 636.5000000000:
                                            return "INB"
                                        else:
                                            return "ONE"
                                    else:
                                        # if Nest_eccentricity <= 0.9478805661
                                        if _get(features, "Nest_eccentricity") <= 0.9478805661:
                                            # if c1_Mouse_Distance <= 464.3133697510
                                            if _get(features, "c1_Mouse_Distance") <= 464.3133697510:
                                                # if Nest_hu_0 <= 0.2064801529
                                                if _get(features, "Nest_hu_0") <= 0.2064801529:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                            else:
                                                # if Nest_aspect_ratio <= 2.1476759911
                                                if _get(features, "Nest_aspect_ratio") <= 2.1476759911:
                                                    return "INB"
                                                else:
                                                    # if Actor_aspect_ratio <= 0.7714531422
                                                    if _get(features, "Actor_aspect_ratio") <= 0.7714531422:
                                                        # if c2_Nest_Distance <= 259.8481521606
                                                        if _get(features, "c2_Nest_Distance") <= 259.8481521606:
                                                            return "INB"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        # if Nest_Mask_IoU <= 0.8529551923
                                                        if _get(features, "Nest_Mask_IoU") <= 0.8529551923:
                                                            # if c1_Nest_Distance <= 777.9269714355
                                                            if _get(features, "c1_Nest_Distance") <= 777.9269714355:
                                                                return "ONE"
                                                            else:
                                                                return "INB"
                                                        else:
                                                            # if Nest_orientation <= 84.0016975403
                                                            if _get(features, "Nest_orientation") <= 84.0016975403:
                                                                return "ONE"
                                                            else:
                                                                # if Actor_Dist_RR_To_Bbox_BR <= 2.6991728544
                                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 2.6991728544:
                                                                    return "ONE"
                                                                else:
                                                                    # if Nest_solidity <= 0.9171781242
                                                                    if _get(features, "Nest_solidity") <= 0.9171781242:
                                                                        return "INB"
                                                                    else:
                                                                        # if Nest_eccentricity <= 0.9258207083
                                                                        if _get(features, "Nest_eccentricity") <= 0.9258207083:
                                                                            return "INB"
                                                                        else:
                                                                            return "ONE"
                                        else:
                                            # if Nest_Dist_RR_To_Bbox_TL <= 836.6636352539
                                            if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 836.6636352539:
                                                return "ONE"
                                            else:
                                                return "INB"
            else:
                # if Nest_bbox_y <= 612.5000000000
                if _get(features, "Nest_bbox_y") <= 612.5000000000:
                    # if Actor_RT_y <= 413.0000000000
                    if _get(features, "Actor_RT_y") <= 413.0000000000:
                        # if Nest_Dist_RT_To_Bbox_TL <= 460.5000000000
                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 460.5000000000:
                            return "ONE"
                        else:
                            return "INB"
                    else:
                        # if Nest_Dist_RB_To_Bbox_TL <= 474.6798706055
                        if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 474.6798706055:
                            # if Actor_Dist_RT_RB <= 188.9419174194
                            if _get(features, "Actor_Dist_RT_RB") <= 188.9419174194:
                                # if Nest_Dist_RT_To_Bbox_TL <= 325.5000000000
                                if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 325.5000000000:
                                    return "ONE"
                                else:
                                    # if foodhopperMid_Nest_Distance <= 450.5648803711
                                    if _get(features, "foodhopperMid_Nest_Distance") <= 450.5648803711:
                                        return "INB"
                                    else:
                                        return "OE"
                            else:
                                # if Actor_RB_x <= 1056.5000000000
                                if _get(features, "Actor_RB_x") <= 1056.5000000000:
                                    return "INB"
                                else:
                                    # if Nest_Dist_RL_To_Bbox_BL <= 166.5000000000
                                    if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 166.5000000000:
                                        # if Nest_Centroid_To_Bbox_TL <= 360.1748657227
                                        if _get(features, "Nest_Centroid_To_Bbox_TL") <= 360.1748657227:
                                            # if Nest_hu_2 <= 0.0000174500
                                            if _get(features, "Nest_hu_2") <= 0.0000174500:
                                                # if Nest_Area_Diff_Abs <= 198.7500000000
                                                if _get(features, "Nest_Area_Diff_Abs") <= 198.7500000000:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                            else:
                                                # if Actor_To_Nest_Dist_Change <= 4.3071537018
                                                if _get(features, "Actor_To_Nest_Dist_Change") <= 4.3071537018:
                                                    # if Actor_centroid_y <= 665.4133911133
                                                    if _get(features, "Actor_centroid_y") <= 665.4133911133:
                                                        return "INB"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    # if Nest_Dist_RT_RR <= 317.9172821045
                                                    if _get(features, "Nest_Dist_RT_RR") <= 317.9172821045:
                                                        # if Nest_Dist_RL_To_Bbox_TL <= 196.0000000000
                                                        if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 196.0000000000:
                                                            return "ONE"
                                                        else:
                                                            return "INB"
                                                    else:
                                                        # if Actor_Dist_RT_To_Bbox_TL <= 210.0000000000
                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 210.0000000000:
                                                            return "ONE"
                                                        else:
                                                            return "INB"
                                        else:
                                            # if Actor_Dist_RR_To_Bbox_TR <= 164.5030364990
                                            if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 164.5030364990:
                                                return "ONE"
                                            else:
                                                return "INB"
                                    else:
                                        # if Nest_Dist_RL_To_Bbox_TL <= 132.5000000000
                                        if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 132.5000000000:
                                            # if Nest_RT_y <= 605.0000000000
                                            if _get(features, "Nest_RT_y") <= 605.0000000000:
                                                return "ONE"
                                            else:
                                                return "INB"
                                        else:
                                            return "INB"
                        else:
                            # if Actor_RB_y <= 950.0000000000
                            if _get(features, "Actor_RB_y") <= 950.0000000000:
                                # if foodhopperLeft_Mouse_Distance <= 343.1147155762
                                if _get(features, "foodhopperLeft_Mouse_Distance") <= 343.1147155762:
                                    return "ONE"
                                else:
                                    # if Actor_Direction_deg <= -176.0258026123
                                    if _get(features, "Actor_Direction_deg") <= -176.0258026123:
                                        return "ONE"
                                    else:
                                        return "INB"
                            else:
                                return "ONE"
                else:
                    # if Nest_eccentricity <= 0.8832995296
                    if _get(features, "Nest_eccentricity") <= 0.8832995296:
                        # if Nest_RB_x <= 595.0000000000
                        if _get(features, "Nest_RB_x") <= 595.0000000000:
                            # if Actor_Dist_RT_To_Bbox_TL <= 61.0000000000
                            if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 61.0000000000:
                                # if Nest_eccentricity <= 0.8599401116
                                if _get(features, "Nest_eccentricity") <= 0.8599401116:
                                    return "INB"
                                else:
                                    return "OE"
                            else:
                                return "ONE"
                        else:
                            # if Nest_Dist_RB_To_Bbox_BL <= 473.0010833740
                            if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 473.0010833740:
                                # if Nest_RL_y <= 729.5000000000
                                if _get(features, "Nest_RL_y") <= 729.5000000000:
                                    return "ONE"
                                else:
                                    return "INB"
                            else:
                                return "ONE"
                    else:
                        # if Nest_RB_y <= 933.5000000000
                        if _get(features, "Nest_RB_y") <= 933.5000000000:
                            # if Nest_Dist_RL_To_Bbox_BR <= 769.6466674805
                            if _get(features, "Nest_Dist_RL_To_Bbox_BR") <= 769.6466674805:
                                # if Nest_solidity <= 0.7443055809
                                if _get(features, "Nest_solidity") <= 0.7443055809:
                                    # if Actor_To_Nest_Distance <= 430.9383544922
                                    if _get(features, "Actor_To_Nest_Distance") <= 430.9383544922:
                                        return "INB"
                                    else:
                                        return "ONE"
                                else:
                                    return "INB"
                            else:
                                # if Actor_hu_5 <= 0.0000043900
                                if _get(features, "Actor_hu_5") <= 0.0000043900:
                                    # if Nest_RB_y <= 925.0000000000
                                    if _get(features, "Nest_RB_y") <= 925.0000000000:
                                        # if Nest_solidity <= 0.8701835871
                                        if _get(features, "Nest_solidity") <= 0.8701835871:
                                            # if Nest_bbox_h <= 300.0000000000
                                            if _get(features, "Nest_bbox_h") <= 300.0000000000:
                                                # if Nest_Dist_RL_To_Bbox_TL <= 81.0000000000
                                                if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 81.0000000000:
                                                    return "INB"
                                                else:
                                                    # if Actor_Mask_IoU <= 0.9567308724
                                                    if _get(features, "Actor_Mask_IoU") <= 0.9567308724:
                                                        return "ONE"
                                                    else:
                                                        return "OE"
                                            else:
                                                # if Nest_Dist_RL_To_Bbox_BL <= 168.5000000000
                                                if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 168.5000000000:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                        else:
                                            # if Actor_Dist_RL_To_Bbox_BL <= 58.0000000000
                                            if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 58.0000000000:
                                                return "OE"
                                            else:
                                                # if Nest_Dist_RT_To_Bbox_BL <= 605.8787841797
                                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 605.8787841797:
                                                    return "INB"
                                                else:
                                                    return "ONE"
                                    else:
                                        # if Actor_Dist_RL_To_Bbox_BR <= 272.1893844604
                                        if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 272.1893844604:
                                            return "INB"
                                        else:
                                            return "ONE"
                                else:
                                    # if Actor_aspect_ratio <= 1.6301245689
                                    if _get(features, "Actor_aspect_ratio") <= 1.6301245689:
                                        # if foodhopperBottom_Mouse_Distance <= 449.1336669922
                                        if _get(features, "foodhopperBottom_Mouse_Distance") <= 449.1336669922:
                                            return "INB"
                                        else:
                                            return "ONE"
                                    else:
                                        return "OE"
                        else:
                            # if Nest_Mask_IoU <= 0.9083100259
                            if _get(features, "Nest_Mask_IoU") <= 0.9083100259:
                                # if Actor_RL_y <= 689.0000000000
                                if _get(features, "Actor_RL_y") <= 689.0000000000:
                                    return "ONE"
                                else:
                                    return "INB"
                            else:
                                # if c2_Nest_Distance <= 338.5186309814
                                if _get(features, "c2_Nest_Distance") <= 338.5186309814:
                                    # if Nest_hu_5 <= -0.0000110500
                                    if _get(features, "Nest_hu_5") <= -0.0000110500:
                                        # if Nest_RR_x <= 1084.0000000000
                                        if _get(features, "Nest_RR_x") <= 1084.0000000000:
                                            return "INB"
                                        else:
                                            return "ONE"
                                    else:
                                        return "ONE"
                                else:
                                    return "INB"
    else:
        # if Actor_Dist_RT_RB <= 26.3247833252
        if _get(features, "Actor_Dist_RT_RB") <= 26.3247833252:
            # if Actor_RT_x <= 732.5000000000
            if _get(features, "Actor_RT_x") <= 732.5000000000:
                return "INB"
            else:
                # if Nest_Centroid_To_Bbox_TL <= 411.6624298096
                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 411.6624298096:
                    # if foodhopperRight_Nest_Distance <= 516.0023498535
                    if _get(features, "foodhopperRight_Nest_Distance") <= 516.0023498535:
                        # if Nest_hu_2 <= 0.0004771630
                        if _get(features, "Nest_hu_2") <= 0.0004771630:
                            # if Actor_extent <= 0.6195370257
                            if _get(features, "Actor_extent") <= 0.6195370257:
                                return "ONE"
                            else:
                                return "OE"
                        else:
                            # if Actor_To_Nest_Distance <= 340.5478668213
                            if _get(features, "Actor_To_Nest_Distance") <= 340.5478668213:
                                return "OE"
                            else:
                                return "ONE"
                    else:
                        # if Nest_Centroid_To_Bbox_BL <= 403.8238220215
                        if _get(features, "Nest_Centroid_To_Bbox_BL") <= 403.8238220215:
                            return "OE"
                        else:
                            # if Nest_Centroid_To_Bbox_BR <= 397.2599334717
                            if _get(features, "Nest_Centroid_To_Bbox_BR") <= 397.2599334717:
                                # if Actor_Dist_RB_To_Bbox_BL <= 21.5232553482
                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 21.5232553482:
                                    return "ONE"
                                else:
                                    return "OE"
                            else:
                                # if Nest_RT_x <= 891.5000000000
                                if _get(features, "Nest_RT_x") <= 891.5000000000:
                                    return "ONE"
                                else:
                                    return "OE"
                else:
                    # if Nest_hu_2 <= 0.0004827770
                    if _get(features, "Nest_hu_2") <= 0.0004827770:
                        return "OE"
                    else:
                        # if Nest_RL_y <= 743.5000000000
                        if _get(features, "Nest_RL_y") <= 743.5000000000:
                            return "OE"
                        else:
                            return "ONE"
        else:
            # if Nest_solidity <= 0.9337595999
            if _get(features, "Nest_solidity") <= 0.9337595999:
                # if Nest_perimeter <= 2297.9200439453
                if _get(features, "Nest_perimeter") <= 2297.9200439453:
                    # if Nest_Dist_RB_To_Bbox_TR <= 617.5718383789
                    if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 617.5718383789:
                        # if Nest_Dist_RB_To_Bbox_TR <= 313.9498443604
                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 313.9498443604:
                            # if Actor_Dist_RR_To_Bbox_TR <= 31.5158729553
                            if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 31.5158729553:
                                # if c3_Mouse_Distance <= 803.5749816895
                                if _get(features, "c3_Mouse_Distance") <= 803.5749816895:
                                    # if Nest_bbox_w <= 789.5000000000
                                    if _get(features, "Nest_bbox_w") <= 789.5000000000:
                                        # if Nest_centroid_x <= 718.7175903320
                                        if _get(features, "Nest_centroid_x") <= 718.7175903320:
                                            return "OE"
                                        else:
                                            return "ONE"
                                    else:
                                        return "ONE"
                                else:
                                    # if Nest_perimeter <= 2113.4154052734
                                    if _get(features, "Nest_perimeter") <= 2113.4154052734:
                                        return "INB"
                                    else:
                                        # if Nest_Dist_RT_To_Bbox_TL <= 566.0000000000
                                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 566.0000000000:
                                            return "ONE"
                                        else:
                                            return "OE"
                            else:
                                # if Nest_Centroid_To_Bbox_BR <= 402.7486572266
                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 402.7486572266:
                                    # if Actor_Mask_IoU <= 0.7331330478
                                    if _get(features, "Actor_Mask_IoU") <= 0.7331330478:
                                        # if foodhopperRight_Nest_Distance <= 520.8576049805
                                        if _get(features, "foodhopperRight_Nest_Distance") <= 520.8576049805:
                                            return "ONE"
                                        else:
                                            # if Nest_RL_y <= 721.5000000000
                                            if _get(features, "Nest_RL_y") <= 721.5000000000:
                                                return "ONE"
                                            else:
                                                return "INB"
                                    else:
                                        # if foodhopperMid_Nest_Distance <= 429.7399902344
                                        if _get(features, "foodhopperMid_Nest_Distance") <= 429.7399902344:
                                            return "INB"
                                        else:
                                            # if Nest_Dist_RB_To_Bbox_BR <= 48.5103092194
                                            if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 48.5103092194:
                                                return "INB"
                                            else:
                                                return "ONE"
                                else:
                                    # if Actor_Centroid_To_Bbox_BR <= 38.4035720825
                                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 38.4035720825:
                                        return "OE"
                                    else:
                                        # if Actor_aspect_ratio <= 2.1675243378
                                        if _get(features, "Actor_aspect_ratio") <= 2.1675243378:
                                            # if Actor_RR_y <= 673.5000000000
                                            if _get(features, "Actor_RR_y") <= 673.5000000000:
                                                # if Actor_hu_4 <= 0.0000000556
                                                if _get(features, "Actor_hu_4") <= 0.0000000556:
                                                    return "ONE"
                                                else:
                                                    return "OE"
                                            else:
                                                # if Actor_Dist_RL_To_Bbox_TL <= 18.5000000000
                                                if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 18.5000000000:
                                                    # if Nest_Dist_RL_RR <= 795.2150268555
                                                    if _get(features, "Nest_Dist_RL_RR") <= 795.2150268555:
                                                        return "ONE"
                                                    else:
                                                        return "OE"
                                                else:
                                                    return "ONE"
                                        else:
                                            # if Nest_Dist_RR_To_Bbox_TL <= 820.6248168945
                                            if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 820.6248168945:
                                                # if Actor_bbox_x <= 791.0000000000
                                                if _get(features, "Actor_bbox_x") <= 791.0000000000:
                                                    return "INB"
                                                else:
                                                    return "OE"
                                            else:
                                                return "ONE"
                        else:
                            # if Nest_orientation <= 95.3822441101
                            if _get(features, "Nest_orientation") <= 95.3822441101:
                                # if Nest_Dist_RT_To_Bbox_BL <= 326.9252624512
                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 326.9252624512:
                                    # if Nest_area <= 133016.2500000000
                                    if _get(features, "Nest_area") <= 133016.2500000000:
                                        return "INB"
                                    else:
                                        # if Actor_centroid_x <= 693.3219604492
                                        if _get(features, "Actor_centroid_x") <= 693.3219604492:
                                            return "ONE"
                                        else:
                                            return "OE"
                                else:
                                    # if c1_Nest_Distance <= 819.5105285645
                                    if _get(features, "c1_Nest_Distance") <= 819.5105285645:
                                        # if Nest_RT_y <= 507.5000000000
                                        if _get(features, "Nest_RT_y") <= 507.5000000000:
                                            # if Nest_orientation <= 94.6651916504
                                            if _get(features, "Nest_orientation") <= 94.6651916504:
                                                # if Actor_Dist_RR_To_Bbox_BR <= 92.5054054260
                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 92.5054054260:
                                                    # if Nest_Dist_RB_RL <= 251.5494308472
                                                    if _get(features, "Nest_Dist_RB_RL") <= 251.5494308472:
                                                        return "OE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    # if Actor_RR_x <= 805.0000000000
                                                    if _get(features, "Actor_RR_x") <= 805.0000000000:
                                                        return "ONE"
                                                    else:
                                                        return "OE"
                                            else:
                                                return "ONE"
                                        else:
                                            # if foodhopperLeft_Nest_Distance <= 125.6444740295
                                            if _get(features, "foodhopperLeft_Nest_Distance") <= 125.6444740295:
                                                # if Nest_Dist_RR_RB <= 400.6357421875
                                                if _get(features, "Nest_Dist_RR_RB") <= 400.6357421875:
                                                    return "INB"
                                                else:
                                                    # if Nest_RR_y <= 728.5000000000
                                                    if _get(features, "Nest_RR_y") <= 728.5000000000:
                                                        # if Nest_Dist_RT_To_Bbox_BR <= 386.0653839111
                                                        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 386.0653839111:
                                                            # if Nest_centroid_x <= 595.8783874512
                                                            if _get(features, "Nest_centroid_x") <= 595.8783874512:
                                                                # if Actor_extent <= 0.7056477070
                                                                if _get(features, "Actor_extent") <= 0.7056477070:
                                                                    return "INB"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                return "ONE"
                                                        else:
                                                            # if Nest_Dist_RR_RB <= 460.1578826904
                                                            if _get(features, "Nest_Dist_RR_RB") <= 460.1578826904:
                                                                # if Actor_bbox_y <= 585.5000000000
                                                                if _get(features, "Actor_bbox_y") <= 585.5000000000:
                                                                    return "ONE"
                                                                else:
                                                                    # if foodhopperBottom_Mouse_Distance <= 475.7303161621
                                                                    if _get(features, "foodhopperBottom_Mouse_Distance") <= 475.7303161621:
                                                                        return "ONE"
                                                                    else:
                                                                        return "INB"
                                                            else:
                                                                return "INB"
                                                    else:
                                                        # if Nest_centroid_y <= 756.2208557129
                                                        if _get(features, "Nest_centroid_y") <= 756.2208557129:
                                                            # if Nest_Dist_RR_To_Bbox_TR <= 238.0020980835
                                                            if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 238.0020980835:
                                                                # if c2_Mouse_Distance <= 48.4175033569
                                                                if _get(features, "c2_Mouse_Distance") <= 48.4175033569:
                                                                    # if Nest_hu_5 <= 0.0000000547
                                                                    if _get(features, "Nest_hu_5") <= 0.0000000547:
                                                                        return "ONE"
                                                                    else:
                                                                        return "OE"
                                                                else:
                                                                    # if Actor_extent <= 0.8168519139
                                                                    if _get(features, "Actor_extent") <= 0.8168519139:
                                                                        # if Actor_aspect_ratio <= 0.3904238194
                                                                        if _get(features, "Actor_aspect_ratio") <= 0.3904238194:
                                                                            # if Actor_Dist_RR_To_Bbox_TL <= 515.0033264160
                                                                            if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 515.0033264160:
                                                                                return "ONE"
                                                                            else:
                                                                                return "INB"
                                                                        else:
                                                                            # if Nest_hu_5 <= 0.0000224500
                                                                            if _get(features, "Nest_hu_5") <= 0.0000224500:
                                                                                # if Actor_Dist_RT_To_Bbox_TL <= 140.5000000000
                                                                                if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 140.5000000000:
                                                                                    return "ONE"
                                                                                else:
                                                                                    # if Actor_RB_x <= 1235.0000000000
                                                                                    if _get(features, "Actor_RB_x") <= 1235.0000000000:
                                                                                        return "ONE"
                                                                                    else:
                                                                                        return "INB"
                                                                            else:
                                                                                return "INB"
                                                                    else:
                                                                        # if Nest_Centroid_To_Bbox_BL <= 332.2859954834
                                                                        if _get(features, "Nest_Centroid_To_Bbox_BL") <= 332.2859954834:
                                                                            return "ONE"
                                                                        else:
                                                                            return "OE"
                                                            else:
                                                                return "INB"
                                                        else:
                                                            # if Nest_RL_y <= 778.0000000000
                                                            if _get(features, "Nest_RL_y") <= 778.0000000000:
                                                                return "INB"
                                                            else:
                                                                return "OE"
                                            else:
                                                # if foodhopperBottom_Mouse_Distance <= 299.4125366211
                                                if _get(features, "foodhopperBottom_Mouse_Distance") <= 299.4125366211:
                                                    # if Actor_RB_x <= 589.5000000000
                                                    if _get(features, "Actor_RB_x") <= 589.5000000000:
                                                        # if Actor_Dist_RB_To_Bbox_TL <= 256.2258605957
                                                        if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 256.2258605957:
                                                            return "INB"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        # if Nest_eccentricity <= 0.8930431008
                                                        if _get(features, "Nest_eccentricity") <= 0.8930431008:
                                                            return "INB"
                                                        else:
                                                            return "ONE"
                                                else:
                                                    # if Nest_Dist_RL_To_Bbox_TL <= 93.5000000000
                                                    if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 93.5000000000:
                                                        # if Actor_Dist_RL_To_Bbox_TL <= 5.5000000000
                                                        if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 5.5000000000:
                                                            # if Nest_hu_2 <= 0.0006363145
                                                            if _get(features, "Nest_hu_2") <= 0.0006363145:
                                                                return "ONE"
                                                            else:
                                                                return "INB"
                                                        else:
                                                            # if Actor_orientation <= 69.4605407715
                                                            if _get(features, "Actor_orientation") <= 69.4605407715:
                                                                # if Actor_RL_x <= 965.0000000000
                                                                if _get(features, "Actor_RL_x") <= 965.0000000000:
                                                                    return "OE"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                # if Actor_area <= 14833.0000000000
                                                                if _get(features, "Actor_area") <= 14833.0000000000:
                                                                    # if Actor_orientation <= 73.3297309875
                                                                    if _get(features, "Actor_orientation") <= 73.3297309875:
                                                                        return "OE"
                                                                    else:
                                                                        # if Actor_Dist_RR_RB <= 28.0506668091
                                                                        if _get(features, "Actor_Dist_RR_RB") <= 28.0506668091:
                                                                            # if Nest_RR_y <= 881.0000000000
                                                                            if _get(features, "Nest_RR_y") <= 881.0000000000:
                                                                                return "INB"
                                                                            else:
                                                                                return "ONE"
                                                                        else:
                                                                            return "ONE"
                                                                else:
                                                                    # if Actor_aspect_ratio <= 1.9629250765
                                                                    if _get(features, "Actor_aspect_ratio") <= 1.9629250765:
                                                                        # if Actor_hu_5 <= 0.0000059150
                                                                        if _get(features, "Actor_hu_5") <= 0.0000059150:
                                                                            return "ONE"
                                                                        else:
                                                                            # if Nest_hu_0 <= 0.3574597389
                                                                            if _get(features, "Nest_hu_0") <= 0.3574597389:
                                                                                return "OE"
                                                                            else:
                                                                                return "INB"
                                                                    else:
                                                                        return "OE"
                                                    else:
                                                        # if Nest_hu_5 <= 0.0001429190
                                                        if _get(features, "Nest_hu_5") <= 0.0001429190:
                                                            # if Nest_Dist_RL_RT <= 568.5956115723
                                                            if _get(features, "Nest_Dist_RL_RT") <= 568.5956115723:
                                                                # if Nest_Dist_RR_To_Bbox_BR <= 290.0017242432
                                                                if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 290.0017242432:
                                                                    # if Actor_centroid_y <= 909.2230224609
                                                                    if _get(features, "Actor_centroid_y") <= 909.2230224609:
                                                                        # if Nest_Dist_RT_RB <= 349.3329315186
                                                                        if _get(features, "Nest_Dist_RT_RB") <= 349.3329315186:
                                                                            # if Nest_Dist_RL_To_Bbox_BL <= 115.0000000000
                                                                            if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 115.0000000000:
                                                                                return "INB"
                                                                            else:
                                                                                # if Nest_Centroid_To_Bbox_TL <= 334.2297668457
                                                                                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 334.2297668457:
                                                                                    # if Actor_Dist_RT_To_Bbox_TL <= 88.5000000000
                                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 88.5000000000:
                                                                                        # if Nest_solidity <= 0.9045752287
                                                                                        if _get(features, "Nest_solidity") <= 0.9045752287:
                                                                                            return "OE"
                                                                                        else:
                                                                                            return "ONE"
                                                                                    else:
                                                                                        return "ONE"
                                                                                else:
                                                                                    # if Nest_Dist_RL_To_Bbox_TL <= 99.5000000000
                                                                                    if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 99.5000000000:
                                                                                        # if Nest_orientation <= 94.6702423096
                                                                                        if _get(features, "Nest_orientation") <= 94.6702423096:
                                                                                            # if Nest_Dist_RT_To_Bbox_BR <= 392.4983978271
                                                                                            if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 392.4983978271:
                                                                                                # if c2_Mouse_Distance <= 155.1613006592
                                                                                                if _get(features, "c2_Mouse_Distance") <= 155.1613006592:
                                                                                                    # if Actor_Dist_RT_RR <= 78.2674942017
                                                                                                    if _get(features, "Actor_Dist_RT_RR") <= 78.2674942017:
                                                                                                        return "OE"
                                                                                                    else:
                                                                                                        return "INB"
                                                                                                else:
                                                                                                    # if Actor_hu_6 <= -0.0000005322
                                                                                                    if _get(features, "Actor_hu_6") <= -0.0000005322:
                                                                                                        return "INB"
                                                                                                    else:
                                                                                                        return "ONE"
                                                                                            else:
                                                                                                # if Nest_aspect_ratio <= 2.7495645285
                                                                                                if _get(features, "Nest_aspect_ratio") <= 2.7495645285:
                                                                                                    # if foodhopperRight_Mouse_Distance <= 375.6399383545
                                                                                                    if _get(features, "foodhopperRight_Mouse_Distance") <= 375.6399383545:
                                                                                                        return "OE"
                                                                                                    else:
                                                                                                        return "ONE"
                                                                                                else:
                                                                                                    return "INB"
                                                                                        else:
                                                                                            # if Actor_orientation <= 82.2926902771
                                                                                            if _get(features, "Actor_orientation") <= 82.2926902771:
                                                                                                # if foodhopperBottom_Nest_Distance <= 424.0672912598
                                                                                                if _get(features, "foodhopperBottom_Nest_Distance") <= 424.0672912598:
                                                                                                    return "ONE"
                                                                                                else:
                                                                                                    return "INB"
                                                                                            else:
                                                                                                # if Actor_bbox_x <= 616.5000000000
                                                                                                if _get(features, "Actor_bbox_x") <= 616.5000000000:
                                                                                                    return "INB"
                                                                                                else:
                                                                                                    return "ONE"
                                                                                    else:
                                                                                        # if Nest_bbox_h <= 333.5000000000
                                                                                        if _get(features, "Nest_bbox_h") <= 333.5000000000:
                                                                                            # if Nest_Dist_RR_To_Bbox_TR <= 270.5018463135
                                                                                            if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 270.5018463135:
                                                                                                # if c1_Mouse_Distance <= 579.2942504883
                                                                                                if _get(features, "c1_Mouse_Distance") <= 579.2942504883:
                                                                                                    # if Nest_Dist_RB_RL <= 490.2649841309
                                                                                                    if _get(features, "Nest_Dist_RB_RL") <= 490.2649841309:
                                                                                                        return "INB"
                                                                                                    else:
                                                                                                        return "ONE"
                                                                                                else:
                                                                                                    # if Nest_orientation <= 82.7849426270
                                                                                                    if _get(features, "Nest_orientation") <= 82.7849426270:
                                                                                                        # if Actor_Dist_RR_To_Bbox_BL <= 162.4540557861
                                                                                                        if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 162.4540557861:
                                                                                                            return "ONE"
                                                                                                        else:
                                                                                                            # if Nest_orientation <= 82.4068603516
                                                                                                            if _get(features, "Nest_orientation") <= 82.4068603516:
                                                                                                                return "ONE"
                                                                                                            else:
                                                                                                                return "OE"
                                                                                                    else:
                                                                                                        # if c4_Nest_Distance <= 403.8547821045
                                                                                                        if _get(features, "c4_Nest_Distance") <= 403.8547821045:
                                                                                                            # if Nest_solidity <= 0.8487964272
                                                                                                            if _get(features, "Nest_solidity") <= 0.8487964272:
                                                                                                                # if Actor_solidity <= 0.9339259565
                                                                                                                if _get(features, "Actor_solidity") <= 0.9339259565:
                                                                                                                    return "ONE"
                                                                                                                else:
                                                                                                                    return "OE"
                                                                                                            else:
                                                                                                                return "ONE"
                                                                                                        else:
                                                                                                            # if Nest_Centroid_To_Bbox_BL <= 378.1512451172
                                                                                                            if _get(features, "Nest_Centroid_To_Bbox_BL") <= 378.1512451172:
                                                                                                                # if Actor_RB_y <= 761.0000000000
                                                                                                                if _get(features, "Actor_RB_y") <= 761.0000000000:
                                                                                                                    return "OE"
                                                                                                                else:
                                                                                                                    return "ONE"
                                                                                                            else:
                                                                                                                return "ONE"
                                                                                            else:
                                                                                                return "INB"
                                                                                        else:
                                                                                            # if foodhopperMid_Mouse_Distance <= 273.2989044189
                                                                                            if _get(features, "foodhopperMid_Mouse_Distance") <= 273.2989044189:
                                                                                                # if Actor_To_Nest_Distance <= 342.4005737305
                                                                                                if _get(features, "Actor_To_Nest_Distance") <= 342.4005737305:
                                                                                                    return "INB"
                                                                                                else:
                                                                                                    # if Nest_Area_Diff_Abs <= 358.0000000000
                                                                                                    if _get(features, "Nest_Area_Diff_Abs") <= 358.0000000000:
                                                                                                        return "OE"
                                                                                                    else:
                                                                                                        return "ONE"
                                                                                            else:
                                                                                                # if c3_Mouse_Distance <= 877.3414001465
                                                                                                if _get(features, "c3_Mouse_Distance") <= 877.3414001465:
                                                                                                    # if Nest_Dist_RL_To_Bbox_TR <= 816.6728210449
                                                                                                    if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 816.6728210449:
                                                                                                        # if Actor_Dist_RT_To_Bbox_TR <= 228.0000000000
                                                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 228.0000000000:
                                                                                                            # if Nest_Mask_IoU <= 0.9902153611
                                                                                                            if _get(features, "Nest_Mask_IoU") <= 0.9902153611:
                                                                                                                # if Actor_solidity <= 0.9666197300
                                                                                                                if _get(features, "Actor_solidity") <= 0.9666197300:
                                                                                                                    return "ONE"
                                                                                                                else:
                                                                                                                    return "INB"
                                                                                                            else:
                                                                                                                return "ONE"
                                                                                                        else:
                                                                                                            return "INB"
                                                                                                    else:
                                                                                                        return "INB"
                                                                                                else:
                                                                                                    return "INB"
                                                                        else:
                                                                            # if Nest_Dist_RT_To_Bbox_BL <= 622.3255004883
                                                                            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 622.3255004883:
                                                                                # if foodhopperLeft_Mouse_Distance <= 16.1886062622
                                                                                if _get(features, "foodhopperLeft_Mouse_Distance") <= 16.1886062622:
                                                                                    return "INB"
                                                                                else:
                                                                                    # if Actor_To_Nest_Distance <= 125.5178260803
                                                                                    if _get(features, "Actor_To_Nest_Distance") <= 125.5178260803:
                                                                                        # if Nest_eccentricity <= 0.8920209110
                                                                                        if _get(features, "Nest_eccentricity") <= 0.8920209110:
                                                                                            return "INB"
                                                                                        else:
                                                                                            return "ONE"
                                                                                    else:
                                                                                        # if Nest_Dist_RT_RR <= 274.2227783203
                                                                                        if _get(features, "Nest_Dist_RT_RR") <= 274.2227783203:
                                                                                            # if Nest_orientation <= 80.5999641418
                                                                                            if _get(features, "Nest_orientation") <= 80.5999641418:
                                                                                                return "INB"
                                                                                            else:
                                                                                                return "ONE"
                                                                                        else:
                                                                                            # if Actor_Dist_RR_RB <= 524.1822509766
                                                                                            if _get(features, "Actor_Dist_RR_RB") <= 524.1822509766:
                                                                                                return "ONE"
                                                                                            else:
                                                                                                # if Actor_Dist_RR_To_Bbox_BR <= 458.5010986328
                                                                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 458.5010986328:
                                                                                                    return "INB"
                                                                                                else:
                                                                                                    return "ONE"
                                                                            else:
                                                                                return "INB"
                                                                    else:
                                                                        return "INB"
                                                                else:
                                                                    # if Actor_aspect_ratio <= 1.6635255218
                                                                    if _get(features, "Actor_aspect_ratio") <= 1.6635255218:
                                                                        return "ONE"
                                                                    else:
                                                                        return "INB"
                                                            else:
                                                                # if Nest_eccentricity <= 0.9379629493
                                                                if _get(features, "Nest_eccentricity") <= 0.9379629493:
                                                                    return "INB"
                                                                else:
                                                                    # if Nest_Dist_RR_To_Bbox_BL <= 752.7134399414
                                                                    if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 752.7134399414:
                                                                        return "ONE"
                                                                    else:
                                                                        return "INB"
                                                        else:
                                                            # if Actor_Dist_RR_To_Bbox_TL <= 176.5560302734
                                                            if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 176.5560302734:
                                                                return "OE"
                                                            else:
                                                                return "ONE"
                                    else:
                                        # if foodhopperBottom_Nest_Distance <= 468.8698730469
                                        if _get(features, "foodhopperBottom_Nest_Distance") <= 468.8698730469:
                                            return "ONE"
                                        else:
                                            return "INB"
                            else:
                                # if Nest_RB_y <= 906.5000000000
                                if _get(features, "Nest_RB_y") <= 906.5000000000:
                                    return "ONE"
                                else:
                                    # if Nest_solidity <= 0.7675957978
                                    if _get(features, "Nest_solidity") <= 0.7675957978:
                                        return "ONE"
                                    else:
                                        return "INB"
                    else:
                        # if Nest_RR_y <= 756.5000000000
                        if _get(features, "Nest_RR_y") <= 756.5000000000:
                            # if Nest_orientation <= 85.6772232056
                            if _get(features, "Nest_orientation") <= 85.6772232056:
                                return "INB"
                            else:
                                # if Nest_Centroid_To_Bbox_TR <= 467.4349670410
                                if _get(features, "Nest_Centroid_To_Bbox_TR") <= 467.4349670410:
                                    return "ONE"
                                else:
                                    return "INB"
                        else:
                            # if Nest_RB_x <= 396.0000000000
                            if _get(features, "Nest_RB_x") <= 396.0000000000:
                                return "ONE"
                            else:
                                return "INB"
                else:
                    # if Nest_orientation <= 83.8796348572
                    if _get(features, "Nest_orientation") <= 83.8796348572:
                        # if Nest_aspect_ratio <= 1.9539937973
                        if _get(features, "Nest_aspect_ratio") <= 1.9539937973:
                            return "INB"
                        else:
                            return "ONE"
                    else:
                        # if Nest_Dist_RR_To_Bbox_BR <= 215.5023193359
                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 215.5023193359:
                            # if Nest_RB_y <= 902.0000000000
                            if _get(features, "Nest_RB_y") <= 902.0000000000:
                                return "ONE"
                            else:
                                # if Actor_Dist_RL_To_Bbox_TL <= 199.5000000000
                                if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 199.5000000000:
                                    # if c4_Nest_Distance <= 350.2456359863
                                    if _get(features, "c4_Nest_Distance") <= 350.2456359863:
                                        # if Nest_orientation <= 97.4269104004
                                        if _get(features, "Nest_orientation") <= 97.4269104004:
                                            return "ONE"
                                        else:
                                            return "INB"
                                    else:
                                        # if Nest_Area_Diff_Abs <= 22.7500000000
                                        if _get(features, "Nest_Area_Diff_Abs") <= 22.7500000000:
                                            # if Actor_RT_y <= 626.0000000000
                                            if _get(features, "Actor_RT_y") <= 626.0000000000:
                                                return "INB"
                                            else:
                                                return "ONE"
                                        else:
                                            return "INB"
                                else:
                                    return "ONE"
                        else:
                            # if Nest_Dist_RL_RT <= 378.9435729980
                            if _get(features, "Nest_Dist_RL_RT") <= 378.9435729980:
                                # if Actor_solidity <= 0.9640617371
                                if _get(features, "Actor_solidity") <= 0.9640617371:
                                    return "ONE"
                                else:
                                    return "INB"
                            else:
                                return "INB"
            else:
                # if Nest_RT_x <= 646.5000000000
                if _get(features, "Nest_RT_x") <= 646.5000000000:
                    # if Nest_Dist_RT_To_Bbox_TL <= 158.5000000000
                    if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 158.5000000000:
                        # if foodhopperLeft_Nest_Distance <= 76.3058395386
                        if _get(features, "foodhopperLeft_Nest_Distance") <= 76.3058395386:
                            return "ONE"
                        else:
                            # if Actor_RR_y <= 896.0000000000
                            if _get(features, "Actor_RR_y") <= 896.0000000000:
                                # if Actor_Dist_RB_To_Bbox_BR <= 223.5022811890
                                if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 223.5022811890:
                                    # if Nest_solidity <= 0.9339904189
                                    if _get(features, "Nest_solidity") <= 0.9339904189:
                                        # if c3_Nest_Distance <= 983.2597351074
                                        if _get(features, "c3_Nest_Distance") <= 983.2597351074:
                                            return "ONE"
                                        else:
                                            return "INB"
                                    else:
                                        # if Nest_Area_Diff_Abs <= 1403.5000000000
                                        if _get(features, "Nest_Area_Diff_Abs") <= 1403.5000000000:
                                            return "INB"
                                        else:
                                            return "ONE"
                                else:
                                    return "ONE"
                            else:
                                return "ONE"
                    else:
                        # if Nest_solidity <= 0.9388174415
                        if _get(features, "Nest_solidity") <= 0.9388174415:
                            # if c3_Nest_Distance <= 925.2591247559
                            if _get(features, "c3_Nest_Distance") <= 925.2591247559:
                                return "INB"
                            else:
                                # if Nest_orientation <= 86.3962211609
                                if _get(features, "Nest_orientation") <= 86.3962211609:
                                    # if c4_Mouse_Distance <= 966.8055419922
                                    if _get(features, "c4_Mouse_Distance") <= 966.8055419922:
                                        # if Nest_Centroid_To_Bbox_TR <= 373.6194152832
                                        if _get(features, "Nest_Centroid_To_Bbox_TR") <= 373.6194152832:
                                            return "ONE"
                                        else:
                                            return "INB"
                                    else:
                                        return "INB"
                                else:
                                    return "INB"
                        else:
                            # if Actor_RL_x <= 750.5000000000
                            if _get(features, "Actor_RL_x") <= 750.5000000000:
                                return "INB"
                            else:
                                # if Actor_solidity <= 0.7650683820
                                if _get(features, "Actor_solidity") <= 0.7650683820:
                                    # if c4_Mouse_Distance <= 677.2018737793
                                    if _get(features, "c4_Mouse_Distance") <= 677.2018737793:
                                        return "ONE"
                                    else:
                                        return "INB"
                                else:
                                    # if Actor_eccentricity <= 0.2742417902
                                    if _get(features, "Actor_eccentricity") <= 0.2742417902:
                                        # if Nest_bbox_x <= 317.0000000000
                                        if _get(features, "Nest_bbox_x") <= 317.0000000000:
                                            return "INB"
                                        else:
                                            return "OE"
                                    else:
                                        # if Actor_Direction_deg <= -179.6280517578
                                        if _get(features, "Actor_Direction_deg") <= -179.6280517578:
                                            return "INB"
                                        else:
                                            # if Actor_solidity <= 0.9752322137
                                            if _get(features, "Actor_solidity") <= 0.9752322137:
                                                return "ONE"
                                            else:
                                                # if Actor_To_Nest_Dist_Change <= -8.5908818245
                                                if _get(features, "Actor_To_Nest_Dist_Change") <= -8.5908818245:
                                                    return "INB"
                                                else:
                                                    return "ONE"
                else:
                    # if Actor_Area_Diff_Abs <= 2956.7500000000
                    if _get(features, "Actor_Area_Diff_Abs") <= 2956.7500000000:
                        # if Actor_RR_y <= 728.5000000000
                        if _get(features, "Actor_RR_y") <= 728.5000000000:
                            # if Nest_Dist_RT_To_Bbox_BL <= 526.4807739258
                            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 526.4807739258:
                                # if foodhopperMid_Mouse_Distance <= 301.9201812744
                                if _get(features, "foodhopperMid_Mouse_Distance") <= 301.9201812744:
                                    # if Actor_Dist_RT_To_Bbox_TR <= 18.5000000000
                                    if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 18.5000000000:
                                        return "INB"
                                    else:
                                        # if Actor_Dist_RT_To_Bbox_TR <= 24.5000000000
                                        if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 24.5000000000:
                                            # if Actor_RL_y <= 644.0000000000
                                            if _get(features, "Actor_RL_y") <= 644.0000000000:
                                                return "INB"
                                            else:
                                                return "OE"
                                        else:
                                            return "OE"
                                else:
                                    # if foodhopperMid_Nest_Distance <= 455.7062377930
                                    if _get(features, "foodhopperMid_Nest_Distance") <= 455.7062377930:
                                        return "OE"
                                    else:
                                        return "ONE"
                            else:
                                # if Actor_Dist_RL_RR <= 78.4916114807
                                if _get(features, "Actor_Dist_RL_RR") <= 78.4916114807:
                                    return "INB"
                                else:
                                    return "ONE"
                        else:
                            # if Nest_Dist_RT_RB <= 388.1687316895
                            if _get(features, "Nest_Dist_RT_RB") <= 388.1687316895:
                                return "INB"
                            else:
                                # if Nest_Dist_RT_To_Bbox_BL <= 520.1252136230
                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 520.1252136230:
                                    return "OE"
                                else:
                                    # if Nest_Dist_RR_To_Bbox_BR <= 247.5020217896
                                    if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 247.5020217896:
                                        return "INB"
                                    else:
                                        return "ONE"
                    else:
                        # if Nest_Dist_RL_RT <= 430.0665283203
                        if _get(features, "Nest_Dist_RL_RT") <= 430.0665283203:
                            return "INB"
                        else:
                            # if c1_Mouse_Distance <= 823.8109741211
                            if _get(features, "c1_Mouse_Distance") <= 823.8109741211:
                                return "OE"
                            else:
                                # if Nest_Centroid_To_Bbox_BR <= 389.0841674805
                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 389.0841674805:
                                    # if Actor_Dist_RR_To_Bbox_BR <= 21.5238742828
                                    if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 21.5238742828:
                                        return "INB"
                                    else:
                                        return "ONE"
                                else:
                                    return "OE"

# --- Wrapper / helpers ---

# --- learned/baked config ---
RATIO_FEATURE  = 'NA'
RATIO_THRESH   = 0.0
RATIO_FLIP     = False

def _unify_cols(cols):
    out = []
    for c in cols:
        if isinstance(c, str) and c.startswith("Mouse_"):
            out.append("Actor_" + c[len("Mouse_"):])
        elif isinstance(c, str) and c.startswith("Rat_"):
            out.append("Actor_" + c[len("Rat_"):])
        else:
            out.append(c)
    return out

def _ensure_ratio_in_df(df):
    if RATIO_FEATURE != "NA" and RATIO_FEATURE in df.columns:
        return RATIO_FEATURE
    # compute from bbox if possible
    for prefix in ["Actor_", "Rat_", "Mouse_"]:
        w, h = prefix+"bbox_w", prefix+"bbox_h"
        ar = prefix+"aspect_ratio"
        if w in df.columns and h in df.columns:
            import pandas as _pd
            df[ar] = _pd.to_numeric(df[w], errors="coerce") / _pd.to_numeric(df[h], errors="coerce")
            return ar
    return RATIO_FEATURE  # may be "NA"

def _gate_ipi_isi(x):
    # flip=False: x <= t -> IPI, else ISI
    # flip=True : x <= t -> ISI, else IPI
    if x != x:  # NaN
        return "IPI"
    if not RATIO_FLIP:
        return "IPI" if x <= RATIO_THRESH else "ISI"
    else:
        return "ISI" if x <= RATIO_THRESH else "IPI"

def _predict_ipi_isi_or_ig(ar):
    # If we trained a real IPI/ISI gate, use it; else return 'IG'
    if RATIO_FEATURE == "NA":
        return "IG"
    return _gate_ipi_isi(ar)

def predict_row(features: dict):
    route = router_tree_predict(features)  # 'IPI_ISI' or 'OTHER4'
    if route == "IPI_ISI":
        ar = _get(features, RATIO_FEATURE)
        return _predict_ipi_isi_or_ig(ar)
    else:
        return other4_tree_predict(features)

def predict_df(df, gt_col=None, unify=True, print_report=True):
    import pandas as _pd
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

    work = df.copy()
    if unify:
        work.columns = _unify_cols(work.columns)

    ratio_col = _ensure_ratio_in_df(work)

    router_cols = ['Nest_solidity', 'Actor_Mask_IoU', 'Actor_RL_x', 'c4_Mouse_Distance', 'Actor_bbox_x', 'foodhopperMid_Nest_Distance', 'Actor_centroid_x', 'foodhopperMid_Mouse_Distance', 'Nest_hu_0', 'Nest_centroid_x', 'c3_Nest_Distance', 'foodhopperRight_Mouse_Distance', 'c2_Nest_Distance', 'Nest_RR_x', 'foodhopperRight_Nest_Distance', 'c3_Mouse_Distance', 'Nest_RB_x', 'c4_Nest_Distance', 'Nest_bbox_y', 'Actor_RB_x', 'Nest_area', 'c2_Mouse_Distance', 'foodhopperLeft_Nest_Distance', 'Nest_RT_y', 'Nest_RB_y', 'Nest_Mask_IoU', 'foodhopperLeft_Mouse_Distance', 'Nest_hu_1', 'Actor_RT_x', 'c1_Nest_Distance', 'Nest_Centroid_To_Bbox_BR', 'Nest_Dist_RR_To_Bbox_BR', 'Nest_centroid_y', 'Actor_Area_Diff_Abs', 'c1_Mouse_Distance', 'foodhopperBottom_Nest_Distance', 'Actor_RR_x', 'Nest_Dist_RB_RL', 'Nest_Centroid_To_Bbox_TR', 'Nest_perimeter', 'Nest_RR_y', 'Nest_hu_2', 'Nest_RL_y', 'Nest_RT_x', 'Nest_Dist_RB_To_Bbox_TL', 'Nest_Dist_RB_To_Bbox_BL', 'Nest_Dist_RR_To_Bbox_BL', 'Nest_extent', 'Nest_Dist_RB_To_Bbox_BR', 'Nest_aspect_ratio', 'Nest_Dist_RR_RB', 'Nest_bbox_x', 'Nest_Dist_RB_To_Bbox_TR', 'Actor_To_Nest_Distance', 'Nest_Dist_RR_To_Bbox_TL', 'Nest_hu_3', 'Nest_bbox_h', 'Nest_Dist_RR_To_Bbox_TR', 'Nest_orientation', 'Nest_RL_x', 'Nest_bbox_w', 'Nest_Area_Diff_Abs', 'Nest_Centroid_To_Bbox_BL', 'foodhopperBottom_Mouse_Distance', 'Nest_Dist_RL_RR', 'Nest_Dist_RL_To_Bbox_BR', 'Nest_eccentricity', 'Actor_RB_y', 'Nest_Dist_RL_To_Bbox_TR', 'Nest_Dist_RT_To_Bbox_BR', 'Nest_Centroid_To_Bbox_TL', 'Nest_Dist_RT_To_Bbox_TL', 'Nest_Dist_RT_RB', 'Nest_Dist_RT_To_Bbox_BL', 'Nest_hu_5', 'Actor_centroid_y', 'Nest_Dist_RL_RT', 'Nest_Dist_RL_To_Bbox_TL', 'Actor_Dist_RB_RL', 'Actor_Dist_RB_To_Bbox_BR', 'Actor_RT_y', 'Actor_Dist_RB_To_Bbox_BL', 'Nest_Dist_RT_RR', 'Actor_orientation', 'Nest_Dist_RT_To_Bbox_TR', 'Actor_bbox_y', 'Nest_Dist_RL_To_Bbox_BL', 'Actor_Dist_RR_RB', 'Actor_Dist_RR_To_Bbox_BR', 'Actor_Dist_RB_To_Bbox_TR', 'Actor_RR_y', 'Actor_Dist_RL_To_Bbox_BL', 'Actor_Centroid_To_Bbox_BL', 'Actor_RL_y', 'Actor_aspect_ratio', 'Actor_extent', 'Actor_Dist_RT_To_Bbox_BL', 'Actor_area', 'Actor_bbox_h', 'Actor_hu_1', 'Actor_Centroid_To_Bbox_TR', 'Actor_Dist_RL_To_Bbox_TL', 'Actor_hu_2', 'Actor_Centroid_To_Bbox_BR', 'Actor_Centroid_To_Bbox_TL', 'Actor_Dist_RL_RT', 'Actor_perimeter', 'Actor_Dist_RB_To_Bbox_TL', 'Actor_Dist_RL_To_Bbox_BR', 'Actor_hu_0', 'Actor_hu_5', 'Actor_bbox_w', 'Actor_Dist_RR_To_Bbox_TL', 'Actor_solidity', 'Actor_Dist_RL_RR', 'Actor_eccentricity', 'Actor_Dist_RT_To_Bbox_BR', 'Actor_Dist_RL_To_Bbox_TR', 'Actor_hu_3', 'Actor_Dist_RT_RB', 'Actor_Dist_RR_To_Bbox_BL', 'Nest_hu_6', 'Actor_Dist_RR_To_Bbox_TR', 'Actor_Dist_RT_To_Bbox_TL', 'Actor_To_Nest_Dist_Change', 'Actor_Dist_RT_RR', 'Actor_Dist_RT_To_Bbox_TR', 'Actor_hu_6', 'Nest_hu_4', 'Actor_hu_4', 'Actor_Direction_deg']
    o4_cols     = ['Actor_area', 'Actor_perimeter', 'Actor_centroid_x', 'Actor_centroid_y', 'Actor_bbox_x', 'Actor_bbox_y', 'Actor_bbox_w', 'Actor_bbox_h', 'Actor_aspect_ratio', 'Actor_extent', 'Actor_solidity', 'Actor_orientation', 'Actor_eccentricity', 'Actor_RL_x', 'Actor_RL_y', 'Actor_RR_x', 'Actor_RR_y', 'Actor_RT_x', 'Actor_RT_y', 'Actor_RB_x', 'Actor_RB_y', 'Actor_hu_0', 'Actor_hu_1', 'Actor_hu_2', 'Actor_hu_3', 'Actor_hu_4', 'Actor_hu_5', 'Actor_hu_6', 'Actor_Dist_RL_RR', 'Actor_Dist_RT_RB', 'Actor_Dist_RL_RT', 'Actor_Dist_RT_RR', 'Actor_Dist_RR_RB', 'Actor_Dist_RB_RL', 'Actor_Centroid_To_Bbox_TL', 'Actor_Centroid_To_Bbox_TR', 'Actor_Centroid_To_Bbox_BR', 'Actor_Centroid_To_Bbox_BL', 'Actor_Dist_RL_To_Bbox_TL', 'Actor_Dist_RL_To_Bbox_TR', 'Actor_Dist_RL_To_Bbox_BR', 'Actor_Dist_RL_To_Bbox_BL', 'Actor_Dist_RR_To_Bbox_TL', 'Actor_Dist_RR_To_Bbox_TR', 'Actor_Dist_RR_To_Bbox_BR', 'Actor_Dist_RR_To_Bbox_BL', 'Actor_Dist_RT_To_Bbox_TL', 'Actor_Dist_RT_To_Bbox_TR', 'Actor_Dist_RT_To_Bbox_BR', 'Actor_Dist_RT_To_Bbox_BL', 'Actor_Dist_RB_To_Bbox_TL', 'Actor_Dist_RB_To_Bbox_TR', 'Actor_Dist_RB_To_Bbox_BR', 'Actor_Dist_RB_To_Bbox_BL', 'Nest_area', 'Nest_perimeter', 'Nest_centroid_x', 'Nest_centroid_y', 'Nest_bbox_x', 'Nest_bbox_y', 'Nest_bbox_w', 'Nest_bbox_h', 'Nest_aspect_ratio', 'Nest_extent', 'Nest_solidity', 'Nest_orientation', 'Nest_eccentricity', 'Nest_RL_x', 'Nest_RL_y', 'Nest_RR_x', 'Nest_RR_y', 'Nest_RT_x', 'Nest_RT_y', 'Nest_RB_x', 'Nest_RB_y', 'Nest_hu_0', 'Nest_hu_1', 'Nest_hu_2', 'Nest_hu_3', 'Nest_hu_4', 'Nest_hu_5', 'Nest_hu_6', 'Nest_Dist_RL_RR', 'Nest_Dist_RT_RB', 'Nest_Dist_RL_RT', 'Nest_Dist_RT_RR', 'Nest_Dist_RR_RB', 'Nest_Dist_RB_RL', 'Nest_Centroid_To_Bbox_TL', 'Nest_Centroid_To_Bbox_TR', 'Nest_Centroid_To_Bbox_BR', 'Nest_Centroid_To_Bbox_BL', 'Nest_Dist_RL_To_Bbox_TL', 'Nest_Dist_RL_To_Bbox_TR', 'Nest_Dist_RL_To_Bbox_BR', 'Nest_Dist_RL_To_Bbox_BL', 'Nest_Dist_RR_To_Bbox_TL', 'Nest_Dist_RR_To_Bbox_TR', 'Nest_Dist_RR_To_Bbox_BR', 'Nest_Dist_RR_To_Bbox_BL', 'Nest_Dist_RT_To_Bbox_TL', 'Nest_Dist_RT_To_Bbox_TR', 'Nest_Dist_RT_To_Bbox_BR', 'Nest_Dist_RT_To_Bbox_BL', 'Nest_Dist_RB_To_Bbox_TL', 'Nest_Dist_RB_To_Bbox_TR', 'Nest_Dist_RB_To_Bbox_BR', 'Nest_Dist_RB_To_Bbox_BL', 'Actor_Area_Diff_Abs', 'Actor_Mask_IoU', 'Nest_Area_Diff_Abs', 'Nest_Mask_IoU', 'Actor_To_Nest_Distance', 'Actor_Direction_deg', 'Actor_To_Nest_Dist_Change', 'c1_Mouse_Distance', 'c1_Nest_Distance', 'c2_Mouse_Distance', 'c2_Nest_Distance', 'c3_Mouse_Distance', 'c3_Nest_Distance', 'c4_Mouse_Distance', 'c4_Nest_Distance', 'foodhopperBottom_Mouse_Distance', 'foodhopperBottom_Nest_Distance', 'foodhopperLeft_Mouse_Distance', 'foodhopperLeft_Nest_Distance', 'foodhopperRight_Mouse_Distance', 'foodhopperRight_Nest_Distance', 'foodhopperMid_Mouse_Distance', 'foodhopperMid_Nest_Distance']
    need = set(router_cols) | set(o4_cols)
    if ratio_col != "NA":
        need |= {ratio_col}

    preds = []
    for _, row in work.iterrows():
        feat_map = {k: row[k] for k in need if k in work.columns}
        preds.append(predict_row(feat_map))

    out = df.copy()
    out["Predicted_Activity"] = preds

    if gt_col is None:
        for c in df.columns:
            if "activity" in str(c).lower():
                gt_col = c
                break

    if print_report and gt_col is not None and gt_col in df.columns:
        y_true = df[gt_col].astype(str).str.strip().str.upper()
        y_pred = _pd.Series(preds, index=df.index)
        acc = accuracy_score(y_true, y_pred)
        print(f"Accuracy: {acc:.4f}")
        labs = sorted(_pd.unique(y_true))
        print(classification_report(y_true, y_pred, labels=labs, digits=3))
        print("Confusion Matrix (labels in order):", labs)
        print(confusion_matrix(y_true, y_pred, labels=labs))
    return out
