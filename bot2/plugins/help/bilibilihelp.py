#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/9 13:22
@author: 0xchang
@E-mail: oxchang@163.com
@file: bilibilihelp.py
@Github: https://github.com/0xchang
"""
import os

from PIL import Image, ImageDraw, ImageFont
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command


def create_bili_img():
    help_detail = '''
                    **********b站 菜单**********
    /关注uid---------------关注主播
    /取关uid---------------取关主播
    /关注列表--------------查看关注了哪些主播
    /关注详情--------------查看关注主播详情
    /测试超管--------------测试超管权限
    /测试权限--------------测试群成员权限
    /开启动态uid------------开启动态推送
    /关闭动态uid------------关闭动态推送
    /开启全体动态-----------开启动态推送at全体成员
    /关闭全体动态-----------关闭动态at全体成员
    /开启直播uid------------开启直播推送
    /关闭直播uid------------关闭直播推送
    /开启全体直播-----------开启直播推送at全体成员
    /关闭全体直播-----------关闭直播at全体成员
    /开启视频uid------------开启视频推送
    /关闭视频uid------------关闭视频推送
    /开启全体视频-----------开启视频推送at全体成员
    /关闭全体视频-----------关闭视频推送at全体成员
    置顶------------------查看up动态置顶信息
    /投稿-----------------查看up投稿视频，默认0
    查粉------------------看看粉丝有多少
    查舰----------看看你有多少个亲爱的舰长
    查成分uid-------------查他
    '''
    lino_path = os.path.join(os.getcwd(), 'img', 'lino.jpg')
    current = Image.open(lino_path)
    draw = ImageDraw.Draw(current)
    font = ImageFont.truetype(os.path.join(os.getcwd(), 'fonts', 'qiantuxiaotuti.ttf'), size=36)
    draw.text((20, 400), text=help_detail, font=font, fill=(94,38,18))
    current.save('./img/helpbili.png')

create_bili_img()

bilimenu = on_command('b站帮助',aliases={'b站菜单'}, priority=150)


@bilimenu.handle()
async def pluginmenu_handle():
    pwd = os.getcwd()
    path = os.path.join(pwd, 'img', 'helpbili.png')
    await bilimenu.finish(Message(f'[CQ:image,file=file:///{path}]'))
