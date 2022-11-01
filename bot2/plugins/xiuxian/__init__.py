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
def create_xian():
    con=sqlite3.connect('data/xiuxian.data')
    cur=con.cursor()
    create_xian_sql='create table if not exists Role(uid int,name text,gold int,attack int,defense int,speed int,HP int,MP int,level int,experience int,stime int,sex text,sign int)'
    cur.execute(create_xian_sql)
    con.commit()
    cur.close()
    con.close()
create_xian()

