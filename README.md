# Fcoin对刷机器人

## 讨论群

提供免费版和付费版，交流群

<img src="./barcode.png" align=center />



## 环境

1. sublime编辑器 (https://www.sublimetext.com/)
2. 安装python3
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000
3. 打开cmd
4. 输入 `pip install requests`
5. 输入 `pip install websocket-client`



## 配置


### auth.py

* 填写fcoin的`api.key`
* 填写fcoin的`api.secret`

### config.py

* `symbols`: 交易类型
* `amoucnt`: 交易数量
* `price_difference`: 深度图买一卖一差值
* `symbol_type`: 查询余额类型
* `second`: 买卖间隔时间
* `fees_start_time`: 需要计算手续费的开始时间



## 运行

windows搜索cmd，mac搜索terminal



一 对刷

1. 搜索cmd（终端）并且打开 回车
2. 执行`cd`空格然后拖拽fcoin这个文件夹到cmd里面 回车
3. mac: `python3 robot.py`   windows: `python robot.py`回车

二 余额

1. 搜索cmd（终端）并且打开
2. 执行`cd`空格然后拖拽fcoin这个文件夹到cmd里面 回车
3. mac: `python3 balance.py` windows: `python balance.py`

三 手续费

1. 搜索cmd（终端）并且打开
2. 执行`cd`空格然后拖拽fcoin这个文件夹到cmd里面 回车
3. mac `python3 fees.py` windows: `python fees.py`