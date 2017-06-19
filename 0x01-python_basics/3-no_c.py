#!/usr/bin/python3

'''Write a function that removes all c and C of a string
and return the new string.'''


def no_c(str):

    '''remove c and C'''
    without = ''
    for i in str:
        if i == 'c' or i == 'C':
            i = ""
        without += i
    return(without)

if __name__ == '__main__':
    no_c()
