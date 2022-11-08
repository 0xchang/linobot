#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/8 19:00
@author: 0xchang
@E-mail: oxchang@163.com
@file: Bank.py
@Github: https://github.com/0xchang
"""
from bot2.plugins.xiuxian.Role import XianRole
import sqlite3


# 查钱
def BgetInfo(u: XianRole) -> list:
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('select * from bank where uid=?', (u.uid,))
    con.commit()
    val = cur.fetchall()
    cur.close()
    con.close()
    return val


# 销户
def BdelInfo(u: XianRole) -> bool:
    if BgetInfo(u)==[]:
        return False
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('delete from bank where uid=?', (u.uid,))
    con.commit()
    cur.close()
    con.close()
    return True


# 开户
def BnewInfo(u: XianRole) -> bool:
    if BgetInfo(u)!=[]:
        return False
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('insert into bank(uid,gold) values(?,?)', (u.uid, 0))
    con.commit()
    cur.close()
    con.close()
    return True


# 存钱
def BpushGold(u: XianRole, gold: int) -> bool:
    if gold < 0 or not isinstance(gold, int) or u.gold < gold or u.gold < 1:
        return False
    val = BgetInfo(u)
    if val == []:
        return False
    val = val[0]
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('update bank set gold=? where uid=?', (val[1] + gold, u.uid))
    con.commit()
    cur.close()
    con.close()
    u.gold -= gold
    return True


# 取钱
def BpopGold(u: XianRole, gold: int) -> bool:
    if gold < 0 or not isinstance(gold, int):
        return False
    val = BgetInfo(u)
    if val == []:
        return False
    val = val[0]
    if val[1] < gold:
        return False
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('update bank set gold=? where uid=?', (val[1] - gold, u.uid))
    con.commit()
    cur.close()
    con.close()
    u.gold += gold
    return True


# 转账
def BchangeGold(u1: XianRole, u2: XianRole, gold: int) -> bool:
    if gold < 0 or not isinstance(gold, int):
        return False
    val1 = BgetInfo(u1)
    val2 = BgetInfo(u2)
    if val1 == []:
        return False
    if val2 == []:
        return False
    val1 = val1[0]
    val2 = val2[0]
    if val1[1] < gold:
        return False
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('update bank set gold=? where uid=?', (val1[1] - gold, val1[0]))
    cur.execute('update bank set gold=? where uid=?', (val2[1] + gold, val2[0]))
    con.commit()
    cur.close()
    con.close()
    return True
