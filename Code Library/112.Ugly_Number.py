# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:02:26 2020

@author: Pratiksha

a number is ugly whose prime factors only include 2,3,5

"""

def isUgly(num):
    while(num>1):
        if num%2==0:
            num=num//2
        elif num%3==0:
            num=num//3
        elif num%5==0:
            num=num//5
        else:
            break
    if num!=1:
        return False
    else:
        return True