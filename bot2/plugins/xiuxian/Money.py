#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/8 19:38
@author: 0xchang
@E-mail: oxchang@163.com
@file: Money.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.params import CommandArg
from nonebot import on_command, on_fullmatch
from bot2.plugins.xiuxian.Role import XianRole
from bot2.plugins.xiuxian.Bank import BpushGold, BpopGold, BgetInfo, BnewInfo, BchangeGold, BdelInfo

Bgetinfo = on_fullmatch('查钱')


@Bgetinfo.handle()
async def bgetinfo_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid)
    res = BgetInfo(u)
    if res == []:
        mess = '你好像没有在这个银行开户'
    else:
        res = res[0]
        mess = f'你的银行余额为{res[1]}灵石!'
    del u
    await Bgetinfo.finish(Message(mess))


Bnewinfo = on_fullmatch('开户')


@Bnewinfo.handle()
async def Bnewinfo_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid)
    name = u.getName()
    if BnewInfo(u):
        mess = f'{name}恭喜你开户成功!'
    else:
        mess = f'{name}开户失败，是不是已经开户了呢!'
    del u
    await Bnewinfo.finish(Message(mess))


Bdelinfo = on_fullmatch('销户')


@Bdelinfo.handle()
async def Bdelinfo_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid)
    if BdelInfo(u):
        mess = '销户成功,你的银行余额全部清空!'
    else:
        mess = '销户失败，你是不是没有开户呢!'

    del u
    await Bdelinfo.finish(Message(mess))


Bpushgold = on_command('存钱')


@Bpushgold.handle()
async def bpushgold_handle(event: GroupMessageEvent, argcom: Message = CommandArg()):
    uid = event.get_user_id()
    argcom = argcom.extract_plain_text()
    if not argcom.isdigit():
        return
    gold = int(argcom)
    u = XianRole(uid)
    name = u.getName()
    if BpushGold(u, gold):
        mess = f'{name}成功存灵石{gold}!'
    else:
        mess = f'{name}存灵石失败,没有银行账户或者身上灵石不足'

    del u
    await Bpushgold.finish((Message(mess)))


Bpopgold = on_command('取钱')


@Bpopgold.handle()
async def bpopgold_handle(event: GroupMessageEvent, argcom: Message = CommandArg()):
    uid = event.get_user_id()
    argcom = argcom.extract_plain_text()
    if not argcom.isdigit():
        return
    gold = int(argcom)
    u = XianRole(uid)
    name = u.getName()
    if BpopGold(u, gold):
        mess = f'{name}取灵石{gold}成功!'
    else:
        mess = f'{name}取灵石失败,应该是银行余额不足，或者你没有开户'

    del u
    await Bpopgold.finish(Message(mess))


Bchangegold = on_command('转账')


@Bchangegold.handle()
async def Bchangegold_handle(event: GroupMessageEvent, argcom: Message = CommandArg()):
    uid1 = event.get_user_id()
    uid2 = argcom[0].get('data').get('qq')
    if uid1==uid2:
        await Bchangegold.finish(Message('不能给自己转账哦!'))
    gold = argcom.extract_plain_text()
    gold=gold.strip()
    if not gold.isdigit():
        return
    gold = int(gold)
    u1 = XianRole(uid1)
    u2 = XianRole(uid2)
    if BchangeGold(u1, u2, gold):
        mess = f'{u1.getName()}成功向{u2.getName()}转账了{gold}灵石,请在钱庄查看余额!'
    else:
        mess = f'转账失败:\n1.你没有开户\n2.对方没有开户\n3.你的钱庄余额不足'
    del u1
    del u2
    await Bchangegold.finish(Message(mess))
