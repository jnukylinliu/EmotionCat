from strategy_func import get_score_volume,get_score_limitup,get_score_limitdown,get_score_updays,get_score_index

# 计算权重
w_volume = 0.25
w_other = 0.25 * (1 - w_volume)
w_limitup = w_other
w_limitdown = w_other
w_updays = w_other
w_index = w_other

# 输入数据
volume = [17300, 16359, 16772,18198,17150,17991,17210,20805,18968]
limit_up = [140, 84, 95,74,200,113,597,282,213]  
limit_down = [2, 68, 17,244,94,699,164,157,85]  
consecutive_up_days = [3, -1, 1,-1,1,-1,1,-1,-2]
index_change = [0.56, -0.12, 0.85,-0.42,0.43,-0.93,0.81,-0.18,-0.8]

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
                   w_limitdown * score_limitdown -
                   w_updays * score_updays +
                   w_index * score_index)
    

    total_scores.append(round(total_score , 2))

# 定义保存到txt的函数
def save_emotion_values_to_txt(file_path, emotion_values):
    with open(file_path, 'w') as file:
        for idx, value in enumerate(emotion_values, 1):
            file.write(f"{value}\n")
            print(f"Emotion Value {idx}:        {value}")  # 打印到控制台

# 保存结果到txt
file_path = 'emotion_values.txt'
save_emotion_values_to_txt(file_path, total_scores)

print(f"结果已保存到 {file_path}")
