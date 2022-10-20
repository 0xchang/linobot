#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 15:46
@author: 0xchang
@E-mail: oxchang@163.com
@file: dyn.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from bot2.plugins.forup.opmessage import op_mess
import bot2.plugins.sql.update_sql as usql
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER

dyn_open=on_command('开启动态',priority=5,permission=SUPERUSER|GROUP_OWNER|GROUP_ADMIN)
dyn_close=on_command('关闭动态',priority=6,permission=SUPERUSER|GROUP_OWNER|GROUP_ADMIN)
dyn_open_at=on_command('开启全体动态',priority=7,permission=SUPERUSER|GROUP_OWNER|GROUP_ADMIN)
dyn_close_at=on_command('关闭全体动态',priority=8,permission=SUPERUSER|GROUP_OWNER|GROUP_ADMIN)
@dyn_open.handle()
async def dynopen_handle(event:Event,comargs:Message=CommandArg()):
    uid = comargs.extract_plain_text()
    res=op_mess(event,uid)
    if res is None:
        await dyn_open.finish(Message(f'uid只能为纯数字'))
    else:
        uid,mtype,qqid=res
        usql.update_data(usql.update_dyn(uid,mtype,qqid,1))
    await dyn_open.finish(Message(f'已经开启动态通知'))

@dyn_open_at.handle()
async def dynatopen_handle(event:Event,comargs:Message=CommandArg()):
    uid = comargs.extract_plain_text()
    res=op_mess(event,uid)
    if res is None:
        await dyn_open_at.finish(Message(f'uid只能为纯数字'))
    else:
        uid,mtype,qqid=res
        usql.update_data(usql.update_dynat(uid,mtype,qqid,1))
    await dyn_open_at.finish(Message(f'已经开启全体动态通知'))

@dyn_close.handle()
async def dynclose_handle(event:Event,comargs:Message=CommandArg()):
    uid = comargs.extract_plain_text()
    res=op_mess(event,uid)
    if res is None:
        await dyn_close.finish(Message(f'uid只能为纯数字'))
    else:
        uid,mtype,qqid=res
        usql.update_data(usql.update_dyn(uid,mtype,qqid,0))
    await dyn_close.finish(Message(f'已经关闭动态通知'))

@dyn_close_at.handle()
async def dynatcloseat_handle(event:Event,comargs:Message=CommandArg()):
    uid = comargs.extract_plain_text()
    res=op_mess(event,uid)
    if res is None:
        await dyn_close_at.finish(Message(f'uid只能为纯数字'))
    else:
        uid,mtype,qqid=res
        usql.update_data(usql.update_dynat(uid,mtype,qqid,0))
    await dyn_close_at.finish(Message(f'已经关闭全体动态通知'))

