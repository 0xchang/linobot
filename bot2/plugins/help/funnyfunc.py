#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/9 13:27
@author: 0xchang
@E-mail: oxchang@163.com
@file: funnyfunc.py
@Github: https://github.com/0xchang
"""
import os

from PIL import Image, ImageDraw, ImageFont
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command


def create_funny_img():
    help_detail = '''
                **********趣味功能菜单**********
    社会语录---------------获取一条社会语录(3秒)
    心灵鸡汤---------------获取一条心灵鸡汤(3秒)
    舔狗日记---------------获取一条舔狗日记(3秒)
    随机语录---------------获取一跳随机语录(3秒)
    骰子--------------------扔出一个数
    /随机数 x--------------获取x个随机数(3秒)
    随机表情---------------获取一个随机表情
    老婆状态---------------查看老婆功能是否开启
    禁老婆-----------------禁止抽老婆功能
    解老婆-----------------解放抽老婆功能
    抽老婆-----------------抽一个老婆送给你
    换老婆-----------------换一个老婆给你
    /偷老婆atxx-------------你可以偷xx的老婆
    抽歌手----------------抽一个歌手
    /看番-----------------搜索番剧并返回网址
    早饭
    午饭
    晚饭
    水果
    昵称颜色---------------可以修改群昵称的颜色
    随机壁纸------------随机壁纸，有可能是美女吧
    随机美女------------我猜一点都不啬
    壁纸推荐------------你猜
    银发少女------------别刷太快
    兽耳少女------------别刷太快
    竖屏少女------------别刷太快
    发话xxx------------让机器人说话
    疫情安全-----------显示疫情注意事项
    提醒--------------提醒你要做什么事情
    '''
    lino_path = os.path.join(os.getcwd(), 'img', 'lino.jpg')
    current = Image.open(lino_path)
    draw = ImageDraw.Draw(current)
    font = ImageFont.truetype(os.path.join(os.getcwd(), 'fonts', 'qiantuxiaotuti.ttf'), size=36)
    draw.text((20, 400), text=help_detail, font=font, fill=(94,38,18))
    current.save('./img/helpfunny.png')

create_funny_img()

helpfunnymenu = on_command('趣味功能',aliases={'趣味菜单'}, priority=150)


@helpfunnymenu.handle()
async def helpfunnymenu_handle():
    pwd = os.getcwd()
    path = os.path.join(pwd, 'img', 'helpfunny.png')
    await helpfunnymenu.finish(Message(f'[CQ:image,file=file:///{path}]'))
