#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 10:20
@author: 0xchang
@E-mail: oxchang@163.com
@file: update_sql.py
@Github: https://github.com/0xchang
"""
import sqlite3

def update_dyn(uid:int,gtype:str,qqid:int,status:int):
    update_sql='update fgroup set dynamic=? where uid=? and gtype=? and qqid=?'
    return (update_sql,(status,uid,gtype,qqid))

def update_dynat(uid:int,gtype:str,qqid:int,status:int):
    update_sql='update fgroup set dynamicat=? where uid=? and gtype=? and qqid=?'
    return (update_sql,(status,uid,gtype,qqid))

def update_live(uid:int,gtype:str,qqid:int,status:int):
    update_sql='update fgroup set live=? where uid=? and gtype=? and qqid=?'
    return (update_sql,(status,uid,gtype,qqid))

def update_liveat(uid:int,gtype:str,qqid:int,status:int):
    update_sql='update fgroup set liveat=? where uid=? and gtype=? and qqid=?'
    return (update_sql,(status,uid,gtype,qqid))

def update_video(uid:int,gtype:str,qqid:int,status:int):
    update_sql='update fgroup set video=? where uid=? and gtype=? and qqid=?'
    return (update_sql,(status,uid,gtype,qqid))

def update_videoat(uid:int,gtype:str,qqid:int,status:int):
    update_sql='update fgroup set videoat=? where uid=? and gtype=? and qqid=?'
    return (update_sql,(status,uid,gtype,qqid))

def update_data(data):
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    print(data)
    cur.execute(data[0],data[1])
    con.commit()
    cur.close()
    con.close()

def update_live(uid:int,status:int):
    update_sql = 'update live set status=? and uid=?'
    return (update_sql,(status,uid))
