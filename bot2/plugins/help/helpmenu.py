#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/15 11:37
@author: 0xchang
@E-mail: oxchang@163.com
@file: helpmenu.py
@Github: https://github.com/0xchang
"""
import os

from PIL import Image, ImageDraw, ImageFont
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command


def create_help_img():
    help_detail = '''
                    **********Bot 菜单**********
    修仙帮助---------------另一个世界，建议加修仙群
    b站帮助----------------b站帮助指南
    趣味功能---------------有意思的小工具
    插件帮助---------------借用第三方插件的功能(感谢)
    '''
    lino_path = os.path.join(os.getcwd(), 'img', 'lino.jpg')
    current = Image.open(lino_path)
    draw = ImageDraw.Draw(current)
    font = ImageFont.truetype(os.path.join(os.getcwd(), 'fonts', 'qiantuxiaotuti.ttf'), size=36)
    draw.text((20, 400), text=help_detail, font=font, fill=(94,38,18))
    current.save('./img/helpbot.png')

create_help_img()

helpmenu = on_command('帮助',aliases={'菜单'}, priority=150)


@helpmenu.handle()
async def helpmenu_handle():
    pwd = os.getcwd()
    path = os.path.join(pwd, 'img', 'helpbot.png')
    await helpmenu.finish(Message(f'[CQ:image,file=file:///{path}]'))
