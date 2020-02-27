# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:04:56 2020

@author: Pratiksha
"""

arr=list(map(int,input('Enter the elements : ').split()))
LIS=[]
for i in range(len(arr)):
    LIS.append(1)
    
for i in range(len(arr)):
    for j in range(0,i):
        if arr[i] > arr[j] and LIS[j]+1 > LIS[i]:
            LIS[i] = LIS[j]+1
            
print('Length of Longest Increasing Subsequence is : ',max(LIS))
print(LIS)