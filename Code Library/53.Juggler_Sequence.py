# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:56:18 2020

@author: Pratiksha
"""
from math import floor,sqrt
def Juggler(n):
    a=n
    print(a,end=' ')
    while(a!=1):
        b=0
        if a%2 == 0:
            b=floor(sqrt(a))
        else:
            b=floor(sqrt(a)*sqrt(a)*sqrt(a))
        print(b,end=' ')
        a=b

n=int(input('Enter value of n :'))
Juggler(n)