#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/2/13 17:25
@author: 0xchang
@E-mail: oxchang@163.com
@file: bilidbs.py
@Github: https://github.com/0xchang
"""
import sqlite3


def op_bili(sql: str, params: tuple):
    '''
    包含bili数据库的增删改
    :param sql:
    :param params:
    :return:
    '''
    con = sqlite3.connect('data/bili.db')
    cur = con.cursor()
    if params:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    con.commit()
    cur.close()
    con.close()


def sel_bili(sql: str, params: tuple) -> list:
    '''
    包含bili数据库的查询
    :param sql:
    :param params:
    :return: list
    '''
    con = sqlite3.connect('data/bili.db')
    cur = con.cursor()
    if params:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    con.commit()
    result = cur.fetchall()
    cur.close()
    con.close()
    return result


class BiliDB:
    '''初始化表以及删除数据'''

    @classmethod
    def create_table(cls):
        con = sqlite3.connect('data/bili.db')
        cur = con.cursor()
        # up主表(用户id,房间id,名字,直播状态,发送信息状态)
        cur.execute('create table if not exists up(uid int,rid int,name text,start_time int,send int)')
        # 群聊表(群QQ,直播通知,动态通知,视频通知,@全体成员(直播,动态,视频))
        cur.execute(
            'create table if not exists qqsetgroup(gid int,live int,dynamic int,video int,liveat int,dynamicat int,videoat int)')
        # up主和群聊关联表
        cur.execute('create table if not exists up_group(uid int,gid int)')
        con.commit()
        cur.close()
        con.close()

    @classmethod
    def delete(cls, uid: int, gid: int):
        op_bili('delete from up_group where uid=? and gid=?', (uid, gid))
        if not sel_bili('select * from up_group where uid=?', (uid,)):
            op_bili('delete from up where uid=?', (uid,))


class UpDB:
    '''
    操作Up数据表
    '''

    @classmethod
    def insert(cls, uid: int, roomid: int, name: str) -> bool:
        if not sel_bili('select * from up where uid=?', (uid,)):
            op_bili('insert into up(uid,rid,name,start_time,send) values(?,?,?,?,?)', (uid, roomid, name, 0, 0))
            return True
        return False

    @classmethod
    def update_start_time(cls, uid: int, start_time: int):
        op_bili('update up set start_time=? where uid=?', (start_time, uid))

    @classmethod
    def update_send(cls, uid: int, send: int):
        op_bili('update up set send=? where uid=?', (send, uid))

    @classmethod
    def sel_uid(cls, uid: int):
        return sel_bili('select * from up where uid=?', (uid,))

    @classmethod
    def sel(cls):
        return sel_bili('select * from up', ())


class GroupDB:
    '''
    操作群聊表
    '''

    @classmethod
    def insert(cls, gid: int) -> bool:
        if not sel_bili('select * from qqsetgroup where gid=?', (gid,)):
            op_bili('insert into qqsetgroup(gid,live,dynamic,video,liveat,dynamicat,videoat) values(?,?,?,?,?,?,?)',
                    (gid, 1, 1, 1, 0, 0, 0))
            return True
        return False

    @classmethod
    def update_live(cls, gid: int, live: int):
        op_bili('update qqsetgroup set live=? where gid=?', (live, gid))

    @classmethod
    def update_liveat(cls, gid: int, liveat: int):
        op_bili('update qqsetgroup set liveat=? where gid=?', (liveat, gid))

    @classmethod
    def update_dyn(cls, gid: int, dyn: int):
        op_bili('update qqsetgroup set dynamic=? where gid=?', (dyn, gid))

    @classmethod
    def update_dynat(cls, gid: int, dynat: int):
        op_bili('update qqsetgroup set dynamicat=? where gid=?', (dynat, gid))

    @classmethod
    def update_video(cls, gid: int, video: int):
        op_bili('update qqsetgroup set video=? where gid=?', (video, gid))

    @classmethod
    def update_videoat(cls, gid: int, videoat: int):
        op_bili('update qqsetgroup set videoat=? where gid=?', (videoat, gid))

    @classmethod
    def sel_gid(cls, gid: int) -> list:
        return sel_bili('select * from qqsetgroup where gid=?', (gid,))


class UpGroupDB:
    '''操作关联表'''

    @classmethod
    def insert(cls, uid, gid) -> bool:
        if not sel_bili('select * from up_group where uid=? and gid=?', (uid, gid)):
            op_bili('insert into up_group(uid,gid) values(?,?)', (uid, gid))
            return True
        return False

    @classmethod
    def sel_uid(cls, uid: int) -> list:
        return sel_bili('select * from up_group where uid=?', (uid,))

    @classmethod
    def sel_gid(cls, gid: int) -> list:
        return sel_bili('select * from up_group where gid=?', (gid,))
