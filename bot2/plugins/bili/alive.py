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

#催早饭
@scheduler.scheduled_job("cron", hour=8,minute=24)
async def good_morning():
    bot, = get_bots().values()
    qqids=select_groupid()
    qqids = set(qqids)
    for qqid in qqids:
        await bot.send_msg(
            message_type="group",
            group_id=qqid[0],
            message='啥时候吃早饭?说的就是你'
        )

#催午饭
@scheduler.scheduled_job("cron", hour=12,minute=10)
async def good_morning():
    bot, = get_bots().values()
    qqids=select_groupid()
    qqids = set(qqids)
    for qqid in qqids:
        await bot.send_msg(
            message_type="group",
            group_id=qqid[0],
            message='吃午饭了吗?宝贝'
        )

#催晚饭
@scheduler.scheduled_job("cron", hour=17,minute=20)
async def good_night():
    bot, = get_bots().values()
    qqids=select_groupid()
    qqids=set(qqids)
    for qqid in qqids:
        await bot.send_msg(
            message_type="group",
            group_id=qqid[0],
            message='你吃晚饭了没?不用我指名道姓吧'
        )
