# This is testing the replace function
import copy
from dataclasses import dataclass

print_counter: int = 0

@dataclass
class Example:
    text: str
    count: int


def main() -> None:
    a: str = "Hello, world!"

    b = a.replace("world", "universe")
    print(b)

    example = Example(text="Hello, world!", count=1)
    print(example)

    another_example = copy.replace(example, text="universe")
    print(another_example)

    for x in locals():
        print(f'Local variable: {x}: {locals()[x]}')
    for x in globals():
        if '__' in x:
            continue
        print(f'Global variable: {x}: {globals()[x]}')


if __name__ == "__main__":
    main()

