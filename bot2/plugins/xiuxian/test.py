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

res1 = json.load(open('weapon_init.json', 'r', encoding='utf8'))
res2 = json.load(open('herbs_init.json', 'r', encoding='utf8'))
res3 = json.load(open('ore_init.json', 'r', encoding='utf-8'))
# print(res)
s1 = set()
s2 = set()
sn = set()
for i in res1:
    materials = i['materials']
    materials = materials.split()
    sn.add(i['name'])
    for m in materials:
        s1.add(m)
for i in res2:
    s2.add(i['name'])
# with open('drug_init.json','w',encoding='utf-8') as f:
# f.write(res)

# print(s1)
# print(s2)
# print(sn)
# print(s1 & s2)
r = []
id = 1100
for i in s1:
    if i in s1 & s2 or i in sn:
        continue
    else:
        d = {
            "id": id,
            "name": i,
            "description": "一种营养丰富、药用价值极高的珍贵食材，具有增强身体灵气、滋补身体等功效。"
        }
        r.append(d)
        id += 1

for i in res3:
    if i['id'] % 8 == 0:
        print('给出', end='')
    print(f'{i["name"]}', end=',')
    if (i['id'] + 1) % 8 == 0:
        print('材料的描述')
