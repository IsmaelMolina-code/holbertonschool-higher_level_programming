#!/usr/bin/python3
""" Add all arguments to a Python list, and then save them to a file """


import sys

if __name__ == '__main__':
    save_to_json_f = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_f = __import__('6-load_from_json_file').load_from_json_file

    try:
        my_list = load_from_json_f("add_item.json")
    except FileNotFoundError:
        my_list = []
    save_to_json_f(my_list + sys.argv[1:], "add_item.json")
