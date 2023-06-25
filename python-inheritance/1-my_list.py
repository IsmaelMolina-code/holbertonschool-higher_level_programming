#!/usr/bin/python3
""" MyList class """


class MyList(list):
    """ Public instance method that prints the list, but sorted (ascending sort) """
    def print_sorted(self):
        print(sorted(self))
