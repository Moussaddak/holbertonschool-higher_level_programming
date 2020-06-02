#!/usr/bin/python3
''' Documentation of Class MyList'''


class MyList(list):
    ''' Mylist is subclass of list class'''
    def print_sorted(self):
        '''  prints the list, but sorted '''
        list = self[:]
        list.sort()
        print(list)
