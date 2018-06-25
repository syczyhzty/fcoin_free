# Fcoin对刷机器人

## 讨论群

提供免费版和付费版，交流群

<img src="./barcode.png" align=center />

## 策略以及风险
1. 先买后卖
2. 根据深度图买一卖一差值
3. 万二的差价

下单成功后则会继续下一笔下单操作，不会管有没有成交，所以存在截单的风险，请大家明白之后再进行操作，<font color = 'red'>**风险自负**</font>

## 建议
大家进行翻墙使用

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


## 打赏
如果你觉得使用不错

* BTC: 3AdbaFQpUWcuQHzQmboC9MzGdL3MesP5GS
* ETH: 0xe17679962f4dc3e4f7f71075f421a0e6897a4b78