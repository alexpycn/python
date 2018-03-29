#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from requests import Request, Session


class HtmlDownloader(object):
    @staticmethod
    def download(url):
        s = Session()
        if url is None:
            return None
        headers = {'User-Agent': 'fake1.3'}
        request = Request('GET', url=url, headers=headers)
        prepped = request.prepare()
        response = s.send(prepped, timeout=5)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            return None

        return response.text
