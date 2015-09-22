# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:12:30 2015

@author: A
"""

import sys
liste = sys.argv
for x in range(len(liste)):
    r=list(enumerate(liste))[x]
    print(r[0],r[1])
