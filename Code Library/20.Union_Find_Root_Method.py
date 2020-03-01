# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:19:03 2020

@author: Pratiksha
"""
def root(arr,i) :
    if arr[i] != i :
        i=arr[i]
    return i
        
def union(a,b,arr):
    roota=root(arr,a)
    rootb=root(arr,b)
    arr[roota]=rootb
    print(arr)
    
def find(a,b):
    if root(arr,a) == root(arr,b) :
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