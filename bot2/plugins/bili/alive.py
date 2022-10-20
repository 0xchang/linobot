#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/15 12:04
@author: 0xchang
@E-mail: oxchang@163.com
@file: alive.py
@Github: https://github.com/0xchang
"""
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from nonebot import get_bots
from bot2.plugins.sql.select_sql import select_groupid

@scheduler.scheduled_job("cron", hour=8,minute=4)
async def good_morning():
    bot, = get_bots().values()
    qqids=select_groupid()
    qqids = set(qqids)
    for qqid in qqids:
        await bot.send_msg(
            message_type="group",
            group_id=qqid[0],
            message='大家早安喵~'
        )

#每天晚上的任务，晚上说晚安
@scheduler.scheduled_job("cron", hour=23,minute=58)
async def good_night():
    bot, = get_bots().values()
    qqids=select_groupid()
    qqids=set(qqids)
    for qqid in qqids:
        await bot.send_msg(
            message_type="group",
            group_id=qqid[0],
            message='大家晚安喵~'
        )
