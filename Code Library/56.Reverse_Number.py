# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:20:52 2020

@author: Pratiksha
"""

def reverse(n):
    rem=0
    reverse_num=0
    while(n!=0):
        rem=n%10
        reverse_num=reverse_num*10+rem
        n=n//10
    return reverse_num

n=int(input('Enter the number : '))
res=reverse(n)
print('Reversed number is : ',res)