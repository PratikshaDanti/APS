# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:04:46 2020

@author: Pratiksha
"""

s=str(input('Enter the string : '))
sm=ord(s[0])
if len(s)>1:
    for i in range(1,len(s)):
        sm=sm^ord(s[i])
print(sm)

