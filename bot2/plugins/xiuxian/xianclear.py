#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 23:41
@author: 0xchang
@E-mail: oxchang@163.com
@file: xianclear.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER

clxian = on_command('清零', priority=236,permission=SUPERUSER)
@clxian.handle()
async def infoxian_handle(argcom:Message=CommandArg()):
    uid1 = argcom[0].get('data').get('qq')
    u = XianRole(uid1)
    u.clear()
    del u
    await clxian.finish(Message(f'他的数据已经清零'))
