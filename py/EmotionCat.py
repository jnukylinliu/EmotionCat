import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QVBoxLayout
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QFont  # 导入 QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import data_process
from matplotlib import rcParams

# 设置中文字体
rcParams['font.family'] = ['Microsoft YaHei']
rcParams['axes.unicode_minus'] = False

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # 窗口标题 & 时间
        current_time = QDateTime.currentDateTime().toLocalTime()
        date_str = current_time.toString("yyyy年M月d日（ddd）")
        self.setWindowTitle("Emotion Factor " + date_str)
        self.setGeometry(100, 100, 1200, 800)

        # 主要容器
        container = QWidget()
        self.setCentralWidget(container)

        # **1. 创建网格布局**
        layout = QGridLayout()
        container.setLayout(layout)

        # **2. Matplotlib 画布**
        self.canvas1 = FigureCanvas(plt.figure(figsize=(10, 5)))  # fig1
        self.canvas2 = FigureCanvas(plt.figure(figsize=(20, 6)))  # fig2

        # **3. 右侧显示框**
        self.create_display_frame(layout)

        # **4. 布局子图**
        layout.addWidget(self.canvas1, 0, 0)  # fig1 (0,0)
        layout.addWidget(self.canvas2, 1, 0, 1, 2)  # fig2 (1,0) & (1,1)
       
        # **5. 绘制图表**
        self.plot_data()

        # **6. 显示窗口**
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowFullScreen)
        self.show()





    def create_display_frame(self, layout):
        """创建右侧显示框 (0,1)"""
        # 设置字体大小
        font = QFont('Microsoft YaHei', 16)  # 使用微软雅黑，字号为16

        # Emotion Factor
        self.emotion_label = QLabel("Emotion Factor(最新):")
        self.emotion_value = QLineEdit("0.75")
        self.emotion_value.setReadOnly(True)
        self.emotion_label.setFont(font)
        self.emotion_value.setFont(font)
        self.emotion_value.setFixedHeight(40)  # 增大显示框高度
        self.emotion_value.setFixedWidth(250)  # 设置更大的宽度
        self.emotion_value.setAlignment(Qt.AlignCenter)  # 设置数据居中

        # Price Changes
        self.position_label = QLabel("实盘收益率:")
        self.position_value = QLineEdit("0.50")
        self.position_value.setReadOnly(True)
        self.position_label.setFont(font)
        self.position_value.setFont(font)
        self.position_value.setFixedHeight(40)  # 增大显示框高度
        self.position_value.setFixedWidth(250)  # 设置更大的宽度
        self.position_value.setAlignment(Qt.AlignCenter)  # 设置数据居中

        # Today 
        self.price_label = QLabel("当日收益率:")
        self.price_value = QLineEdit("1.25")
        self.price_value.setReadOnly(True)
        self.price_label.setFont(font)
        self.price_value.setFont(font)
        self.price_value.setFixedHeight(40)  # 增大显示框高度
        self.price_value.setFixedWidth(250)  # 设置更大的宽度
        self.price_value.setAlignment(Qt.AlignCenter)  # 设置数据居中

        # Real price
        self.extra_label = QLabel("实盘金额:")
        self.extra_value = QLineEdit("Data")
        self.extra_value.setReadOnly(True)
        self.extra_label.setFont(font)
        self.extra_value.setFont(font)
        self.extra_value.setFixedHeight(40)  # 增大显示框高度
        self.extra_value.setFixedWidth(250)  # 设置更大的宽度
        self.extra_value.setAlignment(Qt.AlignCenter)  # 设置数据居中

        # **创建 QGridLayout 来排列这些控件成两列四行**
        display_layout = QGridLayout()

        # 第一列 QLabels
        display_layout.addWidget(self.emotion_label, 0, 0, alignment=Qt.AlignRight)  # 标签右对齐
        display_layout.addWidget(self.position_label, 1, 0, alignment=Qt.AlignRight)
        display_layout.addWidget(self.price_label, 2, 0, alignment=Qt.AlignRight)
        display_layout.addWidget(self.extra_label, 3, 0, alignment=Qt.AlignRight)

        # 第二列 QLineEdits
        display_layout.addWidget(self.emotion_value, 0, 1, alignment=Qt.AlignCenter)  # 文本框居中
        display_layout.addWidget(self.position_value, 1, 1, alignment=Qt.AlignCenter)
        display_layout.addWidget(self.price_value, 2, 1, alignment=Qt.AlignCenter)
        display_layout.addWidget(self.extra_value, 3, 1, alignment=Qt.AlignCenter)

        # 设置行和列的间距
        display_layout.setHorizontalSpacing(20)  # 水平间距
        display_layout.setVerticalSpacing(15)    # 垂直间距

        # 创建一个 QWidget 将布局应用到其中
        widget = QWidget()
        widget.setLayout(display_layout)

        # 将显示框放到网格布局中 (0,1) 位置
        layout.addWidget(widget, 0, 1)




    def plot_data(self):
        """绘制图表"""
        # 读取数据
        filename = '1data.xlsx'
        emotion_values, price_changes, Daily_Return, Actual_Capital = data_process.load_data_from_file(filename)

        emotion_values = emotion_values[-20:]  # 不限制为30个

        #更新数据
        latest_emotion_factor = emotion_values[-1]  # 获取最新的情绪因子值
        self.emotion_value.setText(f"{latest_emotion_factor:.2f}")  # 设置格式化后的数值

        latest_position_rate = price_changes[-1]  # 获取最新的实盘收益率值
        self.position_value.setText(f"{latest_position_rate:.2f}")  # 设置格式化后的数值

        latest_Daily_Return = Daily_Return[-1]
        self.price_value.setText(f"{latest_Daily_Return:.2f}%")  # 设置格式化后的数值

        latest_Actual_Capital = Actual_Capital[-1]
        self.extra_value.setText(f"{latest_Actual_Capital:.0f}")


        fig1, _ = data_process.plot_data(emotion_values, [0]*len(emotion_values))  # 为了只显示 fig1 使用 emotion_values
        # 为 fig2 绘制数据 (price_changes)
        _, fig2 = data_process.plot_data([0]*len(price_changes), price_changes)  # 为了只显示 fig2 使用 price_changes

        # **左上角 (0,0) 更新 fig1**
        self.canvas1.figure = fig1
        self.canvas1.draw()

        # **底部 (1,0) & (1,1) 更新 fig2**
        self.canvas2.figure = fig2
        self.canvas2.draw()



# **运行应用**
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyApp()
    sys.exit(app.exec_())
