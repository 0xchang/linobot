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
from nonebot.params import CommandArg

bgxian = on_command('闭关', priority=245)
@bgxian.handle()
async def bgxian_handle(event: GroupMessageEvent,argcom:Message=CommandArg()):
    uid = event.get_user_id()
    u = XianRole(uid)
    bt=argcom.extract_plain_text()
    if not bt.isdigit():
        return
    bt=int(bt)
    if bt<5 or bt >300:
        mess='时间最短为5分钟，最长为300分钟'
        await bgxian.finish(Message(mess))
    t=u.biguan(bt)
    if t>120*60:
        mess = '你开始闭关，闭关完成后会增长大量经验'
    else:
        mess = f'你在闭关中，闭关时间为{t // 60}分钟'
    del u
    await bgxian.finish(Message(mess),at_sender=True)