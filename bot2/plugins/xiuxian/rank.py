#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/5 0:05
@author: 0xchang
@E-mail: oxchang@163.com
@file: rank.py
@Github: https://github.com/0xchang
"""
import sqlite3
from nonebot import on_command
from bot2.plugins.xiuxian.Role import XianRole


def rankGold():
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select name,gold from role where uid is not null')
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    value = sorted(value, key=lambda t: t[1])
    value.reverse()
    value = value[:10]
    return value


def rankAttack():
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select name,attack from role where uid is not null')
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    value = sorted(value, key=lambda t: t[1])
    value.reverse()
    value = value[:10]
    return value


def rankDefense():
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select name,defense from role where uid is not null')
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    value = sorted(value, key=lambda t: t[1])
    value.reverse()
    value = value[:10]
    return value


def rankSpeed():
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select name,speed from role where uid is not null')
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    value = sorted(value, key=lambda t: t[1])
    value.reverse()
    value = value[:10]
    return value


def rankLevel():
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select name,level,uid from role where uid is not null')
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    value = sorted(value, key=lambda t: t[1])
    value.reverse()
    value = value[:10]
    return value


rgoldxian = on_command('富豪榜', priority=241)


@rgoldxian.handle()
async def rgoldxian_handle():
    value = rankGold()
    mess = ''
    for v in value:
        mess += '姓名:' + v[0] + ',灵石:' + str(v[1]) + '\n'
    mess += '榜单前十'
    await rgoldxian.finish(mess)


rattackxian = on_command('攻击榜', priority=241)


@rattackxian.handle()
async def rattackxian_handle():
    value = rankAttack()
    mess = ''
    for v in value:
        mess += '姓名:' + v[0] + ',攻击力:' + str(v[1]) + '\n'
    mess += '榜单前十'
    await rattackxian.finish(mess)


rdefensexian = on_command('防御榜', priority=241)


@rdefensexian.handle()
async def rdefensexian_handle():
    value = rankDefense()
    mess = ''
    for v in value:
        mess += '姓名:' + v[0] + ',防御力:' + str(v[1]) + '\n'
    mess += '榜单前十'
    await rdefensexian.finish(mess)


rspeedxian = on_command('速度榜', priority=241)


@rspeedxian.handle()
async def rspeedxian_handle():
    value = rankSpeed()
    mess = ''
    for v in value:
        mess += '姓名:' + v[0] + ',速度:' + str(v[1]) + '\n'
    mess += '榜单前十'
    await rspeedxian.finish(mess)


rlevelxian = on_command('境界榜', priority=241)


@rlevelxian.handle()
async def rlevelxian_handle():
    value = rankLevel()
    mess = ''
    for v in value:
        u = XianRole(uid=v[2])
        mess += '姓名:' + v[0] + ',境界:' + u.xianlevel() + '\n'
        del u
    mess += '榜单前十'
    await rlevelxian.finish(mess)
