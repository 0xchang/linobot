#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 15:21
@author: 0xchang
@E-mail: oxchang@163.com
@file: uphm.py
@Github: https://github.com/0xchang
"""
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message

uphmxian = on_fullmatch('回复', priority=240)
@uphmxian.handle()
async def infoxian_handle(event: Event):
    uid = event.get_user_id()
    u = XianRole(uid)
    if u.upHPMP():
        mess='恭喜你消耗20灵石增加了50HP,30MP'
    else:
        mess='您的灵石不足'
    del u
    await uphmxian.finish(Message(mess))

biguphmxian = on_fullmatch('大回复术', priority=241)
@biguphmxian.handle()
async def infoxian_handle(event: Event):
    uid = event.get_user_id()
    u = XianRole(uid)
    if u.upBigHPMP():
        mess='恭喜你消耗200灵石增加了530HP,330MP'
    else:
        mess='您的灵石不足'
    del u
    await biguphmxian.finish(Message(mess))

superuphmxian = on_fullmatch('超级回复', priority=241)
@superuphmxian.handle()
async def infoxian_handle(event: Event):
    uid = event.get_user_id()
    u = XianRole(uid)
    if u.upSuperHPMP():
        mess='恭喜你消耗2000灵石增加了5800HP,3800MP'
    else:
        mess='您的灵石不足'
    del u
    await superuphmxian.finish(Message(mess))