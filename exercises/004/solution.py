# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:33:36 2015

@author: A
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowel = 'a', 'e', 'i', 'o', 'u'
rev = list(reversed(alphabet))
for x in range(len(rev)):
    if rev[x] in vowel:
        rev[x] = rev[x].capitalize()
print(*rev, sep='')
