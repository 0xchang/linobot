#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/2 21:08
@author: 0xchang
@E-mail: oxchang@163.com
@file: gua.py
@Github: https://github.com/0xchang
"""
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message
from nonebot.permission import SUPERUSER

yfctxian = on_fullmatch('一飞冲天', priority=242,permission=SUPERUSER)
@yfctxian.handle()
async def yfctxian_handle(event: Event):
    uid = event.get_user_id()
    u = XianRole(uid)
    u.kaigua()
    del u
    await yfctxian.finish(Message(f'一飞冲天是吧'))