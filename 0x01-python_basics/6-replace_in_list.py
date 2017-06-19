#!/usr/bin/python3

'''Write a function that replaces an element
of a list at a specific position.'''


def replace_in_list(my_list, idx, element):

    ''' If idx is out of range, the function should not modify anything,
     and returns the original list'''
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = element
    return(my_list)

if __name__ == '__main__':
    replace_in_list()
