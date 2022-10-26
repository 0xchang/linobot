#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 14:20
@author: 0xchang
@E-mail: oxchang@163.com
@file: live_to_q.py
@Github: https://github.com/0xchang
"""
import time
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from nonebot import get_bots
from bot2.plugins.bili.uplive import uplive
from bot2.plugins.sql.select_sql import select_uid_from_user,select_info_from_group,select_user,select_live
from bot2.plugins.sql.update_sql import update_live,update_data

@scheduler.scheduled_job("cron", second='*/10')
async def while_live():
    bot, = get_bots().values()
    uids = select_uid_from_user()
    for uid in uids:
        #print('我访问了直播', uid)
        user = select_user(uid[0])[0]
        ginfos = select_info_from_group(user[0])
        liveres=await uplive(user[2],user[1])
        mess=liveres[1]
        if liveres[0]==0:
            await liveBye(bot, liveres[2],ginfos)
        if time.time()-liveres[0]>10:
            continue
        #在播状态,更新live数据库
        update_data(update_live(uid[0], 1))
        for ginfo in ginfos:
            if ginfo[4]!=1:
                continue
            elif ginfo[7]==1:
                if '[CQ:at,qq=all]' not in mess:
                    mess='[CQ:at,qq=all]'+mess
            await bot.send_msg(
                message_type=ginfo[2],
                group_id=ginfo[3],
                user_id=ginfo[3],
                message=mess,
            )

async def liveBye(bot,data:tuple,ginfos:tuple):
    uid,name,liveStatus,pnum,stime=data
    value=select_live(uid)[0]
    if value[1]==0:
        return
    if liveStatus!=0:
        return
    update_data(update_live(uid,0))
    spendtime=int(time.time()-stime)
    second=spendtime%60
    minute=int(spendtime/60)%60
    hour=int(spendtime/3600)
    mess='【下拨提醒】\n'+name+'下播了喵,谢谢观看\n'+'本次直播人气峰值: %d\n'%pnum+'本次直播时长为%s小时%s分钟%s秒\n'%(hour,minute,second)+'希望大家多来看我哦!'
    for ginfo in ginfos:
        await bot.send_msg(
            message_type=ginfo[2],
            group_id=ginfo[3],
            user_id=ginfo[3],
            message=mess,
        )