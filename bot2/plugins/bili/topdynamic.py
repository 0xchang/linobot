#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/28 20:46
@author: 0xchang
@E-mail: oxchang@163.com
@file: topdynamic.py
@Github: https://github.com/0xchang
"""
import bot2.plugins.bili.updynamic as upd
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot import on_command
from bot2.plugins.sql.select_sql import select_uid_from_qid,select_user

topd=on_command('置顶',priority=107)
@topd.handle()
async def topd_handle(event:GroupMessageEvent):
    gid=event.group_id
    qid=event.get_user_id()
    values=select_uid_from_qid(gid)
    for value in values:
        uid=value[0]
        res=await upd.dyn(uid,True)
        res=res[2]
        mess=f'[CQ:at,qq={qid}]'+res
        mess=mess.replace('发布了新','的置顶')
        await topd.send(Message(mess))