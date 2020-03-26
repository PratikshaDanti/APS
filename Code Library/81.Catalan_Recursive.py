# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:32:14 2020

@author: Pratiksha
"""

def catalan(n):
    if (n <= 1):
        return 1
    res = 0
    for i in range(0,n):
        res += catalan(i)*catalan(n-i-1)
    return res

n=int(input('Enter value of n : '))
x=catalan(n)
print('Result is :',x)