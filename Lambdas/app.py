def same_value(x):
    return x


lambda x: x


print((lambda x: x + 1)(2))

add_one = lambda x: x + 1

print(add_one(2))

sum_of_all = lambda x, y, z: x + y + z
print(sum_of_all(1, 2, 3))

sum_of_all_proper = lambda *args: sum(args)

print(sum_of_all_proper(1, 2, 3, 4))


def trace(f):
    def wrapper(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrapper


@trace
def add_two(x):
    return x + 2


print(add_two(3))

print((trace(lambda x: x**3))(3))

mapped = list(map(lambda x: x.upper(), ["cat", "dog", "cow"]))
print(mapped)

not_mapped = [x.upper() for x in ["cat", "dog", "cow"]]
print(not_mapped)
