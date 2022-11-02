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

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event
from bot2.plugins.xiuxian.Role import XianRole
from bot2.plugins.xiuxian.AMonster import Monster
from nonebot.adapters.onebot.v11.message import Message

mon = [('野猪', 240, 210, 205),
       ('野狼', 250, 220, 201),
       ('野熊', 270, 230, 220),
       ('野鬼', 230, 220, 202),
       ('山鸡', 240, 210, 202),
       ('妖狼', 530, 570, 471),
       ('妖猪', 800, 320, 522),
       ('妖狐', 630, 320, 800),
       ('妖虎', 1030, 920, 875),
       ('妖象', 1500, 800, 1240),
       ('魔狼', 2500, 2670, 2001),
       ('魔虎', 3000, 2800, 2701),
       ('魔狐', 2600, 2300, 2600),
       ('魔鬼', 2300, 1800, 3700),
       ('魔象', 3900, 3300, 4100),
       ('魔鼠', 2300, 3100, 2200),
       ('魔猫', 2700, 2865, 2495),
       ('牛魔王', 5165, 4620, 5351),
       ('蜘蛛精', 4230, 6220, 4101), ]

atmoxian = on_command('打怪', priority=240)


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
    while u.attack*1.2+u.defense*1.2<m[2]+m[3] and count<20:
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
