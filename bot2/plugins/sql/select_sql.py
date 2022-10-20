#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 10:19
@author: 0xchang
@E-mail: oxchang@163.com
@file: select_sql.py
@Github: https://github.com/0xchang
"""
import sqlite3
def select_user(uid:int):
    select_sql='select * from user where uid=?'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(select_sql,(uid,))
    con.commit()
    value=cur.fetchall()
    cur.close()
    con.close()
    return value

def select_uid_from_user():
    select_sql='select uid from user'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(select_sql)
    con.commit()
    value=cur.fetchall()
    cur.close()
    con.close()
    return value

def select_group(uid:int,gtype:str,qqid:int):
    select_sql = 'select * from fgroup where uid=? and gtype=? and qqid=? '
    con = sqlite3.connect('data/info.data')
    cur = con.cursor()
    cur.execute(select_sql, (uid,gtype,qqid))
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    return value

def select_groupid():
    select_sql='select qqid from fgroup where gtype=?'
    con = sqlite3.connect('data/info.data')
    cur = con.cursor()
    cur.execute(select_sql, ("group",))
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    return value

def select_follow_group(gtype:str,qqid:int):
    select_sql='select uid from fgroup where gtype=? and qqid=?'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(select_sql,(gtype,qqid))
    con.commit()
    values=cur.fetchall()
    select_sql = 'select name,uid from user where uid=?'
    results=[]
    res=''
    for value in values:
        uid=value[0]
        cur.execute(select_sql,(uid,))
        con.commit()
        results.append(cur.fetchall()[0])
    for result in results:
        name,uid=result
        res+=name+','+str(uid)+'\n'
    return res


def select_info_from_group(uid:int):
    select_sql = 'select * from fgroup where uid=?'
    con = sqlite3.connect('data/info.data')
    cur = con.cursor()
    cur.execute(select_sql, (uid,))
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    return value

def select_follow_info(gtype:str,qqid:int):
    select_sql='select uid,live,dynamic,video,liveat,dynamicat,videoat from fgroup where gtype=? and qqid=?'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(select_sql,(gtype,qqid))
    con.commit()
    values=cur.fetchall()
    select_sql = 'select name,uid from user where uid=?'
    result=''
    for value in values:
        uid=value[0]
        cur.execute(select_sql,(uid,))
        con.commit()
        nvalue=cur.fetchall()[0]
        result=result+nvalue[0]+'|'+str(uid)+' '
        if value[1]==1:
            result+='直播:开,'
        else:
            result+='直播:关,'
        if value[2]==1:
            result+='动态:开,'
        else:
            result+='动态:关,'
        if value[3]==1:
            result+='视频:开,'
        else:
            result+='视频:关,'
        if value[4]==1:
            result+='直播at:开,'
        else:
            result+='直播at:关,'
        if value[5]==1:
            result+='动态at:开,'
        else:
            result+='动态at:关,'
        if value[6]==1:
            result+='视频at:开'
        else:
            result+='视频at:关'
        result+='\n'
    return result

def select_live(uid:int):
    select_sql='select * from  live where uid=?'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(select_sql,(uid,))
    con.commit()
    value=cur.fetchall()
    cur.close()
    con.close()
    return value
