# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:05:03 2015

@author: A
"""
# import sys
from solution0 import love_meet
from solution0 import affair_meet
alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']
silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']
listecommune = []
listecommune = love_meet(alice, bob, listecommune)
print(listecommune)
listecommune = affair_meet(alice, bob, silvester, listecommune)
print(listecommune)
