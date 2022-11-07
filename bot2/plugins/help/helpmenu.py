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
import time

from PIL import Image, ImageDraw, ImageFont
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_fullmatch


def create_help_img():
    help_detail = '''
    帮助----------------------获取帮助信息
    /关注uid-----------------关注主播
    /取关uid-----------------取关主播
    /关注列表----------------查看关注了哪些主播
    /关注详情----------------查看关注主播详情
    /测试超管----------------测试超管权限
    /测试权限----------------测试群成员权限
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
    社会语录-----------------获取一条社会语录(3秒)
    心灵鸡汤-----------------获取一条心灵鸡汤(3秒)
    舔狗日记-----------------获取一条舔狗日记(3秒)
    随机语录-----------------获取一跳随机语录(3秒)
    /随机数 x-----------------获取x个随机数(3秒)
    随机表情-----------------获取一个随机表情
    老婆状态-----------------查看老婆功能是否开启
    禁老婆--------------------禁止抽老婆功能
    解老婆--------------------解放抽老婆功能
    抽老婆--------------------抽一个老婆送给你
    换老婆--------------------换一个老婆给你
    /偷老婆atxx-------------你可以偷xx的老婆
    置顶----------------------查看up动态置顶信息
    /投稿---------------------查看up投稿视频，默认0
    抽歌手-------------------抽一个歌手
    /看番---------------------搜索番剧并返回网址
    早饭
    午饭
    晚饭
    水果
    昵称颜色-----------------可以修改群昵称的颜色
    修仙帮助-----------------另一个世界，建议加修仙群
    '''
    lino_path = os.path.join(os.getcwd(), 'img', 'lino.jpg')
    current = Image.open(lino_path)
    draw = ImageDraw.Draw(current)
    font = ImageFont.truetype(os.path.join(os.getcwd(), 'fonts', 'syht_CN-Heavy.otf'), size=36)
    draw.text((20, 400), text=help_detail, font=font, fill=(48,128,20))
    current.save('./img/helpbot.png')

create_help_img()

helpmenu = on_fullmatch('帮助', priority=150)


@helpmenu.handle()
async def helpmenu_handle():
    pwd = os.getcwd()
    path = os.path.join(pwd, 'img', 'helpbot.png')
    await helpmenu.finish(Message(f'[CQ:image,file=file:///{path}]'))
