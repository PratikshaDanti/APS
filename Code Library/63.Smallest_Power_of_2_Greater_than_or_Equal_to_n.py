# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:52:01 2020

@author: Pratiksha
"""

def nextPowerOf2(n): 
    count = 0; 
    if (n and not(n & (n - 1))): 
        return n 
    while( n != 0): 
        n >>= 1
        count += 1
    return 1 << count; 
n = int(input('Enter the value :'))
print(nextPowerOf2(n)) 
