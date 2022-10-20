#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/14 13:11
@author: 0xchang
@E-mail: oxchang@163.com
@file: tgrj.py
@Github: https://github.com/0xchang
"""
import asyncio
import time

from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event
from nonebot import on_command
import bot2.plugins.yanxi.yanxi as yanxi


tgrj=on_command('舔狗日记',priority=202)
tgrj_time=0

@tgrj.handle()
async def tgrj_handle(event:Event):
    global tgrj_time
    if yanxi.time_check(time.time(),tgrj_time):
        return
    else:
        tgrjtxt=await yanxi.yanxiapi('http://api.yanxi520.cn/api/tiangou.php')
        tgrj_time=time.time()
        await tgrj.finish(Message(f'[CQ:at,qq={event.get_user_id()}]%s'%tgrjtxt))
