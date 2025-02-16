def get_score_volume(volume):
    if volume >= 20000:
        return 0.9
    elif 18000 <= volume < 20000:
        return 0.85
    elif 17000 <= volume < 18000:
        return 0.8
    elif 16000 <= volume < 17000:
        return 0.7
    elif 15000 <= volume < 16000:
        return 0.65
    elif 10000 <= volume < 15000:
        return 0.5
    else:
        return 0

def get_score_limitup(limitup_count):
    if limitup_count >= 100:
        return 0.9
    elif 50 <= limitup_count < 100:
        return 0.7
    elif 20 <= limitup_count < 50:
        return 0.5
    elif 10 <= limitup_count < 20:
        return 0.3
    else:
        return 0

def get_score_limitdown(limitdown_count):
    if limitdown_count >= 100:
        return 0.9
    elif 50 <= limitdown_count < 100:
        return 0.7
    elif 10 <= limitdown_count < 50:
        return 0.5
    else:
        return 0

def get_score_updays(updays_count):
    if updays_count >= 3:
        return 0.9
    elif 2 <= updays_count < 3:
        return 0.7
    elif 1 <= updays_count < 2:
        return 0.5
    else:
        return 0

def get_score_index(index_change):
    if index_change >= 2:
        return 0.9
    elif 1 <= index_change < 2:
        return 0.7
    elif 0 <= index_change < 1:
        return 0.5
    elif -1 <= index_change < 0:
        return -0.5
    elif -2 <= index_change < -1:
        return -0.7
    else:
        return -0.9

# 计算权重
w_volume = 0.6
w_other = 0.25 * (1 - w_volume)
w_limitup = w_other
w_limitdown = w_other
w_updays = w_other
w_index = w_other

# 输入数据
volume = [17300, 16359, 16772,18198]
limit_up = [140, 84, 95,74]  
limit_down = [2, 68, 17,244]  
consecutive_up_days = [3, -1, 1,-1]
index_change = [0.56, -0.12, 0.85,-0.42]

# 计算每一组的综合得分
total_scores = []
for v, lu, ld, cud, ic in zip(volume, limit_up, limit_down, consecutive_up_days, index_change):
    score_volume = get_score_volume(v)
    score_limitup = get_score_limitup(lu)
    score_limitdown = get_score_limitdown(ld)
    score_updays = get_score_updays(cud)
    score_index = get_score_index(ic)
    
    total_score = (w_volume * score_volume +
                   w_limitup * score_limitup -
                   w_limitdown * score_limitdown +
                   w_updays * score_updays +
                   w_index * score_index)
    
    total_scores.append(total_score)

# 定义保存到txt的函数
def save_emotion_values_to_txt(file_path, emotion_values):
    with open(file_path, 'w') as file:
        for idx, value in enumerate(emotion_values, 1):
            file.write(f"{value}\n")

# 保存结果到txt
file_path = 'emotion_values.txt'
save_emotion_values_to_txt(file_path, total_scores)

print(f"结果已保存到 {file_path}")
