# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:33:36 2015

@author: A
"""
# import operator
from solution import sort_a_list
from solution import sort_by_mark
from solution import sort_by_name
liste = [1, 3, 2, 4, 6, 5, 9, 7]
liste2 =\
 [[6, 'Joshua Tran'], [37, 'Jeanette Wafer'], [85, 'Susan Maddox'],
  [84, 'Joseph Pedersen'], [12, 'Bonnie Torres'], [36, 'John Freeman'],
  [27, 'Betty Askins'], [22, 'Mark Osbourne'], [42, 'Lidia Robel']]
# operator.itemgetter(2)(liste2)
sort_a_list(liste)
print(liste)
sort_by_mark(liste2)
print(liste2)
sort_by_name(liste2)
print(liste2)
