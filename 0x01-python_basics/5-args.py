#!/usr/bin/python3
import sys

'''Write a program that prints the number of
and the list of its arguments.'''

for arg in sys.argv:
    if len(sys.argv) > 1:
        print(arg)
    else:
        print('0 Arguments')
