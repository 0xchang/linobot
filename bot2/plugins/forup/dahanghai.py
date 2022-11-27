#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/28 1:41
@author: 0xchang
@E-mail: oxchang@163.com
@file: dahanghai.py
@Github: https://github.com/0xchang
"""
import time

from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot import on_fullmatch
from bilibili_api import live
from bot2.plugins.sql.select_sql import sel_uid_from_fgroup,select_user

dahanghai=on_fullmatch('查舰',priority=292)
@dahanghai.handle()
async def dahanghai_handle(event:GroupMessageEvent):
    qid=event.group_id
    res=sel_uid_from_fgroup(qid)
    if len(res)==0:
        return
    for uid in res:
        uid=uid[0]
        nres=select_user(uid)
        for n in nres:
            _,name,rid=n
            r=live.LiveRoom(rid)
            resp=await r.get_dahanghai()
            num=resp['info']['num']
            time.sleep(0.1)
            await dahanghai.send(Message(f'{name}的舰长数量TM只有<{num}>个了,生产队的驴都不敢像你这么歇的，还不努力一下。。。'))