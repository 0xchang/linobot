#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 13:50
@author: 0xchang
@E-mail: oxchang@163.com
@file: upField.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message

upxian = on_command('进化', priority=239)
@upxian.handle()
async def infoxian_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    if u.goldToField():
        mess='恭喜你消耗部分灵石进化成功，各项属性有所增加！'
    else:
        mess='您的灵石不足'
    del u
    await upxian.finish(Message(mess))

jiujiupxian = on_command('究极进化', priority=239)
@jiujiupxian.handle()
async def jiujiupxian_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    count=0
    while u.goldToField():
        count+=1
    mess=f'恭喜你消耗大量灵石进化{count}次，各项属性大量增加！'
    await jiujiupxian.finish(Message(mess))