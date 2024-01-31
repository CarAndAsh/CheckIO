#!/usr/bin/env checkio --domain=py run chunk
from collections.abc import Iterable


def chunking_by(items: list[int], size: int) -> Iterable[list[int]]:
    return [items[size * (i - 1):size * i] for i in
            range(1, (len(items) // size) + (2 if len(items) % size else 1))] if items else []


print("Example:")
print(list(chunking_by([1, 2, 2, 3], 7)))

# These "asserts" are used for self-checking
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []
assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
