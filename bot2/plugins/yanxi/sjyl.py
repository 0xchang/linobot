#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/14 13:07
@author: 0xchang
@E-mail: oxchang@163.com
@file: sjyl.py
@Github: https://github.com/0xchang
"""
import time

from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event
from nonebot import on_command
import bot2.plugins.yanxi.yanxi as yanxi


sjyl=on_command('随机语录',priority=201)
sjyl_time=0

@sjyl.handle()
async def sjyl_handle(event:Event):
    global sjyl_time
    if yanxi.time_check(time.time(),sjyl_time):
        return
    else:
        sjyltxt=await yanxi.yanxiapi('http://api.yanxi520.cn/api/yan.php')
        sjyl_time = time.time()
        await sjyl.finish(Message(f'[CQ:at,qq={event.get_user_id()}]%s'%sjyltxt))