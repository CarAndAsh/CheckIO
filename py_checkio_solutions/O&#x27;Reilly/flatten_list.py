#!/usr/bin/env checkio --domain=py run flatten-list
from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    # your code here
    if array:
        res = []
        [res.extend(flat_list(x)) if isinstance(x, list) else res.append(x) for x in array]
        return res
    return []


print("Example:")
print(list(flat_list([1, 2, 3])))

# These "asserts" are used for self-checking
assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
