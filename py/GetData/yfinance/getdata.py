import yfinance as yf
import datetime
import pandas as pd

# 获取今天的日期
today = datetime.date.today()

# 获取今年的第一天
start_date = datetime.date(today.year, 1, 1)

# 设置股票代码
stock_code = '000801.SZ'

# 获取股票的历史数据（今年以来）
df = yf.download(stock_code, start=start_date, end=today)

# 保存到Excel
file_path = '000801_SZ_2025_data.xlsx'
df.to_excel(file_path)

print(f"Data saved to {file_path}")
