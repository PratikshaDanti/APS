# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:28:43 2020

@author: Pratiksha
"""

def find(a,l,s):
    for i in range(1,(pow(2,l))+1):
        sm=0
        for j in range(0,l):
            if (((i>>j)&1)&1):
                sm+=a[j]
            if sm==s:
                print('yes')
                return
    print('no')
    
sm=int(input('Enter value of sum : '))
a=list(map(int,input('Enter the array elements : ').split()))
find(a,n,sm)
        