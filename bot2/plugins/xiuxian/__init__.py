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
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    create_xian_sql = 'create table if not exists Role(uid int,name text,gold int,attack int,defense int,speed int,HP int,MP int,level int,experience int,stime int,sex text,sign int)'
    create_xiulian_sql = 'create table if not exists biguan(uid int,xtime int,jtime int)'
    create_chenghao_sql = 'create table if not exists chenghao(uid int,kill int,fish int,dazuo int,work int)'
    create_monster_sql = 'create table if not exists monsters(name text,HP int,attack int,defense int)'
    cur.execute(create_xian_sql)
    cur.execute(create_xiulian_sql)
    cur.execute(create_chenghao_sql)
    cur.execute(create_monster_sql)
    con.commit()
    cur.close()
    con.close()


create_xian()


def create_monster():
    con = sqlite3.connect('data/xiuxian.data')
    cur = con.cursor()
    cur.execute('delete from monsters')
    con.commit()
    monsters = [('野猪', 240, 210, 205),
                ('野狼', 250, 220, 201),
                ('野熊', 270, 230, 220),
                ('野鬼', 230, 220, 202),
                ('山鸡', 240, 210, 202),
                ('妖狼', 530, 570, 471),
                ('妖猪', 800, 320, 522),
                ('妖狐', 630, 320, 800),
                ('妖虎', 1030, 920, 875),
                ('妖象', 1500, 800, 1240),
                ('魔狼', 2500, 2670, 2001),
                ('魔虎', 3000, 2800, 2701),
                ('魔狐', 2600, 2300, 2600),
                ('魔鬼', 2300, 1800, 3700),
                ('魔象', 3900, 3300, 4100),
                ('魔鼠', 2300, 3100, 2200),
                ('魔猫', 2700, 2865, 2495),
                ('牛魔王', 5165, 4620, 5351),
                ('蜘蛛精', 4230, 6220, 4101), ]
    for monster in monsters:
        cur.execute('insert into monsters(name,HP,attack,defense) values(?,?,?,?)', monster)
    con.commit()
    cur.close()
    con.close()


create_monster()
