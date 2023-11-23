#!/usr/bin/env checkio --domain=py run long-repeat
from itertools import groupby


def long_repeat(line: str) -> int:
    """
    length the longest substring that consists of the same char
    """
    return max(map(lambda item: len(''.join(item[1])), groupby(line))) if line else 0


print("Example:")
print(long_repeat("sdsffffse"))

assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
