#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/2 21:18
@author: 0xchang
@E-mail: oxchang@163.com
@file: tanxian.py
@Github: https://github.com/0xchang
"""
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message

txxian = on_fullmatch('探险', priority=245)
@txxian.handle()
async def infoxian_handle(event: Event):
    uid = event.get_user_id()
    u = XianRole(uid)
    if u.upHPMP():
        mess='恭喜你消耗20灵石增加了50HP,30MP'
    else:
        mess='您的灵石不足'
    del u
    await txxian.finish(Message(mess))