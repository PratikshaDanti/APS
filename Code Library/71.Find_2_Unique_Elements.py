# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:01:56 2020

@author: Pratiksha

Let’s say this is our [2, 4, 3, 6, 3, 2, 5, 5] given array where two numbers are unique.
After performing XOR operation on each element in the array, 
it results in an output 4(100)^6(110)=2 (binary 10).
This means the second last bit of two unique numbers are different.
We can split the array into two sub-arrays.
 All the numbers having second last bit one forms one sub-array. 
 Keep the rest of the numbers in another sub-array.
Two sub-arrays after splitting: [4, 5, 5] and [2, 3, 6, 3, 2]
Find the unique number for each sub-array using the XOR operation. 
This will give us the desired output as 4 and 6.

"""

def findUnique(arr):
    out=0
    for i in arr:
        out=i^out
    return out
     
def createSubArray(arr, num):
    num=(-1)*num
    arr1=[]
    arr2=[]
    for i in arr:
        if "{0:b}".format(i)[num]=="0":
           arr1.append(i)
        else:
            arr2.append(i)
    return arr1, arr2
 
def findFirstBit1FromLast(num):
    strNum="{0:b}".format(num)
    for i in range(0, len(strNum)):
        if strNum[len(strNum)-1-i]=="1":
            return i+1
     
 
arr=list(map(int,input('Enter the array elements : ').split()))
temp=findUnique(arr)
bitLoc=findFirstBit1FromLast(temp)
arr1, arr2=createSubArray(arr, bitLoc)
print(findUnique(arr1))
print(findUnique(arr2))