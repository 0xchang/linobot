#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/5 15:14
@author: 0xchang
@E-mail: oxchang@163.com
@file: video_ti_q.py
@Github: https://github.com/0xchang
"""
from bilibili_api import user, video


async def vmess(uid: int, site: str) -> str:
    if site == '':
        site = '0'
    if not site.isdigit():
        return '你的参数不对'
    site = int(site)
    if site > 9:
        return '投稿数字只能0-9哦'
    u = user.User(uid)
    res = await u.get_videos()
    res = res['list']['vlist'][site]
    bvid = 'https://b23.tv/' + res['bvid']
    pic = res['pic']
    description = res['description']
    title = res['title']
    length = res['length']
    play = res['play']
    v = video.Video(res['bvid'])
    res = await v.get_info()
    res = res['stat']
    reply = str(res['reply'])
    danmaku = str(res['danmaku'])
    favorite = str(res['favorite'])
    coin = str(res['coin'])
    share = str(res['share'])
    like = str(res['like'])
    mess = '标题:' + title + '\n描述:' + description + '\n时长:' + str(length) + '\n播放量:' + str(
        play) + '\n点赞:' + like + '\n投币:' + coin + '\n收藏:' + favorite + '\n弹幕:' + danmaku + '\n分享:' + share + '\n评论:' + str(
        reply) + f'[CQ:image,file={pic}]' + bvid + '\n'
    mess = mess[:-1]
    return mess
