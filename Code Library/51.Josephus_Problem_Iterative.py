# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:29:11 2020

@author: Pratiksha
"""

def Josephus(n,k):
    res=0
    for i in range(1,n+1):
        res=(res+k)%i
    print(res+1)
    
n,k=map(int,input('Enter n and k values : ').split())
Josephus(n,k)