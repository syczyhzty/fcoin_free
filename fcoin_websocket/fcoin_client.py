# -*- coding: utf-8 -*-
# @Author: zz
# @Date:   2018-06-24 18:15:55
# @Last Modified by:   zz
# @Last Modified time: 2018-06-24 23:25:44

from fcoin_websocket.client import client
import json

class fcoin_client():
	"""docstring for fcoin_client"""
	def __init__(self):
		self._client = client(
			url = 'wss://api.fcoin.com/v2/ws',
			on_message = self._on_message,
		)

	def start(self):
		self._client.start()

	def send(self, data):
		if self._client.is_connected == False:
			print('waiting...')
		while self._client.is_connected == False:
			pass
		self._client.send(data)
			

	def _subscribe(self, channel):
		req = {
				'cmd': 'sub', 
				'args': [channel], 
				'id': '1'}
		self.send(json.dumps(req))

	def subscribe_depth(self, symbol, level):
		channel = 'depth.%(level)s.%(symbol)s' % {'symbol': symbol, 'level': level}
		self._subscribe(channel)

	def subscribe_ticker(self, symbol, ticker_handler = None):
		channel = 'ticker.%(symbol)s' % {'symbol': symbol}
		self.ticker_handler = ticker_handler
		self._subscribe(channel)

	def subscribe_candle(self, symbol, resolution):
		channel = 'candle.%(resolution)s.%(symbol)s' % {'symbol': symbol, 'resolution': resolution}
		self._subscribe(channel)

	def subscribe_trade(self, symbol, trade_handler):
		self.trade_handler = trade_handler
		channel = 'trade.%(symbol)s' % {'symbol': symbol}
		self._subscribe(channel)

	def _on_message(self, ws, message):
		data = json.loads(message)
		if data['type'] == 'hello':
			return
		if self.ticker_handler:
			self.ticker_handler(data)






