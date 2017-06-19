#!/usr/bin/python3

'''Write a function that divides 2 integers and prints the result.'''


def safe_print_division(a, b):
    try:
        division = (a / b)
    except ZeroDivisionError:
        division = None
    finally:
        print('Inside result: {}'.format(division))

if __name__ == '__main__':
    safe_print_division()
