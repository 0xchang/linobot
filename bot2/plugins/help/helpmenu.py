#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/15 11:37
@author: 0xchang
@E-mail: oxchang@163.com
@file: helpmenu.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event
from nonebot import on_command

helpmenu=on_command('帮助',priority=150)
@helpmenu.handle()
async def helpmenu_handle(event:Event):
    help_detail='''/帮助  获取帮助信息
/关注uid    关注主播
/取关uid    取关主播
/关注列表    查看关注了哪些主播
/关注详情    查看关注主播详情
/测试超管    测试超管权限
/测试权限    测试群成员权限
/开启动态uid 开启动态推送
/关闭动态uid 关闭动态推送
/开启全体动态 开启动态推送at全体成员
/关闭全体动态 关闭动态at全体成员
/开启直播uid 开启直播推送
/关闭直播uid 关闭直播推送
/开启全体直播 开启直播推送at全体成员
/关闭全体直播 关闭直播at全体成员
/开启视频uid 开启视频推送
/关闭视频uid 关闭视频推送
/开启全体视频 开启视频推送at全体成员
/关闭全体视频 关闭视频推送at全体成员
/社会语录    获取一条社会语录(3秒)
/心灵鸡汤    获取一条心灵鸡汤(3秒)
/舔狗日记    获取一条舔狗日记(3秒)
/随机语录    获取一跳随机语录(3秒)
/随机数 x    获取x个随机数(3秒)
/随机表情    获取一个随机表情
/抽老婆      抽一个老婆送给你
/抽歌手      抽一个歌手'''
    await helpmenu.finish(Message(f'[CQ:at,qq={event.get_user_id()}]%s'%help_detail))