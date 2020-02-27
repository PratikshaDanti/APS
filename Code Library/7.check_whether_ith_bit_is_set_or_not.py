# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:33:27 2020

@author: Pratiksha
"""

n=int(input('Enter the number : '))
i=int(input('Enter the bit to be checked : '))
c=n & ( 1 << i)

if c == 0:
    print('Bit is not set')
else:
    print('Bit is set')