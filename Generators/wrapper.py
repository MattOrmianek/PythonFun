from collections.abc import Generator
from typing import Any


def numbers(n: int) -> Generator[str, None, None]:
    for i in range(n):
        yield f"numbers: {i}"


def wrapper(g: Generator) -> Generator[str, None, None]:
    yield "wrapper: first value"
    yield from g
    yield "wrapper: last value"


gen: Generator[Any, None, None] = wrapper(numbers(3))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
