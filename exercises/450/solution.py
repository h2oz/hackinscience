# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:18:09 2015

@author: A
"""


import string
al = list(string.ascii_lowercase)
AL = list(string.ascii_uppercase)


def caesar_cypher(s, key, method):
    sol = ''
    if method == 'forward':
        si = 1
    if method == 'backward':
        si = -1
    for j in range(len(s)):
        x = s[j]
        for i in range(0, len(al)):
            if x == al[i]:
                sol = sol + (al[(i + (si * key)) % len(al)])
        for i in range(0, len(al)):
            if x == AL[i]:
                sol = sol + (al[(i + (si * key)) % len(al)])
    print(sol)
    return()

if __name__ == '__main__':
    caesar_cypher('bol', 1, 'backward')
