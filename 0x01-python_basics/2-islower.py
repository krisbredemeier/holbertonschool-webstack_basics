#!/usr/bin/python3

'''Write a function that checks for lowercase character'''

def islower(c):
    '''check to see if letter is lowecase or not'''
    c =ord(c)
    if c >= 97 and c <= 122:
         return(True)
    return(False)
