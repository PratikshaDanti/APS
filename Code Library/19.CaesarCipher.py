# -*- coding: utf-8 -*-
"""
 Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

"""

def caesarCipher(s, k):
    k=k%26
    st=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Lfirst = st[0 : k] 
    Lsecond = st[k :]
    enc=''
    st1=Lsecond+Lfirst
    for i in range(len(s)):
        f=0
        try : 
            if s[i].isupper():
                f=1
            p=s[i].lower()
            x=st.index(p)
            if f==1:
                val=st1[x].upper()
                enc=enc+val
            else:
                enc=enc+st1[x]
        except ValueError :
            enc=enc+s[i] 
    return(enc)

if __name__ == '__main__':
    s=str(input('Enter the string : '))
    k=int(input('Number of rotations : '))
    x=caesarCipher(s,k)
    print('Encrypted string : ',x)
    