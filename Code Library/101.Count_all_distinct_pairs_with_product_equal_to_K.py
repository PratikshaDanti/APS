# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:57:28 2020

@author: Pratiksha
"""

arr=list(map(int,input('Enter the array : ').split()))
k=int(input('Enter value of k : '))
ctr=0
for i in arr:
    if k/i in arr:
        ctr+=1
        
print(int(ctr/2))