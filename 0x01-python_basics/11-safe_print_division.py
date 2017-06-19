#!/usr/bin/python3

'''Write a function that divides 2 integers and prints the result.'''


def safe_print_division(a, b):
    try:
        (a / b)
    except:
        pass
    finally:
        print('Inside result: {}'.format)

if __name__ == '__main__':
    safe_print_division()
