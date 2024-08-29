import pytest
import sys
import os

sys.path.append(
    os.path.abspath("/Users/mateuszormianek/Desktop/Programming/PythonFun/Cython_fun")
)


from magic import find_function_end


def test_find_function_end_use_case():
    with open("test.py", "r") as file:
        text = file.read()
    assert find_function_end(text, 1) == 2


def test_find_function_end_bad_lines_values():
    with open("test.py", "r") as file:
        text = file.read()
    assert find_function_end(text, 3) == "There are not that many lines"


def test_find_function_end_bad_text_values():
    text = ""
    assert find_function_end(text, 1) == "No text"


def test_find_function_end_bad_lines_reading():
    text = "def test(test): print(test) return test"
    assert find_function_end(text, 1) == "There are not that many lines"
