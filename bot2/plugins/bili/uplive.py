#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 14:06
@author: 0xchang
@E-mail: oxchang@163.com
@file: uplive.py
@Github: https://github.com/0xchang
"""
from bilibili_api import live
from .bilidbs import UpDB


async def uplive(roomid: int, name: str):
    r = live.LiveRoom(roomid)
    liveres = await r.get_room_info()
    pnum = liveres['watched_show']['num']
    liveres = liveres['room_info']
    uid = liveres['uid']
    liveUrl = 'https://live.bilibili.com/' + str(roomid)
    title = liveres['title']
    cover = liveres['cover']
    startTime = liveres['live_start_time']
    res = name + '开播了,快去看看喵\n' + title + '\n[CQ:image,file=%s]' % cover + liveUrl
    if startTime != 0:
        UpDB.update_start_time(uid, startTime)
    return res, pnum, startTime
