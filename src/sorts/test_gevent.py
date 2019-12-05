# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 17:39
# @Author  : jacobzhang
# @File    : test_gevent.py
# @Project : test

import gevent
from gevent import monkey

monkey.patch_all()

import urllib3

def query_content(url):
    print("GET: {}".format(url))
    http = urllib3.PoolManager()
    rsp = http.request("GET", url)
    data = rsp.data
    print("Received {} bytes from url {}".format(len(data), url))

if __name__ == '__main__':
    job_second = gevent.spawn(query_content, "www.163.com")
    job_first = gevent.spawn(query_content, "www.baidu.com")
    job_third = gevent.spawn(query_content, "www.qq.com")

    gevent.joinall([job_first, job_second, job_third], 5)
