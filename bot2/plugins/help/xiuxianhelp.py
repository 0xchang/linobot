#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/9 13:22
@author: 0xchang
@E-mail: oxchang@163.com
@file: xiuxianhelp.py
@Github: https://github.com/0xchang
"""
import os
from nonebot import on_command
from PIL import Image,ImageDraw,ImageFont
from nonebot.adapters.onebot.v11.message import Message

def create_xiuxian_help():
    helpxiuxian='''
                    **********修仙菜单**********
    /查询--------查看个人信息
    进化---------消耗灵石增强属性
    大进化--------比进化牛必
    究极进化------比大进化牛必
    我是变态------变态级别进化
    签到---------签到得奖励
    /改名--------改名字
    /改性别-------改变性别
    打工---------赚钱
    钓鱼---------赚钱得经验
    回复---------消耗灵石回HP,MP
    大回复术------消耗大量灵石回复HP,MP
    超级回复------反正比大回复术还nb
    练功---------你可以练功
    /清零--------直接把xx数据清零(管理员)
    /闭关x--------闭关x分钟，期间不能干任何事
    /杀人x--------攻击十次x
    打怪---------随机打怪，不强的时候别来
    /打bossxx------打xxboss，boss很强，别来
    查boss--------查看boss列表,boss三十分钟复活一次
    高阶boss-------同上
    个人boss-------同上
    杀bossxx-------打xxboss,个人专属boss,私聊打boss
    查钱---------查看钱庄余额
    开户---------向钱庄申请账户
    销户---------向钱庄销户(钱庄余额会全部清空)
    存钱 100------向钱庄存灵石
    取钱 100------向钱庄取灵石
    转账@xx 100----向xx转账100灵石
    换血500--------用500灵石换取1000血量
    换蓝500--------用500灵石换取250蓝量
    攻击榜
    防御榜
    速度榜
    富豪榜
    境界榜
    境界帮助
    赌灵石--------一夜暴富还是上天台?
    殊死一搏-----和别人对赌，输的一方禁言一分钟
    九死一生-----赢的概率上升
    '''
    lino_path=os.path.join(os.getcwd(),'img','lino.jpg')
    current=Image.open(lino_path)
    draw=ImageDraw.Draw(current)
    font=ImageFont.truetype(os.path.join(os.getcwd(),'fonts','qiantuxiaotuti.ttf'),size=40)
    draw.text((10, 420),text=helpxiuxian,font=font,fill=(94,38,18))
    current.save('./img/helpxiuxian.png')

create_xiuxian_help()

helpxian = on_command('修仙帮助',aliases={'修仙菜单'}, priority=239)
@helpxian.handle()
async def infoxian_handle():
    pwd = os.getcwd()
    path = os.path.join(pwd, 'img', 'helpxiuxian.png')
    await helpxian.finish(Message(f'[CQ:image,file=file:///{path}]'))
