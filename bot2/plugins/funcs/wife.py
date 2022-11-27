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
from nonebot import on_command,on_fullmatch
from nonebot.params import CommandArg
import random
from bot2.plugins.sql.select_sql import select_wife,select_wifesta,select_uid_from_qid
from bot2.plugins.sql.insert_sql import insert_wife,insert_wifesta
from bot2.plugins.sql.update_sql import update_wife,update_data,update_wifesta

hwife=on_fullmatch('换老婆',priority=107)
@hwife.handle()
async def hwife_handle(bot:Bot,event:GroupMessageEvent):
    gid=event.group_id
    wsta=select_wifesta(gid)
    if len(wsta)!=0:
        wsta=wsta[0]
        if wsta[1]==0:
            return
    mess=await changewife(bot,event)
    await hwife.finish(Message(mess),at_sender=True)


cwife=on_fullmatch('抽老婆',priority=108)
@cwife.handle()
async def cwife_handle(bot:Bot,event:GroupMessageEvent):
    qqid = event.get_user_id()
    gid = event.group_id
    wsta=select_wifesta(gid)
    if len(wsta)!=0:
        wsta=wsta[0]
        if wsta[1]==0:
            return
    value=select_wife(qqid,gid)
    print(value)
    if len(value)!=0:
        value=value[0]
        mess = f',您亲爱的老婆是[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={value[2]}&spec=5&img_type=jpg]【{value[3]}】 ({value[2]})呐!'
        await hwife.finish(Message(mess),at_sender=True)
    #如果数据库没有数据就换老婆一样的原理
    mess=await changewife(bot,event)
    await cwife.finish(Message(mess),at_sender=True)


async def changewife(bot:Bot,event:GroupMessageEvent):
    qqid=event.get_user_id()
    gid=event.group_id
    data=await bot.call_api('get_group_member_list',**{'group_id':gid})
    mywife=data[random.randint(0,len(data)-1)]
    mess=f',您亲爱的老婆是[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={mywife["user_id"]}&spec=5&img_type=jpg]【{mywife["nickname"]}】 ({mywife["user_id"]})呐!'
    value=select_wife(qqid,gid)
    if len(value)==0:
        #插入
        insert_wife(qqid,gid,mywife['user_id'],mywife['nickname'])
    else:
        #更新
        update_data(update_wife(qqid,gid,mywife['user_id'],mywife['nickname']))
    return mess

jinwife=on_fullmatch('禁老婆',priority=220)
@jinwife.handle()
async def jinwife_handle(event:GroupMessageEvent):
    gid=event.group_id
    res=select_wifesta(gid)
    if len(res)==0:
        #插入
        insert_wifesta(gid,0)
    else:
        #更新
        update_data(update_wifesta(gid,0))
    await jinwife.finish(Message(f'已经禁止抽老婆功能'),at_sender=True)



jiewife=on_command('解老婆',priority=221)
@jiewife.handle()
async def jiewife_handle(event:GroupMessageEvent):
    gid = event.group_id
    res = select_wifesta(gid)
    if len(res) == 0:
        # 插入
        insert_wifesta(gid, 1)
    else:
        # 更新
        update_data(update_wifesta(gid, 1))
    await jiewife.finish(Message(f'已经开启抽老婆功能'),at_sender=True)

wifesta=on_fullmatch('老婆状态',priority=222)
@wifesta.handle()
async def wifesta_handle(event:GroupMessageEvent):
    gid=event.group_id
    res=select_wifesta(gid)
    if len(res)==0:
        await wifesta.finish(Message(f'老婆状态开启'),at_sender=True)
    res=res[0]
    if res[1]==0:
        await wifesta.finish(Message(f'老婆状态关闭'),at_sender=True)
    await wifesta.finish(Message(f'老婆状态开启'),at_sender=True)

stealwife=on_command('偷老婆',priority=223)
@stealwife.handle()
async def stealwife_handle(event:GroupMessageEvent,argcom:Message=CommandArg()):
    uid=argcom[0].get('data').get('qq')
    value0=select_wife(uid,event.group_id)
    if len(value0)==0:
        await stealwife.finish(Message(f'他连老婆都没有呢，你看他这么可怜别偷了！'),at_sender=True)
    else:
        value0=value0[0]
        print(value0)
        if random.choice((True,False)):
            await stealwife.finish(Message(f'偷老婆失败了喵'),at_sender=True)
        value = select_wife(event.get_user_id(), event.group_id)
        if len(value) == 0:
            # 插入
            insert_wife(event.get_user_id(), value0[1], value0[2], value0[3])
        else:
            # 更新
            update_data(update_wife(event.get_user_id(), value0[1], value0[2], value0[3]))
        await stealwife.finish(Message(f'恭喜你偷到了老婆，快看看你老婆吧！'),at_sender=True)