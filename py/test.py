import sys
import logging
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
    QSizePolicy, QHBoxLayout, QSpacerItem, QApplication, QMessageBox
)
import pandas as pd  # 确保导入pandas
from datetime import datetime
import calculatortest  # 引用新的 calculatortest 模块

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("计算器")
        self.setGeometry(200, 200, 400, 250)
        self.init_ui()

    def init_ui(self):
        # 主布局
        self.layout = QVBoxLayout()

        # 创建输入框和结果显示
        self.value1_input = QLineEdit(self)
        self.value2_input = QLineEdit(self)
        self.value3_input = QLineEdit(self)
        self.value4_input = QLineEdit(self)
        self.value5_input = QLineEdit(self)
        self.value6_input = QLineEdit(self)  # 新增输入框1（当天收益）
        self.value7_input = QLineEdit(self)  # 新增输入框2（总额度）
        self.result_display = QLineEdit(self)  # 显示Emotion Factor
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)  # 使计算结果只读

        # 用来显示总收益率的结果
        self.sum_display = QLineEdit(self)
        self.sum_display.setAlignment(Qt.AlignRight)
        self.sum_display.setReadOnly(True)  # 只读

        # 使用 QFormLayout 布局各个控件
        form_layout = QFormLayout()
        form_layout.addRow("成交量:", self.value1_input)
        form_layout.addRow("涨幅大于5%家数:", self.value2_input)
        form_layout.addRow("跌幅大于5%家数:", self.value3_input)
        form_layout.addRow("连续上涨天数(下跌为负):", self.value4_input)
        form_layout.addRow("上证指数变化:", self.value5_input)
        form_layout.addRow("当日收益率:", self.value6_input)  # 改为当天收益
        form_layout.addRow("总额度:", self.value7_input)  # 改为总额度
        form_layout.addRow("Emotion Factor:", self.result_display)  # 显示Emotion Factor
        form_layout.addRow("总收益率:", self.sum_display)  # 修改为总收益率
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

        button_layout.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)




    def get_inputs(self):
        """
        获取用户输入，并转换为浮点数
        """
        try:
            volume = self.get_float_from_input(self.value1_input)
            limit_up = self.get_float_from_input(self.value2_input)
            limit_down = self.get_float_from_input(self.value3_input)
            consecutive_up_days = self.get_float_from_input(self.value4_input)
            index_change = self.get_float_from_input(self.value5_input)
            logging.info(f"用户输入: volume={volume}, limit_up={limit_up}, "
                        f"limit_down={limit_down}, consecutive_up_days={consecutive_up_days}, "
                        f"index_change={index_change}")
            return volume, limit_up, limit_down, consecutive_up_days, index_change
        except ValueError as e:
            logging.warning(f"输入错误: {e}")
            self.result_display.setText("无效输入")
            self.sum_display.setText("无效输入")
            raise



    def calculate(self):
        """
        计算情绪因子（Emotion Factor），并显示结果。
        计算总收益率，根据总额度减去17000后除以17000来得到。
        """
        try:
            # 获取所有输入
            volume, limit_up, limit_down, consecutive_up_days, index_change = self.get_inputs()
            
            # 计算Emotion Factor
            emotion_factor = calculatortest.calculate_total_scores(
                volume, limit_up, limit_down, consecutive_up_days, index_change
            )
            
            # 显示Emotion Factor
            self.result_display.setText(str(emotion_factor))
            
            # 获取总额度
            total_quota = self.get_float_from_input(self.value7_input)
            
            # 计算总收益率
            total_return = (total_quota - 17000) / 17000
            
            # 将总收益率转换为百分比并保留一位小数
            total_return_percentage = round(total_return * 100, 1)
            
            # 显示总收益率
            self.sum_display.setText(f"{total_return_percentage}%")
            
            # 打印计算结果
            logging.info(f"Emotion Factor: {emotion_factor}, 总收益率: {total_return_percentage}%")
            
        except ValueError as e:
            logging.error(f"输入错误: {e}")
            self.result_display.setText("计算错误")
            self.sum_display.setText("计算错误")
        except Exception as e:
            logging.error(f"计算时发生错误: {e}")
            self.result_display.setText("计算错误")
            self.sum_display.setText("计算错误")




    def save_results(self):
        """
        保存计算结果到 Excel 文件的相应列末尾
        """
        try:
            # 直接从 result_display 中获取 Emotion Factor
            emotion_factor = self.result_display.text()
            if not emotion_factor:
                raise ValueError("Emotion Factor 为空")
            
            # 获取总收益率
            total_return_percentage = float(self.sum_display.text().replace('%', ''))  # 总收益率从显示框获取，去掉 '%' 符号
            total_return_percentage =total_return_percentage *0.01
            # 获取总额度
            total_quota = self.get_float_from_input(self.value7_input)
            
            # 获取当天收益（直接从UI界面的value6_input读取）
            daily_return = self.get_float_from_input(self.value6_input)  # 获取当天收益
            
            # 获取当前日期（可选，作为记录）
            current_date = datetime.now().strftime('%Y-%m-%d')  # 格式为 YYYY-MM-DD

            # 读取 Excel 文件
            df = pd.read_excel('1data.xlsx')

            # 检查是否存在相应列，如果不存在则创建空列
            if 'Emotion Values' not in df.columns:
                df['Emotion Values'] = pd.NA
            if 'Price Changes' not in df.columns:
                df['Price Changes'] = pd.NA
            if 'Actual Capital' not in df.columns:
                df['Actual Capital'] = pd.NA
            if 'Daily Return' not in df.columns:
                df['Daily Return'] = pd.NA

            # 将数据添加到列末尾
            df.loc[len(df)] = [
                emotion_factor,                # Emotion Factor (从 result_display 获取)
                total_return_percentage,       # 总收益率
                total_quota,                   # 总额度
                daily_return                   # 当日收益率，从 UI 获取
            ]

            # 保存更新后的 Excel 文件
            df.to_excel('1data.xlsx', index=False)

            # 显示保存成功提示
            self.show_message("保存成功", "结果已成功保存到 Excel 文件中。")
                
        except Exception as e:
            logging.error(f"保存结果时发生错误: {e}")
            self.result_display.setText("保存错误")
            # 显示保存失败提示
            self.show_message("保存失败", "保存结果时发生错误，请重试。")

    def show_message(self, title, message):
        """
        显示消息框
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)  # 信息提示框
        msg.setWindowTitle(title)  # 设置标题
        msg.setText(message)  # 设置提示内容
        msg.setStandardButtons(QMessageBox.Ok)  # 添加一个“确定”按钮
        msg.exec_()  # 显示消息框

    def clear(self):
        """
        清空所有输入和显示控件
        """
        self.value1_input.clear()
        self.value2_input.clear()
        self.value3_input.clear()
        self.value4_input.clear()
        self.value5_input.clear()
        self.value6_input.clear()  # 清空新增输入框1
        self.value7_input.clear()  # 清空新增输入框2
        self.result_display.clear()  # 清空Emotion Factor显示框
        self.sum_display.clear()  # 清空新增输入之和显示框


    def get_float_from_input(self, input_widget):
        """
        将输入控件中的文本转换为浮点数，如果转换失败则抛出异常
        """
        value = input_widget.text().strip()
        if not value:
            raise ValueError("输入不能为空")
        try:
            return float(value)
        except ValueError:
            raise ValueError("无效的数字输入")

if __name__ == "__main__":
    app = QApplication([])
    window = CalculatorApp()
    window.show()
    app.exec_()
