# -*- coding: utf-8 -*-
# @Author: zz
# @Date:   2018-06-24 17:39:28
# @Last Modified by:   zz
# @Last Modified time: 2018-06-25 10:45:17

import os
import hmac
import hashlib
import requests
import time
import base64
import json
from websocket import create_connection
from enum import Enum, unique

@unique
class StatusErrorCode(Enum):
    """docstring for StatusCode"""
    balance_insufficient = 1016
    key_is_empty = 6000


class Fcoin():
    def __init__(self, key, secret):
        self.base_url = 'https://api.fcoin.com/v2/'
        self.key = bytes(key,'utf-8')
        self.secret = bytes(secret, 'utf-8')
        self.time = 0.1
        self.timeout = 10

    def handler_error_if_needed(self, json):
        if 'status' in json:
            status = json['status']
            if status == StatusErrorCode.key_is_empty.value:
                print('请填写key secret')
                os._exit(1)
            elif status == StatusErrorCode.balance_insufficient.value:
                print('余额不足')
                os._exit(1)



    def public_request(self, method, api_url, **payload):
        r_url = self.base_url + api_url
        try:
            r = requests.request(method, r_url, params=payload, timeout = self.timeout)
        except Exception as err:
            print('http error is', err, api_url)
            print('reconnect...')
            time.sleep(self.time)
            return self.public_request(method, api_url, **payload)
        if r.status_code == 200:
            self.handler_error_if_needed(r.json())
            return r.json()
        else:
            print('fcoin error is', r.json(), api_url)
            self.handler_error_if_needed(r.json())
            print('reconnect...')
            time.sleep(self.time)
            return self.public_request(method, api_url, **payload)

    def get_signed(self, sig_str):
        sig_str = base64.b64encode(sig_str)
        signature = base64.b64encode(hmac.new(self.secret, sig_str, digestmod=hashlib.sha1).digest())
        return signature


    def signed_request(self, method, api_url, **payload):
        param=''
        if payload:
            sort_pay = sorted(payload.items())
            for k in sort_pay:
                param += '&' + str(k[0]) + '=' + str(k[1])
            param = param.lstrip('&')
        timestamp = str(int(time.time() * 1000))
        full_url = self.base_url + api_url

        if method == 'GET':
            if param:
                full_url = full_url + '?' +param
            sig_str = method + full_url + timestamp
        elif method == 'POST':
            sig_str = method + full_url + timestamp + param

        signature = self.get_signed(bytes(sig_str, 'utf-8'))

        headers = {
            'FC-ACCESS-KEY': self.key,
            'FC-ACCESS-SIGNATURE': signature,
            'FC-ACCESS-TIMESTAMP': timestamp
        }
        
        print(method, full_url, payload)
        try:
            r = requests.request(method, full_url, headers=headers, json=payload, timeout=self.timeout)
        except Exception as err:
            print('http error is', err)
            print('reconnect...')
            time.sleep(self.time)
            return self.signed_request(method, api_url, **payload)
        if r.status_code == 200:
            self.handler_error_if_needed(r.json())
            return r.json()
        else:
            print('fcoin error is', r.json(), api_url)
            self.handler_error_if_needed(r.json())
            print('reconnect...')
            time.sleep(self.time)
            return self.signed_request(method, api_url, **payload)
            

    def get_server_time(self):
        """Get server time"""
        return self.public_request('GET','/public/server-time')['data']

    def get_currencies(self):
        """get all currencies"""
        return self.public_request('GET', '/public/currencies')['data']

    def get_symbols(self):
        """get all symbols"""
        return self.public_request('GET', '/public/symbols')['data']

    def get_trades(self,symbol):
        """get detail trade"""
        return self.public_request('GET', 'market/trades/{symbol}'.format(symbol=symbol))

    def get_balance(self):
        """get user balance"""
        return self.signed_request('GET', 'accounts/balance')

    def list_orders(self, **payload):
        """get orders"""
        return self.signed_request('GET','orders', **payload)

    def create_order(self, **payload):
        """create order"""
        return self.signed_request('POST','orders', **payload)

    def buy(self,symbol, price, amount, type = 'limit'):
        """buy someting"""
        return self.create_order(symbol=symbol, side='buy', type=type, price=str(price), amount=amount)

    def sell(self, symbol, price, amount, type = 'limit'):
        """buy someting"""
        return self.create_order(symbol=symbol, side='sell', type=type, price=str(price), amount=amount)

    def get_order(self,order_id):
        """get specfic order"""
        return self.signed_request('GET', 'orders/{order_id}'.format(order_id=order_id))

    def cancel_order(self,order_id):
        """cancel specfic order"""
        return self.signed_request('POST', 'orders/{order_id}/submit-cancel'.format(order_id=order_id))

    def order_result(self, order_id):
        """check order result"""
        return self.signed_request('GET', 'orders/{order_id}/match-results'.format(order_id=order_id))
    def get_candle(self,resolution, symbol, **payload):
        """get candle data"""
        return self.public_request('GET', 'market/candles/{resolution}/{symbol}'.format(resolution=resolution, symbol=symbol), **payload)

    def get_market_price(self,symbol):
        ws = create_connection("wss://ws.fcoin.com/api/v2/ws")
        ws.recv()
        s = "ticker.{}".format(symbol)
        req = {
            'cmd':'req',
            'args':[s],
            'id':'1'
        }
        ws.send(json.dumps(req))
        r = json.loads(ws.recv())
        ws.close()
        return r['data']['ticker'][0]

    def websocket_get_market_depth(self, level, symbol):
        ws = create_connection("wss://ws.fcoin.com/api/v2/ws")
        ws.recv()
        s = "depth.{}.{}".format(level ,symbol)
        req = {
            'cmd':'sub',
            'args':[s],
            'id':'1'
        }
        ws.send(json.dumps(req))
        r = json.loads(ws.recv())
        ws.close()
        return r
