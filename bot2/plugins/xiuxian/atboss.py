#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/3 12:40
@author: 0xchang
@E-mail: oxchang@163.com
@file: atboss.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole,MonBoss
from nonebot.adapters.onebot.v11.message import Message
from nonebot.params import CommandArg
import sqlite3

atbossxian = on_command('打boss', priority=260)


@atbossxian.handle()
async def bgxian_handle(event: GroupMessageEvent, argcom: Message = CommandArg()):
    uid = event.get_user_id()
    u = XianRole(uid)
    bt = argcom.extract_plain_text()
    bt = bt.strip()
    if bt == '':
        await atbossxian.finish(Message('您需要输入boss的名字，请输入查boss查看boss情况'))
    else:
        con = sqlite3.connect('data/xiuxian.data')
        cur = con.cursor()
        cur.execute('select * from monboss where name=?', (bt,))
        con.commit()
        val = cur.fetchall()
        if len(val) == 0:
            cur.execute('select * from highmonboss where name=?', (bt,))
            con.commit()
            val = cur.fetchall()
        cur.close()
        con.close()
        if len(val) == 0:
            await atbossxian.finish(Message('好像没有这个boss吧，看一下boss列表吧'))
        val = val[0]
        if val[4] == 0:
            await atbossxian.finish(Message('这个boss好像死了，换个boss或者等会再来吧'))
        m = MonBoss(bt)
        res=u.kmonboss(m)
        if not res[0]:
            mess = f'你是不是有点菜啊,{bt}都没有打过,快去加强一下自己吧,记得回血哦'
        else:
            mess = f'恭喜你打过了{bt},但是你损失了{res[3]}血,你卖掉他的妖丹得到了{res[1]}灵石,你的灵气增长{res[2]}'
        del u
        del m
        await atbossxian.finish(Message(mess))