import pandas as pd
import mplfinance as mpf

# 读取数据
df = pd.read_excel('stock_data.xlsx', sheet_name='Sheet1', index_col=0)

# 将索引转换为日期格式
df.index = pd.to_datetime(df.index, errors='coerce')

# 确保数据列正确
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# 打印数据以确认正确性
print(df.head())

# 绘制日K线图
mpf.plot(df, type='candle', style='charles', title="000801.SZ 日K线图", ylabel='价格 (元)', volume=True)
