# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:34:43 2020

@author: Pratiksha
"""

q=int(input('Enter number of test cases : '))
for _ in range(q):
    n=int(input('Enter value of n : '))
    sm=1
    for i in range(1,n+1):
        sm=sm*i
    sm=(str(sm))
    val=0
    for i in range(len(sm)):
        val+=int(sm[i])
    print('Sum of digits is :',val)
