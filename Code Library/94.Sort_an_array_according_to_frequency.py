# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:13:46 2020

@author: Pratiksha
"""

li=list(map(str,input('Enter the array of words : ').split()))
dict={}
for i in li:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
l1=[]
for key, value in sorted(dict.items(), key=lambda item: item[1]):
    l1.append([key, value])
print(l1)
l=[]
for i in range(len(l1)):
    l.append(l1[i][0])
    
print(l)
