"""This is for testing new methods and functions"""

import json
import pprint
import time
from alive_progress import alive_bar


def pprint_test() -> None:
    """This is for testing pprint"""
    with open("file.json", "r", encoding="utf8") as f:
        data = json.load(f)

    print("\nThis is printed via print:\n")
    print(data)
    print("\nThis is printed via pprint:\n")
    pprint.pprint(data, width=20)


def alive_process() -> None:
    """This is for testing alive process"""
    for x in 1000, 1500, 700, 0:
        with alive_bar(x) as bar:
            for _ in range(1000):
                time.sleep(0.005)
                bar()


# pprint_test()
alive_process()

# TOOD: check more functions:  https://www.youtube.com/watch?v=zPfSwhofPpk
