# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:44:19 2020

@author: Pratiksha
"""
'''
t is test cases
n workers
next line has salary of workers

'''

t=int(input())

for i in range(t):
    c=0
    o=int(input())
    a=list(map(int,input().split()))
    m=min(a)
    for j in range(len(a)):
        c=c+(a[j]-m)
    print(c)

