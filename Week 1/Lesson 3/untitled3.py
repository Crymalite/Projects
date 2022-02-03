# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:50:54 2019

@author: kungk
"""

def scope_test():
    def do_local():
        spam = "local spam"
        
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        
    def do_global():
        global spam
        spam = "global spam"
        
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlogical assignment:", spam)
    do_global()
    print("After global assignment:", spam)
    
scope_test()
print("global scope:", spam)