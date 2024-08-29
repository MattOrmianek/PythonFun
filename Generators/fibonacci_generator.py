from typing import Generator


# types: [yield, input, output]
def fibonacci_generator() -> Generator[int, None, None]:
    """Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b)


def main() -> None:
    """Main function"""
    fib_gen: Generator[int, None, None] = fibonacci_generator()
    n: int = 10
    line_break: str = "-" * 20
    while True:
        input(f"Tap 'enter' for the next {n} numbers of fibonacci")
        print(line_break)
        for i in range(n):
            print(f"{next(fib_gen)}")
        print(line_break)


if __name__ == "__main__":
    main()
