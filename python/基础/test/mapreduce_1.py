#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce

def str2int(s):
    def fn(x,y):
        return x*10+y

    def char2num(c):
        return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}[c]

    return reduce(fn,map(char2num,s))

