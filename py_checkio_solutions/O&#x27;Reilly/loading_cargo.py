#!/usr/bin/env checkio --domain=py run loading-cargo
from itertools import combinations


def checkio(data):
    if data:
        if len(data) == 1:
            return data[0]
        min_diff = None
        for ln in range(1, len(data)//2 + 1):
            for combo_1 in combinations(data, ln):
                combo_2 = data[:]
                [combo_2.remove(el) for el in combo_1]
                diff = abs(sum(combo_2) - sum(combo_1))
                if min_diff is None or diff < min_diff:
                    min_diff = diff
        return min_diff
    return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([10, 10]))
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
