#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/3 13:48
@author: 0xchang
@E-mail: oxchang@163.com
@file: reboss.py
@Github: https://github.com/0xchang
"""
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
import sqlite3
#复活boss,且清空数据库中的无效值
@scheduler.scheduled_job("cron", minute='*/30')
async def reboss():
    con=sqlite3.connect('data/xiuxian.data')
    cur=con.cursor()
    cur.execute('update monboss set live=1')
    cur.execute('update highmonboss set live=1')
    cur.execute('update gerenboss set live=1')
    cur.execute('delete from biguan where uid IS NULL')
    cur.execute('delete from Role where uid IS NULL')
    con.commit()
    cur.close()
    con.close()