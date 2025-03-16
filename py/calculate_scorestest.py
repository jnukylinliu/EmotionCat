from strategy_func import get_score_volume, get_score_limitup, get_score_limitdown, get_score_updays, get_score_index

def calculate_total_scores(volume, limit_up, limit_down, consecutive_up_days, index_change, w_volume, w_limitup, w_limitdown, w_updays, w_index):
    # 计算得分
    score_volume = get_score_volume(volume)
    score_limitup = get_score_limitup(limit_up)
    score_limitdown = get_score_limitdown(limit_down)
    score_updays = get_score_updays(consecutive_up_days)
    score_index = get_score_index(index_change)

    # 使用 match-case 来处理不同的 volume 范围，并调整权重
    match volume:
        case v if v > 20000:
            match consecutive_up_days:
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
            match consecutive_up_days:
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
        # 其余的处理逻辑继续类似...

    # 计算最终得分
    total_score = (w_volume * score_volume +
                   w_limitup * score_limitup -
                   w_limitdown * score_limitdown -
                   w_updays * score_updays +
                   w_index * score_index)

    return round(total_score, 2)
