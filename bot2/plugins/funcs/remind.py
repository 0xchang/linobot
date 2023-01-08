#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/1/8 10:39
@author: 0xchang
@E-mail: oxchang@163.com
@file: remind.py.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot import on_keyword
import asyncio

remind1 = on_keyword({'提醒'}, priority=100, block=False)


@remind1.handle()
async def _(event: GroupMessageEvent):
    mess = event.get_plaintext()
    mess = mess.split('提醒')
    if (not mess[0].isdigit()) or mess[1] == '':
        await remind1.finish(Message('格式不对，请输入时间 提醒 事件,例如30 提醒 记得吃饭(30分钟后提醒吃饭)'))
    t = int(mess[0].strip())
    await remind1.send(Message('已添加到提醒事项中!'))
    await asyncio.sleep(t * 60)
    await remind1.finish(Message(f'\n提醒通知:\n记得{mess[1]}哦!'), at_sender=True)
