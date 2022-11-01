#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 13:43
@author: 0xchang
@E-mail: oxchang@163.com
@file: Myself.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message

infoxian = on_command('查询', priority=231)
@infoxian.handle()
async def infoxian_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    mess=u.getInfo()
    del u
    await infoxian.finish(Message(mess))
