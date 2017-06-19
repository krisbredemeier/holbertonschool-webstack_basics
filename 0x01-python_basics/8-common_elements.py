#!/usr/bin/python3

'''Write a function that returns a set
of common elements in two sets.'''


def common_elements(set_1, set_2):

    sets = []
    for element in set_1:
        if element in set_2:
            sets.append(element)
    return sets

if __name__ == '__main__':
    common_elements()
