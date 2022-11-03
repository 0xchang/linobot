#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/3 20:20
@author: 0xchang
@E-mail: oxchang@163.com
@file: whateat.py
@Github: https://github.com/0xchang
"""
import random

from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command

eatzaocmd = on_command('早饭', priority=281)


@eatzaocmd.handle()
async def songer_handle():
    eats = ('煎饼果子', '水煎包', '皮蛋瘦肉粥', '咸鸭粥', '胡辣汤', '炸糖糕', '炸菜角', '鸡蛋灌饼', '灌汤包', '咸豆腐脑', '菜盒',
            '油馍头', '肉夹馍', '烧麦', '豆浆油条', '土豆饼', '锅贴', '混沌', '肠粉', '羊杂汤')
    eat0 = random.choice(eats)
    eat1 = random.choice(eats)
    eat2 = random.choice(eats)
    eat = eat0 + ',' + eat1 + ',' + eat2
    mess = '你现在是想吃' + eat + '吗[CQ:face,id=66]'
    await eatzaocmd.finish(Message(mess))


eatwucmd = on_command('午饭', priority=281)


@eatwucmd.handle()
async def songer_handle():
    eats = ('咸烧白', '可乐鸡翅', '京酱肉丝', '梅菜扣肉', '锅包肉', '混沌', '鱼香肉丝', '毛血旺', '烤鸭',
            '番茄炒蛋', '糖醋里脊', '红烧肉', '红烧排骨', '粉蒸排骨', '粉蒸牛肉', '清蒸鱼', '白灼生菜', '小鸡炖蘑菇',
            '小葱拌豆腐', '红烧鸡翅', '清炖羊肉', '清炒西兰花', '香菇肉片', '猪肚炖鸡', '蒜末炒肉', '蒜蓉炒油麦菜', '腊肉炒豆角',
            '酱焖黄花鱼', '红烧鸡肉', '辣炒肥肠', '清蒸大虾', '豆角炒肉', '白菜炖豆腐')
    eat0 = random.choice(eats)
    eat1 = random.choice(eats)
    eat2 = random.choice(eats)
    eat = eat0 + ',' + eat1 + ',' + eat2
    mess = '你现在是想吃' + eat + '吗[CQ:face,id=66]'
    await eatwucmd.finish(Message(mess))


eatwancmd = on_command('晚饭', priority=281)


@eatwancmd.handle()
async def songer_handle():
    eats = ('咸烧白', '可乐鸡翅', '京酱肉丝', '梅菜扣肉', '锅包肉', '混沌', '鱼香肉丝', '毛血旺', '烤鸭',
            '番茄炒蛋', '糖醋里脊', '红烧肉', '红烧排骨', '粉蒸排骨', '粉蒸牛肉', '清蒸鱼', '白灼生菜', '小鸡炖蘑菇',
            '小葱拌豆腐', '红烧鸡翅', '清炖羊肉', '清炒西兰花', '香菇肉片', '猪肚炖鸡', '蒜末炒肉', '蒜蓉炒油麦菜', '腊肉炒豆角',
            '酱焖黄花鱼', '红烧鸡肉', '辣炒肥肠', '清蒸大虾', '豆角炒肉', '白菜炖豆腐')
    eat0 = random.choice(eats)
    eat1 = random.choice(eats)
    eat2 = random.choice(eats)
    eat = eat0 + ',' + eat1 + ',' + eat2
    mess = '你现在是想吃' + eat + '吗[CQ:face,id=66]'
    await eatwancmd.finish(Message(mess))
