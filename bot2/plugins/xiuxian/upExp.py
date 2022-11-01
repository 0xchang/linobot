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
    exp=u.dazuo()
    if exp<0:
        mess=f'你在练功的时候走火入魔了，经验{exp}'
    else:
        mess=f'你练功状态还行，经验+{exp}'
    del u
    await upexpxian.finish(Message(mess))
