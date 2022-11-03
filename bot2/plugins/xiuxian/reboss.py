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
#复活boss
@scheduler.scheduled_job("cron", minute='*/30')
async def reboss():
    con=sqlite3.connect('data/xiuxian.data')
    cur=con.cursor()
    cur.execute('update monboss set live=1')
    con.commit()
    cur.close()
    con.close()