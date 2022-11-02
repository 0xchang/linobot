#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 14:18
@author: 0xchang
@E-mail: oxchang@163.com
@file: AT.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message
from nonebot.params import CommandArg

atxian = on_command('攻击', priority=236)
@atxian.handle()
async def infoxian_handle(event: GroupMessageEvent,argcom:Message=CommandArg()):
    uid0 = event.get_user_id()
    uid1 = argcom[0].get('data').get('qq')
    u0 = XianRole(uid0, event.sender.nickname)
    u1 = XianRole(uid1)
    if u0.isBiguan() or u1.isBiguan():
        await atxian.finish(Message(f'你正在闭关或者你攻击的人正在闭关'))
    mess=u0.kill(u1)
    del u1
    del u0
    await atxian.finish(Message(mess))
