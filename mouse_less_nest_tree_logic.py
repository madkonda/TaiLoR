# AUTO-GENERATED: Pure if/else logic for hierarchical mouse classifier.

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
    # if Actor_RL_x <= 668.5000000000
    if _get(features, "Actor_RL_x") <= 668.5000000000:
        # if Actor_Mask_IoU <= 0.9115008116
        if _get(features, "Actor_Mask_IoU") <= 0.9115008116:
            # if Nest_bbox_y <= 750.5000000000
            if _get(features, "Nest_bbox_y") <= 750.5000000000:
                # if foodhopperMid_Nest_Distance <= 418.3722991943
                if _get(features, "foodhopperMid_Nest_Distance") <= 418.3722991943:
                    # if Nest_Dist_RT_To_Bbox_TL <= 9.5000000000
                    if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 9.5000000000:
                        return "IPI_ISI"
                    else:
                        # if Nest_hu_0 <= 0.1703555584
                        if _get(features, "Nest_hu_0") <= 0.1703555584:
                            # if c3_Mouse_Distance <= 770.6017456055
                            if _get(features, "c3_Mouse_Distance") <= 770.6017456055:
                                return "IPI_ISI"
                            else:
                                return "OTHER4"
                        else:
                            return "OTHER4"
                else:
                    # if Actor_centroid_x <= 733.1695861816
                    if _get(features, "Actor_centroid_x") <= 733.1695861816:
                        return "IPI_ISI"
                    else:
                        return "OTHER4"
            else:
                # if Nest_Area_Diff_Abs <= 993.2500000000
                if _get(features, "Nest_Area_Diff_Abs") <= 993.2500000000:
                    # if Actor_aspect_ratio <= 1.4664939642
                    if _get(features, "Actor_aspect_ratio") <= 1.4664939642:
                        # if Nest_RT_x <= 953.5000000000
                        if _get(features, "Nest_RT_x") <= 953.5000000000:
                            # if Nest_eccentricity <= 0.9497051239
                            if _get(features, "Nest_eccentricity") <= 0.9497051239:
                                # if Nest_centroid_y <= 894.2477722168
                                if _get(features, "Nest_centroid_y") <= 894.2477722168:
                                    # if Nest_Dist_RB_To_Bbox_BR <= 360.5013885498
                                    if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 360.5013885498:
                                        # if Nest_RB_x <= 952.0000000000
                                        if _get(features, "Nest_RB_x") <= 952.0000000000:
                                            # if Actor_Dist_RT_RB <= 158.7117767334
                                            if _get(features, "Actor_Dist_RT_RB") <= 158.7117767334:
                                                # if Actor_Dist_RB_To_Bbox_TR <= 162.5408477783
                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 162.5408477783:
                                                    return "IPI_ISI"
                                                else:
                                                    # if Actor_area <= 22414.5000000000
                                                    if _get(features, "Actor_area") <= 22414.5000000000:
                                                        # if Nest_Mask_IoU <= 0.9844741523
                                                        if _get(features, "Nest_Mask_IoU") <= 0.9844741523:
                                                            # if Actor_solidity <= 0.9689121842
                                                            if _get(features, "Actor_solidity") <= 0.9689121842:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                        else:
                                                            # if c4_Nest_Distance <= 236.2432098389
                                                            if _get(features, "c4_Nest_Distance") <= 236.2432098389:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                    else:
                                                        # if Actor_area <= 24246.2500000000
                                                        if _get(features, "Actor_area") <= 24246.2500000000:
                                                            return "IPI_ISI"
                                                        else:
                                                            # if Nest_perimeter <= 981.4026184082
                                                            if _get(features, "Nest_perimeter") <= 981.4026184082:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                            else:
                                                # if Actor_eccentricity <= 0.8608488441
                                                if _get(features, "Actor_eccentricity") <= 0.8608488441:
                                                    # if Nest_hu_3 <= 0.0001989025
                                                    if _get(features, "Nest_hu_3") <= 0.0001989025:
                                                        # if Nest_Dist_RR_To_Bbox_TR <= 83.0060234070
                                                        if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 83.0060234070:
                                                            # if Actor_Centroid_To_Bbox_BR <= 133.0361328125
                                                            if _get(features, "Actor_Centroid_To_Bbox_BR") <= 133.0361328125:
                                                                # if Actor_Dist_RR_RB <= 159.7895660400
                                                                if _get(features, "Actor_Dist_RR_RB") <= 159.7895660400:
                                                                    # if Actor_Centroid_To_Bbox_TR <= 143.7385025024
                                                                    if _get(features, "Actor_Centroid_To_Bbox_TR") <= 143.7385025024:
                                                                        return "IPI_ISI"
                                                                    else:
                                                                        return "OTHER4"
                                                                else:
                                                                    # if Actor_bbox_x <= 610.5000000000
                                                                    if _get(features, "Actor_bbox_x") <= 610.5000000000:
                                                                        # if Actor_Centroid_To_Bbox_TL <= 138.8526763916
                                                                        if _get(features, "Actor_Centroid_To_Bbox_TL") <= 138.8526763916:
                                                                            return "OTHER4"
                                                                        else:
                                                                            return "IPI_ISI"
                                                                    else:
                                                                        return "OTHER4"
                                                            else:
                                                                # if Nest_Dist_RT_To_Bbox_TR <= 37.5000000000
                                                                if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 37.5000000000:
                                                                    return "OTHER4"
                                                                else:
                                                                    # if Actor_RB_y <= 936.5000000000
                                                                    if _get(features, "Actor_RB_y") <= 936.5000000000:
                                                                        # if Nest_hu_5 <= 0.0000245000
                                                                        if _get(features, "Nest_hu_5") <= 0.0000245000:
                                                                            # if Nest_Mask_IoU <= 0.6313444376
                                                                            if _get(features, "Nest_Mask_IoU") <= 0.6313444376:
                                                                                # if Nest_bbox_x <= 878.5000000000
                                                                                if _get(features, "Nest_bbox_x") <= 878.5000000000:
                                                                                    return "OTHER4"
                                                                                else:
                                                                                    return "IPI_ISI"
                                                                            else:
                                                                                # if c3_Mouse_Distance <= 730.9718627930
                                                                                if _get(features, "c3_Mouse_Distance") <= 730.9718627930:
                                                                                    # if c3_Nest_Distance <= 534.2102355957
                                                                                    if _get(features, "c3_Nest_Distance") <= 534.2102355957:
                                                                                        return "IPI_ISI"
                                                                                    else:
                                                                                        return "OTHER4"
                                                                                else:
                                                                                    # if Actor_Dist_RT_To_Bbox_TL <= 54.0000000000
                                                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 54.0000000000:
                                                                                        # if Nest_aspect_ratio <= 1.4193404317
                                                                                        if _get(features, "Nest_aspect_ratio") <= 1.4193404317:
                                                                                            return "IPI_ISI"
                                                                                        else:
                                                                                            return "OTHER4"
                                                                                    else:
                                                                                        # if Actor_Dist_RL_To_Bbox_BR <= 209.4062881470
                                                                                        if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 209.4062881470:
                                                                                            # if Nest_aspect_ratio <= 1.5701992512
                                                                                            if _get(features, "Nest_aspect_ratio") <= 1.5701992512:
                                                                                                return "IPI_ISI"
                                                                                            else:
                                                                                                return "OTHER4"
                                                                                        else:
                                                                                            # if Nest_Dist_RB_RL <= 14.4534792900
                                                                                            if _get(features, "Nest_Dist_RB_RL") <= 14.4534792900:
                                                                                                # if Actor_RR_x <= 867.0000000000
                                                                                                if _get(features, "Actor_RR_x") <= 867.0000000000:
                                                                                                    return "OTHER4"
                                                                                                else:
                                                                                                    return "IPI_ISI"
                                                                                            else:
                                                                                                return "IPI_ISI"
                                                                        else:
                                                                            # if Actor_bbox_h <= 186.5000000000
                                                                            if _get(features, "Actor_bbox_h") <= 186.5000000000:
                                                                                return "OTHER4"
                                                                            else:
                                                                                return "IPI_ISI"
                                                                    else:
                                                                        # if Nest_hu_2 <= 0.0009573505
                                                                        if _get(features, "Nest_hu_2") <= 0.0009573505:
                                                                            return "OTHER4"
                                                                        else:
                                                                            return "IPI_ISI"
                                                        else:
                                                            # if Nest_Dist_RB_To_Bbox_BR <= 93.5053558350
                                                            if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 93.5053558350:
                                                                # if Actor_To_Nest_Distance <= 200.4193954468
                                                                if _get(features, "Actor_To_Nest_Distance") <= 200.4193954468:
                                                                    return "IPI_ISI"
                                                                else:
                                                                    return "OTHER4"
                                                            else:
                                                                # if Actor_Dist_RT_To_Bbox_BR <= 176.4795761108
                                                                if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 176.4795761108:
                                                                    return "IPI_ISI"
                                                                else:
                                                                    # if Nest_Area_Diff_Abs <= 15.5000000000
                                                                    if _get(features, "Nest_Area_Diff_Abs") <= 15.5000000000:
                                                                        return "IPI_ISI"
                                                                    else:
                                                                        # if c4_Mouse_Distance <= 364.8668518066
                                                                        if _get(features, "c4_Mouse_Distance") <= 364.8668518066:
                                                                            return "OTHER4"
                                                                        else:
                                                                            # if Actor_Dist_RL_To_Bbox_TL <= 96.5000000000
                                                                            if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 96.5000000000:
                                                                                return "OTHER4"
                                                                            else:
                                                                                return "IPI_ISI"
                                                    else:
                                                        # if Nest_Dist_RR_To_Bbox_BR <= 149.5033493042
                                                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 149.5033493042:
                                                            # if Nest_Centroid_To_Bbox_BR <= 232.3997955322
                                                            if _get(features, "Nest_Centroid_To_Bbox_BR") <= 232.3997955322:
                                                                # if Nest_hu_3 <= 0.0778727382
                                                                if _get(features, "Nest_hu_3") <= 0.0778727382:
                                                                    # if Nest_solidity <= 0.9123090506
                                                                    if _get(features, "Nest_solidity") <= 0.9123090506:
                                                                        # if Actor_hu_5 <= -0.0000792500
                                                                        if _get(features, "Actor_hu_5") <= -0.0000792500:
                                                                            return "OTHER4"
                                                                        else:
                                                                            # if Nest_Dist_RR_To_Bbox_TL <= 441.8384552002
                                                                            if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 441.8384552002:
                                                                                # if Actor_Dist_RB_To_Bbox_BR <= 6.0926816463
                                                                                if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 6.0926816463:
                                                                                    return "OTHER4"
                                                                                else:
                                                                                    # if Actor_Dist_RL_To_Bbox_BL <= 197.0000000000
                                                                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 197.0000000000:
                                                                                        # if Actor_Dist_RL_RT <= 83.9795417786
                                                                                        if _get(features, "Actor_Dist_RL_RT") <= 83.9795417786:
                                                                                            return "OTHER4"
                                                                                        else:
                                                                                            # if Actor_Centroid_To_Bbox_TR <= 114.6961822510
                                                                                            if _get(features, "Actor_Centroid_To_Bbox_TR") <= 114.6961822510:
                                                                                                # if Actor_To_Nest_Distance <= 110.6762580872
                                                                                                if _get(features, "Actor_To_Nest_Distance") <= 110.6762580872:
                                                                                                    return "IPI_ISI"
                                                                                                else:
                                                                                                    return "OTHER4"
                                                                                            else:
                                                                                                # if Actor_hu_6 <= -0.0000004215
                                                                                                if _get(features, "Actor_hu_6") <= -0.0000004215:
                                                                                                    # if Nest_Centroid_To_Bbox_TR <= 219.6247863770
                                                                                                    if _get(features, "Nest_Centroid_To_Bbox_TR") <= 219.6247863770:
                                                                                                        return "OTHER4"
                                                                                                    else:
                                                                                                        return "IPI_ISI"
                                                                                                else:
                                                                                                    # if c2_Mouse_Distance <= 933.8702697754
                                                                                                    if _get(features, "c2_Mouse_Distance") <= 933.8702697754:
                                                                                                        # if Actor_hu_0 <= 0.2490034476
                                                                                                        if _get(features, "Actor_hu_0") <= 0.2490034476:
                                                                                                            # if Actor_Dist_RT_To_Bbox_TL <= 160.5000000000
                                                                                                            if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 160.5000000000:
                                                                                                                return "IPI_ISI"
                                                                                                            else:
                                                                                                                # if Nest_Dist_RT_RB <= 217.9064788818
                                                                                                                if _get(features, "Nest_Dist_RT_RB") <= 217.9064788818:
                                                                                                                    return "IPI_ISI"
                                                                                                                else:
                                                                                                                    return "OTHER4"
                                                                                                        else:
                                                                                                            # if foodhopperBottom_Nest_Distance <= 316.1271667480
                                                                                                            if _get(features, "foodhopperBottom_Nest_Distance") <= 316.1271667480:
                                                                                                                return "IPI_ISI"
                                                                                                            else:
                                                                                                                return "OTHER4"
                                                                                                    else:
                                                                                                        # if Actor_Dist_RL_To_Bbox_TR <= 222.1034240723
                                                                                                        if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 222.1034240723:
                                                                                                            return "OTHER4"
                                                                                                        else:
                                                                                                            return "IPI_ISI"
                                                                                    else:
                                                                                        # if Actor_Dist_RR_RB <= 163.2678947449
                                                                                        if _get(features, "Actor_Dist_RR_RB") <= 163.2678947449:
                                                                                            return "IPI_ISI"
                                                                                        else:
                                                                                            return "OTHER4"
                                                                            else:
                                                                                return "OTHER4"
                                                                    else:
                                                                        # if Nest_RB_y <= 950.5000000000
                                                                        if _get(features, "Nest_RB_y") <= 950.5000000000:
                                                                            return "OTHER4"
                                                                        else:
                                                                            return "IPI_ISI"
                                                                else:
                                                                    # if Actor_hu_2 <= 0.0000594500
                                                                    if _get(features, "Actor_hu_2") <= 0.0000594500:
                                                                        return "IPI_ISI"
                                                                    else:
                                                                        return "OTHER4"
                                                            else:
                                                                return "OTHER4"
                                                        else:
                                                            return "OTHER4"
                                                else:
                                                    # if Actor_Centroid_To_Bbox_TL <= 125.8731689453
                                                    if _get(features, "Actor_Centroid_To_Bbox_TL") <= 125.8731689453:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                        else:
                                            # if Actor_Dist_RR_To_Bbox_BL <= 324.0786743164
                                            if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 324.0786743164:
                                                return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                    else:
                                        # if Actor_perimeter <= 1005.9797668457
                                        if _get(features, "Actor_perimeter") <= 1005.9797668457:
                                            return "OTHER4"
                                        else:
                                            return "IPI_ISI"
                                else:
                                    # if Nest_hu_0 <= 0.2006980255
                                    if _get(features, "Nest_hu_0") <= 0.2006980255:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                            else:
                                # if Nest_Centroid_To_Bbox_BL <= 263.6753997803
                                if _get(features, "Nest_Centroid_To_Bbox_BL") <= 263.6753997803:
                                    # if Nest_RT_x <= 594.0000000000
                                    if _get(features, "Nest_RT_x") <= 594.0000000000:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                                else:
                                    # if Nest_hu_4 <= 0.0007871660
                                    if _get(features, "Nest_hu_4") <= 0.0007871660:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                        else:
                            # if Nest_Dist_RT_RB <= 97.2907943726
                            if _get(features, "Nest_Dist_RT_RB") <= 97.2907943726:
                                # if Actor_RL_x <= 602.0000000000
                                if _get(features, "Actor_RL_x") <= 602.0000000000:
                                    return "IPI_ISI"
                                else:
                                    # if Actor_Direction_deg <= -168.8204269409
                                    if _get(features, "Actor_Direction_deg") <= -168.8204269409:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                            else:
                                # if c4_Mouse_Distance <= 370.0649719238
                                if _get(features, "c4_Mouse_Distance") <= 370.0649719238:
                                    # if c1_Mouse_Distance <= 403.5236816406
                                    if _get(features, "c1_Mouse_Distance") <= 403.5236816406:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                                else:
                                    # if Actor_area <= 38278.0000000000
                                    if _get(features, "Actor_area") <= 38278.0000000000:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                    else:
                        # if Nest_Dist_RL_To_Bbox_BL <= 17.0000000000
                        if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 17.0000000000:
                            # if Nest_Dist_RR_To_Bbox_BR <= 33.5149517059
                            if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 33.5149517059:
                                # if Actor_Dist_RR_To_Bbox_BR <= 20.5243902206
                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 20.5243902206:
                                    return "IPI_ISI"
                                else:
                                    return "OTHER4"
                            else:
                                # if Nest_extent <= 0.6860899627
                                if _get(features, "Nest_extent") <= 0.6860899627:
                                    # if c3_Nest_Distance <= 667.3489685059
                                    if _get(features, "c3_Nest_Distance") <= 667.3489685059:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                                else:
                                    return "OTHER4"
                        else:
                            # if Actor_RR_x <= 915.5000000000
                            if _get(features, "Actor_RR_x") <= 915.5000000000:
                                # if Nest_RR_x <= 963.5000000000
                                if _get(features, "Nest_RR_x") <= 963.5000000000:
                                    # if Nest_Dist_RL_To_Bbox_BL <= 68.5000000000
                                    if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 68.5000000000:
                                        # if Nest_RB_x <= 602.5000000000
                                        if _get(features, "Nest_RB_x") <= 602.5000000000:
                                            return "OTHER4"
                                        else:
                                            # if Actor_Dist_RL_RT <= 104.7340927124
                                            if _get(features, "Actor_Dist_RL_RT") <= 104.7340927124:
                                                return "OTHER4"
                                            else:
                                                # if Nest_hu_0 <= 0.1894669831
                                                if _get(features, "Nest_hu_0") <= 0.1894669831:
                                                    return "OTHER4"
                                                else:
                                                    # if Nest_orientation <= 74.1262817383
                                                    if _get(features, "Nest_orientation") <= 74.1262817383:
                                                        return "OTHER4"
                                                    else:
                                                        # if Actor_Direction_deg <= -177.5550689697
                                                        if _get(features, "Actor_Direction_deg") <= -177.5550689697:
                                                            return "OTHER4"
                                                        else:
                                                            return "IPI_ISI"
                                    else:
                                        # if Nest_RT_x <= 598.0000000000
                                        if _get(features, "Nest_RT_x") <= 598.0000000000:
                                            return "IPI_ISI"
                                        else:
                                            # if Nest_centroid_y <= 877.4192199707
                                            if _get(features, "Nest_centroid_y") <= 877.4192199707:
                                                # if Nest_Dist_RB_RL <= 114.3917655945
                                                if _get(features, "Nest_Dist_RB_RL") <= 114.3917655945:
                                                    # if Nest_Dist_RT_To_Bbox_TL <= 35.5000000000
                                                    if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 35.5000000000:
                                                        return "OTHER4"
                                                    else:
                                                        return "IPI_ISI"
                                                else:
                                                    # if Actor_Dist_RT_To_Bbox_TR <= 98.5000000000
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 98.5000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        # if Actor_hu_2 <= 0.0002537295
                                                        if _get(features, "Actor_hu_2") <= 0.0002537295:
                                                            # if Nest_aspect_ratio <= 2.2968671322
                                                            if _get(features, "Nest_aspect_ratio") <= 2.2968671322:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                        else:
                                                            return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                else:
                                    # if Nest_hu_3 <= 0.0000043700
                                    if _get(features, "Nest_hu_3") <= 0.0000043700:
                                        # if Actor_RR_y <= 835.5000000000
                                        if _get(features, "Actor_RR_y") <= 835.5000000000:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                    else:
                                        # if Actor_Dist_RB_To_Bbox_BR <= 15.5325279236
                                        if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 15.5325279236:
                                            # if Actor_Dist_RT_To_Bbox_TR <= 101.0000000000
                                            if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 101.0000000000:
                                                return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                        else:
                                            # if Actor_Dist_RL_RT <= 217.7728271484
                                            if _get(features, "Actor_Dist_RL_RT") <= 217.7728271484:
                                                # if Nest_Dist_RL_To_Bbox_TL <= 12.0000000000
                                                if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 12.0000000000:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                            else:
                                # if Actor_hu_0 <= 0.2027519643
                                if _get(features, "Actor_hu_0") <= 0.2027519643:
                                    # if Nest_RR_y <= 862.0000000000
                                    if _get(features, "Nest_RR_y") <= 862.0000000000:
                                        return "IPI_ISI"
                                    else:
                                        # if Nest_extent <= 0.4573925287
                                        if _get(features, "Nest_extent") <= 0.4573925287:
                                            # if Actor_Dist_RB_To_Bbox_BR <= 217.5023880005
                                            if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 217.5023880005:
                                                return "IPI_ISI"
                                            else:
                                                return "OTHER4"
                                        else:
                                            return "OTHER4"
                                else:
                                    # if Nest_Dist_RL_To_Bbox_BL <= 19.5000000000
                                    if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 19.5000000000:
                                        # if Actor_To_Nest_Distance <= 224.2966232300
                                        if _get(features, "Actor_To_Nest_Distance") <= 224.2966232300:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                    else:
                                        return "OTHER4"
                else:
                    # if Actor_Mask_IoU <= 0.8189760745
                    if _get(features, "Actor_Mask_IoU") <= 0.8189760745:
                        # if foodhopperLeft_Mouse_Distance <= 62.8085308075
                        if _get(features, "foodhopperLeft_Mouse_Distance") <= 62.8085308075:
                            # if Nest_RT_y <= 757.5000000000
                            if _get(features, "Nest_RT_y") <= 757.5000000000:
                                # if Nest_Dist_RT_To_Bbox_TR <= 85.0000000000
                                if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 85.0000000000:
                                    return "IPI_ISI"
                                else:
                                    # if Actor_bbox_h <= 154.5000000000
                                    if _get(features, "Actor_bbox_h") <= 154.5000000000:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                            else:
                                # if Nest_RT_x <= 782.0000000000
                                if _get(features, "Nest_RT_x") <= 782.0000000000:
                                    # if Nest_aspect_ratio <= 1.9711828232
                                    if _get(features, "Nest_aspect_ratio") <= 1.9711828232:
                                        return "OTHER4"
                                    else:
                                        # if c1_Mouse_Distance <= 447.3625793457
                                        if _get(features, "c1_Mouse_Distance") <= 447.3625793457:
                                            # if Actor_Dist_RL_RR <= 301.5143280029
                                            if _get(features, "Actor_Dist_RL_RR") <= 301.5143280029:
                                                return "IPI_ISI"
                                            else:
                                                return "OTHER4"
                                        else:
                                            return "OTHER4"
                                else:
                                    # if Nest_perimeter <= 543.8096923828
                                    if _get(features, "Nest_perimeter") <= 543.8096923828:
                                        return "IPI_ISI"
                                    else:
                                        # if Nest_hu_1 <= 0.0023623335
                                        if _get(features, "Nest_hu_1") <= 0.0023623335:
                                            return "IPI_ISI"
                                        else:
                                            # if Nest_solidity <= 0.5839284658
                                            if _get(features, "Nest_solidity") <= 0.5839284658:
                                                return "IPI_ISI"
                                            else:
                                                # if Actor_Dist_RB_To_Bbox_BL <= 16.5303030014
                                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 16.5303030014:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                        else:
                            # if Nest_Centroid_To_Bbox_BL <= 38.8641185760
                            if _get(features, "Nest_Centroid_To_Bbox_BL") <= 38.8641185760:
                                return "IPI_ISI"
                            else:
                                # if Actor_orientation <= 170.3811874390
                                if _get(features, "Actor_orientation") <= 170.3811874390:
                                    # if Nest_solidity <= 0.5669481456
                                    if _get(features, "Nest_solidity") <= 0.5669481456:
                                        return "IPI_ISI"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_TR <= 34.0147151947
                                        if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 34.0147151947:
                                            return "IPI_ISI"
                                        else:
                                            # if Actor_Dist_RL_To_Bbox_BL <= 13.5000000000
                                            if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 13.5000000000:
                                                return "IPI_ISI"
                                            else:
                                                # if foodhopperRight_Nest_Distance <= 350.0389099121
                                                if _get(features, "foodhopperRight_Nest_Distance") <= 350.0389099121:
                                                    # if Nest_hu_3 <= 0.0003557060
                                                    if _get(features, "Nest_hu_3") <= 0.0003557060:
                                                        return "OTHER4"
                                                    else:
                                                        return "IPI_ISI"
                                                else:
                                                    # if Nest_hu_1 <= 0.0019764695
                                                    if _get(features, "Nest_hu_1") <= 0.0019764695:
                                                        # if foodhopperBottom_Nest_Distance <= 180.9338455200
                                                        if _get(features, "foodhopperBottom_Nest_Distance") <= 180.9338455200:
                                                            return "IPI_ISI"
                                                        else:
                                                            return "OTHER4"
                                                    else:
                                                        # if Nest_Mask_IoU <= 0.9516286850
                                                        if _get(features, "Nest_Mask_IoU") <= 0.9516286850:
                                                            return "OTHER4"
                                                        else:
                                                            # if Actor_Dist_RB_To_Bbox_TL <= 266.1251983643
                                                            if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 266.1251983643:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                else:
                                    # if Actor_RB_x <= 725.0000000000
                                    if _get(features, "Actor_RB_x") <= 725.0000000000:
                                        return "OTHER4"
                                    else:
                                        return "IPI_ISI"
                    else:
                        # if Nest_Dist_RR_To_Bbox_BL <= 410.7561492920
                        if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 410.7561492920:
                            # if Nest_Dist_RL_RR <= 370.3355102539
                            if _get(features, "Nest_Dist_RL_RR") <= 370.3355102539:
                                # if Nest_Mask_IoU <= 0.9301631451
                                if _get(features, "Nest_Mask_IoU") <= 0.9301631451:
                                    # if Nest_Dist_RR_To_Bbox_TR <= 82.5060615540
                                    if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 82.5060615540:
                                        # if Nest_Dist_RB_To_Bbox_BL <= 86.0058403015
                                        if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 86.0058403015:
                                            # if Nest_RR_y <= 866.0000000000
                                            if _get(features, "Nest_RR_y") <= 866.0000000000:
                                                # if Nest_Dist_RB_To_Bbox_BL <= 17.5297327042
                                                if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 17.5297327042:
                                                    # if Nest_Dist_RL_To_Bbox_TL <= 52.0000000000
                                                    if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 52.0000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    return "IPI_ISI"
                                            else:
                                                return "OTHER4"
                                        else:
                                            return "OTHER4"
                                    else:
                                        # if Actor_aspect_ratio <= 0.7926829457
                                        if _get(features, "Actor_aspect_ratio") <= 0.7926829457:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                else:
                                    # if Actor_Centroid_To_Bbox_BR <= 191.6038970947
                                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 191.6038970947:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                            else:
                                # if Actor_Direction_deg <= -153.8831100464
                                if _get(features, "Actor_Direction_deg") <= -153.8831100464:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                        else:
                            return "OTHER4"
        else:
            # if Nest_Dist_RL_To_Bbox_TR <= 416.7889099121
            if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 416.7889099121:
                # if Nest_RT_x <= 953.5000000000
                if _get(features, "Nest_RT_x") <= 953.5000000000:
                    # if Nest_Centroid_To_Bbox_BR <= 231.9112777710
                    if _get(features, "Nest_Centroid_To_Bbox_BR") <= 231.9112777710:
                        # if Nest_RT_y <= 746.0000000000
                        if _get(features, "Nest_RT_y") <= 746.0000000000:
                            return "OTHER4"
                        else:
                            # if Nest_RB_y <= 946.5000000000
                            if _get(features, "Nest_RB_y") <= 946.5000000000:
                                # if foodhopperBottom_Nest_Distance <= 101.9522323608
                                if _get(features, "foodhopperBottom_Nest_Distance") <= 101.9522323608:
                                    # if Actor_Centroid_To_Bbox_BR <= 132.9716110229
                                    if _get(features, "Actor_Centroid_To_Bbox_BR") <= 132.9716110229:
                                        # if Nest_Dist_RR_RB <= 124.2935791016
                                        if _get(features, "Nest_Dist_RR_RB") <= 124.2935791016:
                                            return "OTHER4"
                                        else:
                                            return "IPI_ISI"
                                    else:
                                        return "IPI_ISI"
                                else:
                                    # if Nest_RR_x <= 1061.0000000000
                                    if _get(features, "Nest_RR_x") <= 1061.0000000000:
                                        # if Actor_centroid_y <= 811.6524658203
                                        if _get(features, "Actor_centroid_y") <= 811.6524658203:
                                            # if Actor_Centroid_To_Bbox_TL <= 115.4736328125
                                            if _get(features, "Actor_Centroid_To_Bbox_TL") <= 115.4736328125:
                                                # if Nest_Centroid_To_Bbox_BR <= 189.9007110596
                                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 189.9007110596:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                            else:
                                                # if Actor_hu_1 <= 0.0360980816
                                                if _get(features, "Actor_hu_1") <= 0.0360980816:
                                                    # if Actor_RR_x <= 948.5000000000
                                                    if _get(features, "Actor_RR_x") <= 948.5000000000:
                                                        # if Actor_To_Nest_Distance <= 253.4927749634
                                                        if _get(features, "Actor_To_Nest_Distance") <= 253.4927749634:
                                                            # if Nest_RR_y <= 915.5000000000
                                                            if _get(features, "Nest_RR_y") <= 915.5000000000:
                                                                # if Actor_RT_x <= 850.0000000000
                                                                if _get(features, "Actor_RT_x") <= 850.0000000000:
                                                                    # if Nest_RT_y <= 750.0000000000
                                                                    if _get(features, "Nest_RT_y") <= 750.0000000000:
                                                                        # if Nest_Dist_RB_To_Bbox_BL <= 231.5025863647
                                                                        if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 231.5025863647:
                                                                            return "OTHER4"
                                                                        else:
                                                                            return "IPI_ISI"
                                                                    else:
                                                                        # if foodhopperBottom_Mouse_Distance <= 224.6010589600
                                                                        if _get(features, "foodhopperBottom_Mouse_Distance") <= 224.6010589600:
                                                                            # if Nest_RR_y <= 880.5000000000
                                                                            if _get(features, "Nest_RR_y") <= 880.5000000000:
                                                                                return "IPI_ISI"
                                                                            else:
                                                                                return "OTHER4"
                                                                        else:
                                                                            # if Nest_bbox_h <= 180.5000000000
                                                                            if _get(features, "Nest_bbox_h") <= 180.5000000000:
                                                                                # if Actor_bbox_x <= 667.5000000000
                                                                                if _get(features, "Actor_bbox_x") <= 667.5000000000:
                                                                                    # if Actor_Dist_RB_To_Bbox_BL <= 38.5129871368
                                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 38.5129871368:
                                                                                        # if Nest_Dist_RB_RL <= 12.7771735191
                                                                                        if _get(features, "Nest_Dist_RB_RL") <= 12.7771735191:
                                                                                            return "OTHER4"
                                                                                        else:
                                                                                            # if Nest_Mask_IoU <= 0.8674067557
                                                                                            if _get(features, "Nest_Mask_IoU") <= 0.8674067557:
                                                                                                # if Nest_Mask_IoU <= 0.8601705730
                                                                                                if _get(features, "Nest_Mask_IoU") <= 0.8601705730:
                                                                                                    return "IPI_ISI"
                                                                                                else:
                                                                                                    return "OTHER4"
                                                                                            else:
                                                                                                return "IPI_ISI"
                                                                                    else:
                                                                                        # if Actor_RL_y <= 744.5000000000
                                                                                        if _get(features, "Actor_RL_y") <= 744.5000000000:
                                                                                            # if Nest_solidity <= 0.9335536063
                                                                                            if _get(features, "Nest_solidity") <= 0.9335536063:
                                                                                                return "IPI_ISI"
                                                                                            else:
                                                                                                # if Nest_Dist_RR_To_Bbox_TR <= 89.0057220459
                                                                                                if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 89.0057220459:
                                                                                                    return "IPI_ISI"
                                                                                                else:
                                                                                                    return "OTHER4"
                                                                                        else:
                                                                                            return "IPI_ISI"
                                                                                else:
                                                                                    # if Nest_RB_x <= 614.5000000000
                                                                                    if _get(features, "Nest_RB_x") <= 614.5000000000:
                                                                                        return "OTHER4"
                                                                                    else:
                                                                                        return "IPI_ISI"
                                                                            else:
                                                                                # if Nest_Dist_RL_RT <= 291.3016510010
                                                                                if _get(features, "Nest_Dist_RL_RT") <= 291.3016510010:
                                                                                    # if Nest_Centroid_To_Bbox_TR <= 149.4146652222
                                                                                    if _get(features, "Nest_Centroid_To_Bbox_TR") <= 149.4146652222:
                                                                                        return "IPI_ISI"
                                                                                    else:
                                                                                        return "OTHER4"
                                                                                else:
                                                                                    return "IPI_ISI"
                                                                else:
                                                                    return "OTHER4"
                                                            else:
                                                                return "OTHER4"
                                                        else:
                                                            # if Actor_RL_y <= 809.5000000000
                                                            if _get(features, "Actor_RL_y") <= 809.5000000000:
                                                                # if c2_Mouse_Distance <= 893.8361511230
                                                                if _get(features, "c2_Mouse_Distance") <= 893.8361511230:
                                                                    # if Actor_Dist_RR_To_Bbox_TR <= 78.5064849854
                                                                    if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 78.5064849854:
                                                                        return "IPI_ISI"
                                                                    else:
                                                                        return "OTHER4"
                                                                else:
                                                                    # if foodhopperLeft_Mouse_Distance <= 60.6508731842
                                                                    if _get(features, "foodhopperLeft_Mouse_Distance") <= 60.6508731842:
                                                                        # if Actor_Dist_RT_To_Bbox_TL <= 50.5000000000
                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 50.5000000000:
                                                                            return "OTHER4"
                                                                        else:
                                                                            # if Nest_Dist_RT_To_Bbox_BL <= 110.9449424744
                                                                            if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 110.9449424744:
                                                                                # if Actor_hu_2 <= 0.0008530310
                                                                                if _get(features, "Actor_hu_2") <= 0.0008530310:
                                                                                    return "IPI_ISI"
                                                                                else:
                                                                                    return "OTHER4"
                                                                            else:
                                                                                return "OTHER4"
                                                                    else:
                                                                        # if Actor_Dist_RT_To_Bbox_BR <= 179.1054611206
                                                                        if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 179.1054611206:
                                                                            return "IPI_ISI"
                                                                        else:
                                                                            return "OTHER4"
                                                            else:
                                                                return "OTHER4"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    # if Actor_solidity <= 0.7828789949
                                                    if _get(features, "Actor_solidity") <= 0.7828789949:
                                                        # if Actor_To_Nest_Dist_Change <= 0.3796192110
                                                        if _get(features, "Actor_To_Nest_Dist_Change") <= 0.3796192110:
                                                            return "IPI_ISI"
                                                        else:
                                                            # if Nest_Dist_RB_To_Bbox_BR <= 187.5026626587
                                                            if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 187.5026626587:
                                                                return "OTHER4"
                                                            else:
                                                                return "IPI_ISI"
                                                    else:
                                                        # if Actor_area <= 21954.5000000000
                                                        if _get(features, "Actor_area") <= 21954.5000000000:
                                                            return "IPI_ISI"
                                                        else:
                                                            # if Nest_hu_0 <= 0.2090718523
                                                            if _get(features, "Nest_hu_0") <= 0.2090718523:
                                                                return "IPI_ISI"
                                                            else:
                                                                return "OTHER4"
                                        else:
                                            # if Nest_Dist_RT_To_Bbox_TR <= 54.5000000000
                                            if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 54.5000000000:
                                                return "IPI_ISI"
                                            else:
                                                return "OTHER4"
                                    else:
                                        return "OTHER4"
                            else:
                                # if Nest_hu_0 <= 0.2550456226
                                if _get(features, "Nest_hu_0") <= 0.2550456226:
                                    # if Nest_RR_x <= 932.5000000000
                                    if _get(features, "Nest_RR_x") <= 932.5000000000:
                                        # if foodhopperLeft_Nest_Distance <= 120.9618835449
                                        if _get(features, "foodhopperLeft_Nest_Distance") <= 120.9618835449:
                                            return "IPI_ISI"
                                        else:
                                            # if Nest_hu_3 <= 0.0009980030
                                            if _get(features, "Nest_hu_3") <= 0.0009980030:
                                                # if Actor_Dist_RR_To_Bbox_BR <= 24.5208234787
                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 24.5208234787:
                                                    # if Nest_RT_y <= 791.5000000000
                                                    if _get(features, "Nest_RT_y") <= 791.5000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                    else:
                                        return "IPI_ISI"
                                else:
                                    # if Nest_Dist_RB_To_Bbox_BL <= 19.0275125504
                                    if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 19.0275125504:
                                        return "OTHER4"
                                    else:
                                        # if Actor_Centroid_To_Bbox_TR <= 111.0765800476
                                        if _get(features, "Actor_Centroid_To_Bbox_TR") <= 111.0765800476:
                                            return "OTHER4"
                                        else:
                                            # if Nest_hu_6 <= 0.0000008970
                                            if _get(features, "Nest_hu_6") <= 0.0000008970:
                                                # if Actor_Dist_RL_RT <= 96.6821327209
                                                if _get(features, "Actor_Dist_RL_RT") <= 96.6821327209:
                                                    # if c3_Nest_Distance <= 765.5082397461
                                                    if _get(features, "c3_Nest_Distance") <= 765.5082397461:
                                                        return "OTHER4"
                                                    else:
                                                        return "IPI_ISI"
                                                else:
                                                    return "IPI_ISI"
                                            else:
                                                return "OTHER4"
                    else:
                        return "OTHER4"
                else:
                    # if Nest_solidity <= 0.8891299963
                    if _get(features, "Nest_solidity") <= 0.8891299963:
                        # if Nest_Dist_RB_RL <= 61.8410224915
                        if _get(features, "Nest_Dist_RB_RL") <= 61.8410224915:
                            # if foodhopperMid_Nest_Distance <= 303.0269165039
                            if _get(features, "foodhopperMid_Nest_Distance") <= 303.0269165039:
                                # if Actor_perimeter <= 623.5914306641
                                if _get(features, "Actor_perimeter") <= 623.5914306641:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                return "OTHER4"
                        else:
                            return "OTHER4"
                    else:
                        # if Actor_To_Nest_Distance <= 286.0798645020
                        if _get(features, "Actor_To_Nest_Distance") <= 286.0798645020:
                            # if c4_Mouse_Distance <= 373.0554199219
                            if _get(features, "c4_Mouse_Distance") <= 373.0554199219:
                                # if Nest_Dist_RL_To_Bbox_TL <= 85.5000000000
                                if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 85.5000000000:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                return "IPI_ISI"
                        else:
                            # if Nest_orientation <= 84.5614128113
                            if _get(features, "Nest_orientation") <= 84.5614128113:
                                return "IPI_ISI"
                            else:
                                return "OTHER4"
            else:
                # if Nest_hu_6 <= 0.0000647500
                if _get(features, "Nest_hu_6") <= 0.0000647500:
                    return "OTHER4"
                else:
                    # if Nest_area <= 31594.7500000000
                    if _get(features, "Nest_area") <= 31594.7500000000:
                        return "OTHER4"
                    else:
                        return "IPI_ISI"
    else:
        # if foodhopperRight_Nest_Distance <= 383.4586181641
        if _get(features, "foodhopperRight_Nest_Distance") <= 383.4586181641:
            # if Nest_RT_x <= 964.5000000000
            if _get(features, "Nest_RT_x") <= 964.5000000000:
                # if c1_Nest_Distance <= 679.3624572754
                if _get(features, "c1_Nest_Distance") <= 679.3624572754:
                    # if Actor_Dist_RB_To_Bbox_BR <= 186.5026779175
                    if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 186.5026779175:
                        # if Nest_bbox_h <= 118.0000000000
                        if _get(features, "Nest_bbox_h") <= 118.0000000000:
                            # if Actor_Dist_RT_To_Bbox_BR <= 312.2857360840
                            if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 312.2857360840:
                                # if Actor_To_Nest_Dist_Change <= -67.8634223938
                                if _get(features, "Actor_To_Nest_Dist_Change") <= -67.8634223938:
                                    # if c1_Nest_Distance <= 674.3769836426
                                    if _get(features, "c1_Nest_Distance") <= 674.3769836426:
                                        return "OTHER4"
                                    else:
                                        return "IPI_ISI"
                                else:
                                    # if Actor_eccentricity <= 0.7381548285
                                    if _get(features, "Actor_eccentricity") <= 0.7381548285:
                                        # if Actor_To_Nest_Distance <= 179.9252548218
                                        if _get(features, "Actor_To_Nest_Distance") <= 179.9252548218:
                                            # if Nest_Dist_RB_RL <= 59.8634510040
                                            if _get(features, "Nest_Dist_RB_RL") <= 59.8634510040:
                                                return "OTHER4"
                                            else:
                                                # if Actor_Dist_RL_RR <= 265.7447204590
                                                if _get(features, "Actor_Dist_RL_RR") <= 265.7447204590:
                                                    return "IPI_ISI"
                                                else:
                                                    return "OTHER4"
                                        else:
                                            # if Actor_Dist_RL_RT <= 216.1075897217
                                            if _get(features, "Actor_Dist_RL_RT") <= 216.1075897217:
                                                # if Actor_Dist_RT_To_Bbox_TL <= 65.0000000000
                                                if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 65.0000000000:
                                                    return "OTHER4"
                                                else:
                                                    # if Actor_area <= 45603.2500000000
                                                    if _get(features, "Actor_area") <= 45603.2500000000:
                                                        # if Actor_Area_Diff_Abs <= 17028.0000000000
                                                        if _get(features, "Actor_Area_Diff_Abs") <= 17028.0000000000:
                                                            # if Actor_hu_1 <= 0.0093363696
                                                            if _get(features, "Actor_hu_1") <= 0.0093363696:
                                                                # if Actor_Dist_RR_To_Bbox_BR <= 22.5222215652
                                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 22.5222215652:
                                                                    # if Nest_orientation <= 83.9966468811
                                                                    if _get(features, "Nest_orientation") <= 83.9966468811:
                                                                        return "OTHER4"
                                                                    else:
                                                                        return "IPI_ISI"
                                                                else:
                                                                    return "IPI_ISI"
                                                            else:
                                                                return "OTHER4"
                                                        else:
                                                            return "OTHER4"
                                                    else:
                                                        return "OTHER4"
                                            else:
                                                # if Actor_Dist_RR_RB <= 188.4237213135
                                                if _get(features, "Actor_Dist_RR_RB") <= 188.4237213135:
                                                    return "OTHER4"
                                                else:
                                                    return "IPI_ISI"
                                    else:
                                        # if Actor_bbox_x <= 1141.5000000000
                                        if _get(features, "Actor_bbox_x") <= 1141.5000000000:
                                            # if Nest_aspect_ratio <= 2.9118590355
                                            if _get(features, "Nest_aspect_ratio") <= 2.9118590355:
                                                # if Nest_Area_Diff_Abs <= 4000.7500000000
                                                if _get(features, "Nest_Area_Diff_Abs") <= 4000.7500000000:
                                                    return "IPI_ISI"
                                                else:
                                                    # if Nest_Mask_IoU <= 0.7180178463
                                                    if _get(features, "Nest_Mask_IoU") <= 0.7180178463:
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
                        # if Nest_Dist_RT_To_Bbox_TL <= 34.5000000000
                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 34.5000000000:
                            return "IPI_ISI"
                        else:
                            # if Actor_Dist_RL_RR <= 237.6828002930
                            if _get(features, "Actor_Dist_RL_RR") <= 237.6828002930:
                                return "IPI_ISI"
                            else:
                                return "OTHER4"
                else:
                    # if Nest_Dist_RL_To_Bbox_TL <= 85.5000000000
                    if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 85.5000000000:
                        return "OTHER4"
                    else:
                        return "IPI_ISI"
            else:
                # if Nest_extent <= 0.6827108562
                if _get(features, "Nest_extent") <= 0.6827108562:
                    # if Actor_centroid_x <= 1214.1961669922
                    if _get(features, "Actor_centroid_x") <= 1214.1961669922:
                        # if foodhopperMid_Nest_Distance <= 290.4015655518
                        if _get(features, "foodhopperMid_Nest_Distance") <= 290.4015655518:
                            # if c1_Nest_Distance <= 674.5473022461
                            if _get(features, "c1_Nest_Distance") <= 674.5473022461:
                                # if Nest_solidity <= 0.8896165490
                                if _get(features, "Nest_solidity") <= 0.8896165490:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                # if Actor_RL_x <= 678.5000000000
                                if _get(features, "Actor_RL_x") <= 678.5000000000:
                                    # if c3_Nest_Distance <= 513.0261230469
                                    if _get(features, "c3_Nest_Distance") <= 513.0261230469:
                                        return "OTHER4"
                                    else:
                                        # if Nest_hu_2 <= 0.0011356855
                                        if _get(features, "Nest_hu_2") <= 0.0011356855:
                                            return "OTHER4"
                                        else:
                                            return "IPI_ISI"
                                else:
                                    # if Actor_Mask_IoU <= 0.9942398667
                                    if _get(features, "Actor_Mask_IoU") <= 0.9942398667:
                                        # if Nest_orientation <= 71.1078910828
                                        if _get(features, "Nest_orientation") <= 71.1078910828:
                                            return "IPI_ISI"
                                        else:
                                            # if Nest_hu_2 <= 0.0015233690
                                            if _get(features, "Nest_hu_2") <= 0.0015233690:
                                                return "OTHER4"
                                            else:
                                                # if c2_Mouse_Distance <= 806.7502746582
                                                if _get(features, "c2_Mouse_Distance") <= 806.7502746582:
                                                    return "OTHER4"
                                                else:
                                                    return "IPI_ISI"
                                    else:
                                        return "IPI_ISI"
                        else:
                            # if Actor_Dist_RL_To_Bbox_TR <= 432.4915313721
                            if _get(features, "Actor_Dist_RL_To_Bbox_TR") <= 432.4915313721:
                                return "OTHER4"
                            else:
                                return "IPI_ISI"
                    else:
                        # if Nest_Dist_RT_To_Bbox_BR <= 132.7530136108
                        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 132.7530136108:
                            return "IPI_ISI"
                        else:
                            return "OTHER4"
                else:
                    # if Nest_Dist_RB_To_Bbox_TL <= 78.7315883636
                    if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 78.7315883636:
                        return "OTHER4"
                    else:
                        return "IPI_ISI"
        else:
            # if c1_Mouse_Distance <= 478.5873565674
            if _get(features, "c1_Mouse_Distance") <= 478.5873565674:
                # if Nest_aspect_ratio <= 2.5809481144
                if _get(features, "Nest_aspect_ratio") <= 2.5809481144:
                    # if Actor_hu_0 <= 0.1636511907
                    if _get(features, "Actor_hu_0") <= 0.1636511907:
                        return "IPI_ISI"
                    else:
                        # if Nest_extent <= 0.7164552212
                        if _get(features, "Nest_extent") <= 0.7164552212:
                            # if Nest_hu_6 <= -0.0000088650
                            if _get(features, "Nest_hu_6") <= -0.0000088650:
                                return "IPI_ISI"
                            else:
                                # if Nest_Dist_RL_To_Bbox_BL <= 111.5000000000
                                if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 111.5000000000:
                                    # if Nest_aspect_ratio <= 2.4272973537
                                    if _get(features, "Nest_aspect_ratio") <= 2.4272973537:
                                        return "OTHER4"
                                    else:
                                        # if Actor_bbox_h <= 157.0000000000
                                        if _get(features, "Actor_bbox_h") <= 157.0000000000:
                                            return "OTHER4"
                                        else:
                                            return "IPI_ISI"
                                else:
                                    # if Nest_Dist_RB_To_Bbox_BR <= 229.0029258728
                                    if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 229.0029258728:
                                        return "OTHER4"
                                    else:
                                        return "IPI_ISI"
                        else:
                            # if Nest_Area_Diff_Abs <= 79.2500000000
                            if _get(features, "Nest_Area_Diff_Abs") <= 79.2500000000:
                                return "IPI_ISI"
                            else:
                                return "OTHER4"
                else:
                    # if Nest_hu_1 <= 0.0823444538
                    if _get(features, "Nest_hu_1") <= 0.0823444538:
                        return "IPI_ISI"
                    else:
                        return "OTHER4"
            else:
                # if Nest_RR_x <= 748.5000000000
                if _get(features, "Nest_RR_x") <= 748.5000000000:
                    # if Nest_Dist_RB_To_Bbox_BR <= 120.0041694641
                    if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 120.0041694641:
                        # if Nest_RT_x <= 722.5000000000
                        if _get(features, "Nest_RT_x") <= 722.5000000000:
                            return "OTHER4"
                        else:
                            return "IPI_ISI"
                    else:
                        # if Actor_Dist_RL_RT <= 143.0386657715
                        if _get(features, "Actor_Dist_RL_RT") <= 143.0386657715:
                            return "OTHER4"
                        else:
                            return "IPI_ISI"
                else:
                    # if Actor_Dist_RB_To_Bbox_TL <= 48.2130451202
                    if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 48.2130451202:
                        # if Nest_hu_4 <= 0.0001161585
                        if _get(features, "Nest_hu_4") <= 0.0001161585:
                            # if Nest_hu_4 <= 0.0001091685
                            if _get(features, "Nest_hu_4") <= 0.0001091685:
                                # if Actor_hu_1 <= 0.0006713970
                                if _get(features, "Actor_hu_1") <= 0.0006713970:
                                    # if Actor_hu_1 <= 0.0006098435
                                    if _get(features, "Actor_hu_1") <= 0.0006098435:
                                        return "OTHER4"
                                    else:
                                        return "IPI_ISI"
                                else:
                                    return "OTHER4"
                            else:
                                # if Actor_Centroid_To_Bbox_TR <= 44.6088962555
                                if _get(features, "Actor_Centroid_To_Bbox_TR") <= 44.6088962555:
                                    # if Actor_Direction_deg <= -176.8403396606
                                    if _get(features, "Actor_Direction_deg") <= -176.8403396606:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                                else:
                                    return "IPI_ISI"
                        else:
                            # if Actor_area <= 2156.2500000000
                            if _get(features, "Actor_area") <= 2156.2500000000:
                                # if Actor_Mask_IoU <= 0.9583611786
                                if _get(features, "Actor_Mask_IoU") <= 0.9583611786:
                                    # if Actor_Dist_RB_To_Bbox_TL <= 47.9112510681
                                    if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 47.9112510681:
                                        # if Actor_eccentricity <= 0.5193486512
                                        if _get(features, "Actor_eccentricity") <= 0.5193486512:
                                            return "IPI_ISI"
                                        else:
                                            # if Nest_Mask_IoU <= 0.9929978251
                                            if _get(features, "Nest_Mask_IoU") <= 0.9929978251:
                                                # if Actor_Direction_deg <= 178.1851577759
                                                if _get(features, "Actor_Direction_deg") <= 178.1851577759:
                                                    # if Actor_eccentricity <= 0.7076926827
                                                    if _get(features, "Actor_eccentricity") <= 0.7076926827:
                                                        # if Actor_Direction_deg <= 144.2226791382
                                                        if _get(features, "Actor_Direction_deg") <= 144.2226791382:
                                                            return "OTHER4"
                                                        else:
                                                            return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                                else:
                                                    # if Nest_hu_0 <= 0.3636390716
                                                    if _get(features, "Nest_hu_0") <= 0.3636390716:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                            else:
                                                return "IPI_ISI"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_BR <= 13.0538735390
                                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 13.0538735390:
                                            return "OTHER4"
                                        else:
                                            return "IPI_ISI"
                                else:
                                    # if Actor_Dist_RT_RR <= 48.0741958618
                                    if _get(features, "Actor_Dist_RT_RR") <= 48.0741958618:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                            else:
                                # if foodhopperLeft_Nest_Distance <= 166.7157745361
                                if _get(features, "foodhopperLeft_Nest_Distance") <= 166.7157745361:
                                    # if Nest_RR_x <= 999.5000000000
                                    if _get(features, "Nest_RR_x") <= 999.5000000000:
                                        return "IPI_ISI"
                                    else:
                                        return "OTHER4"
                                else:
                                    # if Nest_RL_y <= 918.5000000000
                                    if _get(features, "Nest_RL_y") <= 918.5000000000:
                                        # if Actor_Dist_RB_To_Bbox_BR <= 57.0087814331
                                        if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 57.0087814331:
                                            return "IPI_ISI"
                                        else:
                                            return "OTHER4"
                                    else:
                                        return "IPI_ISI"
                    else:
                        # if c1_Mouse_Distance <= 487.6907348633
                        if _get(features, "c1_Mouse_Distance") <= 487.6907348633:
                            # if Nest_Dist_RB_To_Bbox_BR <= 141.5035400391
                            if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 141.5035400391:
                                # if Actor_Dist_RR_RB <= 103.0822067261
                                if _get(features, "Actor_Dist_RR_RB") <= 103.0822067261:
                                    return "OTHER4"
                                else:
                                    return "IPI_ISI"
                            else:
                                # if c2_Mouse_Distance <= 812.8428649902
                                if _get(features, "c2_Mouse_Distance") <= 812.8428649902:
                                    return "IPI_ISI"
                                else:
                                    return "OTHER4"
                        else:
                            # if Nest_RB_x <= 575.0000000000
                            if _get(features, "Nest_RB_x") <= 575.0000000000:
                                return "IPI_ISI"
                            else:
                                # if Nest_RL_x <= 846.5000000000
                                if _get(features, "Nest_RL_x") <= 846.5000000000:
                                    # if Nest_centroid_x <= 641.7869873047
                                    if _get(features, "Nest_centroid_x") <= 641.7869873047:
                                        return "IPI_ISI"
                                    else:
                                        # if Actor_To_Nest_Dist_Change <= -320.1744384766
                                        if _get(features, "Actor_To_Nest_Dist_Change") <= -320.1744384766:
                                            return "IPI_ISI"
                                        else:
                                            # if Nest_extent <= 0.7301568687
                                            if _get(features, "Nest_extent") <= 0.7301568687:
                                                # if c3_Nest_Distance <= 849.5433959961
                                                if _get(features, "c3_Nest_Distance") <= 849.5433959961:
                                                    # if c1_Mouse_Distance <= 490.3459930420
                                                    if _get(features, "c1_Mouse_Distance") <= 490.3459930420:
                                                        # if Actor_Dist_RR_To_Bbox_BR <= 71.5069961548
                                                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 71.5069961548:
                                                            return "OTHER4"
                                                        else:
                                                            return "IPI_ISI"
                                                    else:
                                                        # if Nest_Centroid_To_Bbox_BR <= 66.2052764893
                                                        if _get(features, "Nest_Centroid_To_Bbox_BR") <= 66.2052764893:
                                                            # if Nest_hu_6 <= -0.0000342950
                                                            if _get(features, "Nest_hu_6") <= -0.0000342950:
                                                                return "IPI_ISI"
                                                            else:
                                                                return "OTHER4"
                                                        else:
                                                            # if c3_Nest_Distance <= 845.9859619141
                                                            if _get(features, "c3_Nest_Distance") <= 845.9859619141:
                                                                # if Nest_Centroid_To_Bbox_TL <= 255.2019577026
                                                                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 255.2019577026:
                                                                    # if Nest_Mask_IoU <= 0.6707277596
                                                                    if _get(features, "Nest_Mask_IoU") <= 0.6707277596:
                                                                        # if Actor_centroid_y <= 751.5286865234
                                                                        if _get(features, "Actor_centroid_y") <= 751.5286865234:
                                                                            return "IPI_ISI"
                                                                        else:
                                                                            return "OTHER4"
                                                                    else:
                                                                        return "OTHER4"
                                                                else:
                                                                    # if c1_Nest_Distance <= 561.2615661621
                                                                    if _get(features, "c1_Nest_Distance") <= 561.2615661621:
                                                                        return "IPI_ISI"
                                                                    else:
                                                                        # if Nest_Dist_RL_RR <= 420.2273101807
                                                                        if _get(features, "Nest_Dist_RL_RR") <= 420.2273101807:
                                                                            # if foodhopperMid_Nest_Distance <= 362.2174530029
                                                                            if _get(features, "foodhopperMid_Nest_Distance") <= 362.2174530029:
                                                                                return "IPI_ISI"
                                                                            else:
                                                                                return "OTHER4"
                                                                        else:
                                                                            return "OTHER4"
                                                            else:
                                                                # if Actor_Dist_RT_To_Bbox_TL <= 196.0000000000
                                                                if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 196.0000000000:
                                                                    return "OTHER4"
                                                                else:
                                                                    return "IPI_ISI"
                                                else:
                                                    # if Nest_bbox_h <= 58.5000000000
                                                    if _get(features, "Nest_bbox_h") <= 58.5000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        return "OTHER4"
                                            else:
                                                # if Actor_To_Nest_Dist_Change <= 12.9640069008
                                                if _get(features, "Actor_To_Nest_Dist_Change") <= 12.9640069008:
                                                    # if Actor_RB_y <= 789.5000000000
                                                    if _get(features, "Actor_RB_y") <= 789.5000000000:
                                                        return "IPI_ISI"
                                                    else:
                                                        # if Actor_extent <= 0.7971087992
                                                        if _get(features, "Actor_extent") <= 0.7971087992:
                                                            return "OTHER4"
                                                        else:
                                                            # if c4_Nest_Distance <= 242.7117767334
                                                            if _get(features, "c4_Nest_Distance") <= 242.7117767334:
                                                                return "IPI_ISI"
                                                            else:
                                                                return "OTHER4"
                                                else:
                                                    # if foodhopperRight_Nest_Distance <= 587.2677917480
                                                    if _get(features, "foodhopperRight_Nest_Distance") <= 587.2677917480:
                                                        return "OTHER4"
                                                    else:
                                                        # if c2_Nest_Distance <= 963.2875671387
                                                        if _get(features, "c2_Nest_Distance") <= 963.2875671387:
                                                            return "IPI_ISI"
                                                        else:
                                                            return "OTHER4"
                                else:
                                    return "IPI_ISI"

# --- OTHER4 tree ---
def other4_tree_predict(features):
    """features: dict[str, float] -> str class label"""
    # if Actor_bbox_y <= 736.5000000000
    if _get(features, "Actor_bbox_y") <= 736.5000000000:
        # if Nest_eccentricity <= 0.9827799201
        if _get(features, "Nest_eccentricity") <= 0.9827799201:
            # if Nest_RT_x <= 632.5000000000
            if _get(features, "Nest_RT_x") <= 632.5000000000:
                # if Nest_extent <= 0.3650372624
                if _get(features, "Nest_extent") <= 0.3650372624:
                    # if Actor_bbox_y <= 668.0000000000
                    if _get(features, "Actor_bbox_y") <= 668.0000000000:
                        # if foodhopperLeft_Nest_Distance <= 109.4079437256
                        if _get(features, "foodhopperLeft_Nest_Distance") <= 109.4079437256:
                            return "ONE"
                        else:
                            return "IM"
                    else:
                        # if Actor_bbox_x <= 1017.0000000000
                        if _get(features, "Actor_bbox_x") <= 1017.0000000000:
                            # if Nest_Dist_RT_RB <= 59.9582061768
                            if _get(features, "Nest_Dist_RT_RB") <= 59.9582061768:
                                return "INB"
                            else:
                                # if Actor_Area_Diff_Abs <= 6595.5000000000
                                if _get(features, "Actor_Area_Diff_Abs") <= 6595.5000000000:
                                    return "IM"
                                else:
                                    return "ONE"
                        else:
                            # if Nest_Dist_RL_RR <= 210.2718505859
                            if _get(features, "Nest_Dist_RL_RR") <= 210.2718505859:
                                return "IM"
                            else:
                                return "ONE"
                else:
                    # if Nest_RL_x <= 559.5000000000
                    if _get(features, "Nest_RL_x") <= 559.5000000000:
                        # if Nest_Dist_RB_To_Bbox_TR <= 270.4041900635
                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 270.4041900635:
                            # if c1_Mouse_Distance <= 549.5846862793
                            if _get(features, "c1_Mouse_Distance") <= 549.5846862793:
                                # if Nest_Centroid_To_Bbox_BL <= 174.8120193481
                                if _get(features, "Nest_Centroid_To_Bbox_BL") <= 174.8120193481:
                                    # if Actor_RB_x <= 914.0000000000
                                    if _get(features, "Actor_RB_x") <= 914.0000000000:
                                        return "IM"
                                    else:
                                        return "ONE"
                                else:
                                    return "ONE"
                            else:
                                # if Actor_Centroid_To_Bbox_BL <= 186.8664093018
                                if _get(features, "Actor_Centroid_To_Bbox_BL") <= 186.8664093018:
                                    return "IM"
                                else:
                                    return "ONE"
                        else:
                            return "INB"
                    else:
                        # if Nest_centroid_y <= 854.2174682617
                        if _get(features, "Nest_centroid_y") <= 854.2174682617:
                            # if Actor_Centroid_To_Bbox_BR <= 204.9454345703
                            if _get(features, "Actor_Centroid_To_Bbox_BR") <= 204.9454345703:
                                return "INB"
                            else:
                                # if Actor_Dist_RB_RL <= 238.0419845581
                                if _get(features, "Actor_Dist_RB_RL") <= 238.0419845581:
                                    return "IM"
                                else:
                                    return "OE"
                        else:
                            # if Nest_solidity <= 0.9267440736
                            if _get(features, "Nest_solidity") <= 0.9267440736:
                                # if Nest_Dist_RB_To_Bbox_TR <= 371.8170166016
                                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 371.8170166016:
                                    # if c1_Nest_Distance <= 535.2082519531
                                    if _get(features, "c1_Nest_Distance") <= 535.2082519531:
                                        # if Nest_Centroid_To_Bbox_TL <= 43.9791812897
                                        if _get(features, "Nest_Centroid_To_Bbox_TL") <= 43.9791812897:
                                            return "INB"
                                        else:
                                            # if Actor_Dist_RT_RB <= 124.2265205383
                                            if _get(features, "Actor_Dist_RT_RB") <= 124.2265205383:
                                                return "ONE"
                                            else:
                                                # if foodhopperRight_Mouse_Distance <= 89.5621376038
                                                if _get(features, "foodhopperRight_Mouse_Distance") <= 89.5621376038:
                                                    # if c4_Nest_Distance <= 202.3186035156
                                                    if _get(features, "c4_Nest_Distance") <= 202.3186035156:
                                                        # if Actor_RB_y <= 886.0000000000
                                                        if _get(features, "Actor_RB_y") <= 886.0000000000:
                                                            return "ONE"
                                                        else:
                                                            # if Actor_Centroid_To_Bbox_TR <= 141.3120803833
                                                            if _get(features, "Actor_Centroid_To_Bbox_TR") <= 141.3120803833:
                                                                return "ONE"
                                                            else:
                                                                return "IM"
                                                    else:
                                                        return "IM"
                                                else:
                                                    # if Actor_RR_y <= 945.5000000000
                                                    if _get(features, "Actor_RR_y") <= 945.5000000000:
                                                        # if Actor_solidity <= 0.9918538034
                                                        if _get(features, "Actor_solidity") <= 0.9918538034:
                                                            # if Nest_extent <= 0.3722363114
                                                            if _get(features, "Nest_extent") <= 0.3722363114:
                                                                # if Actor_Dist_RR_RB <= 39.9200820923
                                                                if _get(features, "Actor_Dist_RR_RB") <= 39.9200820923:
                                                                    return "ONE"
                                                                else:
                                                                    # if Actor_bbox_y <= 679.5000000000
                                                                    if _get(features, "Actor_bbox_y") <= 679.5000000000:
                                                                        # if Nest_Centroid_To_Bbox_TR <= 132.3570556641
                                                                        if _get(features, "Nest_Centroid_To_Bbox_TR") <= 132.3570556641:
                                                                            return "IM"
                                                                        else:
                                                                            return "ONE"
                                                                    else:
                                                                        return "IM"
                                                            else:
                                                                # if Actor_RR_y <= 732.5000000000
                                                                if _get(features, "Actor_RR_y") <= 732.5000000000:
                                                                    return "INB"
                                                                else:
                                                                    # if Nest_Centroid_To_Bbox_BR <= 236.9570541382
                                                                    if _get(features, "Nest_Centroid_To_Bbox_BR") <= 236.9570541382:
                                                                        # if Nest_bbox_y <= 822.5000000000
                                                                        if _get(features, "Nest_bbox_y") <= 822.5000000000:
                                                                            # if Nest_extent <= 0.7496951520
                                                                            if _get(features, "Nest_extent") <= 0.7496951520:
                                                                                # if Nest_hu_0 <= 0.2210152671
                                                                                if _get(features, "Nest_hu_0") <= 0.2210152671:
                                                                                    # if Nest_extent <= 0.6393205822
                                                                                    if _get(features, "Nest_extent") <= 0.6393205822:
                                                                                        return "IM"
                                                                                    else:
                                                                                        return "INB"
                                                                                else:
                                                                                    # if Actor_aspect_ratio <= 2.2106782198
                                                                                    if _get(features, "Actor_aspect_ratio") <= 2.2106782198:
                                                                                        # if Actor_Dist_RR_To_Bbox_BR <= 10.5476179123
                                                                                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 10.5476179123:
                                                                                            # if Nest_RB_y <= 948.5000000000
                                                                                            if _get(features, "Nest_RB_y") <= 948.5000000000:
                                                                                                return "IM"
                                                                                            else:
                                                                                                return "ONE"
                                                                                        else:
                                                                                            return "IM"
                                                                                    else:
                                                                                        # if Actor_Dist_RL_To_Bbox_BL <= 82.0000000000
                                                                                        if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 82.0000000000:
                                                                                            return "IM"
                                                                                        else:
                                                                                            return "ONE"
                                                                            else:
                                                                                # if Nest_Dist_RB_To_Bbox_TR <= 264.8641738892
                                                                                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 264.8641738892:
                                                                                    return "ONE"
                                                                                else:
                                                                                    return "IM"
                                                                        else:
                                                                            # if Actor_solidity <= 0.9623449147
                                                                            if _get(features, "Actor_solidity") <= 0.9623449147:
                                                                                return "IM"
                                                                            else:
                                                                                return "ONE"
                                                                    else:
                                                                        # if Actor_bbox_y <= 717.0000000000
                                                                        if _get(features, "Actor_bbox_y") <= 717.0000000000:
                                                                            return "INB"
                                                                        else:
                                                                            return "IM"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        return "INB"
                                    else:
                                        return "INB"
                                else:
                                    # if Nest_Dist_RB_RL <= 117.8634490967
                                    if _get(features, "Nest_Dist_RB_RL") <= 117.8634490967:
                                        return "INB"
                                    else:
                                        return "ONE"
                            else:
                                # if Nest_bbox_w <= 372.0000000000
                                if _get(features, "Nest_bbox_w") <= 372.0000000000:
                                    # if Nest_Dist_RB_To_Bbox_BL <= 80.0068664551
                                    if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 80.0068664551:
                                        return "IM"
                                    else:
                                        return "INB"
                                else:
                                    return "ONE"
            else:
                # if Actor_To_Nest_Distance <= 183.5564727783
                if _get(features, "Actor_To_Nest_Distance") <= 183.5564727783:
                    # if c2_Mouse_Distance <= 811.6156005859
                    if _get(features, "c2_Mouse_Distance") <= 811.6156005859:
                        # if Nest_bbox_h <= 113.5000000000
                        if _get(features, "Nest_bbox_h") <= 113.5000000000:
                            # if Nest_orientation <= 86.0609893799
                            if _get(features, "Nest_orientation") <= 86.0609893799:
                                # if Actor_orientation <= 85.4475708008
                                if _get(features, "Actor_orientation") <= 85.4475708008:
                                    return "OE"
                                else:
                                    # if c3_Mouse_Distance <= 687.6815490723
                                    if _get(features, "c3_Mouse_Distance") <= 687.6815490723:
                                        return "IM"
                                    else:
                                        # if foodhopperRight_Nest_Distance <= 326.6313629150
                                        if _get(features, "foodhopperRight_Nest_Distance") <= 326.6313629150:
                                            return "ONE"
                                        else:
                                            return "INB"
                            else:
                                # if Nest_Dist_RB_To_Bbox_BR <= 219.5024642944
                                if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 219.5024642944:
                                    return "OE"
                                else:
                                    return "INB"
                        else:
                            # if Actor_RB_y <= 842.5000000000
                            if _get(features, "Actor_RB_y") <= 842.5000000000:
                                # if Nest_eccentricity <= 0.9307151437
                                if _get(features, "Nest_eccentricity") <= 0.9307151437:
                                    # if Actor_Centroid_To_Bbox_TL <= 184.4727172852
                                    if _get(features, "Actor_Centroid_To_Bbox_TL") <= 184.4727172852:
                                        # if Nest_Mask_IoU <= 0.8505923450
                                        if _get(features, "Nest_Mask_IoU") <= 0.8505923450:
                                            return "IM"
                                        else:
                                            # if Nest_RT_x <= 685.5000000000
                                            if _get(features, "Nest_RT_x") <= 685.5000000000:
                                                # if c4_Nest_Distance <= 242.0855636597
                                                if _get(features, "c4_Nest_Distance") <= 242.0855636597:
                                                    return "IM"
                                                else:
                                                    return "INB"
                                            else:
                                                return "ONE"
                                    else:
                                        return "INB"
                                else:
                                    # if Actor_RB_y <= 822.5000000000
                                    if _get(features, "Actor_RB_y") <= 822.5000000000:
                                        # if Actor_Dist_RR_To_Bbox_BL <= 152.6828918457
                                        if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 152.6828918457:
                                            return "ONE"
                                        else:
                                            return "INB"
                                    else:
                                        return "IM"
                            else:
                                # if Actor_bbox_w <= 370.0000000000
                                if _get(features, "Actor_bbox_w") <= 370.0000000000:
                                    # if Actor_Mask_IoU <= 0.3735243529
                                    if _get(features, "Actor_Mask_IoU") <= 0.3735243529:
                                        # if Actor_RL_x <= 744.0000000000
                                        if _get(features, "Actor_RL_x") <= 744.0000000000:
                                            # if Nest_bbox_x <= 571.5000000000
                                            if _get(features, "Nest_bbox_x") <= 571.5000000000:
                                                return "INB"
                                            else:
                                                return "IM"
                                        else:
                                            return "ONE"
                                    else:
                                        # if Nest_Centroid_To_Bbox_BR <= 245.1016769409
                                        if _get(features, "Nest_Centroid_To_Bbox_BR") <= 245.1016769409:
                                            # if Actor_eccentricity <= 0.4580006748
                                            if _get(features, "Actor_eccentricity") <= 0.4580006748:
                                                return "ONE"
                                            else:
                                                # if Nest_Dist_RT_RB <= 181.7318954468
                                                if _get(features, "Nest_Dist_RT_RB") <= 181.7318954468:
                                                    # if Nest_orientation <= 82.9130554199
                                                    if _get(features, "Nest_orientation") <= 82.9130554199:
                                                        return "INB"
                                                    else:
                                                        # if Actor_RB_y <= 868.5000000000
                                                        if _get(features, "Actor_RB_y") <= 868.5000000000:
                                                            # if foodhopperLeft_Nest_Distance <= 195.4180908203
                                                            if _get(features, "foodhopperLeft_Nest_Distance") <= 195.4180908203:
                                                                return "OE"
                                                            else:
                                                                return "IM"
                                                        else:
                                                            return "IM"
                                                else:
                                                    # if Actor_centroid_x <= 814.1141357422
                                                    if _get(features, "Actor_centroid_x") <= 814.1141357422:
                                                        return "ONE"
                                                    else:
                                                        # if Nest_RR_y <= 831.0000000000
                                                        if _get(features, "Nest_RR_y") <= 831.0000000000:
                                                            return "INB"
                                                        else:
                                                            # if Nest_extent <= 0.7033000588
                                                            if _get(features, "Nest_extent") <= 0.7033000588:
                                                                return "IM"
                                                            else:
                                                                return "INB"
                                        else:
                                            return "ONE"
                                else:
                                    # if Nest_Centroid_To_Bbox_BL <= 221.7222595215
                                    if _get(features, "Nest_Centroid_To_Bbox_BL") <= 221.7222595215:
                                        return "INB"
                                    else:
                                        # if Actor_RT_y <= 694.5000000000
                                        if _get(features, "Actor_RT_y") <= 694.5000000000:
                                            return "INB"
                                        else:
                                            return "IM"
                    else:
                        # if Nest_Dist_RR_To_Bbox_BR <= 71.5069923401
                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 71.5069923401:
                            # if Nest_RB_x <= 586.5000000000
                            if _get(features, "Nest_RB_x") <= 586.5000000000:
                                # if Nest_eccentricity <= 0.9682156742
                                if _get(features, "Nest_eccentricity") <= 0.9682156742:
                                    # if c4_Nest_Distance <= 319.8213500977
                                    if _get(features, "c4_Nest_Distance") <= 319.8213500977:
                                        # if Actor_Dist_RT_To_Bbox_TR <= 71.0000000000
                                        if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 71.0000000000:
                                            # if Actor_RB_y <= 825.5000000000
                                            if _get(features, "Actor_RB_y") <= 825.5000000000:
                                                return "IM"
                                            else:
                                                return "INB"
                                        else:
                                            # if Actor_hu_6 <= -0.0000068600
                                            if _get(features, "Actor_hu_6") <= -0.0000068600:
                                                # if c4_Mouse_Distance <= 361.2807159424
                                                if _get(features, "c4_Mouse_Distance") <= 361.2807159424:
                                                    return "INB"
                                                else:
                                                    return "IM"
                                            else:
                                                # if Nest_hu_1 <= 0.0052897211
                                                if _get(features, "Nest_hu_1") <= 0.0052897211:
                                                    # if Actor_perimeter <= 543.1650390625
                                                    if _get(features, "Actor_perimeter") <= 543.1650390625:
                                                        return "INB"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    # if Actor_To_Nest_Distance <= 100.7691650391
                                                    if _get(features, "Actor_To_Nest_Distance") <= 100.7691650391:
                                                        return "INB"
                                                    else:
                                                        # if Actor_Dist_RT_RR <= 86.5520858765
                                                        if _get(features, "Actor_Dist_RT_RR") <= 86.5520858765:
                                                            # if Actor_RR_x <= 813.5000000000
                                                            if _get(features, "Actor_RR_x") <= 813.5000000000:
                                                                return "INB"
                                                            else:
                                                                return "IM"
                                                        else:
                                                            return "IM"
                                    else:
                                        return "INB"
                                else:
                                    return "INB"
                            else:
                                # if Actor_Dist_RB_To_Bbox_BL <= 68.5073013306
                                if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 68.5073013306:
                                    # if Nest_Mask_IoU <= 0.9761264622
                                    if _get(features, "Nest_Mask_IoU") <= 0.9761264622:
                                        # if foodhopperLeft_Nest_Distance <= 163.2992401123
                                        if _get(features, "foodhopperLeft_Nest_Distance") <= 163.2992401123:
                                            # if foodhopperLeft_Nest_Distance <= 95.2135429382
                                            if _get(features, "foodhopperLeft_Nest_Distance") <= 95.2135429382:
                                                return "IM"
                                            else:
                                                # if Actor_bbox_x <= 664.0000000000
                                                if _get(features, "Actor_bbox_x") <= 664.0000000000:
                                                    # if Actor_Centroid_To_Bbox_TL <= 82.0926589966
                                                    if _get(features, "Actor_Centroid_To_Bbox_TL") <= 82.0926589966:
                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    # if Nest_area <= 43300.2500000000
                                                    if _get(features, "Nest_area") <= 43300.2500000000:
                                                        return "IM"
                                                    else:
                                                        return "INB"
                                        else:
                                            # if c2_Nest_Distance <= 877.8423767090
                                            if _get(features, "c2_Nest_Distance") <= 877.8423767090:
                                                # if Actor_RB_y <= 871.5000000000
                                                if _get(features, "Actor_RB_y") <= 871.5000000000:
                                                    # if Actor_Dist_RB_To_Bbox_BL <= 53.0094871521
                                                    if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 53.0094871521:
                                                        # if Nest_Dist_RB_To_Bbox_TL <= 58.2952194214
                                                        if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 58.2952194214:
                                                            return "IM"
                                                        else:
                                                            return "INB"
                                                    else:
                                                        # if Nest_hu_0 <= 0.4045561701
                                                        if _get(features, "Nest_hu_0") <= 0.4045561701:
                                                            return "OE"
                                                        else:
                                                            # if Nest_Dist_RR_To_Bbox_BR <= 48.0109920502
                                                            if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 48.0109920502:
                                                                return "IM"
                                                            else:
                                                                return "INB"
                                                else:
                                                    # if Nest_extent <= 0.4496359527
                                                    if _get(features, "Nest_extent") <= 0.4496359527:
                                                        return "INB"
                                                    else:
                                                        # if Nest_area <= 34774.7500000000
                                                        if _get(features, "Nest_area") <= 34774.7500000000:
                                                            # if Actor_Area_Diff_Abs <= 8724.5000000000
                                                            if _get(features, "Actor_Area_Diff_Abs") <= 8724.5000000000:
                                                                # if Nest_Dist_RB_RL <= 24.2405211926
                                                                if _get(features, "Nest_Dist_RB_RL") <= 24.2405211926:
                                                                    return "INB"
                                                                else:
                                                                    # if Nest_Mask_IoU <= 0.9756872058
                                                                    if _get(features, "Nest_Mask_IoU") <= 0.9756872058:
                                                                        return "IM"
                                                                    else:
                                                                        return "INB"
                                                            else:
                                                                return "INB"
                                                        else:
                                                            return "INB"
                                            else:
                                                # if Nest_hu_0 <= 0.1758007556
                                                if _get(features, "Nest_hu_0") <= 0.1758007556:
                                                    return "INB"
                                                else:
                                                    return "IM"
                                    else:
                                        # if Nest_area <= 36291.2500000000
                                        if _get(features, "Nest_area") <= 36291.2500000000:
                                            # if foodhopperRight_Nest_Distance <= 395.0695495605
                                            if _get(features, "foodhopperRight_Nest_Distance") <= 395.0695495605:
                                                return "ONE"
                                            else:
                                                return "IM"
                                        else:
                                            return "ONE"
                                else:
                                    # if Nest_Dist_RB_To_Bbox_BR <= 173.5028762817
                                    if _get(features, "Nest_Dist_RB_To_Bbox_BR") <= 173.5028762817:
                                        # if Actor_solidity <= 0.9461060762
                                        if _get(features, "Actor_solidity") <= 0.9461060762:
                                            # if Nest_bbox_h <= 91.5000000000
                                            if _get(features, "Nest_bbox_h") <= 91.5000000000:
                                                # if Actor_Dist_RB_To_Bbox_TR <= 227.6431274414
                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 227.6431274414:
                                                    return "OE"
                                                else:
                                                    return "IM"
                                            else:
                                                # if Actor_Mask_IoU <= 0.5612772405
                                                if _get(features, "Actor_Mask_IoU") <= 0.5612772405:
                                                    # if Nest_Dist_RT_RR <= 169.2548828125
                                                    if _get(features, "Nest_Dist_RT_RR") <= 169.2548828125:
                                                        return "IM"
                                                    else:
                                                        # if Actor_solidity <= 0.8848785162
                                                        if _get(features, "Actor_solidity") <= 0.8848785162:
                                                            return "ONE"
                                                        else:
                                                            return "INB"
                                                else:
                                                    # if Actor_Dist_RL_To_Bbox_BR <= 218.1348571777
                                                    if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 218.1348571777:
                                                        return "IM"
                                                    else:
                                                        # if Actor_hu_1 <= 0.0001480990
                                                        if _get(features, "Actor_hu_1") <= 0.0001480990:
                                                            return "IM"
                                                        else:
                                                            return "INB"
                                        else:
                                            # if Nest_Dist_RB_To_Bbox_TL <= 127.4793395996
                                            if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 127.4793395996:
                                                # if c4_Mouse_Distance <= 373.4349212646
                                                if _get(features, "c4_Mouse_Distance") <= 373.4349212646:
                                                    # if Nest_hu_5 <= 0.0000680760
                                                    if _get(features, "Nest_hu_5") <= 0.0000680760:
                                                        return "INB"
                                                    else:
                                                        return "OE"
                                                else:
                                                    return "IM"
                                            else:
                                                return "IM"
                                    else:
                                        # if Actor_bbox_w <= 172.0000000000
                                        if _get(features, "Actor_bbox_w") <= 172.0000000000:
                                            return "IM"
                                        else:
                                            # if Nest_hu_0 <= 0.5260623991
                                            if _get(features, "Nest_hu_0") <= 0.5260623991:
                                                # if c1_Nest_Distance <= 497.7704010010
                                                if _get(features, "c1_Nest_Distance") <= 497.7704010010:
                                                    return "IM"
                                                else:
                                                    # if Nest_RL_y <= 929.5000000000
                                                    if _get(features, "Nest_RL_y") <= 929.5000000000:
                                                        # if Nest_Dist_RB_To_Bbox_BL <= 151.0033111572
                                                        if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 151.0033111572:
                                                            # if Actor_Direction_deg <= 179.4451828003
                                                            if _get(features, "Actor_Direction_deg") <= 179.4451828003:
                                                                # if Actor_hu_4 <= -0.0000003590
                                                                if _get(features, "Actor_hu_4") <= -0.0000003590:
                                                                    return "IM"
                                                                else:
                                                                    # if Actor_To_Nest_Dist_Change <= -51.1027603149
                                                                    if _get(features, "Actor_To_Nest_Dist_Change") <= -51.1027603149:
                                                                        return "IM"
                                                                    else:
                                                                        # if Actor_hu_1 <= 0.0003336875
                                                                        if _get(features, "Actor_hu_1") <= 0.0003336875:
                                                                            # if Nest_hu_4 <= 0.0001200085
                                                                            if _get(features, "Nest_hu_4") <= 0.0001200085:
                                                                                return "IM"
                                                                            else:
                                                                                return "INB"
                                                                        else:
                                                                            # if Actor_Centroid_To_Bbox_TR <= 214.7240905762
                                                                            if _get(features, "Actor_Centroid_To_Bbox_TR") <= 214.7240905762:
                                                                                # if Nest_Centroid_To_Bbox_BR <= 244.3006668091
                                                                                if _get(features, "Nest_Centroid_To_Bbox_BR") <= 244.3006668091:
                                                                                    return "INB"
                                                                                else:
                                                                                    # if Nest_Dist_RL_To_Bbox_TL <= 114.0000000000
                                                                                    if _get(features, "Nest_Dist_RL_To_Bbox_TL") <= 114.0000000000:
                                                                                        return "IM"
                                                                                    else:
                                                                                        return "INB"
                                                                            else:
                                                                                # if foodhopperMid_Mouse_Distance <= 303.7663726807
                                                                                if _get(features, "foodhopperMid_Mouse_Distance") <= 303.7663726807:
                                                                                    return "IM"
                                                                                else:
                                                                                    return "INB"
                                                            else:
                                                                return "IM"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        # if c4_Nest_Distance <= 321.0200500488
                                                        if _get(features, "c4_Nest_Distance") <= 321.0200500488:
                                                            return "IM"
                                                        else:
                                                            return "INB"
                                            else:
                                                # if Nest_Dist_RR_To_Bbox_TL <= 486.7416381836
                                                if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 486.7416381836:
                                                    return "INB"
                                                else:
                                                    return "IM"
                        else:
                            # if Nest_RT_x <= 867.5000000000
                            if _get(features, "Nest_RT_x") <= 867.5000000000:
                                # if Nest_Dist_RT_To_Bbox_BR <= 265.4151306152
                                if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 265.4151306152:
                                    # if Nest_hu_1 <= 0.0416295193
                                    if _get(features, "Nest_hu_1") <= 0.0416295193:
                                        # if Actor_centroid_y <= 798.3324584961
                                        if _get(features, "Actor_centroid_y") <= 798.3324584961:
                                            # if Actor_RB_y <= 824.0000000000
                                            if _get(features, "Actor_RB_y") <= 824.0000000000:
                                                # if Actor_Dist_RB_To_Bbox_TL <= 152.6908950806
                                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 152.6908950806:
                                                    # if Actor_hu_3 <= 0.0002159985
                                                    if _get(features, "Actor_hu_3") <= 0.0002159985:
                                                        return "IM"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    # if Nest_Area_Diff_Abs <= 848.0000000000
                                                    if _get(features, "Nest_Area_Diff_Abs") <= 848.0000000000:
                                                        return "IM"
                                                    else:
                                                        # if Actor_perimeter <= 563.6086730957
                                                        if _get(features, "Actor_perimeter") <= 563.6086730957:
                                                            return "IM"
                                                        else:
                                                            return "INB"
                                            else:
                                                # if Actor_Centroid_To_Bbox_BR <= 118.1437416077
                                                if _get(features, "Actor_Centroid_To_Bbox_BR") <= 118.1437416077:
                                                    return "ONE"
                                                else:
                                                    # if Actor_Dist_RT_To_Bbox_TR <= 165.5000000000
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 165.5000000000:
                                                        return "INB"
                                                    else:
                                                        # if Actor_Dist_RT_To_Bbox_BL <= 204.8388442993
                                                        if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 204.8388442993:
                                                            return "IM"
                                                        else:
                                                            return "INB"
                                        else:
                                            # if Actor_Direction_deg <= 150.1323127747
                                            if _get(features, "Actor_Direction_deg") <= 150.1323127747:
                                                return "IM"
                                            else:
                                                return "INB"
                                    else:
                                        # if Nest_Centroid_To_Bbox_TR <= 226.8796157837
                                        if _get(features, "Nest_Centroid_To_Bbox_TR") <= 226.8796157837:
                                            # if Nest_bbox_y <= 794.5000000000
                                            if _get(features, "Nest_bbox_y") <= 794.5000000000:
                                                # if Actor_Dist_RB_To_Bbox_TR <= 184.9233932495
                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 184.9233932495:
                                                    # if Nest_RB_y <= 958.5000000000
                                                    if _get(features, "Nest_RB_y") <= 958.5000000000:
                                                        return "ONE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    # if Actor_Direction_deg <= -173.7613830566
                                                    if _get(features, "Actor_Direction_deg") <= -173.7613830566:
                                                        return "ONE"
                                                    else:
                                                        # if Nest_Area_Diff_Abs <= 12539.7500000000
                                                        if _get(features, "Nest_Area_Diff_Abs") <= 12539.7500000000:
                                                            # if c3_Mouse_Distance <= 835.8265991211
                                                            if _get(features, "c3_Mouse_Distance") <= 835.8265991211:
                                                                return "IM"
                                                            else:
                                                                return "INB"
                                                        else:
                                                            return "INB"
                                            else:
                                                # if foodhopperRight_Nest_Distance <= 550.0313415527
                                                if _get(features, "foodhopperRight_Nest_Distance") <= 550.0313415527:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                        else:
                                            return "INB"
                                else:
                                    # if Nest_perimeter <= 871.4061889648
                                    if _get(features, "Nest_perimeter") <= 871.4061889648:
                                        # if foodhopperBottom_Mouse_Distance <= 303.8945617676
                                        if _get(features, "foodhopperBottom_Mouse_Distance") <= 303.8945617676:
                                            return "INB"
                                        else:
                                            return "ONE"
                                    else:
                                        # if c1_Mouse_Distance <= 472.3278198242
                                        if _get(features, "c1_Mouse_Distance") <= 472.3278198242:
                                            # if Nest_bbox_y <= 776.5000000000
                                            if _get(features, "Nest_bbox_y") <= 776.5000000000:
                                                # if Actor_Direction_deg <= 177.8080062866
                                                if _get(features, "Actor_Direction_deg") <= 177.8080062866:
                                                    # if foodhopperMid_Mouse_Distance <= 276.4852905273
                                                    if _get(features, "foodhopperMid_Mouse_Distance") <= 276.4852905273:
                                                        return "ONE"
                                                    else:
                                                        # if Nest_hu_5 <= 0.0020569341
                                                        if _get(features, "Nest_hu_5") <= 0.0020569341:
                                                            return "INB"
                                                        else:
                                                            # if Nest_area <= 39169.0000000000
                                                            if _get(features, "Nest_area") <= 39169.0000000000:
                                                                # if c3_Nest_Distance <= 690.9290771484
                                                                if _get(features, "c3_Nest_Distance") <= 690.9290771484:
                                                                    return "ONE"
                                                                else:
                                                                    return "IM"
                                                            else:
                                                                return "INB"
                                                else:
                                                    return "ONE"
                                            else:
                                                # if Actor_Area_Diff_Abs <= 2560.0000000000
                                                if _get(features, "Actor_Area_Diff_Abs") <= 2560.0000000000:
                                                    return "INB"
                                                else:
                                                    return "IM"
                                        else:
                                            # if Nest_hu_5 <= 0.0001782795
                                            if _get(features, "Nest_hu_5") <= 0.0001782795:
                                                return "INB"
                                            else:
                                                # if Actor_hu_5 <= -0.0000444300
                                                if _get(features, "Actor_hu_5") <= -0.0000444300:
                                                    return "ONE"
                                                else:
                                                    return "IM"
                            else:
                                # if Actor_RL_x <= 702.5000000000
                                if _get(features, "Actor_RL_x") <= 702.5000000000:
                                    # if Nest_RB_x <= 574.5000000000
                                    if _get(features, "Nest_RB_x") <= 574.5000000000:
                                        # if Nest_Dist_RL_RR <= 470.1677856445
                                        if _get(features, "Nest_Dist_RL_RR") <= 470.1677856445:
                                            return "IM"
                                        else:
                                            return "INB"
                                    else:
                                        # if Nest_Dist_RR_To_Bbox_BR <= 73.0068511963
                                        if _get(features, "Nest_Dist_RR_To_Bbox_BR") <= 73.0068511963:
                                            # if Actor_Dist_RL_To_Bbox_TL <= 104.0000000000
                                            if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 104.0000000000:
                                                return "IM"
                                            else:
                                                return "INB"
                                        else:
                                            # if Nest_eccentricity <= 0.9538711607
                                            if _get(features, "Nest_eccentricity") <= 0.9538711607:
                                                return "INB"
                                            else:
                                                # if Actor_Area_Diff_Abs <= 410.2500000000
                                                if _get(features, "Actor_Area_Diff_Abs") <= 410.2500000000:
                                                    return "IM"
                                                else:
                                                    return "INB"
                                else:
                                    # if Actor_Dist_RL_To_Bbox_BR <= 196.4109497070
                                    if _get(features, "Actor_Dist_RL_To_Bbox_BR") <= 196.4109497070:
                                        return "ONE"
                                    else:
                                        return "IM"
                else:
                    # if Nest_RB_y <= 950.5000000000
                    if _get(features, "Nest_RB_y") <= 950.5000000000:
                        # if Nest_Dist_RL_RT <= 80.3554229736
                        if _get(features, "Nest_Dist_RL_RT") <= 80.3554229736:
                            # if Actor_Dist_RL_RR <= 291.7455902100
                            if _get(features, "Actor_Dist_RL_RR") <= 291.7455902100:
                                # if Nest_Dist_RT_RB <= 97.1467971802
                                if _get(features, "Nest_Dist_RT_RB") <= 97.1467971802:
                                    # if Actor_Dist_RR_To_Bbox_BR <= 57.5086956024
                                    if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 57.5086956024:
                                        # if Nest_hu_3 <= 0.0000058750
                                        if _get(features, "Nest_hu_3") <= 0.0000058750:
                                            return "OE"
                                        else:
                                            # if Actor_Centroid_To_Bbox_TR <= 149.4554061890
                                            if _get(features, "Actor_Centroid_To_Bbox_TR") <= 149.4554061890:
                                                return "IM"
                                            else:
                                                return "INB"
                                    else:
                                        # if Nest_Centroid_To_Bbox_BR <= 89.4390945435
                                        if _get(features, "Nest_Centroid_To_Bbox_BR") <= 89.4390945435:
                                            # if Actor_Centroid_To_Bbox_TR <= 175.6518020630
                                            if _get(features, "Actor_Centroid_To_Bbox_TR") <= 175.6518020630:
                                                return "IM"
                                            else:
                                                return "ONE"
                                        else:
                                            # if Actor_centroid_x <= 1199.5593261719
                                            if _get(features, "Actor_centroid_x") <= 1199.5593261719:
                                                # if Nest_extent <= 0.7560068071
                                                if _get(features, "Nest_extent") <= 0.7560068071:
                                                    # if Actor_Centroid_To_Bbox_TR <= 122.4889183044
                                                    if _get(features, "Actor_Centroid_To_Bbox_TR") <= 122.4889183044:
                                                        # if Actor_Centroid_To_Bbox_TL <= 132.4273147583
                                                        if _get(features, "Actor_Centroid_To_Bbox_TL") <= 132.4273147583:
                                                            return "OE"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    return "OE"
                                            else:
                                                return "INB"
                                else:
                                    # if Actor_bbox_x <= 1059.0000000000
                                    if _get(features, "Actor_bbox_x") <= 1059.0000000000:
                                        # if Actor_aspect_ratio <= 1.0735967159
                                        if _get(features, "Actor_aspect_ratio") <= 1.0735967159:
                                            # if Actor_bbox_w <= 181.5000000000
                                            if _get(features, "Actor_bbox_w") <= 181.5000000000:
                                                return "INB"
                                            else:
                                                return "IM"
                                        else:
                                            # if Actor_bbox_h <= 221.0000000000
                                            if _get(features, "Actor_bbox_h") <= 221.0000000000:
                                                # if Nest_Dist_RL_To_Bbox_BL <= 110.0000000000
                                                if _get(features, "Nest_Dist_RL_To_Bbox_BL") <= 110.0000000000:
                                                    # if foodhopperLeft_Mouse_Distance <= 529.5047302246
                                                    if _get(features, "foodhopperLeft_Mouse_Distance") <= 529.5047302246:
                                                        # if Actor_Dist_RB_RL <= 68.1248779297
                                                        if _get(features, "Actor_Dist_RB_RL") <= 68.1248779297:
                                                            return "IM"
                                                        else:
                                                            return "OE"
                                                    else:
                                                        return "INB"
                                                else:
                                                    # if Actor_Dist_RT_To_Bbox_BR <= 219.7959442139
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 219.7959442139:
                                                        return "INB"
                                                    else:
                                                        return "ONE"
                                            else:
                                                return "INB"
                                    else:
                                        # if Actor_bbox_x <= 1070.5000000000
                                        if _get(features, "Actor_bbox_x") <= 1070.5000000000:
                                            # if Nest_Dist_RR_To_Bbox_TL <= 170.6795196533
                                            if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 170.6795196533:
                                                # if Actor_Area_Diff_Abs <= 21.0000000000
                                                if _get(features, "Actor_Area_Diff_Abs") <= 21.0000000000:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                            else:
                                                # if Nest_hu_1 <= 0.0119533152
                                                if _get(features, "Nest_hu_1") <= 0.0119533152:
                                                    return "IM"
                                                else:
                                                    # if Nest_centroid_y <= 849.6574096680
                                                    if _get(features, "Nest_centroid_y") <= 849.6574096680:
                                                        return "INB"
                                                    else:
                                                        return "ONE"
                                        else:
                                            # if Nest_Area_Diff_Abs <= 1017.5000000000
                                            if _get(features, "Nest_Area_Diff_Abs") <= 1017.5000000000:
                                                return "ONE"
                                            else:
                                                # if Nest_hu_6 <= 0.0000243027
                                                if _get(features, "Nest_hu_6") <= 0.0000243027:
                                                    return "INB"
                                                else:
                                                    return "OE"
                            else:
                                # if Nest_RL_y <= 817.0000000000
                                if _get(features, "Nest_RL_y") <= 817.0000000000:
                                    # if Actor_Area_Diff_Abs <= 5592.5000000000
                                    if _get(features, "Actor_Area_Diff_Abs") <= 5592.5000000000:
                                        # if Nest_Dist_RL_To_Bbox_TR <= 149.2282333374
                                        if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 149.2282333374:
                                            return "IM"
                                        else:
                                            return "OE"
                                    else:
                                        # if Actor_RT_x <= 566.0000000000
                                        if _get(features, "Actor_RT_x") <= 566.0000000000:
                                            return "IM"
                                        else:
                                            return "INB"
                                else:
                                    # if foodhopperBottom_Nest_Distance <= 100.9803962708
                                    if _get(features, "foodhopperBottom_Nest_Distance") <= 100.9803962708:
                                        return "ONE"
                                    else:
                                        # if Actor_area <= 86083.7500000000
                                        if _get(features, "Actor_area") <= 86083.7500000000:
                                            # if c4_Mouse_Distance <= 290.4972229004
                                            if _get(features, "c4_Mouse_Distance") <= 290.4972229004:
                                                return "IM"
                                            else:
                                                # if Nest_RB_y <= 870.5000000000
                                                if _get(features, "Nest_RB_y") <= 870.5000000000:
                                                    # if Nest_Dist_RR_To_Bbox_BL <= 129.7581596375
                                                    if _get(features, "Nest_Dist_RR_To_Bbox_BL") <= 129.7581596375:
                                                        return "OE"
                                                    else:
                                                        return "IM"
                                                else:
                                                    return "OE"
                                        else:
                                            return "IM"
                        else:
                            # if Nest_Dist_RT_To_Bbox_BR <= 149.3599548340
                            if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 149.3599548340:
                                # if Nest_RT_x <= 956.5000000000
                                if _get(features, "Nest_RT_x") <= 956.5000000000:
                                    # if Nest_RT_x <= 891.0000000000
                                    if _get(features, "Nest_RT_x") <= 891.0000000000:
                                        # if Nest_Dist_RL_RT <= 105.1294479370
                                        if _get(features, "Nest_Dist_RL_RT") <= 105.1294479370:
                                            return "INB"
                                        else:
                                            return "OE"
                                    else:
                                        # if Actor_Centroid_To_Bbox_BR <= 130.2096405029
                                        if _get(features, "Actor_Centroid_To_Bbox_BR") <= 130.2096405029:
                                            # if Nest_hu_1 <= 0.0060421822
                                            if _get(features, "Nest_hu_1") <= 0.0060421822:
                                                # if Actor_orientation <= 86.0709686279
                                                if _get(features, "Actor_orientation") <= 86.0709686279:
                                                    # if Actor_Centroid_To_Bbox_BL <= 139.1297378540
                                                    if _get(features, "Actor_Centroid_To_Bbox_BL") <= 139.1297378540:
                                                        return "IM"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    # if Actor_RL_x <= 599.5000000000
                                                    if _get(features, "Actor_RL_x") <= 599.5000000000:
                                                        return "ONE"
                                                    else:
                                                        # if foodhopperMid_Nest_Distance <= 285.4256134033
                                                        if _get(features, "foodhopperMid_Nest_Distance") <= 285.4256134033:
                                                            return "OE"
                                                        else:
                                                            return "IM"
                                            else:
                                                # if Actor_Dist_RB_To_Bbox_TL <= 158.7649230957
                                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 158.7649230957:
                                                    # if Nest_Dist_RR_RB <= 122.2345008850
                                                    if _get(features, "Nest_Dist_RR_RB") <= 122.2345008850:
                                                        return "IM"
                                                    else:
                                                        # if Actor_RL_x <= 623.0000000000
                                                        if _get(features, "Actor_RL_x") <= 623.0000000000:
                                                            # if Nest_Area_Diff_Abs <= 16.7500000000
                                                            if _get(features, "Nest_Area_Diff_Abs") <= 16.7500000000:
                                                                return "OE"
                                                            else:
                                                                return "IM"
                                                        else:
                                                            return "ONE"
                                                else:
                                                    # if c1_Mouse_Distance <= 431.0985565186
                                                    if _get(features, "c1_Mouse_Distance") <= 431.0985565186:
                                                        # if Actor_hu_2 <= 0.0002040940
                                                        if _get(features, "Actor_hu_2") <= 0.0002040940:
                                                            return "IM"
                                                        else:
                                                            return "OE"
                                                    else:
                                                        # if Nest_Dist_RB_To_Bbox_BL <= 169.0033264160
                                                        if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 169.0033264160:
                                                            return "ONE"
                                                        else:
                                                            return "OE"
                                        else:
                                            # if Nest_Dist_RB_RL <= 110.8202590942
                                            if _get(features, "Nest_Dist_RB_RL") <= 110.8202590942:
                                                # if Nest_extent <= 0.7235914469
                                                if _get(features, "Nest_extent") <= 0.7235914469:
                                                    # if Actor_Dist_RB_To_Bbox_TR <= 176.6266479492
                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 176.6266479492:
                                                        # if Actor_hu_2 <= 0.0006060985
                                                        if _get(features, "Actor_hu_2") <= 0.0006060985:
                                                            return "IM"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        # if c4_Nest_Distance <= 274.2414245605
                                                        if _get(features, "c4_Nest_Distance") <= 274.2414245605:
                                                            return "ONE"
                                                        else:
                                                            # if Nest_aspect_ratio <= 1.4522727728
                                                            if _get(features, "Nest_aspect_ratio") <= 1.4522727728:
                                                                return "ONE"
                                                            else:
                                                                # if Nest_Dist_RB_To_Bbox_BL <= 98.0051040649
                                                                if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 98.0051040649:
                                                                    return "IM"
                                                                else:
                                                                    # if Nest_centroid_y <= 844.6203308105
                                                                    if _get(features, "Nest_centroid_y") <= 844.6203308105:
                                                                        return "ONE"
                                                                    else:
                                                                        return "IM"
                                                else:
                                                    # if Nest_bbox_x <= 895.5000000000
                                                    if _get(features, "Nest_bbox_x") <= 895.5000000000:
                                                        return "INB"
                                                    else:
                                                        return "ONE"
                                            else:
                                                # if Actor_Centroid_To_Bbox_TL <= 164.5123291016
                                                if _get(features, "Actor_Centroid_To_Bbox_TL") <= 164.5123291016:
                                                    return "ONE"
                                                else:
                                                    # if Actor_Dist_RT_To_Bbox_TL <= 146.0000000000
                                                    if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 146.0000000000:
                                                        return "IM"
                                                    else:
                                                        return "OE"
                                else:
                                    # if c4_Nest_Distance <= 479.5443420410
                                    if _get(features, "c4_Nest_Distance") <= 479.5443420410:
                                        # if Actor_Dist_RB_To_Bbox_BL <= 90.5056304932
                                        if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 90.5056304932:
                                            return "IM"
                                        else:
                                            return "OE"
                                    else:
                                        # if Actor_Dist_RB_To_Bbox_TL <= 285.7130737305
                                        if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 285.7130737305:
                                            # if Actor_RB_x <= 835.5000000000
                                            if _get(features, "Actor_RB_x") <= 835.5000000000:
                                                return "IM"
                                            else:
                                                # if Nest_Dist_RR_To_Bbox_TR <= 58.5085468292
                                                if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 58.5085468292:
                                                    return "INB"
                                                else:
                                                    # if Nest_Mask_IoU <= 0.9619426727
                                                    if _get(features, "Nest_Mask_IoU") <= 0.9619426727:
                                                        return "IM"
                                                    else:
                                                        return "ONE"
                                        else:
                                            # if Actor_Area_Diff_Abs <= 6401.5000000000
                                            if _get(features, "Actor_Area_Diff_Abs") <= 6401.5000000000:
                                                # if Nest_hu_0 <= 0.2004014999
                                                if _get(features, "Nest_hu_0") <= 0.2004014999:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                            else:
                                                return "IM"
                            else:
                                # if Nest_RB_y <= 945.5000000000
                                if _get(features, "Nest_RB_y") <= 945.5000000000:
                                    # if Nest_Dist_RB_To_Bbox_TR <= 170.4709777832
                                    if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 170.4709777832:
                                        # if Actor_Dist_RR_To_Bbox_TL <= 327.3954315186
                                        if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 327.3954315186:
                                            # if Actor_RB_y <= 868.5000000000
                                            if _get(features, "Actor_RB_y") <= 868.5000000000:
                                                # if Nest_eccentricity <= 0.8465267718
                                                if _get(features, "Nest_eccentricity") <= 0.8465267718:
                                                    # if foodhopperMid_Nest_Distance <= 290.6125488281
                                                    if _get(features, "foodhopperMid_Nest_Distance") <= 290.6125488281:
                                                        return "ONE"
                                                    else:
                                                        return "IM"
                                                else:
                                                    return "INB"
                                            else:
                                                # if Actor_Dist_RB_To_Bbox_TL <= 449.8392181396
                                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 449.8392181396:
                                                    return "IM"
                                                else:
                                                    return "ONE"
                                        else:
                                            # if Nest_bbox_h <= 144.5000000000
                                            if _get(features, "Nest_bbox_h") <= 144.5000000000:
                                                return "OE"
                                            else:
                                                return "ONE"
                                    else:
                                        # if Nest_Dist_RT_To_Bbox_TL <= 254.0000000000
                                        if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 254.0000000000:
                                            # if Actor_RT_x <= 678.0000000000
                                            if _get(features, "Actor_RT_x") <= 678.0000000000:
                                                # if foodhopperBottom_Nest_Distance <= 136.9962272644
                                                if _get(features, "foodhopperBottom_Nest_Distance") <= 136.9962272644:
                                                    return "INB"
                                                else:
                                                    return "IM"
                                            else:
                                                # if Nest_Centroid_To_Bbox_TL <= 224.8547973633
                                                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 224.8547973633:
                                                    # if Nest_bbox_y <= 803.0000000000
                                                    if _get(features, "Nest_bbox_y") <= 803.0000000000:
                                                        # if Nest_extent <= 0.6788566709
                                                        if _get(features, "Nest_extent") <= 0.6788566709:
                                                            # if Nest_Dist_RT_To_Bbox_BR <= 362.4129028320
                                                            if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 362.4129028320:
                                                                # if Actor_Dist_RB_To_Bbox_TR <= 314.5543212891
                                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 314.5543212891:
                                                                    # if Nest_Dist_RR_RB <= 99.6421661377
                                                                    if _get(features, "Nest_Dist_RR_RB") <= 99.6421661377:
                                                                        return "IM"
                                                                    else:
                                                                        # if Nest_hu_2 <= 0.0032762215
                                                                        if _get(features, "Nest_hu_2") <= 0.0032762215:
                                                                            return "INB"
                                                                        else:
                                                                            # if Actor_bbox_w <= 341.0000000000
                                                                            if _get(features, "Actor_bbox_w") <= 341.0000000000:
                                                                                return "ONE"
                                                                            else:
                                                                                return "INB"
                                                                else:
                                                                    return "IM"
                                                            else:
                                                                return "IM"
                                                        else:
                                                            # if Nest_perimeter <= 817.6416931152
                                                            if _get(features, "Nest_perimeter") <= 817.6416931152:
                                                                return "INB"
                                                            else:
                                                                return "IM"
                                                    else:
                                                        return "IM"
                                                else:
                                                    return "ONE"
                                        else:
                                            # if foodhopperMid_Mouse_Distance <= 222.3377609253
                                            if _get(features, "foodhopperMid_Mouse_Distance") <= 222.3377609253:
                                                # if Actor_Dist_RT_To_Bbox_TR <= 210.0000000000
                                                if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 210.0000000000:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                            else:
                                                # if Nest_area <= 43143.0000000000
                                                if _get(features, "Nest_area") <= 43143.0000000000:
                                                    return "IM"
                                                else:
                                                    return "OE"
                                else:
                                    # if Nest_Dist_RR_To_Bbox_TL <= 438.6045532227
                                    if _get(features, "Nest_Dist_RR_To_Bbox_TL") <= 438.6045532227:
                                        # if Nest_Dist_RB_To_Bbox_TL <= 163.9954071045
                                        if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 163.9954071045:
                                            # if Actor_Dist_RB_To_Bbox_BL <= 238.0020980835
                                            if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 238.0020980835:
                                                return "IM"
                                            else:
                                                return "OE"
                                        else:
                                            # if Actor_Dist_RB_To_Bbox_BL <= 422.5011901855
                                            if _get(features, "Actor_Dist_RB_To_Bbox_BL") <= 422.5011901855:
                                                return "IM"
                                            else:
                                                return "INB"
                                    else:
                                        # if Actor_Mask_IoU <= 0.3431767523
                                        if _get(features, "Actor_Mask_IoU") <= 0.3431767523:
                                            return "ONE"
                                        else:
                                            return "INB"
                    else:
                        # if c2_Mouse_Distance <= 682.0773620605
                        if _get(features, "c2_Mouse_Distance") <= 682.0773620605:
                            # if Nest_bbox_x <= 557.0000000000
                            if _get(features, "Nest_bbox_x") <= 557.0000000000:
                                # if Actor_perimeter <= 813.4859008789
                                if _get(features, "Actor_perimeter") <= 813.4859008789:
                                    # if Nest_Centroid_To_Bbox_TR <= 226.4017791748
                                    if _get(features, "Nest_Centroid_To_Bbox_TR") <= 226.4017791748:
                                        return "OE"
                                    else:
                                        return "ONE"
                                else:
                                    return "IM"
                            else:
                                # if Nest_centroid_y <= 886.5340881348
                                if _get(features, "Nest_centroid_y") <= 886.5340881348:
                                    # if Nest_Dist_RR_RB <= 468.4882659912
                                    if _get(features, "Nest_Dist_RR_RB") <= 468.4882659912:
                                        # if Nest_RL_y <= 952.0000000000
                                        if _get(features, "Nest_RL_y") <= 952.0000000000:
                                            # if Actor_RT_x <= 1008.5000000000
                                            if _get(features, "Actor_RT_x") <= 1008.5000000000:
                                                # if Actor_Dist_RT_RR <= 132.0101623535
                                                if _get(features, "Actor_Dist_RT_RR") <= 132.0101623535:
                                                    return "IM"
                                                else:
                                                    # if Actor_Dist_RB_To_Bbox_BR <= 187.5026702881
                                                    if _get(features, "Actor_Dist_RB_To_Bbox_BR") <= 187.5026702881:
                                                        # if Actor_Dist_RR_To_Bbox_TL <= 431.8200225830
                                                        if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 431.8200225830:
                                                            # if Actor_RB_x <= 981.5000000000
                                                            if _get(features, "Actor_RB_x") <= 981.5000000000:
                                                                return "IM"
                                                            else:
                                                                return "ONE"
                                                        else:
                                                            return "IM"
                                                    else:
                                                        # if Actor_To_Nest_Dist_Change <= -48.1487224102
                                                        if _get(features, "Actor_To_Nest_Dist_Change") <= -48.1487224102:
                                                            return "ONE"
                                                        else:
                                                            return "IM"
                                            else:
                                                return "ONE"
                                        else:
                                            return "IM"
                                    else:
                                        # if Nest_Dist_RB_To_Bbox_TR <= 555.7845458984
                                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 555.7845458984:
                                            return "IM"
                                        else:
                                            return "ONE"
                                else:
                                    # if Actor_Dist_RB_To_Bbox_TL <= 186.3176574707
                                    if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 186.3176574707:
                                        return "ONE"
                                    else:
                                        # if Nest_RL_y <= 924.0000000000
                                        if _get(features, "Nest_RL_y") <= 924.0000000000:
                                            return "INB"
                                        else:
                                            return "IM"
                        else:
                            # if Actor_Mask_IoU <= 0.5316696167
                            if _get(features, "Actor_Mask_IoU") <= 0.5316696167:
                                # if Nest_area <= 30305.2500000000
                                if _get(features, "Nest_area") <= 30305.2500000000:
                                    # if Actor_Dist_RT_To_Bbox_TR <= 82.0000000000
                                    if _get(features, "Actor_Dist_RT_To_Bbox_TR") <= 82.0000000000:
                                        return "OE"
                                    else:
                                        # if Nest_bbox_x <= 576.5000000000
                                        if _get(features, "Nest_bbox_x") <= 576.5000000000:
                                            return "IM"
                                        else:
                                            # if Actor_bbox_h <= 217.5000000000
                                            if _get(features, "Actor_bbox_h") <= 217.5000000000:
                                                return "INB"
                                            else:
                                                # if Nest_Dist_RT_To_Bbox_BL <= 275.4507141113
                                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 275.4507141113:
                                                    return "IM"
                                                else:
                                                    return "ONE"
                                else:
                                    # if foodhopperLeft_Nest_Distance <= 158.4627532959
                                    if _get(features, "foodhopperLeft_Nest_Distance") <= 158.4627532959:
                                        # if foodhopperRight_Mouse_Distance <= 316.2242889404
                                        if _get(features, "foodhopperRight_Mouse_Distance") <= 316.2242889404:
                                            return "IM"
                                        else:
                                            # if Nest_eccentricity <= 0.4723497182
                                            if _get(features, "Nest_eccentricity") <= 0.4723497182:
                                                # if Nest_Dist_RR_RB <= 279.1355285645
                                                if _get(features, "Nest_Dist_RR_RB") <= 279.1355285645:
                                                    return "IM"
                                                else:
                                                    return "ONE"
                                            else:
                                                return "ONE"
                                    else:
                                        return "IM"
                            else:
                                # if Nest_hu_0 <= 0.3042215258
                                if _get(features, "Nest_hu_0") <= 0.3042215258:
                                    # if Nest_eccentricity <= 0.4864213914
                                    if _get(features, "Nest_eccentricity") <= 0.4864213914:
                                        return "ONE"
                                    else:
                                        return "IM"
                                else:
                                    # if foodhopperLeft_Nest_Distance <= 147.4800567627
                                    if _get(features, "foodhopperLeft_Nest_Distance") <= 147.4800567627:
                                        # if Nest_hu_2 <= 0.0038796264
                                        if _get(features, "Nest_hu_2") <= 0.0038796264:
                                            return "IM"
                                        else:
                                            return "ONE"
                                    else:
                                        # if Actor_Dist_RR_To_Bbox_BR <= 156.0032043457
                                        if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 156.0032043457:
                                            # if Actor_Dist_RL_To_Bbox_BL <= 62.0000000000
                                            if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 62.0000000000:
                                                # if Actor_bbox_y <= 717.5000000000
                                                if _get(features, "Actor_bbox_y") <= 717.5000000000:
                                                    return "INB"
                                                else:
                                                    return "ONE"
                                            else:
                                                # if Actor_RT_x <= 780.0000000000
                                                if _get(features, "Actor_RT_x") <= 780.0000000000:
                                                    # if Actor_RL_x <= 607.5000000000
                                                    if _get(features, "Actor_RL_x") <= 607.5000000000:
                                                        return "IM"
                                                    else:
                                                        return "INB"
                                                else:
                                                    # if Actor_RT_x <= 954.5000000000
                                                    if _get(features, "Actor_RT_x") <= 954.5000000000:
                                                        return "IM"
                                                    else:
                                                        # if Nest_hu_1 <= 0.0819379874
                                                        if _get(features, "Nest_hu_1") <= 0.0819379874:
                                                            return "ONE"
                                                        else:
                                                            return "INB"
                                        else:
                                            return "INB"
        else:
            # if foodhopperMid_Nest_Distance <= 390.5260925293
            if _get(features, "foodhopperMid_Nest_Distance") <= 390.5260925293:
                return "OE"
            else:
                # if Nest_Centroid_To_Bbox_TL <= 213.4552383423
                if _get(features, "Nest_Centroid_To_Bbox_TL") <= 213.4552383423:
                    return "ONE"
                else:
                    return "INB"
    else:
        # if Nest_Dist_RT_RR <= 160.4898757935
        if _get(features, "Nest_Dist_RT_RR") <= 160.4898757935:
            # if Nest_Dist_RB_To_Bbox_TL <= 219.3843688965
            if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 219.3843688965:
                # if Nest_solidity <= 0.6717503369
                if _get(features, "Nest_solidity") <= 0.6717503369:
                    # if Nest_centroid_x <= 821.0084838867
                    if _get(features, "Nest_centroid_x") <= 821.0084838867:
                        # if foodhopperBottom_Mouse_Distance <= 35.7110996246
                        if _get(features, "foodhopperBottom_Mouse_Distance") <= 35.7110996246:
                            # if Nest_hu_6 <= 0.0034905390
                            if _get(features, "Nest_hu_6") <= 0.0034905390:
                                return "IM"
                            else:
                                return "OE"
                        else:
                            # if foodhopperLeft_Nest_Distance <= 108.0287818909
                            if _get(features, "foodhopperLeft_Nest_Distance") <= 108.0287818909:
                                return "IM"
                            else:
                                # if Actor_Area_Diff_Abs <= 12676.2500000000
                                if _get(features, "Actor_Area_Diff_Abs") <= 12676.2500000000:
                                    return "ONE"
                                else:
                                    return "IM"
                    else:
                        return "OE"
                else:
                    # if Nest_area <= 35641.0000000000
                    if _get(features, "Nest_area") <= 35641.0000000000:
                        # if Actor_eccentricity <= 0.9764281809
                        if _get(features, "Actor_eccentricity") <= 0.9764281809:
                            # if c1_Nest_Distance <= 537.9988403320
                            if _get(features, "c1_Nest_Distance") <= 537.9988403320:
                                # if Actor_orientation <= 91.2193527222
                                if _get(features, "Actor_orientation") <= 91.2193527222:
                                    # if c1_Nest_Distance <= 518.0592651367
                                    if _get(features, "c1_Nest_Distance") <= 518.0592651367:
                                        # if Actor_hu_2 <= 0.0006629750
                                        if _get(features, "Actor_hu_2") <= 0.0006629750:
                                            return "IM"
                                        else:
                                            return "ONE"
                                    else:
                                        # if Actor_Dist_RT_To_Bbox_BL <= 88.4500503540
                                        if _get(features, "Actor_Dist_RT_To_Bbox_BL") <= 88.4500503540:
                                            return "IM"
                                        else:
                                            return "OE"
                                else:
                                    return "IM"
                            else:
                                # if Nest_hu_3 <= 0.0012264145
                                if _get(features, "Nest_hu_3") <= 0.0012264145:
                                    # if Nest_Dist_RT_To_Bbox_TL <= 95.5000000000
                                    if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 95.5000000000:
                                        # if Actor_solidity <= 0.9329767227
                                        if _get(features, "Actor_solidity") <= 0.9329767227:
                                            return "IM"
                                        else:
                                            return "INB"
                                    else:
                                        # if Nest_Dist_RB_To_Bbox_TR <= 306.3042449951
                                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 306.3042449951:
                                            # if Actor_Dist_RL_RT <= 14.8784828186
                                            if _get(features, "Actor_Dist_RL_RT") <= 14.8784828186:
                                                return "IM"
                                            else:
                                                # if Nest_hu_5 <= 0.0002490075
                                                if _get(features, "Nest_hu_5") <= 0.0002490075:
                                                    return "ONE"
                                                else:
                                                    # if Nest_hu_2 <= 0.0028381435
                                                    if _get(features, "Nest_hu_2") <= 0.0028381435:
                                                        return "ONE"
                                                    else:
                                                        return "IM"
                                        else:
                                            return "IM"
                                else:
                                    # if Nest_Dist_RT_RR <= 141.1707077026
                                    if _get(features, "Nest_Dist_RT_RR") <= 141.1707077026:
                                        return "IM"
                                    else:
                                        return "ONE"
                        else:
                            # if Nest_Mask_IoU <= 0.9860044718
                            if _get(features, "Nest_Mask_IoU") <= 0.9860044718:
                                # if Nest_extent <= 0.6410754323
                                if _get(features, "Nest_extent") <= 0.6410754323:
                                    return "ONE"
                                else:
                                    # if Nest_orientation <= 84.8996315002
                                    if _get(features, "Nest_orientation") <= 84.8996315002:
                                        return "OE"
                                    else:
                                        return "IM"
                            else:
                                # if foodhopperMid_Mouse_Distance <= 206.2021636963
                                if _get(features, "foodhopperMid_Mouse_Distance") <= 206.2021636963:
                                    return "IM"
                                else:
                                    return "OE"
                    else:
                        # if Nest_perimeter <= 1393.3214721680
                        if _get(features, "Nest_perimeter") <= 1393.3214721680:
                            # if Nest_RT_x <= 910.5000000000
                            if _get(features, "Nest_RT_x") <= 910.5000000000:
                                # if Actor_Dist_RL_RR <= 281.5799102783
                                if _get(features, "Actor_Dist_RL_RR") <= 281.5799102783:
                                    # if Actor_RR_x <= 1279.5000000000
                                    if _get(features, "Actor_RR_x") <= 1279.5000000000:
                                        # if Nest_Dist_RT_RB <= 183.0928192139
                                        if _get(features, "Nest_Dist_RT_RB") <= 183.0928192139:
                                            return "ONE"
                                        else:
                                            # if Actor_Dist_RT_RB <= 34.2920627594
                                            if _get(features, "Actor_Dist_RT_RB") <= 34.2920627594:
                                                # if Nest_Centroid_To_Bbox_TR <= 219.4578170776
                                                if _get(features, "Nest_Centroid_To_Bbox_TR") <= 219.4578170776:
                                                    return "ONE"
                                                else:
                                                    return "OE"
                                            else:
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
                # if Actor_Mask_IoU <= 0.9788886011
                if _get(features, "Actor_Mask_IoU") <= 0.9788886011:
                    # if Nest_Dist_RL_RT <= 310.4351654053
                    if _get(features, "Nest_Dist_RL_RT") <= 310.4351654053:
                        # if Nest_hu_4 <= 0.0000026300
                        if _get(features, "Nest_hu_4") <= 0.0000026300:
                            # if Nest_centroid_x <= 728.8796691895
                            if _get(features, "Nest_centroid_x") <= 728.8796691895:
                                return "OE"
                            else:
                                # if Nest_bbox_x <= 557.5000000000
                                if _get(features, "Nest_bbox_x") <= 557.5000000000:
                                    # if Actor_Dist_RR_To_Bbox_BR <= 60.0083522797
                                    if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 60.0083522797:
                                        return "ONE"
                                    else:
                                        return "OE"
                                else:
                                    # if Actor_Dist_RT_RB <= 152.3241271973
                                    if _get(features, "Actor_Dist_RT_RB") <= 152.3241271973:
                                        return "ONE"
                                    else:
                                        # if Actor_Dist_RL_To_Bbox_BL <= 18.5000000000
                                        if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 18.5000000000:
                                            return "OE"
                                        else:
                                            return "ONE"
                        else:
                            # if Nest_bbox_h <= 135.5000000000
                            if _get(features, "Nest_bbox_h") <= 135.5000000000:
                                return "OE"
                            else:
                                return "IM"
                    else:
                        return "OE"
                else:
                    # if Actor_perimeter <= 468.2497863770
                    if _get(features, "Actor_perimeter") <= 468.2497863770:
                        # if Actor_bbox_x <= 957.5000000000
                        if _get(features, "Actor_bbox_x") <= 957.5000000000:
                            return "ONE"
                        else:
                            # if Actor_Dist_RB_To_Bbox_TR <= 90.8094100952
                            if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 90.8094100952:
                                return "OE"
                            else:
                                return "ONE"
                    else:
                        return "OE"
        else:
            # if Nest_bbox_x <= 558.5000000000
            if _get(features, "Nest_bbox_x") <= 558.5000000000:
                # if Nest_Dist_RB_To_Bbox_TR <= 396.7092285156
                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 396.7092285156:
                    return "OE"
                else:
                    return "ONE"
            else:
                # if Nest_hu_1 <= 0.5744390786
                if _get(features, "Nest_hu_1") <= 0.5744390786:
                    # if Nest_Dist_RT_RB <= 331.2211914062
                    if _get(features, "Nest_Dist_RT_RB") <= 331.2211914062:
                        # if foodhopperMid_Mouse_Distance <= 206.3451309204
                        if _get(features, "foodhopperMid_Mouse_Distance") <= 206.3451309204:
                            # if Actor_Dist_RL_To_Bbox_TL <= 31.0000000000
                            if _get(features, "Actor_Dist_RL_To_Bbox_TL") <= 31.0000000000:
                                # if Actor_Dist_RT_RR <= 10.5965571404
                                if _get(features, "Actor_Dist_RT_RR") <= 10.5965571404:
                                    return "OE"
                                else:
                                    return "ONE"
                            else:
                                return "OE"
                        else:
                            # if Nest_RB_y <= 947.5000000000
                            if _get(features, "Nest_RB_y") <= 947.5000000000:
                                # if Nest_Dist_RR_RB <= 111.2425079346
                                if _get(features, "Nest_Dist_RR_RB") <= 111.2425079346:
                                    # if foodhopperBottom_Mouse_Distance <= 52.3972129822
                                    if _get(features, "foodhopperBottom_Mouse_Distance") <= 52.3972129822:
                                        return "IM"
                                    else:
                                        # if Actor_To_Nest_Dist_Change <= -92.0556907654
                                        if _get(features, "Actor_To_Nest_Dist_Change") <= -92.0556907654:
                                            return "IM"
                                        else:
                                            return "ONE"
                                else:
                                    # if Actor_RR_x <= 868.5000000000
                                    if _get(features, "Actor_RR_x") <= 868.5000000000:
                                        # if Nest_hu_5 <= 0.0000076400
                                        if _get(features, "Nest_hu_5") <= 0.0000076400:
                                            # if Nest_Dist_RB_RL <= 101.6210861206
                                            if _get(features, "Nest_Dist_RB_RL") <= 101.6210861206:
                                                return "ONE"
                                            else:
                                                return "INB"
                                        else:
                                            return "OE"
                                    else:
                                        # if Actor_perimeter <= 367.1578979492
                                        if _get(features, "Actor_perimeter") <= 367.1578979492:
                                            # if Nest_Dist_RB_To_Bbox_BL <= 149.0033569336
                                            if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 149.0033569336:
                                                # if Nest_orientation <= 72.9826698303
                                                if _get(features, "Nest_orientation") <= 72.9826698303:
                                                    # if Nest_Dist_RT_To_Bbox_BL <= 267.6934051514
                                                    if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 267.6934051514:
                                                        return "INB"
                                                    else:
                                                        return "ONE"
                                                else:
                                                    # if Nest_bbox_w <= 214.5000000000
                                                    if _get(features, "Nest_bbox_w") <= 214.5000000000:
                                                        return "OE"
                                                    else:
                                                        # if Nest_perimeter <= 1377.1620483398
                                                        if _get(features, "Nest_perimeter") <= 1377.1620483398:
                                                            # if Actor_To_Nest_Distance <= 109.2855873108
                                                            if _get(features, "Actor_To_Nest_Distance") <= 109.2855873108:
                                                                # if Actor_Centroid_To_Bbox_TL <= 50.3539600372
                                                                if _get(features, "Actor_Centroid_To_Bbox_TL") <= 50.3539600372:
                                                                    return "OE"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                # if Actor_Dist_RB_To_Bbox_TL <= 105.0464172363
                                                                if _get(features, "Actor_Dist_RB_To_Bbox_TL") <= 105.0464172363:
                                                                    return "ONE"
                                                                else:
                                                                    # if Actor_RB_y <= 796.0000000000
                                                                    if _get(features, "Actor_RB_y") <= 796.0000000000:
                                                                        return "ONE"
                                                                    else:
                                                                        return "INB"
                                                        else:
                                                            return "INB"
                                            else:
                                                return "INB"
                                        else:
                                            # if Nest_extent <= 0.5897411108
                                            if _get(features, "Nest_extent") <= 0.5897411108:
                                                # if Actor_RR_y <= 766.0000000000
                                                if _get(features, "Actor_RR_y") <= 766.0000000000:
                                                    # if foodhopperLeft_Nest_Distance <= 108.4528198242
                                                    if _get(features, "foodhopperLeft_Nest_Distance") <= 108.4528198242:
                                                        # if Actor_To_Nest_Distance <= 380.6712036133
                                                        if _get(features, "Actor_To_Nest_Distance") <= 380.6712036133:
                                                            return "OE"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        # if Actor_RT_x <= 1000.5000000000
                                                        if _get(features, "Actor_RT_x") <= 1000.5000000000:
                                                            # if Nest_Dist_RT_RR <= 218.4053573608
                                                            if _get(features, "Nest_Dist_RT_RR") <= 218.4053573608:
                                                                return "IM"
                                                            else:
                                                                return "ONE"
                                                        else:
                                                            return "OE"
                                                else:
                                                    # if foodhopperRight_Nest_Distance <= 648.0783691406
                                                    if _get(features, "foodhopperRight_Nest_Distance") <= 648.0783691406:
                                                        # if Nest_RB_x <= 614.0000000000
                                                        if _get(features, "Nest_RB_x") <= 614.0000000000:
                                                            # if Actor_RR_x <= 1262.5000000000
                                                            if _get(features, "Actor_RR_x") <= 1262.5000000000:
                                                                # if Actor_Dist_RB_To_Bbox_TR <= 112.4862098694
                                                                if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 112.4862098694:
                                                                    return "OE"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                return "IM"
                                                        else:
                                                            # if Actor_hu_0 <= 0.4991103113
                                                            if _get(features, "Actor_hu_0") <= 0.4991103113:
                                                                return "ONE"
                                                            else:
                                                                return "OE"
                                                    else:
                                                        return "IM"
                                            else:
                                                # if Nest_Dist_RT_RR <= 218.9383087158
                                                if _get(features, "Nest_Dist_RT_RR") <= 218.9383087158:
                                                    # if Nest_hu_2 <= 0.0007204330
                                                    if _get(features, "Nest_hu_2") <= 0.0007204330:
                                                        return "IM"
                                                    else:
                                                        # if Nest_RT_x <= 756.0000000000
                                                        if _get(features, "Nest_RT_x") <= 756.0000000000:
                                                            return "OE"
                                                        else:
                                                            return "ONE"
                                                else:
                                                    return "INB"
                            else:
                                # if Nest_hu_0 <= 0.3714939207
                                if _get(features, "Nest_hu_0") <= 0.3714939207:
                                    # if Actor_RR_x <= 1297.5000000000
                                    if _get(features, "Actor_RR_x") <= 1297.5000000000:
                                        # if Nest_Mask_IoU <= 0.8634133637
                                        if _get(features, "Nest_Mask_IoU") <= 0.8634133637:
                                            # if Actor_hu_1 <= 0.0139082512
                                            if _get(features, "Actor_hu_1") <= 0.0139082512:
                                                return "IM"
                                            else:
                                                # if Nest_Dist_RR_To_Bbox_TR <= 142.5035820007
                                                if _get(features, "Nest_Dist_RR_To_Bbox_TR") <= 142.5035820007:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                                        else:
                                            # if Nest_hu_1 <= 0.0004687790
                                            if _get(features, "Nest_hu_1") <= 0.0004687790:
                                                return "IM"
                                            else:
                                                # if Nest_Dist_RT_To_Bbox_BL <= 340.0740356445
                                                if _get(features, "Nest_Dist_RT_To_Bbox_BL") <= 340.0740356445:
                                                    # if Nest_RR_x <= 1012.5000000000
                                                    if _get(features, "Nest_RR_x") <= 1012.5000000000:
                                                        # if Actor_RL_y <= 849.5000000000
                                                        if _get(features, "Actor_RL_y") <= 849.5000000000:
                                                            # if Nest_Dist_RT_RR <= 165.2768478394
                                                            if _get(features, "Nest_Dist_RT_RR") <= 165.2768478394:
                                                                # if Actor_Dist_RT_To_Bbox_TL <= 36.5000000000
                                                                if _get(features, "Actor_Dist_RT_To_Bbox_TL") <= 36.5000000000:
                                                                    return "OE"
                                                                else:
                                                                    return "ONE"
                                                            else:
                                                                # if Actor_hu_0 <= 0.1746681556
                                                                if _get(features, "Actor_hu_0") <= 0.1746681556:
                                                                    # if c1_Mouse_Distance <= 503.4868469238
                                                                    if _get(features, "c1_Mouse_Distance") <= 503.4868469238:
                                                                        # if Actor_hu_0 <= 0.1718368232
                                                                        if _get(features, "Actor_hu_0") <= 0.1718368232:
                                                                            return "ONE"
                                                                        else:
                                                                            return "OE"
                                                                    else:
                                                                        # if Nest_hu_5 <= -0.0000012800
                                                                        if _get(features, "Nest_hu_5") <= -0.0000012800:
                                                                            return "IM"
                                                                        else:
                                                                            # if Actor_Dist_RR_RB <= 15.2432842255
                                                                            if _get(features, "Actor_Dist_RR_RB") <= 15.2432842255:
                                                                                return "OE"
                                                                            else:
                                                                                # if Actor_Dist_RR_To_Bbox_BR <= 8.5588216782
                                                                                if _get(features, "Actor_Dist_RR_To_Bbox_BR") <= 8.5588216782:
                                                                                    # if c4_Nest_Distance <= 302.9258728027
                                                                                    if _get(features, "c4_Nest_Distance") <= 302.9258728027:
                                                                                        return "OE"
                                                                                    else:
                                                                                        return "ONE"
                                                                                else:
                                                                                    return "ONE"
                                                                else:
                                                                    # if Nest_Area_Diff_Abs <= 8188.0000000000
                                                                    if _get(features, "Nest_Area_Diff_Abs") <= 8188.0000000000:
                                                                        # if Actor_Area_Diff_Abs <= 9950.2500000000
                                                                        if _get(features, "Actor_Area_Diff_Abs") <= 9950.2500000000:
                                                                            # if Actor_hu_3 <= 0.0000246000
                                                                            if _get(features, "Actor_hu_3") <= 0.0000246000:
                                                                                # if Nest_Dist_RB_To_Bbox_TR <= 317.5988311768
                                                                                if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 317.5988311768:
                                                                                    return "OE"
                                                                                else:
                                                                                    # if Actor_Dist_RR_To_Bbox_TR <= 4.6110625267
                                                                                    if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 4.6110625267:
                                                                                        # if Actor_RB_x <= 798.5000000000
                                                                                        if _get(features, "Actor_RB_x") <= 798.5000000000:
                                                                                            # if Nest_Dist_RL_To_Bbox_TR <= 429.6667633057
                                                                                            if _get(features, "Nest_Dist_RL_To_Bbox_TR") <= 429.6667633057:
                                                                                                return "ONE"
                                                                                            else:
                                                                                                return "OE"
                                                                                        else:
                                                                                            return "ONE"
                                                                                    else:
                                                                                        # if Actor_hu_3 <= 0.0000243000
                                                                                        if _get(features, "Actor_hu_3") <= 0.0000243000:
                                                                                            return "ONE"
                                                                                        else:
                                                                                            # if Actor_Dist_RT_To_Bbox_BR <= 49.2958602905
                                                                                            if _get(features, "Actor_Dist_RT_To_Bbox_BR") <= 49.2958602905:
                                                                                                return "OE"
                                                                                            else:
                                                                                                return "ONE"
                                                                            else:
                                                                                # if Nest_hu_2 <= 0.0002553645
                                                                                if _get(features, "Nest_hu_2") <= 0.0002553645:
                                                                                    # if Nest_Dist_RT_To_Bbox_TL <= 172.0000000000
                                                                                    if _get(features, "Nest_Dist_RT_To_Bbox_TL") <= 172.0000000000:
                                                                                        return "ONE"
                                                                                    else:
                                                                                        return "OE"
                                                                                else:
                                                                                    # if Actor_Dist_RB_To_Bbox_TR <= 167.8642807007
                                                                                    if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 167.8642807007:
                                                                                        # if Nest_Dist_RB_To_Bbox_BL <= 83.5060844421
                                                                                        if _get(features, "Nest_Dist_RB_To_Bbox_BL") <= 83.5060844421:
                                                                                            # if Nest_hu_1 <= 0.0010543720
                                                                                            if _get(features, "Nest_hu_1") <= 0.0010543720:
                                                                                                # if Nest_perimeter <= 1062.6280517578
                                                                                                if _get(features, "Nest_perimeter") <= 1062.6280517578:
                                                                                                    return "IM"
                                                                                                else:
                                                                                                    return "ONE"
                                                                                            else:
                                                                                                return "ONE"
                                                                                        else:
                                                                                            # if Nest_hu_3 <= 0.0009759255
                                                                                            if _get(features, "Nest_hu_3") <= 0.0009759255:
                                                                                                return "ONE"
                                                                                            else:
                                                                                                return "INB"
                                                                                    else:
                                                                                        # if Actor_Dist_RB_To_Bbox_TR <= 168.1561813354
                                                                                        if _get(features, "Actor_Dist_RB_To_Bbox_TR") <= 168.1561813354:
                                                                                            return "IM"
                                                                                        else:
                                                                                            return "ONE"
                                                                        else:
                                                                            # if Actor_RB_x <= 988.0000000000
                                                                            if _get(features, "Actor_RB_x") <= 988.0000000000:
                                                                                # if foodhopperLeft_Mouse_Distance <= 264.7692642212
                                                                                if _get(features, "foodhopperLeft_Mouse_Distance") <= 264.7692642212:
                                                                                    return "ONE"
                                                                                else:
                                                                                    # if c2_Nest_Distance <= 924.9417724609
                                                                                    if _get(features, "c2_Nest_Distance") <= 924.9417724609:
                                                                                        return "OE"
                                                                                    else:
                                                                                        return "IM"
                                                                            else:
                                                                                return "ONE"
                                                                    else:
                                                                        # if foodhopperRight_Mouse_Distance <= 354.6188354492
                                                                        if _get(features, "foodhopperRight_Mouse_Distance") <= 354.6188354492:
                                                                            return "IM"
                                                                        else:
                                                                            return "ONE"
                                                        else:
                                                            # if Nest_eccentricity <= 0.8324589729
                                                            if _get(features, "Nest_eccentricity") <= 0.8324589729:
                                                                return "IM"
                                                            else:
                                                                return "ONE"
                                                    else:
                                                        # if Actor_Dist_RR_To_Bbox_BL <= 104.5694313049
                                                        if _get(features, "Actor_Dist_RR_To_Bbox_BL") <= 104.5694313049:
                                                            return "ONE"
                                                        else:
                                                            return "IM"
                                                else:
                                                    return "OE"
                                    else:
                                        # if Nest_Dist_RT_To_Bbox_BR <= 326.4930725098
                                        if _get(features, "Nest_Dist_RT_To_Bbox_BR") <= 326.4930725098:
                                            return "ONE"
                                        else:
                                            return "IM"
                                else:
                                    # if Nest_Dist_RB_To_Bbox_TL <= 202.0433044434
                                    if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 202.0433044434:
                                        # if Actor_bbox_x <= 728.0000000000
                                        if _get(features, "Actor_bbox_x") <= 728.0000000000:
                                            # if Nest_Dist_RT_To_Bbox_TR <= 165.0000000000
                                            if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 165.0000000000:
                                                return "IM"
                                            else:
                                                return "OE"
                                        else:
                                            # if Actor_RR_x <= 1418.5000000000
                                            if _get(features, "Actor_RR_x") <= 1418.5000000000:
                                                # if Nest_hu_5 <= 0.0044315590
                                                if _get(features, "Nest_hu_5") <= 0.0044315590:
                                                    # if Nest_orientation <= 87.2301826477
                                                    if _get(features, "Nest_orientation") <= 87.2301826477:
                                                        # if Nest_hu_1 <= 0.0902563781
                                                        if _get(features, "Nest_hu_1") <= 0.0902563781:
                                                            # if Nest_hu_1 <= 0.0902444236
                                                            if _get(features, "Nest_hu_1") <= 0.0902444236:
                                                                return "ONE"
                                                            else:
                                                                return "OE"
                                                        else:
                                                            return "ONE"
                                                    else:
                                                        # if Actor_RB_y <= 815.0000000000
                                                        if _get(features, "Actor_RB_y") <= 815.0000000000:
                                                            return "ONE"
                                                        else:
                                                            return "IM"
                                                else:
                                                    # if Actor_Dist_RL_To_Bbox_BL <= 64.0000000000
                                                    if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 64.0000000000:
                                                        return "ONE"
                                                    else:
                                                        return "OE"
                                            else:
                                                return "INB"
                                    else:
                                        # if Actor_Dist_RL_To_Bbox_BL <= 53.0000000000
                                        if _get(features, "Actor_Dist_RL_To_Bbox_BL") <= 53.0000000000:
                                            # if Nest_Dist_RB_To_Bbox_TR <= 454.5953674316
                                            if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 454.5953674316:
                                                # if Nest_bbox_y <= 742.5000000000
                                                if _get(features, "Nest_bbox_y") <= 742.5000000000:
                                                    return "IM"
                                                else:
                                                    # if Actor_Dist_RR_To_Bbox_TR <= 59.5084171295
                                                    if _get(features, "Actor_Dist_RR_To_Bbox_TR") <= 59.5084171295:
                                                        # if c1_Mouse_Distance <= 469.6789093018
                                                        if _get(features, "c1_Mouse_Distance") <= 469.6789093018:
                                                            # if Actor_hu_5 <= -0.0000013055
                                                            if _get(features, "Actor_hu_5") <= -0.0000013055:
                                                                return "ONE"
                                                            else:
                                                                return "OE"
                                                        else:
                                                            # if Nest_Area_Diff_Abs <= 1316.0000000000
                                                            if _get(features, "Nest_Area_Diff_Abs") <= 1316.0000000000:
                                                                return "ONE"
                                                            else:
                                                                # if Actor_To_Nest_Dist_Change <= 39.3241834641
                                                                if _get(features, "Actor_To_Nest_Dist_Change") <= 39.3241834641:
                                                                    return "OE"
                                                                else:
                                                                    return "ONE"
                                                    else:
                                                        return "OE"
                                            else:
                                                # if Nest_hu_2 <= 0.0168404030
                                                if _get(features, "Nest_hu_2") <= 0.0168404030:
                                                    return "OE"
                                                else:
                                                    # if Actor_Dist_RB_RL <= 13.0674719810
                                                    if _get(features, "Actor_Dist_RB_RL") <= 13.0674719810:
                                                        return "OE"
                                                    else:
                                                        return "ONE"
                                        else:
                                            # if Actor_Dist_RR_To_Bbox_TL <= 82.1764984131
                                            if _get(features, "Actor_Dist_RR_To_Bbox_TL") <= 82.1764984131:
                                                # if Actor_hu_2 <= 0.0027541025
                                                if _get(features, "Actor_hu_2") <= 0.0027541025:
                                                    return "ONE"
                                                else:
                                                    return "OE"
                                            else:
                                                # if c2_Nest_Distance <= 891.5429077148
                                                if _get(features, "c2_Nest_Distance") <= 891.5429077148:
                                                    return "ONE"
                                                else:
                                                    return "INB"
                    else:
                        # if Nest_hu_0 <= 0.3367402554
                        if _get(features, "Nest_hu_0") <= 0.3367402554:
                            # if Actor_solidity <= 0.6762227416
                            if _get(features, "Actor_solidity") <= 0.6762227416:
                                return "ONE"
                            else:
                                # if Actor_bbox_h <= 73.5000000000
                                if _get(features, "Actor_bbox_h") <= 73.5000000000:
                                    # if Nest_area <= 32959.5000000000
                                    if _get(features, "Nest_area") <= 32959.5000000000:
                                        # if Actor_Mask_IoU <= 0.6684056222
                                        if _get(features, "Actor_Mask_IoU") <= 0.6684056222:
                                            return "ONE"
                                        else:
                                            return "OE"
                                    else:
                                        # if Nest_Dist_RB_To_Bbox_TR <= 424.7664031982
                                        if _get(features, "Nest_Dist_RB_To_Bbox_TR") <= 424.7664031982:
                                            return "ONE"
                                        else:
                                            # if Actor_orientation <= 134.8530197144
                                            if _get(features, "Actor_orientation") <= 134.8530197144:
                                                return "OE"
                                            else:
                                                return "ONE"
                                else:
                                    # if Nest_Dist_RB_To_Bbox_TL <= 213.2592315674
                                    if _get(features, "Nest_Dist_RB_To_Bbox_TL") <= 213.2592315674:
                                        return "ONE"
                                    else:
                                        # if Actor_hu_6 <= 0.0000008440
                                        if _get(features, "Actor_hu_6") <= 0.0000008440:
                                            return "OE"
                                        else:
                                            return "ONE"
                        else:
                            # if Actor_RT_x <= 1064.5000000000
                            if _get(features, "Actor_RT_x") <= 1064.5000000000:
                                # if c1_Nest_Distance <= 559.2149963379
                                if _get(features, "c1_Nest_Distance") <= 559.2149963379:
                                    return "OE"
                                else:
                                    return "ONE"
                            else:
                                return "OE"
                else:
                    # if Actor_To_Nest_Distance <= 454.9692993164
                    if _get(features, "Actor_To_Nest_Distance") <= 454.9692993164:
                        # if Nest_Dist_RT_To_Bbox_TR <= 214.0000000000
                        if _get(features, "Nest_Dist_RT_To_Bbox_TR") <= 214.0000000000:
                            return "OE"
                        else:
                            return "ONE"
                    else:
                        return "ONE"

# --- Wrapper / helpers ---

# --- learned config ---
RATIO_FEATURE  = 'Actor_aspect_ratio'
RATIO_THRESH   = 0.9307145
RATIO_FLIP     = True

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
    if RATIO_FEATURE in df.columns:
        return RATIO_FEATURE
    # compute from bbox if possible
    for prefix in ["Actor_", "Rat_", "Mouse_"]:
        w, h = prefix+"bbox_w", prefix+"bbox_h"
        ar = prefix+"aspect_ratio"
        if w in df.columns and h in df.columns:
            import pandas as _pd
            df[ar] = _pd.to_numeric(df[w], errors="coerce") / _pd.to_numeric(df[h], errors="coerce")
            return ar
    return RATIO_FEATURE

def _gate_ipi_isi(x):
    # flip=False: x <= t -> IPI, else ISI
    # flip=True : x <= t -> ISI, else IPI
    if x != x:  # NaN
        return "IPI"
    if not RATIO_FLIP:
        return "IPI" if x <= RATIO_THRESH else "ISI"
    else:
        return "ISI" if x <= RATIO_THRESH else "IPI"

def predict_row(features: dict):
    route = router_tree_predict(features)  # 'IPI_ISI' or 'OTHER4'
    if route == "IPI_ISI":
        ar = _get(features, RATIO_FEATURE)
        return _gate_ipi_isi(ar)
    else:
        return other4_tree_predict(features)

def predict_df(df, gt_col=None, unify=True, print_report=True):
    import pandas as _pd
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

    work = df.copy()
    if unify:
        work.columns = _unify_cols(work.columns)

    ratio_col = _ensure_ratio_in_df(work)

    router_cols = ['Actor_RL_x', 'c1_Mouse_Distance', 'foodhopperLeft_Mouse_Distance', 'c3_Mouse_Distance', 'Actor_bbox_x', 'Actor_centroid_x', 'c4_Mouse_Distance', 'c2_Mouse_Distance', 'Actor_Mask_IoU', 'foodhopperRight_Mouse_Distance', 'foodhopperBottom_Mouse_Distance', 'Actor_RT_x', 'Nest_RB_y', 'Nest_Dist_RT_To_Bbox_BR', 'foodhopperMid_Mouse_Distance', 'Actor_RR_x', 'Actor_Centroid_To_Bbox_TL', 'Nest_RT_y', 'Actor_area', 'Nest_bbox_h', 'Actor_Centroid_To_Bbox_BL', 'Nest_RB_x', 'Nest_RR_x', 'Nest_bbox_y', 'Nest_Dist_RL_To_Bbox_TR', 'Actor_bbox_h', 'Actor_Area_Diff_Abs', 'Actor_bbox_y', 'Actor_RB_x', 'Nest_RT_x', 'Nest_Dist_RL_RR', 'Actor_RB_y', 'Actor_perimeter', 'foodhopperLeft_Nest_Distance', 'Nest_Dist_RL_To_Bbox_BR', 'Nest_Dist_RR_RB', 'c3_Nest_Distance', 'Actor_Dist_RT_RB', 'Nest_Dist_RR_To_Bbox_BL', 'Nest_centroid_x', 'Nest_Dist_RR_To_Bbox_TL', 'c2_Nest_Distance', 'Nest_bbox_w', 'Nest_Dist_RT_To_Bbox_TR', 'foodhopperRight_Nest_Distance', 'c1_Nest_Distance', 'Nest_Dist_RL_To_Bbox_TL', 'c4_Nest_Distance', 'Nest_Dist_RB_To_Bbox_BR', 'Actor_To_Nest_Distance', 'Nest_Centroid_To_Bbox_TL', 'Actor_Centroid_To_Bbox_BR', 'Nest_bbox_x', 'Actor_Dist_RT_To_Bbox_BR', 'Nest_RL_x', 'foodhopperBottom_Nest_Distance', 'Nest_Centroid_To_Bbox_BL', 'Nest_Dist_RT_RB', 'Actor_Dist_RT_To_Bbox_BL', 'Nest_solidity', 'Actor_Centroid_To_Bbox_TR', 'Nest_RR_y', 'Nest_Dist_RL_To_Bbox_BL', 'Nest_Dist_RR_To_Bbox_TR', 'Nest_Centroid_To_Bbox_TR', 'Actor_RT_y', 'Actor_Dist_RL_To_Bbox_TR', 'Nest_Dist_RT_RR', 'Nest_centroid_y', 'Actor_Dist_RL_To_Bbox_TL', 'Nest_area', 'foodhopperMid_Nest_Distance', 'Nest_Area_Diff_Abs', 'Nest_hu_1', 'Nest_RL_y', 'Nest_aspect_ratio', 'Actor_Dist_RL_To_Bbox_BR', 'Nest_hu_0', 'Nest_hu_2', 'Nest_Dist_RB_To_Bbox_TR', 'Nest_orientation', 'Actor_centroid_y', 'Nest_Centroid_To_Bbox_BR', 'Nest_extent', 'Nest_Dist_RB_RL', 'Actor_bbox_w', 'Actor_Dist_RR_To_Bbox_TL', 'Nest_Dist_RB_To_Bbox_TL', 'Nest_Mask_IoU', 'Actor_hu_1', 'Actor_Dist_RL_RR', 'Nest_hu_3', 'Nest_Dist_RB_To_Bbox_BL', 'Nest_eccentricity', 'Nest_perimeter', 'Actor_Dist_RT_RR', 'Nest_Dist_RR_To_Bbox_BR', 'Actor_hu_0', 'Actor_aspect_ratio', 'Actor_Dist_RB_To_Bbox_TL', 'Actor_Dist_RB_To_Bbox_TR', 'Nest_hu_5', 'Nest_Dist_RL_RT', 'Nest_Dist_RT_To_Bbox_BL', 'Actor_Dist_RB_To_Bbox_BL', 'Actor_Dist_RB_RL', 'Nest_hu_4', 'Actor_solidity', 'Actor_Dist_RL_RT', 'Nest_Dist_RT_To_Bbox_TL', 'Actor_Dist_RT_To_Bbox_TR', 'Actor_Dist_RB_To_Bbox_BR', 'Actor_Dist_RR_To_Bbox_BL', 'Actor_eccentricity', 'Actor_Dist_RR_To_Bbox_TR', 'Actor_Dist_RR_RB', 'Actor_hu_3', 'Actor_RR_y', 'Actor_extent', 'Nest_hu_6', 'Actor_orientation', 'Actor_Dist_RL_To_Bbox_BL', 'Actor_Dist_RT_To_Bbox_TL', 'Actor_RL_y', 'Actor_hu_2', 'Actor_Dist_RR_To_Bbox_BR', 'Actor_hu_5', 'Actor_To_Nest_Dist_Change', 'Actor_Direction_deg', 'Actor_hu_6', 'Actor_hu_4']
    o4_cols     = ['Actor_area', 'Actor_perimeter', 'Actor_centroid_x', 'Actor_centroid_y', 'Actor_bbox_x', 'Actor_bbox_y', 'Actor_bbox_w', 'Actor_bbox_h', 'Actor_aspect_ratio', 'Actor_extent', 'Actor_solidity', 'Actor_orientation', 'Actor_eccentricity', 'Actor_RL_x', 'Actor_RL_y', 'Actor_RR_x', 'Actor_RR_y', 'Actor_RT_x', 'Actor_RT_y', 'Actor_RB_x', 'Actor_RB_y', 'Actor_hu_0', 'Actor_hu_1', 'Actor_hu_2', 'Actor_hu_3', 'Actor_hu_4', 'Actor_hu_5', 'Actor_hu_6', 'Actor_Dist_RL_RR', 'Actor_Dist_RT_RB', 'Actor_Dist_RL_RT', 'Actor_Dist_RT_RR', 'Actor_Dist_RR_RB', 'Actor_Dist_RB_RL', 'Actor_Centroid_To_Bbox_TL', 'Actor_Centroid_To_Bbox_TR', 'Actor_Centroid_To_Bbox_BR', 'Actor_Centroid_To_Bbox_BL', 'Actor_Dist_RL_To_Bbox_TL', 'Actor_Dist_RL_To_Bbox_TR', 'Actor_Dist_RL_To_Bbox_BR', 'Actor_Dist_RL_To_Bbox_BL', 'Actor_Dist_RR_To_Bbox_TL', 'Actor_Dist_RR_To_Bbox_TR', 'Actor_Dist_RR_To_Bbox_BR', 'Actor_Dist_RR_To_Bbox_BL', 'Actor_Dist_RT_To_Bbox_TL', 'Actor_Dist_RT_To_Bbox_TR', 'Actor_Dist_RT_To_Bbox_BR', 'Actor_Dist_RT_To_Bbox_BL', 'Actor_Dist_RB_To_Bbox_TL', 'Actor_Dist_RB_To_Bbox_TR', 'Actor_Dist_RB_To_Bbox_BR', 'Actor_Dist_RB_To_Bbox_BL', 'Nest_area', 'Nest_perimeter', 'Nest_centroid_x', 'Nest_centroid_y', 'Nest_bbox_x', 'Nest_bbox_y', 'Nest_bbox_w', 'Nest_bbox_h', 'Nest_aspect_ratio', 'Nest_extent', 'Nest_solidity', 'Nest_orientation', 'Nest_eccentricity', 'Nest_RL_x', 'Nest_RL_y', 'Nest_RR_x', 'Nest_RR_y', 'Nest_RT_x', 'Nest_RT_y', 'Nest_RB_x', 'Nest_RB_y', 'Nest_hu_0', 'Nest_hu_1', 'Nest_hu_2', 'Nest_hu_3', 'Nest_hu_4', 'Nest_hu_5', 'Nest_hu_6', 'Nest_Dist_RL_RR', 'Nest_Dist_RT_RB', 'Nest_Dist_RL_RT', 'Nest_Dist_RT_RR', 'Nest_Dist_RR_RB', 'Nest_Dist_RB_RL', 'Nest_Centroid_To_Bbox_TL', 'Nest_Centroid_To_Bbox_TR', 'Nest_Centroid_To_Bbox_BR', 'Nest_Centroid_To_Bbox_BL', 'Nest_Dist_RL_To_Bbox_TL', 'Nest_Dist_RL_To_Bbox_TR', 'Nest_Dist_RL_To_Bbox_BR', 'Nest_Dist_RL_To_Bbox_BL', 'Nest_Dist_RR_To_Bbox_TL', 'Nest_Dist_RR_To_Bbox_TR', 'Nest_Dist_RR_To_Bbox_BR', 'Nest_Dist_RR_To_Bbox_BL', 'Nest_Dist_RT_To_Bbox_TL', 'Nest_Dist_RT_To_Bbox_TR', 'Nest_Dist_RT_To_Bbox_BR', 'Nest_Dist_RT_To_Bbox_BL', 'Nest_Dist_RB_To_Bbox_TL', 'Nest_Dist_RB_To_Bbox_TR', 'Nest_Dist_RB_To_Bbox_BR', 'Nest_Dist_RB_To_Bbox_BL', 'Actor_Area_Diff_Abs', 'Actor_Mask_IoU', 'Nest_Area_Diff_Abs', 'Nest_Mask_IoU', 'Actor_To_Nest_Distance', 'Actor_Direction_deg', 'Actor_To_Nest_Dist_Change', 'c1_Mouse_Distance', 'c1_Nest_Distance', 'c2_Mouse_Distance', 'c2_Nest_Distance', 'c3_Mouse_Distance', 'c3_Nest_Distance', 'c4_Mouse_Distance', 'c4_Nest_Distance', 'foodhopperBottom_Mouse_Distance', 'foodhopperBottom_Nest_Distance', 'foodhopperLeft_Mouse_Distance', 'foodhopperLeft_Nest_Distance', 'foodhopperRight_Mouse_Distance', 'foodhopperRight_Nest_Distance', 'foodhopperMid_Mouse_Distance', 'foodhopperMid_Nest_Distance']
    need = set(router_cols) | set(o4_cols) | {ratio_col}

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
        labs = ["IM","INB","IPI","ISI","OE","ONE"]
        print(classification_report(y_true, y_pred, labels=labs, digits=3))
        print("Confusion Matrix (IM,INB,IPI,ISI,OE,ONE):\\n", confusion_matrix(y_true, y_pred, labels=labs))
    return out
