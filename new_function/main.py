"""This is for testing new methods and functions"""

import json
import pprint


def pprint_test() -> None:
    """This is for testing pprint"""
    with open("file.json", "r", encoding="utf8") as f:
        data = json.load(f)

    print("\nThis is printed via print:\n")
    print(data)
    print("\nThis is printed via pprint:\n")
    pprint.pprint(data, width=20)


pprint_test()

# TOOD: check more functions:  https://www.youtube.com/watch?v=zPfSwhofPpk
