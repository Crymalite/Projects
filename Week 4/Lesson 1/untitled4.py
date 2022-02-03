# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 12:43:44 2019

@author: kungk
"""

def f(t):
    return t**2+11
def computation(result):
    result += result**2
    return result
def g(t):
    z = 0
    y = f(t)
    for x in range(y/2):
        z += computation(x)
        return z
print g(3)