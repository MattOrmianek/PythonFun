# Tuples:
coordinate = (1, 2)  # tuple
coordinate = 1, 2  # also tuple
coordinate = ()  # empty tuple
coordinate = (1,)  # empty tuple
coordinate = 1  # integer, not a tuple

# is ==
x: int = 100
y: int = 100
print(x, y)
print(x == y)
print(x is y)


x: int = 100
y: int = 90

print(x, y)
print(x == y)
print(x is y)

x: float = 100
y: float = 1000 / 10
print(x, y)
print(x == y)
print(x is y)
# is is checking if memory address is the same, == checks value


class Car:
    fuel_type: str = "gas"

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year


bmw: Car = Car("BMW", "G20", 2018)
bmw.fuel_type = "electric"

volvo: Car = Car("Volvo", "X90", 2020)
volvo.fuel_type = "electric"

print(bmw.fuel_type)
print(volvo.fuel_type)
Car.fuel_type = "diesel"
mercedes: Car = Car("Mercedes", "G63", 2024)

print(mercedes.fuel_type)  # defined fuel_type in class was gas but with Car.fuel_type it changed
