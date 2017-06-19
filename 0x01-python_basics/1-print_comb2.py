#!/usr/bin/python3

'''Write a program that prints numbers from 0 to 99'''

for number in range(0, 100):
    if number == 99:
        print('99')
    else:
        print('{}'.format(str(number)).zfill(2), '', sep=", ", end="")
