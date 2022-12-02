#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/3 12:40
@author: 0xchang
@E-mail: oxchang@163.com
@file: atboss.py
@Github: https://github.com/0xchang
"""
import time

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Event
from bot2.plugins.xiuxian.Role import XianRole, MonBoss
from nonebot.adapters.onebot.v11.message import Message
from nonebot.params import CommandArg
import sqlite3
from bot2.plugins.xiuxian.moncfg import gerenboss
from bot2.plugins.xiuxian.AMonster import GeRBoss

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
        res = u.kmonboss(m)
        if not res[0]:
            mess = f'你是不是有点菜啊,{bt}都没有打过,快去加强一下自己吧,记得回血哦'
        else:
            mess = f'恭喜你打过了{bt},但是你损失了{res[3]}血,你卖掉他的妖丹得到了{res[1]}灵石,你的灵气增长{res[2]}'
        del u
        del m
        await atbossxian.finish(Message(mess))


atgrbossxian = on_command('杀boss', rule=to_me(), priority=261)


@atgrbossxian.handle()
async def asgrboss_handle(event: Event, argcom: Message = CommandArg()):
    uid = event.get_user_id()
    bname = argcom.extract_plain_text().strip()
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select * from gerenboss where uid=?', (uid,))
    con.commit()
    grboss = cur.fetchall()
    if grboss == []:
        for gb in gerenboss:
            cur.execute('insert into gerenboss(uid,name,HP,attack,defense,live) values(?,?,?,?,?,?)',
                        (uid, gb[0], gb[1], gb[2], gb[3], 1))
            con.commit()
            if gb[0] == bname:
                grboss = (uid, gb[0], gb[1], gb[2], gb[3], 1)
    else:
        cur.execute('select * from gerenboss where uid=? and name=?', (uid, bname))
        con.commit()
        grboss = cur.fetchall()
        if grboss == []:
            await atgrbossxian.finish(Message('没有这个个人boss'))
        grboss = grboss[0]
    cur.close()
    con.close()
    if grboss[5] == 0:
        time.sleep(0.2)
        await atgrbossxian.finish(Message('这个boss好像没有复活'))
    else:
        u = XianRole(uid)
        g = GeRBoss(grboss[1], grboss[2], grboss[3], grboss[4])
        res = u.kmonboss(g)
        if not res[0]:
            mess = f'你是不是有点菜啊,{grboss[1]}都没有打过,快去加强一下自己吧,记得回血哦'
        else:
            mess = f'恭喜你打过了{grboss[1]},但是你损失了{res[3]}血,你卖掉他的妖丹得到了{res[1]}灵石,你的灵气增长{res[2]}'
        del u
        await atgrbossxian.finish(Message(mess))
