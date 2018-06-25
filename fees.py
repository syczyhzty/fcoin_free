# -*- coding: utf-8 -*-
# @Author: zz
# @Date:   2018-06-24 18:15:55
# @Last Modified by:   zz
# @Last Modified time: 2018-06-25 10:49:07

from fcoin import Fcoin
from auth import api_key, api_secret
from config import symbols, fees_start_time
from datetime import datetime
import time

# 初始化
fcoin = Fcoin(api_key, api_secret)
symbol = symbols[0] + symbols[1]
symbol_0_fees = 0 
symbol_1_fees = 0

count = 1

fees = 0
buy_count = 0
sell_count = 0


def fees(after = None, state = 'filled'):
	global symbol_0_fees, symbol_1_fees, count, buy_count, sell_count
	if after:
		order_list = fcoin.list_orders(symbol = symbol, states = state, after = after)
	else:
		dt = datetime(fees_start_time['year'], fees_start_time['month'], fees_start_time['day'], fees_start_time['hour'], fees_start_time['minute'], fees_start_time['second'])
		timestamp = int(dt.timestamp() * 1000)
		order_list = fcoin.list_orders(symbol = symbol, states = state, after = timestamp)
	for order in order_list['data']:
		strcount = '%4d.'%(count)
		formatstr = '{:.9f}'
		print(strcount, '挂单价格', formatstr.format(float(order['price'])), '成交数量', formatstr.format(float(order['filled_amount'])), '方向', order['side'])
		if order['side'] == 'sell':
			sell_count += 1
			symbol_1_fees += float(order['fill_fees'])
		else:
			buy_count += 1
			symbol_0_fees += float(order['fill_fees'])
		
		count += 1
	time.sleep(2)
	if len(order_list['data']) == 100:
		fees(order_list['data'][0]['created_at'])

if __name__ == '__main__':
	print('正在计算中，请耐心等待...')
	fees()
	time.sleep(2)
	fees(None, 'canceled')
	print('当前手续费:', symbols[0], ':', symbol_0_fees, symbols[1], symbol_1_fees)
	print('买入', buy_count, '卖出', sell_count)