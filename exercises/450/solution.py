# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:18:09 2015

@author: A
"""


import string
al = list(string.ascii_lowercase)
AL = list(string.ascii_uppercase)


def forward():
    return(1)


def backward():
    return(-1)


def caesar_cypher(s, key, method):
    sol = ''
    si = locals()["method"]()
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
    caesar_cypher('Python is super disco !', 31, forward)
