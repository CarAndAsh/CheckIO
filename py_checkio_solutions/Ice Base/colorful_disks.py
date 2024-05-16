#!/usr/bin/env checkio --domain=py run colorful-disks
from functools import reduce


def count_discs(discs: tuple[int, ...]) -> int:
    vis_disc = 0
    с = 0
    for i in range(len(discs) - 1, -1, -1):
        if discs[i] > vis_disc:
            vis_disc = discs[i]
            с += 1
    return с


print("Example:")
print(count_discs((3, 2)))

# These "asserts" are used for self-checking
assert count_discs((3, 6, 7, 4, 5, 1, 2)) == 3
assert count_discs((6, 5, 4, 3, 2, 1)) == 6
assert count_discs((5,)) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
