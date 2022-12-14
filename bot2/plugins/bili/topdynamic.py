#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/28 20:46
@author: 0xchang
@E-mail: oxchang@163.com
@file: topdynamic.py
@Github: https://github.com/0xchang
"""
from bot2.plugins.bili.updynamic import dyn
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot import on_fullmatch
from bot2.plugins.sql.select_sql import select_uid_from_qid

topd=on_fullmatch('置顶',priority=107)
@topd.handle()
async def topd_handle(event:GroupMessageEvent):
    gid=event.group_id
    values=select_uid_from_qid(gid)
    for value in values:
        uid=value[0]
        res=await dyn(uid,True)
        res=res[2]
        mess=res
        mess=mess.replace('发布了新','的置顶')
        await topd.send(Message(mess),at_sender=True)