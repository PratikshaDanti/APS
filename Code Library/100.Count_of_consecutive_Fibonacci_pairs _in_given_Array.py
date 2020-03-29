# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:50:49 2020

@author: Pratiksha
"""

fib=[]
fib.append(0)
fib.append(1)
for i in range(2,1000):
    fib.append(fib[i-1]+fib[i-2])
cnt=0
arr=list(map(int,input('Enter the array : ').split()))
for i in range(len(arr)-1):
    if arr[i] and arr[i+1] in fib:
        cnt+=1
print(cnt)