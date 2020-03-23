# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:27:17 2020

@author: Pratiksha
"""

def print_Kaprekar_nums(start, end):
    for i in range(start, end + 1):
        if i==1:
            print(i)
        sqr = i ** 2
        digits = str(sqr)
        length = len(digits)
        for x in range(1, length):
            left = int("".join(digits[:x]))
            right = int("".join(digits[x:]))
            if (left + right) == i:
                if i%10!=0 :
                    print(i)

p,q=map(int,input('Enter the range : ').split())
print_Kaprekar_nums(p,q)
