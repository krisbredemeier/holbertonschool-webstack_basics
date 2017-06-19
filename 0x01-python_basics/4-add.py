#!/usr/bin/python3
# from add_4.py import add(a, b)
this = __import__('add_4')
'''program imports function from file'''

def addThem():
    a = 1
    b = 2
    print('{} + {} = {}'(a, b, this(a, b)))
