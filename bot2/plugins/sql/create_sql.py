#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 10:18
@author: 0xchang
@E-mail: oxchang@163.com
@file: create_sql.py
@Github: https://github.com/0xchang
"""
import sqlite3
def create_table():
    '''创建初始化user表和group表'''
    create_user_sql='create table if not exists user(uid integer,name text,roomid integer)'
    create_group_sql='create table if not exists fgroup(uid integer,roomid integer,gtype text,qqid integer,live integer,dynamic integer,video integer,liveat integer,dynamicat integer,videoat integer)'
    create_live_sql='create table if not exists live(uid integer,status integer)'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(create_user_sql)
    cur.execute(create_group_sql)
    cur.execute(create_live_sql)
    con.commit()
    cur.close()
    con.close()