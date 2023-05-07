#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/5/7 0:19
@author: 0xchang
@E-mail: oxchang@163.com
@file: petdbs.py
@Github: https://github.com/0xchang
"""
from peewee import *

petsdb = SqliteDatabase('data/pets.db', thread_safe=True)


class Pets(Model):
    uid = IntegerField(unique=True,primary_key=True)
    name = CharField(max_length=25)
    pet_type = CharField(max_length=20)
    coins = IntegerField(default=100)
    hunger = IntegerField(default=100)
    thirst = IntegerField(default=100)
    happiness = IntegerField(default=100)
    exp = IntegerField(default=0)
    level = IntegerField(default=1)

    class Meta:
        database = petsdb


def petlive(pet: Pets) -> bool:
    if pet.thirst > 0 and pet.hunger > 0 and pet.happiness > 0:
        return True
    return False
