import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.family'] = ['Microsoft YaHei']
rcParams['axes.unicode_minus'] = False

def load_data_from_file(filename):
    """从文件中读取数据"""
    df = pd.read_excel(filename)
    emotion_values = df['Emotion Values'].values.tolist()
    price_changes = df['Price Changes'].values.tolist()
    Daily_Return = df['Daily Return'].values.tolist()
    Actual_Capital = df['Actual Capital'].values.tolist()

    return emotion_values, price_changes, Daily_Return, Actual_Capital

import numpy as np

def plot_data(emotion_values, price_changes):
    """绘制两个子图并返回 fig1, fig2"""
    x = np.arange(1, len(emotion_values) + 1)

    # **第一个图 (fig1)：情绪因子柱状图**
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    cmap = plt.cm.RdYlGn_r
    norm = plt.Normalize(vmin=0, vmax=1)
    bars = ax1.bar(x, emotion_values, color=cmap(norm(emotion_values)))
    ax1.set_title('Emotion Factor(最近20天)', fontsize=16)
    ax1.set_ylim(0, 1)
    ax1.grid(True, linestyle="--", linewidth=0.5)

    # **数值显示在柱状图上**
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax1.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=10)

    # 设置 fig1 的横坐标刻度为整数
    ax1.set_xticks(x)  # 设置为整数
    ax1.set_xticklabels(x, fontsize=12)

    # **第二个图 (fig2)：价格趋势折线图**
    fig2, ax2 = plt.subplots(figsize=(20, 6))
    ax2.plot(x, price_changes, label='实盘收益率', color='red', marker='o')

    ax2.set_title('实盘收益率', fontsize=16)
    ax2.grid(True, linestyle="--", linewidth=0.5)
    ax2.legend()

    # **计算合适的横坐标间隔**
    interval = max(1, len(x) // 10)  # 例如：100个数据 -> 每10个显示一个
    xticks = list(range(x[0], x[-1] + 1, interval))  # 生成等间隔刻度
    xticks.append(x[-1])  # 确保最后一个点也显示

    ax2.set_xticks(xticks)
    ax2.set_xticklabels(xticks, rotation=0, fontsize=12, fontstyle='normal')  # 设置横坐标为正常字体

    # **仅在最后一个点显示数值（红色）**
    x_last, y_last = x[-1], price_changes[-1]
    ax2.text(x_last, y_last, f'{y_last:.2f}', ha='left', va='bottom', fontsize=12, color='red', fontweight='bold')

    return fig1, fig2





