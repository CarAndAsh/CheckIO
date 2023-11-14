#!/usr/bin/env checkio --domain=py run frequency-sorting
from collections import Counter
from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    # replace this for solution
    if numbers:
        count_list = Counter(sorted(numbers)).most_common()
        return [i for i, j in count_list for _ in range(j)]
    return []


print("Example:")
print(list(frequency_sorting([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
