#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/26 14:15
@author: 0xchang
@E-mail: oxchang@163.com
@file: wife.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot
from nonebot import on_command
import random
from bot2.plugins.sql.select_sql import select_wife
from bot2.plugins.sql.insert_sql import insert_wife
from bot2.plugins.sql.update_sql import update_wife,update_data

hwife=on_command('换老婆',priority=107)
@hwife.handle()
async def hwife_handle(bot:Bot,event:GroupMessageEvent):
    mess=await changewife(bot,event)
    await hwife.finish(Message(mess))


cwife=on_command('抽老婆',priority=108)
@cwife.handle()
async def cwife_handle(bot:Bot,event:GroupMessageEvent):
    qqid = event.get_user_id()
    gid = event.group_id
    value=select_wife(qqid,gid)
    print(value)
    if len(value)!=0:
        value=value[0]
        mess = f'[CQ:at,qq={qqid}],您亲爱的老婆是[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={value[2]}&spec=5&img_type=jpg]【{value[3]}】 ({value[2]})呐!'
        await hwife.finish(Message(mess))
    #如果数据库没有数据就换老婆一样的原理
    mess=await changewife(bot,event)
    await cwife.send(Message(mess))


async def changewife(bot:Bot,event:GroupMessageEvent):
    qqid=event.get_user_id()
    gid=event.group_id
    data=await bot.call_api('get_group_member_list',**{'group_id':gid})
    mywife=data[random.randint(0,len(data)-1)]
    mess=f'[CQ:at,qq={qqid}],您亲爱的老婆是[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={mywife["user_id"]}&spec=5&img_type=jpg]【{mywife["nickname"]}】 ({mywife["user_id"]})呐!'
    value=select_wife(qqid,gid)
    print(value)
    if len(value)==0:
        #插入
        insert_wife(qqid,gid,mywife['user_id'],mywife['nickname'])
    else:
        #更新
        update_data(update_wife(qqid,gid,mywife['user_id'],mywife['nickname']))
    return mess