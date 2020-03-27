# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:38:42 2020

@author: Pratiksha
"""

def binarySearch(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found   
arr = list(map(int,input('Enter the values to be sorted : ').split())) 
x = int(input('Enter element to be searched : '))
result = binarySearch(arr, x) 
if result: 
    print ("Element is present" )
else: 
    print ("Element is not present in array")
