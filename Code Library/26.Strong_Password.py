# -*- coding: utf-8 -*-
"""
The password is considered to be strong if it satisfies the following criteria:

Its length is at least 6 .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+

If password isn't strong return minimum number of characters to be added to make it strong.
"""

def minimumNumber(n, password):
    condition=[False,False,False,False,False]
    password=str(password)
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num="0123456789"
    spl="!@#$%^&*()-+"
    for i in range(n):
        if condition.count(True)==5:
            break
        if password[i] in lower:
            condition[2]=True
        elif password[i] in upper:
            condition[3]=True
        elif password[i] in spl:
            condition[4]=True
        elif password[i] in num:
            condition[1]=True
        elif n>=6:
            condition[0]=True
    x=condition.count(False)
    if condition[0]==False:
        if n+x-1>=6:
            return x-1
        else:
            return 6-n
    return x            

if __name__ == '__main__':
    password = input('Enter the password : ')
    n=len(password)
    answer = minimumNumber(n, password)
    print('Number of characters to be added to make it strong : ',answer)