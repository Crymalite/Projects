# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:39:08 2019

@author: kungk
"""

class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print("Hello")
    
ob=MyClass()

print(MyClass.func)

print(ob.func)

ob.func()