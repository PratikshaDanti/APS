# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:35:56 2020

@author: Pratiksha
"""

def insertionSort(a,n):
    for j in range(2,n):
        item=a[j]
        i=j-1
        while(i>=0 and item<a[i]):
            a[i+1]=a[i]
            i-=1
        a[i+1]=item
    return a

a=list(map(int,input('Enter the elements to be sorted : ').split()))
a=insertionSort(a,len(a))
print('Elements after sorting : ',a)