#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/12/27 22:34
@author: 0xchang
@E-mail: oxchang@163.com
@file: histoday.py
@Github: https://github.com/0xchang
"""
import time

from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_fullmatch
import bot2.plugins.yanxi.yanxi as yanxi

histoday=on_fullmatch('历史上的今天',priority=204)
histoday_time=0

@histoday.handle()
async def histoday_handle():
    global histoday_time
    print(histoday_time)
    if yanxi.time_check(time.time(),histoday_time):
        return
    else:
        shyltxt=await yanxi.yanxiapi('http://yanxi520.cn/api/today.php')
        histoday_time = time.time()
        await histoday.finish(Message('%s'%shyltxt))

