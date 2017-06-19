#!/usr/bin/python3
import sys

'''Write a program that prints the number of
and the list of its arguments.'''


def numArgs():

    '''checks to see if there are more than 1 args'''
    arguments = "arguments"
    if len(sys.argv) < 1:
        print('{} {}'.format(0, arguments))
    else:
        print('{} {}:'.format(len(sys.argv) - 1, arguments))
        for arg in range(len(sys.argv)):
            if arg != 0:
                print('{}: {}'.format(arg, sys.argv[arg]))

if __name__ == '__main__':
    numArgs()
