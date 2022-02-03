# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:51:19 2019

@author: kungk
"""

def fun(n):
 if (n > 100):
     return n - 5
 return fun(fun(n+11));
print(fun(45))