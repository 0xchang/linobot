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
            '油馍头', '肉夹馍', '烧麦', '豆浆油条', '土豆饼', '锅贴', '混沌', '肠粉', '羊杂汤', '鱿鱼仔', '秘制咸鸭蛋',
            '九阳豆浆', '香菇鲜肉包', '涪陵榨菜')
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
            '酱焖黄花鱼', '红烧鸡肉', '辣炒肥肠', '清蒸大虾', '豆角炒肉', '白菜炖豆腐', '烧饼', '鸭锁骨', '虾条', '黑芝麻球')
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
            '酱焖黄花鱼', '红烧鸡肉', '辣炒肥肠', '清蒸大虾', '豆角炒肉', '白菜炖豆腐', '烧饼', '鸭锁骨', '虾条', '黑芝麻球')
    eat0 = random.choice(eats)
    eat1 = random.choice(eats)
    eat2 = random.choice(eats)
    eat = eat0 + ',' + eat1 + ',' + eat2
    mess = '你现在是想吃' + eat + '吗[CQ:face,id=66]'
    await eatwancmd.finish(Message(mess))


eatsgcmd = on_command('水果', priority=281)


@eatsgcmd.handle()
async def songer_handle():
    eats = ('苹果', '梨', '葡萄', '红提', '枣', '柑橘', '桃', '西瓜', '杏', '甜瓜', '香瓜', '荔枝', '甘蔗',
            '柿', '柠檬', '香蕉', '芒果', '菠萝', '哈密瓜', '李子', '石榴', '枸杞', '山楂', '椰子', '桑葚',
            '柚子', '草莓', '沙糖桔', '木瓜', '橙', '圣女果', '龙眼', '黄瓜', '枇杷', '山竹', '红毛丹', '无花果',
            '布朗', '杨桃', '人参果', '猕猴桃', '芭乐', '杨梅', '乌梅', '蓝莓', '西梅', '释迦', '百花果', '黄皮',
            '樱桃', '雪莲果', '榴莲', '火龙果', '番石榴', '菠萝蜜', '百香果', '罗汉果', '莲雾', '核桃', '板栗',
            '开心果', '瓜子', '榛子', '银杏', '松子', '果仁', '白果', '坚果', '果脯', '槟榔果', '腰果', '果汁',
            '果酒', '罐头', '果酱', '果干', '脱水水果', '果茶',)
    eat0 = random.choice(eats)
    eat1 = random.choice(eats)
    eat2 = random.choice(eats)
    eat = eat0 + ',' + eat1 + ',' + eat2
    mess = '你现在是想吃' + eat + '吗[CQ:face,id=66]'
    await eatsgcmd.finish(Message(mess))
