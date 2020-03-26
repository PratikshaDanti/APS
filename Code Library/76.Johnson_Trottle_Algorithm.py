# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:03:56 2020

@author: Pratiksha
"""

def compute(a,l,r):
    if l==r:
        p=''
        for x in range(len(a)):
            p=p+a[x]
        print(p)
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            compute(a,l+1,r)
            a[l],a[i]=a[i],a[l]
            
s=str(input('Enter the string : '))
s=list(s)
n=len(s)
compute(s,0,n-1)