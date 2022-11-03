#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 20:27
@author: 0xchang
@E-mail: oxchang@163.com
@file: upExp.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message
upexpxian = on_command('练功', priority=241)
@upexpxian.handle()
async def infoxian_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid)
    if u.isBiguan():
        await upexpxian.finish(Message(f'你正在闭关'))
    exp, status = u.dazuo()
    if status == -3:
        mess = f'你在练功的时候走火入魔了，等级-1'
    elif status == -2:
        mess = f'你在练功的时候走火入魔了，好在你稳住了心神,没有掉级，灵气{exp}'
    elif status == -1:
        mess = f'你不小心走火入魔了，灵气{exp}'
    elif status == 0:
        mess = f'你正常修炼，灵气+{exp}'
    elif status == 1:
        mess = f'你tm顿悟了，灵气+{exp}'
    else:
        mess = f'你tm遇到高人了，灵气+{exp}'
    del u
    await upexpxian.finish(Message(mess))
