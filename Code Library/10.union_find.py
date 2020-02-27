# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:48:02 2020

@author: Pratiksha
"""
def union(a,b,arr):
    var=arr[a]
    for i in range(len(arr)):
        if arr[i]==var:
            arr[i]=arr[b]
    print(arr)
    
def find(a,b):
    if arr[a]==arr[b]:
        print(True)
    else:
        print(False)
    
arr=list(map(int,input('Enter the elements of array : ').split()))
n=1
while(n!=3):
    print('1. Union\t2. Find\t3. Exit\n')
    n=int(input('Enter the choice : '))
    if n==1:
        a,b=map(int,input('Enter the values : ').split())
        union(a,b,arr)
    if n==2:
        a,b=map(int,input('Enter the values : ').split())
        find(a,b)