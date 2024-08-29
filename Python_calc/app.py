def print_pass(test_name):
    print(f"{test_name}: \t Pass")


def print_fail(test_name):
    print(f"{test_name}: \t Fail")


# Ex 1: multiply without using * symbol


def test_multiply(func):
    if func(4, 3) == 4 * 3:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


def weird_multiply(num1, num2):
    result = 0
    for i in range(0, num2):
        result += num1
    return result


test_multiply(weird_multiply)

print(f"weird_mulipy: 4 times 8 is equal to {weird_multiply(4,8)}")


def second_weird_multiply(num1, num2):
    if num2 == 1:
        return num1
    else:
        return num1 + second_weird_multiply(num1, num2 - 1)


test_multiply(second_weird_multiply)

print(f"second_weird_mulipy: 4 times 8 is equal to {second_weird_multiply(4,8)}")

from math import log, pow, exp


def third_weird_multiply(num1, num2):
    return log(pow(exp(num1), num2))


test_multiply(third_weird_multiply)

print(f"third_weird_multiply: 4 times 8 is equal to {third_weird_multiply(4,8)}")
