import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# 设置数据（可以是实时数据源，示例中使用了随机数据）
x = np.arange(1, 21)
y1 = np.random.randint(0, 100, size=20)
y2 = np.random.randint(0, 100, size=20)

# Data for the pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Data for the bar chart
bar_labels = ['A', 'B', 'C', 'D']
bar_values = [20, 35, 30, 50]

# 创建动态更新的绘图函数
def update(frame):
    # 更新折线图
    ax[0, 0].cla()  # 清空当前图
    ax[0, 0].plot(x, y1 + np.random.randint(0, 10, size=20), label='Line 1', color='blue', marker='o')
    ax[0, 0].set_title('Line Chart 1', fontsize=14)
    ax[0, 0].set_xlabel('X', fontsize=12)
    ax[0, 0].set_ylabel('Y', fontsize=12)
    ax[0, 0].set_ylim(0, 150)  # Set y-axis range to 0-150
    ax[0, 0].tick_params(axis='x')
    ax[0, 0].grid(True)

    # 更新第二个折线图
    ax[1, 0].cla()
    ax[1, 0].plot(x, y2 + np.random.randint(0, 10, size=20), label='Line 2', color='green', marker='s')
    ax[1, 0].set_title('Line Chart 2', fontsize=14)
    ax[1, 0].set_xlabel('X', fontsize=12)
    ax[1, 0].set_ylabel('Y', fontsize=12)
    ax[1, 0].set_ylim(0, 150)
    ax[1, 0].tick_params(axis='x')
    ax[1, 0].grid(True)

    # 更新饼图
    ax[0, 1].cla()
    sizes = np.random.randint(10, 50, size=4)  # 更新饼图数据
    ax[0, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'yellow', 'blue', 'purple'])
    ax[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax[0, 1].set_title('Pie Chart', fontsize=14)

    # 更新柱状图
    ax[1, 1].cla()
    bar_values = np.random.randint(10, 60, size=4)  # 更新柱状图数据
    ax[1, 1].bar(bar_labels, bar_values, color=['orange', 'blue', 'green', 'purple'])
    ax[1, 1].set_title('Bar Chart', fontsize=14)
    ax[1, 1].set_xlabel('Categories', fontsize=12)
    ax[1, 1].set_ylabel('Values', fontsize=12)

    # 调整布局
    plt.tight_layout(pad=5.0)

# 创建图形和子图
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# 使用生成器来创建动态的帧
def generate_frames():
    while True:  # 无限生成帧
        yield None  # 返回空帧，实际更新操作由update函数完成

# 创建动画对象，frames使用生成器
ani = FuncAnimation(fig, update, frames=generate_frames, interval=5000, repeat=True, cache_frame_data=False)

# 显示图表
plt.show()
