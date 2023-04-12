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

res = json.load(open('drug_init.json', 'r', encoding='utf8'))
a = set()
for r in res:
    for s in r.get('materials').split():
        # print(s)
        a.add(s)

count = 3000

q='''龙鳞战甲

魔法长袍

钢铁盔甲

火焰护甲

寒冰铠甲

神圣铠甲

暗影盔甲

地狱之衣

萨满外套

火花护甲

冰川战甲

狂野兽皮

魔法护甲

巨人铠甲

黑暗外衣

水晶盾甲

奥术长袍

银月战甲

圣光铠甲

风暴斗篷'''.split()
index=0
for a1 in range(len(q)):
    out = {
        "id": count,
        "name": f"{q[index]}",
        "materials": "",
        "description": "",
        "effect": "defense",
        "amount": 1,
        "multiple": 1.01
    }
    # print(out)
    out = json.dumps(out, ensure_ascii=False)
    out = out + ','
    print(out)
    count += 1
    index+=1
