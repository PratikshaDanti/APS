# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:28:53 2020

@author: Pratiksha
"""

def binaryPallindrome(num): 
     binary = bin(num) 
     binary = binary[2:] 
     return binary == binary[-1::-1] 
  
if __name__ == "__main__": 
    num = int(input('Enter the number : '))
    print(binaryPallindrome(num))