import sys
import logging
from PyQt5.QtCore import Qt
import calculatortest  # 导入你的计算逻辑
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit, 
                             QPushButton, QSizePolicy, QHBoxLayout, QSpacerItem, QApplication)

# 设置日志
logging.basicConfig(
    filename="0run.log",  # 指定日志文件
    level=logging.INFO,  # 记录级别（INFO 及以上）
    format="%(asctime)s - %(levelname)s - %(message)s",  # 日志格式
    datefmt="%Y-%m-%d %H:%M:%S"
)

# 重定向 print 输出到 log 文件
class Logger(object):
    def __init__(self, filename="0run.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)  # 控制台打印
        self.log.write(message)  # 记录到日志文件

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = Logger()
sys.stderr = Logger()  # 错误输出也写入日志


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("计算器")
        self.setGeometry(200, 200, 400, 250)

        self.layout = QVBoxLayout()

        # 创建输入框
        self.value1_input = QLineEdit(self)
        self.value2_input = QLineEdit(self)
        self.value3_input = QLineEdit(self)
        self.value4_input = QLineEdit(self)
        self.value5_input = QLineEdit(self)
        self.result_display = QLineEdit(self)

        # 右对齐显示结果
        self.result_display.setAlignment(Qt.AlignRight)

        # 使用 QFormLayout 布局
        form_layout = QFormLayout()
        form_layout.addRow("成交量:", self.value1_input)
        form_layout.addRow("涨幅大于5%家数:", self.value2_input)
        form_layout.addRow("跌幅大于5%家数:", self.value3_input)
        form_layout.addRow("连续上涨天数(下跌为负):", self.value4_input)
        form_layout.addRow("上证指数变化:", self.value5_input)
        form_layout.addRow("Emotion Factor:", self.result_display)

        self.layout.addLayout(form_layout)

        # 按钮布局
        button_layout = QHBoxLayout()
        equals_button = QPushButton('计算', self)
        equals_button.clicked.connect(self.calculate)
        button_layout.addWidget(equals_button)

        save_button = QPushButton('保存结果', self)
        save_button.clicked.connect(self.save_results)
        button_layout.addWidget(save_button)

        clear_button = QPushButton('清空', self)
        clear_button.clicked.connect(self.clear)
        button_layout.addWidget(clear_button)

        button_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

    def calculate(self):
        try:
            # 获取用户输入
            volume = self.get_float_from_input(self.value1_input)
            limit_up = self.get_float_from_input(self.value2_input)
            limit_down = self.get_float_from_input(self.value3_input)
            consecutive_up_days = self.get_float_from_input(self.value4_input)
            index_change = self.get_float_from_input(self.value5_input)

            logging.info(f"用户输入: volume={volume}, limit_up={limit_up}, limit_down={limit_down}, "
                         f"consecutive_up_days={consecutive_up_days}, index_change={index_change}")

            # 计算结果
            result = calculatortest.calculate_total_scores(volume, limit_up, limit_down, consecutive_up_days, index_change)
            self.result_display.setText(str(result))

            logging.info(f"计算结果: {result}")

        except ValueError:
            logging.warning("无效输入")
            self.result_display.setText("无效输入")

    def save_results(self):
        try:
            volume = self.get_float_from_input(self.value1_input)
            limit_up = self.get_float_from_input(self.value2_input)
            limit_down = self.get_float_from_input(self.value3_input)
            consecutive_up_days = self.get_float_from_input(self.value4_input)
            index_change = self.get_float_from_input(self.value5_input)

            result = calculatortest.calculate(volume, limit_up, limit_down, consecutive_up_days, index_change,
                                              w_volume=0, w_limitup=0, w_limitdown=0, w_updays=0, w_index=0)

            calculatortest.save_emotion_values_to_txt("emotion_values.txt", result)

            logging.info(f"结果已保存: {result}")

        except ValueError:
            logging.warning("保存时输入无效")
            self.result_display.setText("无效输入")

    def clear(self):
        self.value1_input.clear()
        self.value2_input.clear()
        self.value3_input.clear()
        self.value4_input.clear()
        self.value5_input.clear()
        self.result_display.clear()

    def get_float_from_input(self, input_widget):
        try:
            value = input_widget.text().strip()
            if value == "":
                raise ValueError("输入不能为空")
            return float(value)
        except ValueError:
            raise ValueError("无效的数字输入")


if __name__ == "__main__":
    app = QApplication([])
    window = CalculatorApp()
    window.show()
    app.exec_()
