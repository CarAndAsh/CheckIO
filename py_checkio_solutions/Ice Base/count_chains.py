#!/usr/bin/env checkio --domain=py run count-chains
from itertools import combinations
from typing import List, Tuple


def check_cross(c_1, c_2):
    dist = ((c_1[0] - c_2[0]) ** 2 + (c_1[1] - c_2[1]) ** 2) ** 0.5
    return -1 if abs(c_1[2] - c_2[2]) < dist < (c_1[2] + c_2[2]) else 0


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    # circle = tpl(x, y, r)
    res = len(circles) + sum(map(lambda crcl_pair: check_cross(*crcl_pair), combinations((circles), 2)))
    print(res)
    return res or 1


if __name__ == "__main__":
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, "basic"
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, "basic #2"
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, "trinity"
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, "inclusion"
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, "adjacent"
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, "negative coordinates"
    assert count_chains([(1, 3, 1), (2, 2, 1), (4, 2, 1), (5, 3, 1), (3, 3, 1)]) == 1
    assert count_chains([[0,0,2],[1,0,3],[3,0,1],[2,1,1],[-2,-2,1],[0,0,4],[-3,0,1]]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
