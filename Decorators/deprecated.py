from deprecated import deprecated


@deprecated("Adding ain't cool no more", version="1.0.0")
def add(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    print(add(5, 7))