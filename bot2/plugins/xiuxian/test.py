#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/3/16 12:02
@author: 0xchang
@E-mail: oxchang@163.com
@file: test.py
@Github: https://github.com/0xchang
"""
import json

stones = {
    "火之石": "一种能够提升火属性攻击力的特殊石头。",
    "水之石": "一种能够提升水属性攻击力的特殊石头。",
    "雷之石": "一种能够提升电属性攻击力的特殊石头。",
    "叶之石": "一种能够提升草属性攻击力的特殊石头。",
    "月之石": "一种神秘的石头，能够强化攻击速度。",
    "太阳之石": "一种能够提升阳光属性攻击力的特殊石头。",
    "光之石": "一种能够提升辉光属性攻击力的特殊石头。",
    "冰之石": "一种能够提升冰属性攻击力的特殊石头。",
    "灵魂之石": "一种能够提升黑暗属性攻击力的特殊石头。",
    "坚硬之石": "一种能够提升物理防御力的特殊石头。"
}
count=10
k=list(stones.keys())
v=list(stones.values())
index=0
a=[]
for i in range(500, 530):
    count+=100
    if (i + 1) % 3 == 0:
        g = '劣质'
    if (i + 1) % 3 == 1:
        g = '普通'
    if (i + 1) % 3 == 2:
        g = '完美'
    d = {
        "id": i,
        "name": k[index],
        "grade": g,
        "level ": (i + 1) % 3+ 1,
        "effect": "attack",
        "amount": int(count/1.1),
        "description": v[index]
    }
    a.append(d)
    if (i+1)%3==2:
        index += 1

#json.dump(a,open('evolve_init.json','w',encoding='utf-8'),ensure_ascii=False)
for i in a:
    print(i)