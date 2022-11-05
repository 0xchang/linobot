#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/3 13:30
@author: 0xchang
@E-mail: oxchang@163.com
@file: lookboss.py
@Github: https://github.com/0xchang
"""
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11.message import Message
import sqlite3

lbossxian = on_fullmatch('查boss', priority=262, )


@lbossxian.handle()
async def lbossxian_handle():
    mess = ''
    con=sqlite3.connect('data/xiuxian.data')
    cur=con.cursor()
    cur.execute('select * from monboss')
    con.commit()
    monboss=cur.fetchall()
    cur.close()
    con.close()
    for mon in monboss:
        mess = mess + mon[0] + '->血量:' + str(mon[1]) + ',攻击:' + str(mon[2]) + ',防御:' + str(mon[3]) + ',存活:'
        if mon[4] == 1:
            mess += '是'
        else:
            mess += '否'
        mess += '\n'
    await lbossxian.finish(Message(mess))
