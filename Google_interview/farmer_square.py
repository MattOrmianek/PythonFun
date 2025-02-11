"""
A farmer wants to farm their land with the maximum area where good land is present.
The "land" is represented as a matrix with ls and Os, where 1s mean good land and Os
mean bad land. The farmer only want to farm in a square of good land with the maximum
area. Please help the farmer to find the maximum area of the land they can farm in
good land.

0 1 1 0 1
1 1 0 1 0
0 1 1 1 0
1 1 1 1 0
1 1 1 1 1
0 0 0 0 0
Additional: create function for generating random fields, with provided dimensions
"""

import random
from typing import List

def farmer_square(field: List[List[int]]) -> int:
    """
    Returns the area of the largest square submatrix that contains only 1's.

    Parameters:
        field (List[List[int]]): A 2D list representing the land, where 1 means good land.

    Returns:
        int: The area (side_length**2) of the largest square of 1's.
    """
    if not field or not field[0]:
        return 0

    rows, cols = len(field), len(field[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if field[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side ** 2

def generate_random_field(rows: int, cols: int, prob_good: float = 0.5) -> List[List[int]]:
    """
    Generates a random field (matrix) with given dimensions.

    Parameters:
        rows (int): Number of rows.
        cols (int): Number of columns.
        prob_good (float): Probability that a cell is good land (1). Default is 0.5.

    Returns:
        List[List[int]]: A randomly generated matrix of 0's and 1's.
    """
    return [
        [1 if random.random() < prob_good else 0 for _ in range(cols)]
        for _ in range(rows)
    ]


def main() -> None:
    sample_field = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]

    print("Max square area in sample field:", farmer_square(sample_field))
    for i in range(10):
        random_x = random.randint(3, 18)
        random_y = random.randint(3, 10)
        random_field = generate_random_field(random_x, random_y, prob_good=0.4)
        print("Random field:")
        for row in random_field:
            print(row)
        print("Max square area in random field:", farmer_square(random_field))

if __name__ == "__main__":
    main()