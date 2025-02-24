import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import pandas as pd

# 设置字体为支持中文的字体
rcParams['font.sans-serif'] = ['Microsoft YaHei']  # Windows上使用微软雅黑
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def load_data_from_file(filename):
    """从文件中读取数据"""
    emotion_values = []
    position_ratio = []
    price_changes = []
    
    # 读取xlsx文件
    df = pd.read_excel(filename)

    # 假设文件有 'Emotion Values'，'Position Ratio'，'Price Changes' 三列
    emotion_values = df['Emotion Values'].values.tolist()
    position_ratio = df['Position Ratio'].values.tolist()
    price_changes = df['Price Changes'].values.tolist()

    return emotion_values, position_ratio, price_changes

def start_trading():
    print("开始实盘交易...")
    
    # 读取数据文件
    filename = 'data.xlsx'  # 数据文件的路径
    emotion_values, position_ratio, price_changes = load_data_from_file(filename)
    
    # 获取最后30个数据
    emotion_values = emotion_values[-30:]
    position_ratio = position_ratio[-30:]
    price_changes = price_changes[-30:]
    
    # 处理x的长度，确保横坐标与数据长度一致
    x = np.arange(1, len(emotion_values) + 1)  # 横坐标：天数
    
    # 创建一个新的布局，3行1列，第1列是3个折线图
    fig, ax = plt.subplots(3, 1, figsize=(10, 15))  # 使用 3 行 1 列的布局



    # 创建渐变色
    cmap = plt.cm.RdYlGn_r  # 从绿色到红色的渐变色
    # 归一化 emotion_values，确保值在 [0, 1] 范围内
    norm = plt.Normalize(vmin=0, vmax=1)
    # 1. Emotion Values 图 (纵坐标 0 到 1)
    bars = ax[0].bar(x, emotion_values, label='Emotion Values', color=cmap(norm(emotion_values)))
    # 在每个条形上方标记 y 数据（当值不为 0 时）
    for i, value in enumerate(emotion_values):
        if value != 0:  # 如果值不为 0，才显示标签
            ax[0].text(x[i], value + 0.02, f'{value:.2f}', ha='center', va='bottom', fontsize=12, color='black')
    ax[0].set_title('Emotion Values', fontsize=16)
    ax[0].set_xlabel('天数', fontsize=14)
    ax[0].set_ylabel('Emotion Values', fontsize=14)
    ax[0].set_ylim(0, 1)
    ax[0].tick_params(axis='both', labelsize=12)
    ax[0].grid(True)





    # 2. 仓位占比图 (纵坐标 0 到 1)
    ax[1].bar(x, position_ratio, label='仓位占比', color='green')
    ax[1].set_title('仓位占比', fontsize=16)
    ax[1].set_xlabel('天数', fontsize=14)
    ax[1].set_ylabel('仓位占比', fontsize=14)
    ax[1].set_ylim(0, 1)
    ax[1].tick_params(axis='both', labelsize=12)
    ax[1].grid(True)


    # 3. 实盘跟随涨跌幅图 (纵坐标根据点位值变化)
    ax[2].plot(x, price_changes, label='实盘涨跌幅', color='red')
    ax[2].set_title('实盘跟随涨跌幅', fontsize=16)
    ax[2].set_xlabel('天数', fontsize=14)
    ax[2].set_ylabel('点位变化', fontsize=14)
    ax[2].tick_params(axis='both', labelsize=12)
    ax[2].grid(True)

    # 调整布局，确保标签不重叠
    plt.tight_layout(pad=3.0)  # 自动调整间距，增加 pad 参数使得间距更宽松

    # 手动调整子图的间距，避免文字碰撞
    plt.subplots_adjust(hspace=0.4)  # 调整子图的垂直间距

    # 设置每个图的横坐标“天数”标签在30旁边
    for axes in ax:
        axes.set_xticks(x)
        axes.set_xticklabels(x, fontsize=12)

    # 将横坐标的“天数”放在横坐标末端
    ax[0].set_xlabel('天数', fontsize=14, labelpad=10, loc='right')  # 第一幅图
    ax[1].set_xlabel('天数', fontsize=14, labelpad=10, loc='right')  # 第二幅图
    ax[2].set_xlabel('天数', fontsize=14, labelpad=10, loc='right')  # 第三幅图

    # 显示所有图表
    plt.show()

# 如果直接运行 real_trading.py，自动调用 start_trading()
if __name__ == "__main__":
    start_trading()