#!/usr/bin/python3
# from add_4.py import add(a, b)
add = __import__('add_4').add
'''program imports function from file'''

def addThem():
    ''' uses imported fuction to add variables'''
    a = 1
    b = 2
    print('{} + {} = {}'.format(a, b, add(a, b)))

if __name__ == '__main__':
    addThem()
