# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:56:19 2015

@author: A
"""


def love_meet(liste1, liste2, listecommune):
    listecommune = list(set(liste1).intersection(liste2))
    listecommune.sort(key=lambda listecommune: listecommune[1])
    return(listecommune)


def affair_meet(liste1, liste2, liste3, listecommune):
    listep = list(set(liste1) - set(liste2))
    listecommune = list(set(listep).intersection(liste3))
    return(listecommune)
