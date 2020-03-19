# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:33:38 2020

@author: Pratiksha
"""


a,b=map(int,input('Enter the range : ').split())
print('Prime numbers are :',end=' ')
for i in range(a,b+1):
    f=0
    for j in range(2,i//2+1):
        if i%2==0:
            f=1
            break
    if f==0:
        print(i,end=' ')