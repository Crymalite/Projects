# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:14:43 2019

@author: kungk
"""

while True:
    reply = raw_input('Enter text, [type "stop" to quit]: ')
    print reply.lower()
    if reply == 'stop':
        break