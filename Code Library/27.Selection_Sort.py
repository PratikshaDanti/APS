# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 06:43:19 2020

@author: Pratiksha
"""
a=list(map(int,input('Enter the array elements : ').split()))
for i in range(len(a)):
    min_idx=i
    for j in range(i+1,len(a)):
        if a[min_idx]>a[j]:
            min_idx=j
    a[i],a[min_idx]=a[min_idx],a[i]
print('Array after sorting is : ',a)