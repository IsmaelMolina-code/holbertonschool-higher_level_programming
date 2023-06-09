#!/usr/bin/python3
""" Function that writes an Object to a text file,
    using a JSON representation """


def save_to_json_file(my_obj, filename):
    """ Protoype with the function
    that writes an Object to a text file,
    using a JSON representation """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
