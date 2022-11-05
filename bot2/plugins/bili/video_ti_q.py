#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/5 15:14
@author: 0xchang
@E-mail: oxchang@163.com
@file: video_ti_q.py
@Github: https://github.com/0xchang
"""
from bilibili_api import user
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.sql.select_sql import select_uid_from_qid
from nonebot.params import CommandArg

vcmd = on_command('投稿', priority=241)


@vcmd.handle()
async def vcmd_handle(event: GroupMessageEvent,argcom:Message=CommandArg()):
    arg=argcom.extract_plain_text()
    arg=arg.strip()
    if arg=='':
        arg='0'
    if not arg.isdigit():
        await vcmd.finish(Message('你的参数不对'))
    arg=int(arg)
    if arg>4:
        await vcmd.finish(Message('投稿数字只能0-4哦'))
    gid = event.group_id
    values = select_uid_from_qid(gid)
    if len(values) == 0:
        await vcmd.finish(Message('没有关注任何主播哦'))
    mess = ''
    for v in values:
        v = v[0]
        u = user.User(v)
        res = await u.get_videos()
        res = res['list']['vlist'][arg]
        comment = res['comment']
        pic = res['pic']
        description = res['description']
        title = res['title']
        length = res['length']
        bvid = 'https://b23.tv/' + res['bvid']
        play = res['play']
        mess += '标题:' + title + '\n描述:' + description + '\n时长:' + str(length) + '\n播放量:' + str(play) + '\n评论:' + str(
            comment) + f'[CQ:image,file={pic}]' + bvid + '\n'
    mess=mess[:-1]
    await vcmd.finish(Message(mess))
