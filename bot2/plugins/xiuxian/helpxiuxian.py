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
from nonebot.adapters.onebot.v11.message import Message

helpxiuxian='''
/修仙帮助          获取帮助
/查询             查看个人信息
/进化             消耗灵石增强属性
/大进化            比进化牛必
/究极进化          比大进化牛必
/签到             签到得奖励
/改名             改名字
/改性别           改变性别
/打工             赚钱
/钓鱼             赚钱得经验
/回复             消耗灵石回HP,MP
/大回复术          消耗大量灵石回复HP,MP
/超级回复          反正比大回复术还nb
/练功             你可以练功
/清零             直接把xx数据清零(管理员)
/闭关x            闭关x分钟，期间不能干任何事
/杀人x            攻击十次x
/打怪             随机打怪，不强的时候别来
/打bossxx        打xxboss，boss很强，别来
/查boss          查看boss列表,boss每三十分钟复活一次
'''
helpxian = on_command('修仙帮助', priority=239)
@helpxian.handle()
async def infoxian_handle():
    pwd=os.getcwd()
    await helpxian.finish(Message(f'[CQ:image,file=file:///{pwd}/img/helpxiuxian.png]'))
