# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:50:27 2020

@author: Pratiksha
"""

def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a

a=list(map(int,input('Enter the elements to be sorted : ').split()))
a=bubbleSort(a)
print('After sorting, values are : ',a)