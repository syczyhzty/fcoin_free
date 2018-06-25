# -*- coding: utf-8 -*-
# @Author: zz
# @Date:   2018-06-24 18:15:55
# @Last Modified by:   zhiz
# @Last Modified time: 2018-06-25 13:24:31

from fcoin import Fcoin
from auth import api_key, api_secret
from config import symbol_type

# 初始化
fcoin = Fcoin(api_key, api_secret)

# 查询账户余额
def get_balance_action(symbols):
    balance_info = fcoin.get_balance()
    print(balance_info)
    for info in balance_info['data']:
    	for symbol in symbols:
	        if info['currency'] == symbol:
	            balance = info
	            print(balance['currency'], '账户余额', balance['balance'], '可用', balance['available'], '冻结', balance['frozen'])

def balance():
    # 账户余额
    get_balance_action(symbol_type)


# 守护进程
if __name__ == '__main__':
    balance()
