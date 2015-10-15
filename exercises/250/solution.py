# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:38:36 2015

@author: A
"""


# def draw_n_squares(n):
#    for k in range(n):
#        for i in range(n):
#            print('+---', end=""),
#        print('+')
#        for j in range(n):
#            print('|   ', end=""),
#        print('|')
#    for i in range(n):
#        print('+---', end=""),
#    print('+')
#    return ''
#
# print(draw_n_squares(3))


def draw_n_squares(n):
    draw = []
    for i in range(0, n):
        draw.append('+---'*n + '+')
        draw.append('|   '*n + '|')
    draw.append('+---'*n + '+')
    return '\n'.join(str(item) for item in draw)

# print(draw_n_squares(3))
