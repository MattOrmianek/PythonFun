"""
Challenge 1:
Reverse a string
"""
example_string = "This is example string"

def reverse_string(s: str) -> str:
    return s[::-1]

assert reverse_string(example_string) == "gnirts elpmaxe si sihT"


"""
Challenge 2:
Write a program that prints the numbers from 1 to 50. But for multiples of three,
print "Fizz" instead of the number, and for multiples of five, print "Buzz".
For numbers that are multiples of both three and five, print "FizzBuzz".
"""
def create_fizz_buzz(times: int) -> str:
    if times <= 0:
        print("Invalid argument")
        return ""
    result = ""
    for i in range(1,times+1):
        if i % 15 == 0:
            result += "FizzBuzz"
        elif i % 3 == 0:
            result += "Fizz"
        elif i % 5 == 0:
            result += "Buzz"
        else:
            result += str(i)
    return result

fizz_buzz = create_fizz_buzz(50)
assert create_fizz_buzz(16) == "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz16"

"""
Challenge 3:
Write a function to check if two strings are anagrams of each other.
"""

def anagram_check(s1: str, s2: str) -> bool:
    for char in s1:
        if char in s2:
            continue
        else:
            return False
    return True

assert anagram_check("listen", "silent") == True
assert anagram_check("hello", "world") == False


"""
Challenge 4:
Write a function that returns the nth number in the Fibonacci sequence.
"""

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(6) == 8

"""
Challenge 5:
Write a function that checks if a given string is a palindrome (reads the same backward as forward).
"""

def is_palindrome(s: str) -> bool:
    middle = len(s)//2
    for i in range (0, middle):
        if s[middle + i] == s[middle - i]:
            continue
        else:
            return False
    return True

assert is_palindrome("racecar") == True
assert is_palindrome("python") == False

"""
Challenge 6:
Given a list containing all the numbers from 1 to 100 except one, write a function to find the missing number.
"""
import random
def find_missing_number(l: list) -> int:
    expected_sum = 100 * 101 // 2
    actual_sum = sum(l)
    return expected_sum - actual_sum

example_list = [x for x in range(1,101)]
random_number = random.randint(1, 101)
example_list.pop(random_number - 1) # Because array starts at 0
assert find_missing_number(example_list) == random_number

"""
Challange 7:
Write a function that flattens a nested list structure.
"""

def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        elif isinstance(item, int):
            flat_list.append(item)
    return flat_list

assert flatten([1, [2, [3, 4], 5], 6])  ==  [1, 2, 3, 4, 5, 6]


"""
Challenge 8:
Given two sorted lists, write a function to merge them into a single sorted list.
"""

def merge_lists(l1: list, l2: list) -> list:
    merged_list = []
    middle = min(len(l1), len(l2))

    for i in range(middle):
        merged_list.append(l1[i])
        merged_list.append(l2[i])

    if len(l1) > len(l2):
        merged_list.extend(l1[middle:])
    else:
        merged_list.extend(l2[middle:])

    return merged_list


assert merge_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
assert merge_lists([1, 3, 5], [2, 4, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
assert merge_lists([1, 3, 5], [2, 4, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]

"""
Challenge 9:
Write a context manager using the with statement to manage a file resource.
"""

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Open the file when entering the context
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the file when exiting the context
        if self.file:
            self.file.close()
        # Returning False allows any exception to propagate; return True to suppress exceptions
        return False

"""
Challenge 10:
Write functions to serialize a Python dictionary into a JSON string and deserialize it back into a dictionary.
"""
import json

def serialize_to_json(data_dict):
    try:
        return json.dumps(data_dict)
    except TypeError as e:
        raise ValueError(f"Data could not be serialized: {e}")

def deserialize_from_json(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON data: {e}")


"""
Challenge 11:
Write a decorator that logs the execution time of a function.
"""
import time
def timeit(f):
    def wraps(*args, **kwargs):
        time_of_start = time.time()
        c = f(*args, **kwargs)
        time_of_end = time.time() - time_of_start
        print("function takes: %s" % time_of_end)
        return c  # Return the result of the function call
    return wraps  # Return the wraps function

@timeit
def calculate(n) -> None:
    sum = 0
    for i in range(0,n*n*n):
        sum += i

calculate(40)


"""
Challenge 12:
Calucate factorial recursively
"""
def factorial(n):
    if n == 1:
       return n
    else:
       return n*factorial(n-1)

assert factorial(5) == 120

"""
Challenge 13:
Implement the binary search algorithm to find the position of a target value within a sorted list.
"""

def binary_search(sorted_list: list, target: int) -> int:
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid  # Target found
        elif sorted_list[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Target not found

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert binary_search(sorted_list, 5) == 4
assert binary_search(sorted_list, 11) == -1



person = [
    {"name": "Adam",
     "id": 123,
     "age": 23},
    {"name": "Marek",
     "id": 523,
     "age": 35},
    {"name": "Michal",
     "id": 1223,
     "age": 13}
]
person = sorted(person, key=lambda item: item.get("age"))
print(person)