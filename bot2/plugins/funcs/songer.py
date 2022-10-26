#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/26 14:01
@author: 0xchang
@E-mail: oxchang@163.com
@file: songer.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command
import random

songercmd=on_command('抽歌手',priority=210)
songerT=('刘德华','张学友','黎明','郭富城','谭咏麟','李克勤','陈奕迅','周杰伦','周华健','莫文蔚','林忆莲','张惠妹','刘若英','王心凌','王菲','那英','梁静茹','张靓颖','金莎','韩红','孙楠','刘欢','汪峰','刀郎','郑源','欢子','六哲','冷漠','庞龙','高安','龙梅子','胡扬林','庄心妍','李荣浩','杨宗纬','崔伟立','张远','路飞文','杨小壮','赵雷','薛之谦','罗聪')
@songercmd.handle()
async def songer_handle():
    global songerT
    songer=random.choice(songerT)
    await songercmd.finish(Message(f'您抽中的歌手是%s'%songer))