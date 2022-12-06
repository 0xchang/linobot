#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/12/7 0:27
@author: 0xchang
@E-mail: oxchang@163.com
@file: tspeak.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command
from nonebot.params import CommandArg

speak_cmd = on_command('发话',priority=302)


@speak_cmd.handle()
async def speak_handle(argcom:Message=CommandArg()):
    txt=argcom.extract_plain_text().strip().replace(' ','')
    mess = f'[CQ:tts,text={txt}]'
    await speak_cmd.finish(Message(mess))