#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/14 22:05
@author: 0xchang
@E-mail: oxchang@163.com
@file: suiji.py
@Github: https://github.com/0xchang
"""
import random
import time

from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Event
from bot2.plugins.yanxi.yanxi import time_check

rand_num=on_command('随机数',priority=199)
rand_num_time=0
@rand_num.handle()
async def rand_num_handle(event:Event,comargs:Message=CommandArg()):
    global rand_num_time
    if time_check(time.time(),rand_num_time):
        return
    num = comargs.extract_plain_text()
    try:
        if num=='':
            num=random.randint(0,1000)
            rand_num_time=time.time()
            await rand_num.finish(Message('%d' % num),at_sender=True)
            return
        else:
            num=int(num)
            if num>100:
                await rand_num.finish(Message('亲,最多生成100个随机数呢'),at_sender=True)
            num=[random.randint(0,1000) for _ in range(num)]
            rand_num_time=time.time()
            await rand_num.finish(Message('%s'%str(num)),at_sender=True)
            return
    except Exception:
        pass
