# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:24:30 2020

@author: Pratiksha
"""

n=int(input('Enter the number of queries : '))
l=[]
for i in range(n):
    a,b=map(int,input('Enter the pair : ').split())
    l.append([a,b])
k=int(input('Enter value of k : '))
for i in range(len(l)):
    if k in range(l[i][0],l[i][1]+1):
        print(l[i][0],l[i][1])