python

//生成可执行文件
pyinstaller --onefile your_script.py

这样不需要安装环境

加入预测：

基于成交量

如果成交量volume >20000
	判断大盘涨跌天数consecutive_up_days, ，如果consecutive_up_days<0 //下跌
		判断成交量相比上一个交易日变化，如果change>0
			预测反弹
		如果change<0
			预测反弹
	如果consecutive_up_days=1	//上涨
		判断成交量相比上一个交易日变化，如果change>0  //放量上涨
			预测继续涨
		如果change<0    //缩量上涨
			预测继续涨
	如果consecutive_up_days>2	//上涨两天
		判断成交量相比上一个交易日变化，如果change>0  //放量上涨
			预测继续涨
		如果change<0    //缩量上涨
			预测继续涨
如果成交量18000<volume<20000
	判断大盘涨跌天数consecutive_up_days, ，如果consecutive_up_days<0 //下跌
		判断成交量相比上一个交易日变化，如果change>0
			预测反弹
		如果change<0
			预测反弹
	如果consecutive_up_days=1	//上涨
		判断成交量相比上一个交易日变化，如果change>0  //放量上涨
			预测继续涨
		如果change<0    //缩量上涨
			预测继续涨
	如果consecutive_up_days>2	//上涨两天
		判断成交量相比上一个交易日变化，如果change>0  //放量上涨
			预测继续涨
		如果change<0    //缩量上涨
			预测继续涨




