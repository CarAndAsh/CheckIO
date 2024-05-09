#!/usr/bin/env checkio --domain=py run the-brick-factory-problem
from functools import reduce


def crosses(k: int, s: int = None) -> int:
    return reduce(lambda x, y: x * y, map(lambda num: num >> 1, (k, k - 1, s, s - 1)) if s else map(lambda num: num >> 1, range(k, k - 4, -1)))//(1 if s else 4)


print("Example:")
print(crosses(5, 5))

# These "asserts" are used for self-checking
assert crosses(1, 1) == 0
assert crosses(5) == 1
assert crosses(5, 5) == 16
assert crosses(7) == 9

print("The mission is done! Click 'Check Solution' to earn rewards!")
