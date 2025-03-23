from alpha_vantage.timeseries import TimeSeries

# 设置你的 API Key
api_key = 'your_api_key'
ts = TimeSeries(key=api_key, output_format='pandas')

# 获取平安银行（000001.SZ）的日线数据
stock_code = '000001.SZ'
data, meta_data = ts.get_daily(symbol=stock_code, outputsize='full')

print(data.head())
