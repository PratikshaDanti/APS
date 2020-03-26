# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:20:18 2020

@author: Pratiksha
"""

a=list(map(str,input('Enter the array of characters : ').split()))
n=len(a)
for i in range(0,(1<<n)):
    for j in range(0,n):
        if i&(1<<j):
            print(a[j],end='')
    print('\n')