""" This is testing iterators and how to work with them """

import itertools


def buildins() -> None:
    """This is testing filter function"""
    example_list = [1, 2, None, 3]
    filtered_list = list(filter(None, example_list))
    assert filtered_list == [1, 2, 3]


def example_counter() -> None:
    """This is example of counter"""
    counter = itertools.count(start=10, step=2)
    values = [next(counter) for _ in range(5)]
    assert values == [10, 12, 14, 16, 18]


def example_accumulate() -> None:
    """This is example of accumulate"""
    values_min = list(itertools.accumulate([1, 2, 3, 4, 5], min))
    values_max = list(itertools.accumulate([1, 2, 3, 4, 5], max))
    assert values_min == [1, 1, 1, 1, 1]
    assert values_max == [1, 2, 3, 4, 5]


def example_batched() -> None:
    """This is example of batched"""
    values = list(itertools.batched([1, 2, 3, 4, 5], 3))  # pylint: disable=no-member
    values_even = list(itertools.batched([1, 2, 3, 4, 5, 6], 2))  # pylint: disable=no-member
    assert values == [(1, 2, 3), (4, 5)]
    assert values_even == [(1, 2), (3, 4), (5, 6)]


def example_chain_from_iterable() -> None:
    """This is example of chain from iterable"""
    iterables = [[1, 2, 3], [4, 5], [6, 7, 8]]
    values = list(itertools.chain.from_iterable(iterables))
    assert values == [1, 2, 3, 4, 5, 6, 7, 8]


def example_compress() -> None:
    """This is example of compress"""
    data = [1, 2, 3, 4, 5]
    selectros = [True, False, True, False, False]
    values = list(itertools.compress(data, selectros))
    assert values == [1, 3]


def example_dropwhile() -> None:
    """This is example of dropwhile"""
    data = [1, 2, 3, 4, 5]
    values = list(itertools.dropwhile(lambda x: x < 3, data))
    assert values == [3, 4, 5]


def example_filterfalse() -> None:
    """This is example of filterfalse"""
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = list(itertools.filterfalse(lambda x: x % 2 == 0, data))
    assert result == [1, 3, 5, 7, 9]


def example_groupby() -> None:
    """This is example of groupby"""
    data = [
        ("a", 1),
        ("a", 2),
        ("b", 3),
        ("b", 4),
        ("c", 5),
        ("c", 6),
    ]
    grouped = itertools.groupby(data, key=lambda x: x[0])
    result = [(key, list(group)) for key, group in grouped]
    assert result == [
        ("a", [("a", 1), ("a", 2)]),
        ("b", [("b", 3), ("b", 4)]),
        ("c", [("c", 5), ("c", 6)]),
    ]


if __name__ == "__main__":
    buildins()
    example_counter()
    example_accumulate()
    example_batched()
    example_chain_from_iterable()
    example_compress()
    example_dropwhile()
    example_filterfalse()
    example_groupby()
