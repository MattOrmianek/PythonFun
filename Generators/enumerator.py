from collections.abc import Generator, Iterable
from typing import Any

type Enumerator = Generator[tuple[int, Any], None, None]


def enumerations(iterable: Iterable) -> Enumerator:
    yield from enumerate(iterable, start=1)


enumerator: Enumerator = enumerations("ABCDEF")
print(next(enumerator))
print(next(enumerator))
print(next(enumerator))
print(next(enumerator))
print(next(enumerator))
print(next(enumerator))
