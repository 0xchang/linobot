#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/31 20:53
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""
import sqlite3
from bot2.plugins.xiuxian.moncfg import monsters

def create_xian():
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    create_xian_sql = 'create table if not exists Role(uid int,name text,gold int,attack int,defense int,speed int,HP int,MP int,level int,experience int,stime int,sex text,sign int)'
    create_xiulian_sql = 'create table if not exists biguan(uid int,xtime int,jtime int)'
    create_chenghao_sql = 'create table if not exists chenghao(uid int,kill int,fish int,dazuo int,work int)'
    create_monster_sql = 'create table if not exists monsters(name text,HP int,attack int,defense int)'
    cur.execute(create_xian_sql)
    cur.execute(create_xiulian_sql)
    cur.execute(create_chenghao_sql)
    cur.execute(create_monster_sql)
    con.commit()
    cur.close()
    con.close()


create_xian()


def create_monster():
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('delete from monsters')
    con.commit()
    for monster in monsters:
        cur.execute('insert into monsters(name,HP,attack,defense) values(?,?,?,?)', monster)
    con.commit()
    cur.close()
    con.close()


create_monster()
