#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/15 11:41
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""

import sqlite3

def create_fname_table():
    con = sqlite3.connect('./data/fname.data')
    cur = con.cursor()
    cur.execute('create table if not exists user(uid integer,gid interger,name text)')
    con.commit()
    cur.close()
    con.close()

create_fname_table()