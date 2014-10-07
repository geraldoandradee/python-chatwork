# -*- coding:utf8 -*-
"""Python Chatwork-API client library
"""
from __future__ import unicode_literals
from urllib2 import Request, urlopen
import json


__author__ = 'attakei'
__version__ = '0.0.1'


ENDPOINT_BASE_URL = 'https://api.chatwork.com/v1'

ENDPOINT_TOKEN_HEADER = 'X-ChatWorkToken'


class ChatworkApi(object):
    def __init__(self, token):
        self.token = token
        self.req = None

    def _call(self, url):
        req = Request(url, headers={ENDPOINT_TOKEN_HEADER: self.token})
        resp = urlopen(req)
        return json.load(resp)

    def _build_url(self, endpoint):
        return '{base_url}{endpoint}'.format(base_url=ENDPOINT_BASE_URL, endpoint=endpoint)

    def me(self):
        url = self._build_url('/me')
        return self._call(url)
