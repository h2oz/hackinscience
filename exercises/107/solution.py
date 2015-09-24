# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 01:26:52 2015

@author: A
"""


def select_student(liste, note):
    # liste = [['Kermit Wade', 27], ['Hattie Schleusner', 67],\
    # ['Ben Ball', 5], ['William Lee', 2]]
    # note = 20
    temp1 = []
    temp2 = []
    pas = {}
    sorted(liste, key=lambda student: student[1])
    for i in range(len(liste)):
        if (liste[i])[1] >= note:
            temp1.append(liste[i])
        else:
            temp2.append(liste[i])
    pas['Accepted'] = temp1
    pas['Refused'] = temp2
    print(pas)
