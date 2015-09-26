# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:11:00 2015

@author: A
"""


def mul(liste):
    res = 1
    for x in range(len(liste)):
        res = res * liste[x]
    return res
