from jqdatasdk import *
import datetime

# 登录聚宽账户
auth('18190626428', 'tanggu670Q')

# 设置日期为2024年12月15日
stock_code = '000001.XSHE'
date = datetime.date(2024, 12, 19)

# 获取指定日期的数据
data = get_price(stock_code, start_date=date, end_date=date, fields=['close', 'volume'])

if not data.empty:
    # 打印成交量
    volume = data['volume'].iloc[0]
    print(f"股票 {stock_code} 在 {date} 的成交量: {volume}")

    # 获取前一天的数据并计算涨幅
    prev_data = get_price(stock_code, start_date=(date - datetime.timedelta(days=1)), end_date=(date - datetime.timedelta(days=1)), fields=['close'])
    prev_close_price = prev_data['close'].iloc[0] if not prev_data.empty else data['close'].iloc[0]

    # 计算涨幅
    if prev_close_price != 0:
        change = (data['close'].iloc[0] - prev_close_price) / prev_close_price * 100
        print(f"股票 {stock_code} 在 {date} 的涨幅: {change:.2f}%")
    else:
        print("前一天的收盘价为0，无法计算涨幅")
else:
    print(f"无法获取股票 {stock_code} 的数据")
