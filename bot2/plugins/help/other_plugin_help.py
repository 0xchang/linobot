#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/9 10:57
@author: 0xchang
@E-mail: oxchang@163.com
@file: other_plugin_help.py
@Github: https://github.com/0xchang
"""
import os

from PIL import Image, ImageDraw, ImageFont
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command


def create_plugin_img():
    help_detail = '''
                    **********插件 菜单**********
    点歌/qq点歌/网易点歌/酷我点歌/酷狗点歌
    /咪咕点歌/b站点歌 + 关键词
    remake/liferestart/人生重开/人生重来
                        ---人生重开模拟器
    头像表情包----------好像是一堆头像
    @bot xx-----------针对xx进行智障回消息
    塔罗牌-------------单张塔罗牌
    占卜---------------[占卜]
    setu 白丝---------搜索白丝图片
    查成分------------查的就是你
    绘画-------------绘图
    以图绘图---------以图绘图
    个人标签排行-----查看我的所有使用过的标签的排行
    群标签排行------查看本期所有使用过的标签的排行
    疯狂星期[一|二|三|四|五|六|日|天]
    @机器人 续写 标题
    #感谢各个插件的帮助
    '''
    lino_path = os.path.join(os.getcwd(), 'img', 'lino.jpg')
    current = Image.open(lino_path)
    draw = ImageDraw.Draw(current)
    font = ImageFont.truetype(os.path.join(os.getcwd(), 'fonts', 'qiantuxiaotuti.ttf'), size=36)
    draw.text((20, 400), text=help_detail, font=font, fill=(94,38,18))
    current.save('./img/helpplugin.png')

create_plugin_img()

pluginmenu = on_command('插件帮助',aliases={'插件菜单'}, priority=150)


@pluginmenu.handle()
async def pluginmenu_handle():
    pwd = os.getcwd()
    path = os.path.join(pwd, 'img', 'helpplugin.png')
    await pluginmenu.finish(Message(f'[CQ:image,file=file:///{path}]'))
