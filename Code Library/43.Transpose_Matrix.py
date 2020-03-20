# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:53:42 2020

@author: Pratiksha
"""

def transposeMatrix(a,n):
    for i in range(n):
        for j in range(i+1,n):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    return a
            
n=int(input('Enter the dimension of square matrix : '))
a=[]
l=[]
print('Enter the array elements : ')
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)

a=transposeMatrix(a,n)
print('After transpose : ')
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print("\n")
    