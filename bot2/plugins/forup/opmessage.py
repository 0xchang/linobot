#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/19 10:35
@author: 0xchang
@E-mail: oxchang@163.com
@file: opmessage.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11 import Event

def op_mess(event:Event,uid:str):
    if not uid.isdigit():
        return None
    else:
        uid = int(uid)
        mtype = event.message_type
        if mtype == 'group':
            qqid = event.group_id
        elif mtype == 'private':
            qqid = event.user_id
    return (uid,mtype,qqid)