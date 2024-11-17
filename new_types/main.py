# This is testing new types in 3.13

from typing import TypedDict, ReadOnly

class Leader(TypedDict):
    name: ReadOnly[str]
    age: int


def main() -> None:
    Leader = TypedDict("Leader", {"name": ReadOnly[str], "age": int})

    author: Leader = {'name': 'Yang Zhou', 'age': 30}
    author['age'] = 31  # no problem to change
    author['name'] = 'Tim'  # Type check error: "name" is read-only
    # Tested on 3.13.0 installed via pyenv on macOS - not working - can't get type check error

    for x in locals():
        print(f'Local variable: {x}: {locals()[x]}')
    for x in globals():
        if '__' in x:
            continue
        print(f'Global variable: {x}: {globals()[x]}')


if __name__ == "__main__":
    main()

