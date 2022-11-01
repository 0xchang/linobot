#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 13:55
@author: 0xchang
@E-mail: oxchang@163.com
@file: morege.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message

workxian = on_command('打工', priority=234)
@workxian.handle()
async def infoxian_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    res=u.work()
    if res<=20:
        mess=f'你打工不认真，仅仅得了{res}金币'
    elif res>=40:
        mess=f'你打工很认真，得了{res}金币'
    else:
        mess=f'你打工一般，得了{res}金币'
    del u
    await workxian.finish(Message(mess))

fishxian = on_command('钓鱼', priority=235)
@fishxian.handle()
async def infoxian_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    gold,exp=u.fishing()
    del u
    mess=f'你钓鱼得到了金币+{gold}，经验+{exp}'
    await fishxian.finish(Message(mess))