# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:47:04 2020

@author: Pratiksha
"""

arr1=list(map(int,input('Enter array 1 elements : ').split()))
arr2=list(map(int,input('Enter array 2 elements : ').split()))
arr1.sort()
arr2.sort()
l=[]
for i in range(len(arr1)):
    l.append(arr1[i]+arr2[i])
print(l)
    