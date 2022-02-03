# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 11:33:20 2019

@author: kungk
"""

def aWhile():
    x = True
    count = 0
    while(x==True):
        count += 1
        print "Looped ", count, " times."
        if count == 21:
            x = False
            print "break"
aWhile()
