#!/usr/bin/python3



def write_file(filename="", text=""):
    chars = 0
    for chars in range(len(text)):
        chars += 1
    with open(filename, "w") as f:
        f.write(text)
        return chars
