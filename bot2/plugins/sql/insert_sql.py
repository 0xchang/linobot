#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 10:20
@author: 0xchang
@E-mail: oxchang@163.com
@file: insert_sql.py
@Github: https://github.com/0xchang
"""
import sqlite3
def insert_user(uid:int,name:str,roomid:int):
    insert_user_sql='insert into user(uid,name,roomid) values(?,?,?)'
    con = sqlite3.connect('data/info.data')
    cur = con.cursor()
    cur.execute(insert_user_sql,(uid,name,roomid))
    con.commit()
    cur.close()
    con.close()


def insert_group(uid:int,roomid:int,gtype:str,qqid:int):
    insert_user_sql='insert into fgroup(uid,roomid,gtype,qqid,live,dynamic,video,liveat,dynamicat,videoat) values(?,?,?,?,?,?,?,?,?,?)'
    con = sqlite3.connect('data/info.data')
    cur = con.cursor()
    cur.execute(insert_user_sql,(uid,roomid,gtype,qqid,1,1,1,1,1,1))
    con.commit()
    cur.close()
    con.close()

def insert_live(uid:int):
    insert_sql='insert into live(uid,status) values(?,0)'
    con = sqlite3.connect('data/info.data')
    cur = con.cursor()
    cur.execute(insert_sql,(uid,))
    con.commit()
    cur.close()
    con.close()