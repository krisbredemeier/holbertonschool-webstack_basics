#!/usr/bin/python3
''' Write a function that finds the biggest integer of a list.'''


def max_integer(my_list=[]):
    '''If the list is empty, return None'''
    if len(my_list) <= 0:
        return None
    biggest = my_list[0]
    for i in range(0, len(my_list)):
        if biggest < my_list[i]:
            biggest = my_list[i]
    return(biggest)

if __name__ == '__main__':
    max_integer()
