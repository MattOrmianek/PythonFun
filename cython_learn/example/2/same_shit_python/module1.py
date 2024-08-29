"""This is example of a simple external module"""


def module1_function():
    """This is a simple function from module1"""
    # inifity loop
    while True:
        print("This is inside a loop in function in module")


def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
