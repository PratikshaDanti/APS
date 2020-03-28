# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:59:19 2020

@author: Pratiksha

Given a String str, the task is to check the sum of ASCII values of all characters
in this string is a perfect cube or not.
"""

def is_perfect_cube(number):
    number = abs(number)
    return round(number ** (1 / 3)) ** 3 == number

s=str(input('Enter the string : '))
sm=0
for i in s:
    sm=sm+ord(i)

res=is_perfect_cube(sm)
if res:
    print('YES')
else:
    print('NO')
    