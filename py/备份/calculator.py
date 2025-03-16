from strategy_func import get_score_volume,get_score_limitup,get_score_limitdown,get_score_updays,get_score_index
from calculate_scores import calculate_total_scores



# 输入数据
volume = [17300, 16359, 16772,18198,17150,17991,17210,20805,18968,16247,14356,14938,19065,18182,15057,14819,16838]
limit_up = [140, 84, 95,74,200,113,597,282,213,339,396,287,448,236,274,242,274]
limit_down = [2, 68, 17,244,94,699,164,157,85,169,94,41,26,126,90,53,40]
consecutive_up_days = [3, -1, 1,-1,1,-1,1,-1,-2,-2,1,2,3,-1,-2,1,-1]
index_change = [0.56, -0.12, 0.85,-0.42,0.43,-0.93,0.81,-0.18,-0.8,-0.12,0.22,0.53,1.17,-0.25,-0.19,0.41,-0.23]

# 计算每一组的综合得分

w_volume = 0  # 示例初始值
w_limitup = 0
w_limitdown = 0
w_updays = 0
w_index = 0


total_scores = calculate_total_scores(volume, limit_up, limit_down, consecutive_up_days, index_change, 
                                      w_volume, w_limitup, w_limitdown, w_updays, w_index)




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
