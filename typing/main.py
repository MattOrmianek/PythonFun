class Fruit:
    ...

fruit: Fruit = Fruit()

#elements: list[str] = [1,2,'a'] #issue
elements: list[str] = ['a']

def get_data() -> dict[str, int]:
    return {'a': 1, 'b': 2}

data: dict[str, int] = get_data()
print(data)

def greet_people(people: list[str]) -> None:
    for person in people:
        print(f'Hello, {person.capitalize()}!')
