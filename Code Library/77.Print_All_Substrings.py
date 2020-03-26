# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:09:53 2020

@author: Pratiksha
"""

def compute(a,n):
    for l in range(1,n+1):
        for i in range(0,(n-l)+1):
            j=i+l-1
            for k in range(i,j+1):
                print(a[k],end='')
            print("\n")

s=str(input('Enter the string : '))
s=list(s)
compute(s,len(s))