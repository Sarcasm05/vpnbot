#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid4
import requests
import threading
import time


class QiwiAPIException(Exception):
    pass


class ArgumentException(Exception):
    pass


class InvalidLexemException(Exception):
    pass


class ReplaceException(Exception):
    pass


class QApi(object):

    private_header = {'Accept' : 'application/json', 'Content-Type' : 'application/json','Authorization' : 'Bearer' }
    private_url_pay = 'https://edge.qiwi.com/payment-history/v1/persons/%s/payments'
    private_url_current = 'https://edge.qiwi.com/funding-sources/v1/accounts/current'

    def __init__(self, token, phone, delay=1):

        self._s = requests.Session()
        self.private_header['Authorization'] = 'Bearer ' + token
        self._s.headers  = self.private_header
        self.phone = phone
        self._inv = {}
        self._echo = None
        self.delay = delay
        self.thread = False
    def _async_loop(self, target):
        lock = threading.Lock()

        while self.thread:
            try:
                lock.acquire()
                target()
            except:
                print('error _async_loop im module WalletQIWI | esli eta hyeta ne robit to go: pip3 install async aiohttp and e.t.c')

            finally:
                lock.release()


    @property
    def _transaction_id(self):
        return str(int(time.time() * 1000))

    @property
    def pay_ins(self):
        return self._get_pay_ins()

    @property
    def full_balance(self):
        return self._get_balance()

    @property
    def balance(self):


        balances = self.full_balance
        balance = []

        for wallet in balances:
            if wallet['balance'] is not None:
                balance.append(wallet['balance']['amount'])

        return balance


    def _get_pay_ins(self, rows=20):

        post_args = {
            'rows': rows,
            'operation': 'IN'
        }

        response = self._s.get(
            url= self.private_url_pay % self.phone,
            params=post_args
        )

        data = response.json()

        if 'code' in data or 'errorCode' in data:
            raise QiwiAPIException(data)

        return data
    def bill(self, comment, price=150, currency=643):

        comment = str(comment)

        if comment in self._inv:
            raise ReplaceException('Overriding bill, common bro :D')

        self._inv[comment] = {
            'price': price,
            'currency': currency,
            'success': False
        }

        return comment


    def _get_balance(self):


        response = self._s.get(private_url_current)

        if response is None:
            raise InvalidLexemException('Invalid token!')

        json = response.json()

        if 'code' in json or 'errorCode' in json:
            raise QiwiAPIException(json)

        balances = []

        for account in json['accounts']:
            if account['hasBalance']:
                balances.append({
                   'type': account['type'],
                   'balance': account['balance']
                })

        return balances


    def bind_echo(self):

        def decorator(func):
            if func.__code__.co_argcount != 1:
                raise ArgumentException('Echo function error')

            self._echo = func

        return decorator

    def check_info(self, comment):

        if comment not in self._inv:
            return False

        return self._inv[comment]['success']


    def _parse_pay_ins(self):
        pay_ins = self.pay_ins

        if 'errorCode' in pay_ins:
            time.sleep(30)
            return

        for pay_in in pay_ins['data']:
            if pay_in['comment'] in self._inv:
                if pay_in['total']['amount'] >= self._inv[pay_in['comment']]['price'] and pay_in['total']['currency'] == \
                        self._inv[pay_in['comment']]['currency'] and not self._inv[pay_in['comment']]['success']:

                    self._inv[pay_in['comment']]['success'] = True

                    if self._echo is not None:
                        self._echo({
                            pay_in['comment']: self._inv[pay_in['comment']]
                        })

        time.sleep(self.delay)

    def run(self):

        if not self.thread:
            self.thread = True
            th = threading.Thread(target=self._async_loop, args=(self._parse_pay_ins,))
            th.start()

    def close(self):
        self.thread = False
