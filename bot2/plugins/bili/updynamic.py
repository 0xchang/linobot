#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 9:49
@author: 0xchang
@E-mail: oxchang@163.com
@file: updynamic.py
@Github: https://github.com/0xchang
"""

# 获取up动态信息并进行解析
from bilibili_api import user


async def dyn(uid: int, name: str, top: bool) -> (int, int, str):
    u = user.User(uid)
    res = await u.get_dynamics(0, top)
    contype = res['cards'][0]['desc']['type']
    mess = f'{name}发布了新动态,大家快去瞅瞅\n'
    if contype == 1:
        mess = mess + '如果我没猜错的话，这好像是一个投票捏，快去看看喵\n' + 'https://t.bilibili.com/' + str(
            res['cards'][0]['desc']['dynamic_id'])
        return contype, res['cards'][0]['desc']['timestamp'], mess
    elif contype == 2:
        desccripton = res['cards'][0]['card']['item']['description']
        mess += desccripton + '\n'
        for pic in res['cards'][0]['card']['item']['pictures']:
            pic = pic['img_src']
            mess += f'[CQ:image,file={pic}]'
    elif contype == 4:
        mess += res['cards'][0]['card']['item']['content']
    elif contype == 8:
        mess += res['cards'][0]['card']['title']
        mess += '[CQ:image,file={}]'.format(res['cards'][0]['card']['pic'])
        mess += '这是一条视频哦!快去看喵!{}'.format(res['cards'][0]['card'].get('short_link'))
        return contype, res['cards'][0]['desc']['timestamp'], mess
    mess += '\nhttps://t.bilibili.com/' + str(res['cards'][0]['desc']['dynamic_id'])
    return contype, res['cards'][0]['desc']['timestamp'], mess
