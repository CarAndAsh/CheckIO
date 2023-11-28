#!/usr/bin/env checkio --domain=py run can-balance
from typing import Iterable


def can_balance(weights: Iterable) -> int:
    for indx, _ in enumerate(weights):
        weights_on_torque = tuple(el * (i - indx) for i, el in enumerate(weights))
        if not (sum(weights_on_torque[:indx]) + sum(weights_on_torque[indx + 1:])):
            return indx
    return -1


if __name__ == '__main__':
    print("Example:")
    print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
