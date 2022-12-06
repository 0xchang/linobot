#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/5 17:26
@author: 0xchang
@E-mail: oxchang@163.com
@file: colorname.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.params import CommandArg
from nonebot import on_command, on_fullmatch
from nonebot import get_bot

group_name = on_command('群昵称', priority=280)


@group_name.handle()
async def colorname_handle(event: GroupMessageEvent, argcom: Message = CommandArg()):
    bot = get_bot()
    # 保留颜色符号，没有改成彩色名字
    color = ''
    print(event.get_plaintext())
    uid = event.get_user_id()
    gid = event.group_id
    argcom = argcom.extract_plain_text()
    argcom = argcom.strip()
    newname = color + argcom
    if len(newname.encode()) >= 60:
        await group_name.finish(Message('名字有点长了哦，短一点试试吧'))
    await bot.call_api('set_group_card',
                       group_id=gid,
                       user_id=uid,
                       card=newname)
    await group_name.finish(Message(f'成功改群名为{argcom}'))


color_name = on_fullmatch('昵称颜色', priority=281)


@color_name.handle()
async def color_name_handle():
    color0 = '<&ÿĀĀĀ>黑色 \n<&ÿÿ5@>红色 \n<&ÿÿ]>粉色 \n<&ÿÒUÐ>紫色 \n<&ÿÿÏP>黄色 \n<%ĀĀÐ>初春 \n'
    color1 = '<%ĀĀÑ>冬梅 \n<%ĀĀÒ>高级灰 \n<%ĀĀÓ>黄昏 \n<%ĀĀÔ>科技感 \n<%ĀĀÕ>马卡龙 \n<%ĀĀÖ>霓虹闪烁 \n'
    color2 = '<%ĀĀ×>日出 \n<%ĀĀØ>盛夏 \n<%ĀĀÙ>糖果缤纷 \n<%ĀĀÚ>​晚​秋 \n<%ĀĀÛ>夜空 \n<%ĀĀÜ>粉黛 \n'
    color3 = '<%ĀĀÝ>朝夕 \n<%ĀĀÞ>潮流 ​ \n'
    mess = color0 + color1 + color2 + color3 + '\n以上特殊代码+名字即可，仅适用于群昵称'
    await color_name.finish(Message(mess))

