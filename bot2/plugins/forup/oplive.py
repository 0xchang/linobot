#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 16:53
@author: 0xchang
@E-mail: oxchang@163.com
@file: oplive.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
import bot2.plugins.sql.update_sql as usql
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER
from bot2.plugins.forup.opmessage import op_mess

live_open=on_command('开启直播',priority=9,permission=SUPERUSER|GROUP_OWNER|GROUP_ADMIN)
live_close=on_command('关闭直播',priority=10,permission=SUPERUSER|GROUP_OWNER|GROUP_ADMIN)
live_open_at=on_command('开启全体直播',priority=11,permission=SUPERUSER|GROUP_OWNER|GROUP_ADMIN)
live_close_at=on_command('关闭全体直播',priority=12,permission=SUPERUSER|GROUP_OWNER|GROUP_ADMIN)

@live_open.handle()
async def live_open_handle(event:Event,comargs:Message=CommandArg()):
    uid = comargs.extract_plain_text()
    res = op_mess(event, uid)
    if res is None:
        await live_open.finish(Message(f'uid只能为纯数字'))
    else:
        uid, mtype, qqid = res
        usql.update_data(usql.update_live(uid, mtype, qqid, 1))
    await live_open.finish(Message(f'已经开启直播通知'))

@live_open_at.handle()
async def live_openat_handle(event:Event,comargs:Message=CommandArg()):
    uid = comargs.extract_plain_text()
    res = op_mess(event, uid)
    if res is None:
        await live_open_at.finish(Message(f'uid只能为纯数字'))
    else:
        uid, mtype, qqid = res
        usql.update_data(usql.update_liveat(uid, mtype, qqid, 1))
    await live_open_at.finish(Message(f'已经开启全体直播通知'))

@live_close.handle()
async def live_close_handle(event:Event,comargs:Message=CommandArg()):
    uid = comargs.extract_plain_text()
    res = op_mess(event, uid)
    if res is None:
        await live_close.finish(Message(f'uid只能为纯数字'))
    else:
        uid, mtype, qqid = res
        usql.update_data(usql.update_live(uid, mtype, qqid, 0))
    await live_close.finish(Message(f'已经关闭直播通知'))

@live_close_at.handle()
async def live_closeat_handle(event:Event,comargs:Message=CommandArg()):
    uid = comargs.extract_plain_text()
    res = op_mess(event, uid)
    if res is None:
        await live_close_at.finish(Message(f'uid只能为纯数字'))
    else:
        uid, mtype, qqid = res
        usql.update_data(usql.update_liveat(uid, mtype, qqid, 0))
    await live_close_at.finish(Message(f'已经关闭全体直播通知'))

