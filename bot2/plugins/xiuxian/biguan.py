#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/2 0:26
@author: 0xchang
@E-mail: oxchang@163.com
@file: biguan.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message

bgxian = on_command('闭关', priority=245)
@bgxian.handle()
async def bgxian_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    t=u.biguan()
    if t>30*60:
        mess='你开始闭关，闭关完成后会增长大量经验'
    else:
        mess=f'你在闭关中，闭关时间为{t//60}分钟'
    del u
    await bgxian.finish(Message(mess))