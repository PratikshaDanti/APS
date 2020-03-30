# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:30:15 2020

@author: Pratiksha
"""

a=list(map(int,input('Enter the list : ').split()))
k=int(input('Enter value of k : '))
dict={}
l1=[]
for i in a:
    dict[i]=i%k
for key, value in sorted(dict.items(), key=lambda item: item[1]):
    l1.append([key, value])
for i in range(len(l1)):
    print(l1[i][0])