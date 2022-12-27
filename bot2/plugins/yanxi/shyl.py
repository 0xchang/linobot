#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/14 13:15
@author: 0xchang
@E-mail: oxchang@163.com
@file: shyl.py
@Github: https://github.com/0xchang
"""
import time

from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_fullmatch
import bot2.plugins.yanxi.yanxi as yanxi

shyl=on_fullmatch('社会语录',priority=203)
shyl_time=0

@shyl.handle()
async def shyl_handle():
    global shyl_time
    print(shyl_time)
    if yanxi.time_check(time.time(),shyl_time):
        return
    else:
        shyltxt=await yanxi.yanxiapi('http://yanxi520.cn/api/shehui.php')
        shyl_time = time.time()
        await shyl.finish(Message('%s'%shyltxt),at_sender=True)

