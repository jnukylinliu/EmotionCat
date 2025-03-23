from iexfinance.stocks import get_historical_data
from datetime import datetime

# 设置 API Token
api_token = 'your_api_token'

# 获取平安银行（000001.SZ）的历史数据
stock_code = '000001'
data = get_historical_data(stock_code, start=datetime(2023, 1, 1), end=datetime(2023, 3, 1), token=api_token)

print(data.head())
