# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:15:36 2020

@author: Pratiksha
"""

n=int(input('Enter n : '))
a=list(map(int,input('Enter the values : ').split()))
for j in range(0,n+1):
    for i in range(0,n-1):
        a[i],a[i+1]=a[i+1],a[i]
        for k in range(0,n):
            print(a[k],end=' ')
        print('\n')