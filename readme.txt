/**********************************************************************
EmotionCat是一个A股买卖点判断软件。
众所周知，A股是以情绪为主的市场，笔者具备数十年实盘交易的经验，侧重于情绪投资策略研究。
顾名思义，EmotionCat是通过计算来衡量当前的买卖时机，不在情绪走弱的时候开仓，不在情绪高潮时开仓，控制交易者情绪，控制回撤，并以笔者实盘作为参考。
**********************************************************************/


当前推送：
git add .
git commit -m "Add */."
git push origin master

删除缓存：
git rm --cached -r .



2025-2-9
之前nginx可能和github推送的端口冲突，需要修改配置文件
/*
尝试使用 GitHub 的备用 SSH 端口（端口 443）
如果端口 22 被阻塞，您可以尝试使用 GitHub 的备用端口（端口 443）。按以下步骤进行设置：

打开 Git Bash，编辑 SSH 配置文件（如果没有该文件，您可以创建一个）：

bash
复制
编辑
nano ~/.ssh/config
在配置文件中添加以下内容：

nginx
复制
编辑
Host github.com
  Hostname ssh.github.com
  Port 443
保存并退出（按 Ctrl + X，然后按 Y 和 Enter）。

重新运行 SSH 测试命令：

bash
复制
编辑
ssh -T git@github.com
这样可以让 Git 通过端口 443 连接 GitHub，通常这个端口不受防火墙限制。
*/

exe在debug目录下，可直接运行

优化了ui界面的显示，增加了条形图和纵坐标

建议：
对当日的策略有影响可以看开盘成交、前五分钟成交和前半小时（一小时）成交量的变化

优化py界面，优化EmotionFactor计算方式

增加基于transformaer模型的py代码，用于训练计算Emotion Factor的模型，还不成熟，数据集不够。

手写transformaer模型，然后用来训练，正在进行中



