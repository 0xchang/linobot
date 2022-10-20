#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/14 11:12
@author: 0xchang
@E-mail: oxchang@163.com
@file: xljt.py
@Github: https://github.com/0xchang
"""
import time

from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event
from nonebot import on_command
import bot2.plugins.yanxi.yanxi as yanxi




xljt=on_command("心灵鸡汤",priority=200)
xljt_time=0

@xljt.handle()
async def xljt_handle(event:Event):
        global xljt_time
        if yanxi.time_check(time.time(),xljt_time):
                return
        else:
                xjlttxt=await yanxi.yanxiapi('http://api.yanxi520.cn/api/xljtwr.php')
                xljt_time=time.time()
                await xljt.finish(Message(f'[CQ:at,qq={event.get_user_id()}]%s'%xjlttxt))


