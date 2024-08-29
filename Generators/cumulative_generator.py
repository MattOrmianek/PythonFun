import sys
from typing import Generator


def cumulative_sum() -> Generator[float, float, None]:
    """Cumulative sum generator"""
    total: float = 0
    while True:
        new_value: float = yield total
        total += new_value


def main() -> None:
    """Main function"""
    cumulative_generator: Generator[float, float, None] = cumulative_sum()
    next(cumulative_generator)
    while True:
        value: float = float(input("Enter a value:"))
        current_sum: float = cumulative_generator.send(value)
        print(f"Cumulative sum: {current_sum}")


if __name__ == "__main__":
    main()
