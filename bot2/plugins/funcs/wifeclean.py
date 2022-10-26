#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/26 22:06
@author: 0xchang
@E-mail: oxchang@163.com
@file: wifeclean.py
@Github: https://github.com/0xchang
"""
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from bot2.plugins.sql.del_sql import del_wife

@scheduler.scheduled_job("cron", hour=1,minute=0)
async def clean_wife():
    del_wife()