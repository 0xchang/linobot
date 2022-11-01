#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 14:46
@author: 0xchang
@E-mail: oxchang@163.com
@file: helpxiuxian.py
@Github: https://github.com/0xchang
"""
import os
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message

helpxian = on_command('修仙帮助', priority=239)
@helpxian.handle()
async def infoxian_handle(event: GroupMessageEvent):
    help='''
/修仙帮助          获取帮助
/查询             查看个人信息
/进化             消耗金币增强属性
/签到             签到得奖励
/改名             改名字
/改性别           改变性别
/打工             赚钱
/钓鱼             赚钱得经验
/回复             消耗金币回HP,MP
'''
    pwd=os.getcwd()
    await helpxian.finish(Message(f'[CQ:image,file=file:///{pwd}/img/helpxiuxian.png]'))
