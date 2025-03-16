# calculatortest.py

# 定义权重变量
w_volume = 0.25
w_limitup = 0.25
w_limitdown = 0.25
w_updays = 0.25
w_index = 0.25
w_other = 0

import logging
from strategy_func import get_score_volume, get_score_limitup, get_score_limitdown, get_score_updays, get_score_index
# from calculate_scorestest import calculate_total_scores

# 配置日志记录
logging.basicConfig(
    filename="0run.log",  # 日志文件名
    level=logging.INFO,  # 记录 INFO 级别及以上的日志
    format="%(asctime)s - %(levelname)s - %(message)s",  # 日志格式
    datefmt="%Y-%m-%d %H:%M:%S"
)

def calculate_total_scores(volume, limit_up, limit_down, consecutive_up_days, index_change):
    # 计算得分
    global w_volume, w_limitup, w_limitdown, w_updays, w_index, w_other # 在函数内部声明 global
    score_volume = get_score_volume(volume)
    score_limitup = get_score_limitup(limit_up)
    score_limitdown = get_score_limitdown(limit_down)
    score_updays = get_score_updays(consecutive_up_days)
    score_index = get_score_index(index_change)

    logging.info(f"传入的值: volume={volume}, consecutive_up_days={consecutive_up_days}")

    # 使用 match-case 来处理不同的 volume 范围，并调整权重
    match volume:
        case v if v > 20000:
            match consecutive_up_days:
                case cud if cud < 0:
                    w_volume = 0.6
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 1:
                    w_volume = 0.5
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 2:
                    w_volume = 0.3
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case _:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
        case v if 18000 <= v <= 20000:
            match consecutive_up_days:
                case cud if cud < 0:
                    w_volume = 0.5
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 1:
                    w_volume = 0.4
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 2:
                    w_volume = 0.3
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case _:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
        case v if 17000 <= v < 18000:
            match consecutive_up_days:
                case cud if cud < 0:
                    w_volume = 0.45
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 1:
                    w_volume = 0.3
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 2:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case _:
                    w_volume = 0.2
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
        case v if 16000 <= v < 17000:
            match consecutive_up_days:
                case cud if cud < 0:
                    w_volume = 0.4
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 1:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 2:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case _:
                    w_volume = 0.2
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
        case v if 15000 <= v < 16000:
            match consecutive_up_days:
                case cud if cud < 0:
                    w_volume = 0.3
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 1:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 2:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case _:
                    w_volume = 0.2
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
        case v if 14000 <= v < 15000:
            match consecutive_up_days:
                case cud if cud < 0:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 1:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 2:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case _:
                    w_volume = 0.2
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
        case v if 13000 <= v < 14000:
            match consecutive_up_days:
                case cud if cud < 0:
                    w_volume = 0.15
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 1:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 2:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case _:
                    w_volume = 0.2
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
        case v if 12000 <= v < 13000:
            match consecutive_up_days:
                case cud if cud < 0:
                    w_volume = 0.1
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 1:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 2:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case _:
                    w_volume = 0.2
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
        case v if 11000 <= v < 12000:
            match consecutive_up_days:
                case cud if cud < 0:
                    w_volume = 0.1
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 1:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case 2:
                    w_volume = 0.25
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
                case _:
                    w_volume = 0.2
                    w_other = 0.25 * (1 - w_volume)
                    w_limitup = w_other
                    w_limitdown = w_other
                    w_updays = w_other
                    w_index = w_other
        case v if 10000 <= v < 11000:
            w_volume = 0.15
            w_other = 0.25 * (1 - w_volume)
            w_limitup = w_other
            w_limitdown = w_other
            w_updays = w_other
            w_index = w_other
        case _:
            w_volume = 0.2
            w_other = 0.25 * (1 - w_volume)
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

    logging.info(f"权重: w_volume={w_volume}, w_limitup={w_limitup}, w_limitdown={w_limitdown}, "
                 f"w_updays={w_updays}, w_index={w_index}")


    return round(total_score, 2)