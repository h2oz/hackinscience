# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:05:03 2015

@author: A
"""
# import sys
from solution import love_meet
from solution import affair_meet
alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II', 'III', 'IX']
bob = ['IV', 'III', 'II', 'XX', 'II', 'XX', 'XXI', 'VI', 'IX']
silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']
love_meet(alice, bob)
affair_meet(alice, bob, silvester)
