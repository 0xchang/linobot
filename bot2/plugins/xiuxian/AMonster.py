#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/2 22:48
@author: 0xchang
@E-mail: oxchang@163.com
@file: AMonster.py
@Github: https://github.com/0xchang
"""
import sqlite3


class Monster:
    def __init__(self, name: str):
        self.name = name
        self.attack = 0
        self.defense = 0
        self.HP = 0
        self.getSql()

    def getSql(self):
        con = sqlite3.connect('data/xiuxian.data')
        cur = con.cursor()
        cur.execute('select * from monsters where name=?', (self.name,))
        con.commit()
        val = cur.fetchall()
        _, self.HP, self.attack, self.defense = val[0]

    def getAttack(self) -> int:
        return self.attack

    def getHP(self) -> int:
        return self.HP

    def getDefense(self) -> int:
        return self.defense


class MonBoss:
    def __init__(self, name: str):
        self.name = name
        self.attack = 0
        self.defense = 0
        self.HP = 0
        self.getSql()

    def getSql(self):
        con = sqlite3.connect('data/xiuxian.data')
        cur = con.cursor()
        cur.execute('select * from monboss where name=?', (self.name,))
        con.commit()
        val = cur.fetchall()
        if val==[]:
            cur.execute('select * from highmonboss where name=?', (self.name,))
            con.commit()
            val = cur.fetchall()
        _1, self.HP, self.attack, self.defense, _2 = val[0]
        cur.close()
        con.close()

    def getAttack(self) -> int:
        return self.attack

    def getHP(self) -> int:
        return self.HP

    def getDefense(self) -> int:
        return self.defense


class GeRBoss:
    def __init__(self,name,attack,defense,HP):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.HP = HP

    def getAttack(self) -> int:
        return self.attack

    def getHP(self) -> int:
        return self.HP

    def getDefense(self) -> int:
        return self.defense