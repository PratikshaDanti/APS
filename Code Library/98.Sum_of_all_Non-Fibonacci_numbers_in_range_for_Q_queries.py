# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:30:54 2020

@author: Pratiksha
"""
fib=[]
fib.append(0)
fib.append(1)
for i in range(2,1000):
    fib.append(fib[i-1]+fib[i-2])

a,b=map(int,input('Enter the range : ').split())
a1=a-1
sm=(a1*(a1+1))/2
sm1=(b*(b+1))/2
sm2=sm1-sm

for i in range(a,b+1):
    if i in fib:
        sm2-=i
print('Sum of all Non-Fibonacci numbers in a range for Q queries : ',sm2)