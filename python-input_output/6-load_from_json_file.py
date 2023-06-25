#!/usr/bin/python3
""" Function that creates an Object from a “JSON file‟ """


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file‟ """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
