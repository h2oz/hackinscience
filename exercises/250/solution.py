# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:38:36 2015

@author: A
"""


def draw_n_squares(n):
    for k in range(n):
        for i in range(n):
            print('+---', end=""),
        print('+')
        for j in range(n):
            print('|   ', end=""),
        print('|')
    for i in range(n):
        print('+---', end=""),
    print('+')
    return ''

print(draw_n_squares(3))
