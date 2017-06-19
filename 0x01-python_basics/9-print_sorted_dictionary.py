#!/usr/bin/python3

'''Write a function that prints a dictionary by ordered keys.'''


def print_sorted_dictionary(my_dict):
    for key, value in sorted(my_dict.items()):
        print('{} : {}'.format(key, value))


if __name__ == '__main__':
    print_sorted_dictionary()
