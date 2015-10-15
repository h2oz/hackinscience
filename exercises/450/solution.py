# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:18:09 2015

@author: A
"""


import string
al = list(string.ascii_lowercase)
AL = list(string.ascii_uppercase)


def forward(method):
    if method == 'forward':
        si = 1
    else:
        si = 1
    return(si)


def backward(method):
    if method == 'backward':
        si = -1
    else:
        si = 1
    return(si)


def caesar_cypher(s, key, method):
    sol = ''
    si = forward(method) * backward(method)
    for j in range(len(s)):
        x = s[j]
        if (x not in al) and (x not in AL):
            sol = sol + x
        for i in range(0, len(al)):
            if x == al[i]:
                sol = sol + (al[(i + (si * key)) % len(al)])
        for i in range(0, len(al)):
            if x == AL[i]:
                sol = sol + (AL[(i + (si * key)) % len(al)])
    print(sol)
    return()

if __name__ == '__main__':
    caesar_cypher('Python is super disco !', 31, 'backward')
