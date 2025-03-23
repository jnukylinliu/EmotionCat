import tushare as ts
import pandas as pd

# 设置 TuShare API Token
ts.set_token('9401d81854111c16e3e2283e57e0793109ae827fa6f4f5e81c932083')

# 初始化 TuShare API
pro = ts.pro_api()

def get_daily_data(ts_code, start_date, end_date, save_csv=False):
    """
    获取指定股票的日线数据。

    参数:
    - ts_code: 股票代码（例如 '002182.SZ'）
    - start_date: 开始日期（格式 'YYYYMMDD'）
    - end_date: 结束日期（格式 'YYYYMMDD'）
    - save_csv: 是否保存为 CSV 文件，默认 False

    返回:
    - DataFrame 格式的日线行情数据
    """

    try:
        # 调用 TuShare daily API 获取数据
        df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)

        # 检查是否获取到数据
        if df.empty:
            print(f"未获取到 {ts_code} 从 {start_date} 到 {end_date} 的数据，请检查日期或代码是否正确")
            return None

        # 按日期降序排列
        df.sort_values(by="trade_date", ascending=True, inplace=True)

        # 打印数据
        print(df)

        # 如果需要保存为 CSV
        if save_csv:
            file_name = f"{ts_code}_{start_date}_{end_date}.csv"
            df.to_csv(file_name, index=False)
            print(f"数据已保存为 {file_name}")

        return df

    except Exception as e:
        print(f"获取数据时出错: {e}")
        return None

# 示例：获取平安银行（000001.SZ）的日线数据（2024年1月1日至2024年3月1日）
df = get_daily_data(ts_code='002182.SZ', start_date='20250101', end_date='20250301', save_csv=True)
