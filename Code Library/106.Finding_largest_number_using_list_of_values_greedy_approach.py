# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:08:38 2020

@author: Pratiksha
"""

a=list(map(int,input('Enter list of numbers : ').split()))
l=[]
while(len(a)>0):
    x=max(a)
    l.append(x)
    a.remove(x)
    
print(l)