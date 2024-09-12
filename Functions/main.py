""" Functions how they work and how to use them """

from collections.abc import Iterable
from datetime import datetime

# 1. Short and concise
# 2. Specify a return type
# 3. Make as simple and reusable as possible
# 4. Document all your functions
# 5. Handle errorsa ppropriately


def get_time() -> str:
    """Returns the current time in the format 'HH:MM:SS'"""
    now: datetime = datetime.now()
    return f"{now:%X}"


def get_total_discount(prices: Iterable[float], percent: float) -> float:
    """Calculates the total discount for a list of prices and a discount percentage"""
    if not 0 <= percent <= 1:
        raise ValueError("Discount percentage must be between 0 and 1")

    if not all(isinstance(price, (int, float)) and price >= 0 for price in prices):
        raise ValueError("All prices must be non-negative numbers")
    total: float = sum(prices)
    return total * (1 - percent)


def main() -> None:
    """Main function"""
    print(get_time())
    total_discount: float = get_total_discount([10, 20, 30], 0.1)
    print(total_discount)


if __name__ == "__main__":
    main()
