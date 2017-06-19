#!/usr/bin/python3

'''Write a function that deletes a key in a dictionary.'''


def simple_delete(my_dict, key=""):
    '''key argument will be always a string'''
    try:
        del my_dict[key]
    except:
        pass
    return(my_dict)

if __name__ == '__main__':
    simple_delete()
