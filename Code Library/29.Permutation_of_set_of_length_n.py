# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 07:31:12 2020

@author: Pratiksha
"""

def Perm(arr,k,n):
    if k==n:
        print(arr[0:n])
    else:
        for i in range(k,n):
            arr[k],arr[i]=arr[i],arr[k]
            Perm(arr,k+1,n)
            arr[k],arr[i]=arr[i],arr[k]

print("Enter the values : ")
arr=list(map(str,input().split()))
Perm(arr,0,len(arr))
