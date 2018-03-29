#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
This is an example of requests
Bodyle By 2018-02-22
"""

import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'


# 不带参数的requests请求
def use_simple_requests():
    response = requests.get(URL_IP)
    print("=====>headers")
    print(response.headers)
    print("=====>text")
    print(response.text)


# 带参数的requests请求
def use_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}

    response = requests.get(URL_GET, params=params)

    print("=====>headers")
    print(response.headers)
    print("=====>status code")
    print(response.status_code)
    print(response.reason)
    print("=====>text")
    print(response.text)


if __name__ == '__main__':
    print("=====>Use simple requests:")
    use_simple_requests()
    print()
    print("=====>Use params requests:")
    use_params_requests()
