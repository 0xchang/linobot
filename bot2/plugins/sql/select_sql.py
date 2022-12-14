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

def select_userName(name:str):
    select_sql='select * from user where name=?'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(select_sql,(name,))
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

def sel_uid_from_fgroup(qid:int):
    select_sql='select uid from fgroup where gtype=? and qqid=?'
    con = sqlite3.connect('data/info.data')
    cur = con.cursor()
    cur.execute(select_sql, ('group',qid))
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
            result+='??????:???,'
        else:
            result+='??????:???,'
        if value[2]==1:
            result+='??????:???,'
        else:
            result+='??????:???,'
        if value[3]==1:
            result+='??????:???,'
        else:
            result+='??????:???,'
        if value[4]==1:
            result+='??????at:???,'
        else:
            result+='??????at:???,'
        if value[5]==1:
            result+='??????at:???,'
        else:
            result+='??????at:???,'
        if value[6]==1:
            result+='??????at:???'
        else:
            result+='??????at:???'
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

def select_wife(uid:int,gid:int):
    select_sql='select * from wifes where uid=? and gid=?'
    con=sqlite3.connect('data/info.data')
    cur=con.cursor()
    cur.execute(select_sql,(uid,gid))
    con.commit()
    value=cur.fetchall()
    cur.close()
    con.close()
    return value

def select_wifesta(gid:int):
    select_sql = 'select * from wifesta where gid=?'
    con = sqlite3.connect('data/info.data')
    cur = con.cursor()
    cur.execute(select_sql, (gid,))
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    return value

def select_uid_from_qid(qid:int):
    select_sql = 'select uid from fgroup where qqid=? and gtype="group"'
    con = sqlite3.connect('data/info.data')
    cur = con.cursor()
    cur.execute(select_sql, (qid,))
    con.commit()
    value = cur.fetchall()
    cur.close()
    con.close()
    return value

