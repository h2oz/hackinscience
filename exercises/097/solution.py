# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:56:19 2015

@author: A
"""


def love_meet(liste1, liste2):
    listecommune = list(set(liste1).intersection(liste2))
    listecommune.sort(key=lambda listecommune: listecommune[1])
    print(set(listecommune))


def affair_meet(liste1, liste2, liste3):
    listep = list(set(liste1) - set(liste2))
    listecommune = list(set(listep).intersection(liste3))
    print(set(listecommune))
