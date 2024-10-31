import re

import time

def timeit(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start} seconds")
        return result
    return inner

def is_prime(n: int) -> bool:
    return re.match(r'^.?$|^(..+?)\1+$', '1' * n) is None

@timeit
def loop_is_prime(n: int):
    for i in range(1, n, 2):
        if is_prime(i):
            print(i)
@timeit
def largest_prime(n: int):
    if n % 2 == 0:
        n -= 1
    for i in range(n, 0, -2):
        if is_prime(i):
            return i
@timeit
def largest_prime_optimized(n: int):
    if n < 2:
        return None
    if n == 2:
        return 2

    if n % 2 == 0:
        n -= 1

    def is_prime_fast(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    for num in range(n, 2, -2):
        if is_prime_fast(num):
            return num

n = 10**19
print("N: ", n)

print("OPTIMIZED way:")
print(largest_prime_optimized(n))

if n < 10**5: # regex way can't handle numbers above 10^5 in reasonable time
    print("REGEX way:")
    print(largest_prime(n))
