# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:05:40 2019

@author: kungk
"""

count=0
while(count<5):
    print(count)
    count+=1
else:
    print("count value reached %d"%(count))
    
for i in range(1,10):
   if(i%5==0):
       break
   print(i)
else:
    ("this is not printed because the loop is terminated because of break but not due to fail in condition")
    