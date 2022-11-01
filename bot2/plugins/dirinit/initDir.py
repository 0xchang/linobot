#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/31 21:27
@author: 0xchang
@E-mail: oxchang@163.com
@file: initDir.py
@Github: https://github.com/0xchang
"""
import os
def mk(path:str):
    if not os.path.exists('data'):
        os.mkdir(path)
    print(f'Init {path} OK!')

mk('data')
mk('img')