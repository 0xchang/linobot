#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/2 23:05
@author: 0xchang
@E-mail: oxchang@163.com
@file: atmon.py
@Github: https://github.com/0xchang
"""
import random

from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event
from bot2.plugins.xiuxian.Role import XianRole
from bot2.plugins.xiuxian.AMonster import Monster
from nonebot.adapters.onebot.v11.message import Message
from bot2.plugins.xiuxian.moncfg import monsters
mon = monsters

atmoxian = on_fullmatch('打怪', priority=240)

@atmoxian.handle()
async def infoxian_handle(event: Event):
    uid = event.get_user_id()
    u = XianRole(uid)
    if u.isBiguan():
        await atmoxian.finish(Message('你正在闭关'))
    if not u.isLive():
        await atmoxian.finish(Message('你的血量不足'))
    m = random.choice(mon)
    count=0
    while (u.attack+u.defense)*1.3<m[2]+m[3] and count<10:
        count+=1
        m = random.choice(mon)
    if count==20:
        await atmoxian.finish(Message('你没有找到怪物,可能是你实力不够,快去提升一下吧'))
    mname=m[0]
    m= Monster(mname)
    res = u.kmonster(m)
    if not res[0]:
        mess = f'你是不是有点菜啊,{mname}都没有打过,快去加强一下自己吧,记得回血哦'
    else:
        mess = f'恭喜你打过了{mname},但是你损失了{res[2]}血,你卖掉他的妖丹得到了{res[1]}灵石'
    del u
    del m
    await atmoxian.finish(Message(mess))
