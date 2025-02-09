当前推送：
git add .
git commit -m "Add */."
git push origin master




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

