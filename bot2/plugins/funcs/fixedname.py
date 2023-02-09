#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/2/9 14:09
@author: 0xchang
@E-mail: oxchang@163.com
@file: fixedname.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.params import CommandArg
from nonebot import on_command
from nonebot.permission import SUPERUSER
import sqlite3
from nonebot import require

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from nonebot import get_bots

fname = on_command('固定昵称', permission=SUPERUSER, priority=600)


@fname.handle()
async def fname_handle(event: GroupMessageEvent, arg: Message = CommandArg()):
    gid = event.group_id
    arg = arg.extract_plain_text().strip()
    arg = arg.split()
    uid = int(arg[0])
    name = arg[1]
    con = sqlite3.connect('./data/fname.data')
    cur = con.cursor()
    cur.execute('select * from user where uid=? and gid=?', (uid, gid))
    con.commit()
    if cur.fetchall() == []:
        cur.execute('insert into user(uid,gid,name) values(?,?,?)', (uid, gid, name))
    else:
        cur.execute('update user set name=? where uid=? and gid=?', (name, uid, gid))
    con.commit()
    cur.close()
    con.close()
    await fname.finish(Message('成功固定他的名字'))


clfname = on_command('取消固定昵称', permission=SUPERUSER, priority=601)


@clfname.handle()
async def clfname_handle(event: GroupMessageEvent, arg: Message = CommandArg()):
    gid = event.group_id
    arg = arg.extract_plain_text().strip()
    uid = int(arg)
    con = sqlite3.connect('./data/fname.data')
    cur = con.cursor()
    cur.execute('select * from user where uid=? and gid=?', (uid, gid))
    con.commit()
    res=cur.fetchall()
    if res != []:
        cur.execute('delete from user where uid=? and gid=?', (uid, gid))
        con.commit()
    cur.close()
    con.close()
    await clfname.finish(Message('成功删除用户'))


@scheduler.scheduled_job("cron", second='*/5')
async def while_live():
    bot, = get_bots().values()
    con = sqlite3.connect('./data/fname.data')
    cur = con.cursor()
    cur.execute('select * from user')
    con.commit()
    res = cur.fetchall()
    for r in res:
        uid, gid, name = r
        print(r)
        result = await bot.call_api("get_group_member_info", user_id=uid, group_id=gid)
        card = result['card']
        if name != card:
            await bot.call_api("set_group_card", user_id=uid, group_id=gid, card=name)
    cur.close()
    con.close()
