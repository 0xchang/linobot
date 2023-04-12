#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/2/15 16:56
@author: 0xchang
@E-mail: oxchang@163.com
@file: wifedbs.py
@Github: https://github.com/0xchang
"""
import sqlite3


def op_wife(sql, params):
    con = sqlite3.connect('data/wifes.db')
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    cur.close()
    con.close()


def sel_wife(sql, params) -> list:
    con = sqlite3.connect('data/wifes.db')
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


class WifesDB:
    @classmethod
    def create(cls):
        con = sqlite3.connect('data/wifes.db')
        cur = con.cursor()
        # 创建wifes表，群号，QQ，Wife QQ，Wife name
        cur.execute('create table if not exists wifes(gid int,uid int,wid int,name text)')
        # 创建群聊是否开启老婆功能表
        cur.execute('create table if not exists gset(gid int,isEnable int)')
        con.commit()
        cur.close()
        con.close()

    @classmethod
    def insert(cls, gid: int, uid: int, wid: int, name: str):
        if not sel_wife('select * from wifes where gid=? and uid=?', (gid, uid)):
            op_wife('insert into wifes(gid,uid,wid,name) values(?,?,?,?)', (gid, uid, wid, name))

    @classmethod
    def update(cls, gid: int, uid: int, wid: int, name: str):
        op_wife('update wifes set wid=?,name=? where gid=? and uid=?', (wid, name, gid, uid))

    @classmethod
    def sel_gau(cls, gid: int, uid: int):
        return sel_wife('select * from wifes where gid=? and uid=?', (gid, uid))

    @classmethod
    def clear(cls):
        con = sqlite3.connect('data/wifes.db')
        cur = con.cursor()
        cur.execute('delete from wifes')
        con.commit()
        cur.close()
        con.close()


class WifeDBSet:
    @classmethod
    def insert(cls, gid: int):
        if not sel_wife('select * from gset where gid=?', (gid,)):
            op_wife('insert into gset(gid,isEnable) values(?,?)', (gid, 1))

    @classmethod
    def update(cls, gid, isEnable: bool):
        op_wife('update gset set isEnable=? where gid=?', (1 if isEnable else 0, gid))

    @classmethod
    def sel_gid(cls, gid: int) -> bool:
        return True if sel_wife('select isEnable from gset where gid=?', (gid,))[0][0] else False
