#!/usr/bin/python3
add = __import__("add_4").add
'''program imports function from file'''


def addThem():

    ''' uses imported fuction to add variables'''
    a = 1
    b = 2
    print('{} + {} = {}'.format(a, b, add(a, b)))

if __name__ == '__main__':
    addThem()
