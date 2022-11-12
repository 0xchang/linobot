#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 12:29
@author: 0xchang
@E-mail: oxchang@163.com
@file: dyn_to_q.py
@Github: https://github.com/0xchang
"""
import time
from nonebot.adapters.onebot.v11.message import Message
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from nonebot import get_bots
from bot2.plugins.bili import updynamic
from bot2.plugins.sql.select_sql import select_uid_from_user, select_info_from_group


async def senddyn(bot,value,dynres):
    if value[0] != 1:
        return
    else:
        if value[1] != 1:
            await bot.send_msg(
                message_type=value[2],
                group_id=value[3],
                user_id=value[3],
                message=Message(dynres[2]),
            )
        else:
            out = '[CQ:at,qq=all]' + dynres[2]
            await bot.send_msg(
                message_type=value[2],
                group_id=value[3],
                user_id=value[3],
                message=Message(out),
            )


@scheduler.scheduled_job("cron", second='*/18')
async def while_dyn():
    bot, = get_bots().values()
    uids=select_uid_from_user()
    for uid in uids:
        values=select_info_from_group(uid[0])
        now = time.time()
        #print('我访问了动态',uid)
        dynres=await updynamic.dyn(uid[0],False)

        if now-dynres[1]>20:
            continue
        elif dynres[0]==1:
            for value in values:
                time.sleep(0.1)
                await senddyn(bot,(value[5], value[8], value[2], value[3]),dynres)
        elif dynres[0]==8:
            for value in values:
                time.sleep(0.1)
                await senddyn(bot,(value[6],value[9],value[2],value[3]),dynres)
        else:
            for value in values:
                time.sleep(0.1)
                await senddyn(bot,(value[5], value[8], value[2], value[3]), dynres)
