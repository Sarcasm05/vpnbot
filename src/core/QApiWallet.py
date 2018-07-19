#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid4
#from SimpleQIWI import OverridingEx, InvalidTokenError, ArgumentError, QIWIAPIError
import requests
import threading
import time


class QIWIAPIError(Exception):
    pass


class ArgumentError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


class OverridingEx(Exception):
    pass

class QApi(object):

    def __init__(self, token, phone, delay=1):
        self._s = requests.Session()

        self._s.headers['Accept'] = 'application/json'
        self._s.headers['Content-Type'] = 'application/json'
        self._s.headers['Authorization'] = 'Bearer ' + token

        self.phone = phone
        self._inv = {}
        self._echo = None
        self.delay = delay
        self.thread = False

    @property
    def _transaction_id(self):

        return str(int(time.time() * 1000))

    @property
    def payments(self):

        return self._get_payments()

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
    def bill(self, price, comment=uuid4(), currency=643):
        comment = str(comment)
        if comment in self._inv:
            raise OverridingEx('Overriding bill!')

        self._inv[comment] = {
            'price': price,
            'currency': currency,
            'success': False
        }

        return comment

    def _get_balance(self):

        response = self._s.get('https://edge.qiwi.com/funding-sources/v1/accounts/current')
        if response is None:
            raise InvalidTokenError('Invalid token!')
        json = response.json()

        if 'code' in json or 'errorCode' in json:
            raise QIWIAPIError(json)

        balances = []

        for account in json['accounts']:
            if account['hasBalance']:
                balances.append({
                   'type': account['type'],
                   'balance': account['balance']
                })

        return balances

    def _get_payments(self, rows=20):
        post_args = {
            'rows': rows,
            'operation': 'IN'
        }

        response = self._s.get(
            url='https://edge.qiwi.com/payment-history/v1/persons/%s/payments' % self.phone,
            params=post_args
        )

        data = response.json()

        if 'code' in data or 'errorCode' in data:
            raise QIWIAPIError(data)

        return data

    def check(self, comment):
        if comment not in self._inv:
            return False

        return self._inv[comment]['success']

    def _async_loop(self, target):
        lock = threading.Lock()

        while self.thread:
            try:
                lock.acquire()
                target()

            finally:
                lock.release()

    def _parse_payments(self):
        payments = self.payments

        if 'errorCode' in payments:
            time.sleep(10)
            return

        for payment in payments['data']:

            if payment['comment'] in self._inv:

                if payment['total']['amount'] >= self._inv[payment['comment']]['price'] and payment['total']['currency'] == \
                        self._inv[payment['comment']]['currency'] and not self._inv[payment['comment']]['success']:
                    self._inv[payment['comment']]['success'] = True
                    if self._echo is not None:
                        self._echo({
                            payment['comment']: self._inv[payment['comment']]
                        })

        time.sleep(self.delay)

    def start(self):

        if not self.thread:
            self.thread = True
            th = threading.Thread(target=self._async_loop, args=(self._parse_payments,))
            th.start()

    def stop(self):
        self.thread = False
