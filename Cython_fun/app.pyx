
def loop_function(num1: int):
    result = 0
    for i in range(num1):
        result += i * i
        result += i * loop_function(i)
    return result
