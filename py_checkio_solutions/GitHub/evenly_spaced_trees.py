#!/usr/bin/env checkio --domain=py run evenly-spaced-trees
from typing import List


def evenly_spaced_trees(trees: List[int]) -> int:
    diff_list = [trees[ind] - trees[ind - 1] for ind in range(1, len(trees))]
    while len(diff_list) != 1:
        diff_list.sort()
        b = diff_list.pop(0)
        if b != 0:
            diff_list = list(map(lambda x: x % b, diff_list))
            diff_list.append(b)
    return len(range(min(trees), max(trees) + 1, diff_list[0])) - len(trees)


if __name__ == '__main__':
    print("Example:")
    print(evenly_spaced_trees([1, 52, 100]))
    assert evenly_spaced_trees([0, 2, 6]) == 1, 'add 1'
    assert evenly_spaced_trees([1, 3, 6]) == 3, 'add 3'
    assert evenly_spaced_trees([0, 2, 4]) == 0, 'no add'
    assert evenly_spaced_trees([1, 52, 100]) == 31
    print("Coding complete? Click 'Check' to earn cool rewards!")
