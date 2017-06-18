#!/usr/bin/python3

'''Write a program that prints the alphabet, in lowercase,
not followed by a new line.'''
for one in range(97, 123):
    if one != 101 and one != 113:
        print('{}'.format(chr(one)), end="")
