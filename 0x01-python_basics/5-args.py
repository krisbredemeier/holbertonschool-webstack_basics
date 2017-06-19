#!/usr/bin/python3
import sys

'''Write a program that prints the number of
and the list of its arguments.'''


def numArgs():

    '''checks to see if there are more than 1 args'''
    arguments = "arguments"
    argument = "argument"
    if len(sys.argv) < 2:
        print('{} {}.'.format(0, argument))
    elif len(sys.argv) == 2:
        print('{} {}:'.format(len(sys.argv) - 1, argument))
        for arg in range(len(sys.argv)):
            if arg != 0:
                print('{}: {}'.format(arg, sys.argv[arg]))
    else:
        print('{} {}:'.format(len(sys.argv) - 1, arguments))
        for arg in range(len(sys.argv)):
            if arg != 0:
                print('{}: {}'.format(arg, sys.argv[arg]))

if __name__ == '__main__':
    numArgs()
