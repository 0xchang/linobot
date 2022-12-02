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
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event
import sqlite3
from bot2.plugins.xiuxian.moncfg import gerenboss

lbossxian = on_fullmatch('查boss', priority=262)


@lbossxian.handle()
async def lbossxian_handle():
    mess = ''
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select * from monboss')
    con.commit()
    monboss = cur.fetchall()
    cur.close()
    con.close()
    for mon in monboss:
        mess = mess + mon[0] + '->血量:' + str(mon[1]) + ',攻击:' + str(mon[2]) + ',防御:' + str(mon[3]) + ',存活:'
        if mon[4] == 1:
            mess += '是'
        else:
            mess += '否'
        mess += '\n'
    mess = mess[:-1]
    await lbossxian.finish(Message(mess))


lhbossxian = on_fullmatch('高阶boss', priority=263)


@lhbossxian.handle()
async def lhbossxian_handle():
    mess = ''
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select * from highmonboss')
    con.commit()
    monboss = cur.fetchall()
    cur.close()
    con.close()
    for mon in monboss:
        mess = mess + mon[0] + '->血量:' + str(mon[1]) + ',攻击:' + str(mon[2]) + ',防御:' + str(mon[3]) + ',存活:'
        if mon[4] == 1:
            mess += '是'
        else:
            mess += '否'
        mess += '\n'
    mess = mess[:-1]
    await lhbossxian.finish(Message(mess))


grbossxian = on_fullmatch('个人boss', priority=263, rule=to_me())


@grbossxian.handle()
async def grboss_handle(event: Event):
    uid = event.get_user_id()
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select * from gerenboss where uid=?', (uid,))
    con.commit()
    boss = cur.fetchall()
    cur.close()
    con.close()
    mess = ''
    if boss == []:
        for grb in gerenboss:
            mess += 'boss:' + grb[0] + '->血量:' + str(grb[1]) + ',攻击:' + str(grb[2]) + ',防御:' + str(grb[3]) + '存活:是\n'
    else:
        for grb in boss:
            mess += 'boss:' + grb[1] + '->血量:' + str(grb[2]) + ',攻击:' + str(grb[3]) + ',防御:' + str(grb[4]) + '存活:'
            if grb[5] == 1:
                mess += '是\n'
            else:
                mess += '否\n'
    await grbossxian.finish(Message(mess),at_sender=True)
