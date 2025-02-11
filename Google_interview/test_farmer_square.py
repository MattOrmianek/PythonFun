from farmer_square import farmer_square
first_test_matrix  = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
first_test_answer = 9
second_test_matrix  = [
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
second_test_answer = 16
third_test_matrix  = [
        [0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
third_test_answer = 1

def test_farmer_square():
    assert farmer_square(first_test_matrix) == first_test_answer
    assert farmer_square(second_test_matrix) == second_test_answer
    assert farmer_square(third_test_matrix) == third_test_answer
if __name__ == "__main__":
    test_farmer_square()