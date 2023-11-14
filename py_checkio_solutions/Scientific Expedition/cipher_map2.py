#!/usr/bin/env checkio --domain=py run cipher-map2
from typing import List


def recall_password(grille: List[str], password: List[str]) -> str:
    def read_chars(password, grille):
        line_pswd = ''.join(password)
        line_grille = ''.join(grille)
        return ''.join([ch for i, ch in enumerate(line_pswd) if line_grille[i] == 'X'])

    if password and grille:
        res = read_chars(password, grille)
        rotate_times = 3
        # "rotate" grille
        while rotate_times:
            grille = [''.join(reversed(line)) for line in zip(*grille)]
            res += read_chars(password, grille)
            rotate_times -= 1
        return res
    return None


if __name__ == '__main__':
    print("Example:")
    print(recall_password(['X...', '..X.', 'X..X', '....'],
 ['itdf', 'gdce', 'aton', 'qrdi']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert recall_password(['X...', '..X.', 'X..X', '....'],
 ['itdf', 'gdce', 'aton', 'qrdi']) == 'icantforgetiddqd'
    assert recall_password(['....', 'X..X', '.X..', '...X'],
 ['xhwc', 'rsqx', 'xqzz', 'fyzr']) == 'rxqrwsfzxqxzhczy'
    print("Coding complete? Click 'Check' to earn cool rewards!")
