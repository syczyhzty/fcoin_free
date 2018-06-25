# -*- coding: utf-8 -*-
# @Author: zz
# @Date:   2018-06-24 17:39:28
# @Last Modified by:   zz
# @Last Modified time: 2018-06-25 00:11:43

import websocket
import time
import json
from threading import Thread
from websocket import setdefaulttimeout


class client(Thread):
	"""docstring for client"""
	def __init__(self, url, on_open = None, on_message = None, on_error = None, on_close = None):
		Thread.__init__(self)
		self._url = url
		self._on_open = on_open
		self._on_message = on_message
		self._on_error = on_error
		self._on_close = on_close
		self._is_connected = False

	def _connect(self):
		websocket.enableTrace(True)
		self._ws = websocket.WebSocketApp(url = self._url,
									on_open = self.on_open,
									on_message = self.on_message,
									on_error = self.on_error,
									on_close = self.on_close)
		setdefaulttimeout(5)
		while True:
			print('try to connect...')
			self._ws.run_forever()

	@property
	def is_connected(self):
		return self._is_connected

	def send(self, msg):
		self._ws.send(msg)

	def run(self):
		self._connect()

	def on_message(self, ws, message):
		# print('message is', message)
		if self._on_message:
			self._on_message(ws, message)
		

	def on_error(self, ws, error):
		self._is_connected = False
		print('error is ', error)
		if self._on_error:
			self._on_error(ws, error)

	def on_close(self, ws):
		print("### closed ###")
		self._is_connected = False
		if self._on_close:
			self._on_close(ws)

	def on_open(self, ws):
		print('websocket is connected')
		self._is_connected = True
		if self._on_open:
			self._on_open(ws)




