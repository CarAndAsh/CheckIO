#!/usr/bin/env checkio --domain=py run expand-intervals
from typing import Iterable
from itertools import chain


def expand_intervals(items: Iterable) -> Iterable:
    return chain(*[range(start, end+1) for start, end in items])


if __name__ == "__main__":
    print("Example:")
    print(list(expand_intervals([(1, 3), (5, 7)])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(expand_intervals([(1, 3), (5, 7)])) == [1, 2, 3, 5, 6, 7]
    assert list(expand_intervals([(1, 3)])) == [1, 2, 3]
    assert list(expand_intervals([])) == []
    assert list(expand_intervals([(1, 2), (4, 4)])) == [1, 2, 4]
    print("Coding complete? Click 'Check' to earn cool rewards!")
