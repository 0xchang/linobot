#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/14 14:22
@author: 0xchang
@E-mail: oxchang@163.com
@file: yanxi.py
@Github: https://github.com/0xchang
"""
import aiohttp

async def yanxiapi(url):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(url) as resp:
            resptxt = await resp.read()
            resptxt = resptxt.decode('utf8')
    return resptxt

#设置命令间隔时长为3
def time_check(nowTime,beforeTime):
    if nowTime-beforeTime>3:
        return False
    else:
        return True