# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:39:23 2020

@author: Pratiksha
"""
import math
n=int(input('Enter the number : '))

if n==0:
    print('Number of digits in the number are : ',1)
else:
    d=math.floor(math.log10(n)+1)
    print('Number of digits in the number are : ',d)