#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 13:32
@author: 0xchang
@E-mail: oxchang@163.com
@file: sign.py
@Github: https://github.com/0xchang
"""
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
import sqlite3
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
from bot2.plugins.xiuxian.Role import XianRole

@scheduler.scheduled_job("cron", hour=0,minute=0)
async def good_morning():
    con=sqlite3.connect('data/xiuxian.data')
    cur=con.cursor()
    cur.execute('update Role set sign=?',(0,))
    con.commit()
    cur.close()
    con.close()

signxian=on_fullmatch('签到',priority=230)
@signxian.handle()
async def signxian_handle(event:GroupMessageEvent):
    uid=event.get_user_id()
    u=XianRole(uid,event.sender.nickname)
    if u.incSign():
        mess=f'恭喜你签到成功!\n灵气+{u.level*5}  灵石+50'
    else:
        mess='你已经签到过了!'
    del u
    await signxian.finish(Message(mess))
