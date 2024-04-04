#!/usr/bin/env checkio --domain=py run shortest-knight-path
from string import ascii_lowercase


def knight_step(start):
    pos_list = []
    for l_part in (2, -2):
        for s_part in (1, -1):
            num_1 = int(start[1]) + s_part
            num_2 = int(start[1]) + l_part
            pos_1 = chr(ord(start[0]) + l_part) + str(num_1 if num_1 > 0 else 0)
            pos_2 = chr(ord(start[0]) + s_part) + str(num_2 if num_2 > 0 else 0)
            if 0 < int(pos_1[1]) < 9 and pos_1[0] in ascii_lowercase[:8]:
                pos_list.append(pos_1)
            if 0 < int(pos_2[1]) < 9 and pos_2[0] in ascii_lowercase[:8]:
                pos_list.append(pos_2)
    return pos_list


def checkio(cells):
    """str -> int
    Number of moves in the shortest path of knight
    """
    start, end = cells.split('-')
    end_pos_list = knight_step(start)
    step = 1
    while end not in end_pos_list:
        step += 1
        end_pos_list = list(item for lst in map(lambda pos: knight_step(pos), end_pos_list) for item in lst)
    return step


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"
