# Make a list with uniqe names and in order of appearance
x = ["Alice", "Bob", "Alice", "Monika", "Bob", "Alice", "Fred", "Alice"]
expected = ["Alice", "Bob", "Monika", "Fred"]

result = []
i = set()
for name in x:
    if name not in i:
        result.append(name)
        i.add(name)

assert result == expected
# sort by order
x = [
    {'order': 5, 'name': 'Bob'},
    {'order': 3, 'name': 'Alice'},
    {'order': 8, 'name': 'Monika'},
]
expected = [{'order': 3, 'name': 'Alice'}, {'order': 5, 'name': 'Bob'}, {'order': 8, 'name': 'Monika'}]

x.sort(key=lambda x: x['order'])
assert x == expected

def multiply(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs) * 2
    return wrapper

@multiply
def hello():
    return "Hello World "

print(hello())

# check if int
x = ['233','a2332', '2323','323b']

result = [i for i in x if i.isdigit()]
assert result == ['233', '2323']


y = ['abC', 'as', 'asd']
result = [i for i in y if i.islower()]
assert result == ['as', 'asd']


