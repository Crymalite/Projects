# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:35:09 2019

@author: kungk
"""

class Dog:
    kind = 'canine'
    
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
        