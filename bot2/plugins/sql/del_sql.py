#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 10:20
@author: 0xchang
@E-mail: oxchang@163.com
@file: del_sql.py
@Github: https://github.com/0xchang
"""
import sqlite3
def del_group(uid:int,gtype:str,qqid:int):
    del_sql='delete from fgroup where uid=? and gtype=? and qqid=?'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(del_sql,(uid,gtype,qqid))
    con.commit()
    cur.close()
    con.close()



def del_user(uid:int):
    select_group_sql='select * from fgroup where uid=?'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(select_group_sql,(uid,))
    con.commit()
    value=cur.fetchall()
    if len(value)==0:
        del_user_sql='delete from user where uid=?'
        cur.execute(del_user_sql,(uid,))
        con.commit()
    cur.close()
    con.close()
