1. python -m venv:以脚本的方式运行Python内置的venv（虚拟环境）模块
最后的 venv：你给虚拟环境文件夹起的名字（可以换成别的，比如 myenv）
执行后，当前目录会多出一个 venv 文件夹，里面包含一个独立的 Python 解释器和独立的 pip 包管理工具，与系统全局的 Python 完全隔离。

2. 虚拟环境有什么用？
隔离项目依赖：不同的项目可能需要同一个库的不同版本，虚拟环境可以避免冲突。
干净的环境：不会污染系统 Python，方便打包和部署。
便于协作：用 requirements.txt 可以让别人快速复现一模一样的依赖环境。

3. pip:Python的软件包管理器
 pip = 专门给你跑腿买菜的人
但是，如果你今天想做水煮鱼，家里没有鱼，也没有水煮鱼调料，怎么办？
你需要一个专门帮你采购食材的人。你只要喊一声：“去给我买条鱼，再买包水煮鱼调料回来！”
pip 就是这个人。
你想做一个网站？跟 pip 说：pip install flask（“去买 flask 这个做网站的调料”）。
想处理表格数据？pip install pandas（“去买 pandas 这个处理表格的肉”）。
想爬取网页？pip install requests（“去买 requests 这个上网抓东西的鱼”）。
pip 会跑到一个叫 PyPI（Python Package Index）的超级大菜市场里，把你需要的食材（包）找到，自动下载、装进你的厨房，你直接就能用。

4. requirement.txt:各个库所需要的版本清单
    4.1 手写
    4.2 自动生成：你已经在虚拟环境里装好了一堆包（用 pip install 买好了菜），想把这堆包的名字全记下来，就用：pip freeze >requirement.txt
想要直接配置上面的环境：pip install -r requirement.txt

