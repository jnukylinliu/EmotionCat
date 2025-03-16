from strategy_func import get_score_volume,get_score_limitup,get_score_limitdown,get_score_updays,get_score_index


def calculate_total_scores(volume, limit_up, limit_down, consecutive_up_days, index_change, w_volume, w_limitup, w_limitdown, w_updays, w_index):
    total_scores = []
    
    # 遍历每个数据点
    for v, lu, ld, cud, ic in zip(volume, limit_up, limit_down, consecutive_up_days, index_change):
        # 初步计算得分
        score_volume = get_score_volume(v)
        score_limitup = get_score_limitup(lu)
        score_limitdown = get_score_limitdown(ld)
        score_updays = get_score_updays(cud)
        score_index = get_score_index(ic)

        # 使用 match-case 来处理不同的 volume 范围，并调整权重
        match v:
            case v if v > 20000:
                match cud:
                    case cud if cud < 0:
                        # 计算权重
                        w_volume = 0.6
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 1:
                        # 计算权重
                        w_volume = 0.5
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 2:
                        # 计算权重
                        w_volume = 0.3
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case _:
                        # 其他情况的默认权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
            case v if 18000 <= v <= 20000:
                match cud:
                    case cud if cud < 0:
                        # 计算权重
                        w_volume = 0.5
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 1:
                        # 计算权重
                        w_volume = 0.4
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 2:
                        # 计算权重
                        w_volume = 0.3
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case _:
                        # 其他情况的默认权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
            case v if 17000 <= v < 18000:
                match cud:
                    case cud if cud < 0:
                        # 计算权重
                        w_volume = 0.45
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 1:
                        # 计算权重
                        w_volume = 0.3
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 2:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case _:
                        # 其他情况的默认权重
                        w_volume = 0.2
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
            case v if 16000 <= v < 17000:
                match cud:
                    case cud if cud < 0:
                        # 计算权重
                        w_volume = 0.4
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 1:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 2:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case _:
                        # 其他情况的默认权重
                        w_volume = 0.2
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
            case v if 15000 <= v < 16000:
                match cud:
                    case cud if cud < 0:
                        # 计算权重
                        w_volume = 0.3
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 1:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 2:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case _:
                        # 其他情况的默认权重
                        w_volume = 0.2
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
            case v if 14000 <= v < 15000:
                match cud:
                    case cud if cud < 0:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 1:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 2:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case _:
                        # 其他情况的默认权重
                        w_volume = 0.2
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
            case v if 13000 <= v < 14000:
                match cud:
                    case cud if cud < 0:
                        # 计算权重
                        w_volume = 0.15
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 1:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 2:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case _:
                        # 其他情况的默认权重
                        w_volume = 0.2
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
            case v if 12000 <= v < 13000:
                match cud:
                    case cud if cud < 0:
                        # 计算权重
                        w_volume = 0.1
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 1:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 2:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case _:
                        # 其他情况的默认权重
                        w_volume = 0.2
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
            case v if 11000 <= v < 12000:
                match cud:
                    case cud if cud < 0:
                        # 计算权重
                        w_volume = 0.1
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 1:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case 2:
                        # 计算权重
                        w_volume = 0.25
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
                    case _:
                        # 其他情况的默认权重
                        w_volume = 0.2
                        w_other = 0.25 * (1 - w_volume)
                        w_limitup = w_other
                        w_limitdown = w_other
                        w_updays = w_other
                        w_index = w_other
            case v if 10000 <= v < 11000:
                # 计算权重
                w_volume = 0
                w_other = 0
                w_limitup = w_other
                w_limitdown = w_other
                w_updays = w_other
                w_index = w_other
            case v if v < 10000:
                # 计算权重
                w_volume = 0
                w_other = 0
                w_limitup = w_other
                w_limitdown = w_other
                w_updays = w_other
                w_index = w_other

        # 计算最终得分
        total_score = (w_volume * score_volume +
                       w_limitup * score_limitup -
                       w_limitdown * score_limitdown -
                       w_updays * score_updays +
                       w_index * score_index)

        total_scores.append(round(total_score, 2))
    
    return total_scores
