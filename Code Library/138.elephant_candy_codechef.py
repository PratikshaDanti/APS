# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:27:40 2020

@author: Pratiksha
"""

'''
N elephants
each elephant is happy if it recieves ak candies
C candies in total
T is no. of test cases
first line N C 
second line a1,a2.....an
output Yes or No

2
2 3
1 1
3 7
4 2 2
'''
t=int(input())
for i in range(t):
    n,c= map(int, input().split())
    a=list(map(int,input().split()))
    for j in a:
        c=c-j
    if c<0:
        print('No')
    else:
        print('Yes')
        
        

    