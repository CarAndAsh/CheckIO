#!/usr/bin/env checkio --domain=py run x-o-referee
from collections import Counter


def checkio(game_result: list[str]) -> str:
    # your code here
    if game_result:
        # check diagonals
        diag_1 = {}
        diag_2 = {}
        for i, line in enumerate(game_result):
            line_dict = {char: line.count(char) for char in line if char != '.'}
            if len(line_dict) == 1 and len(line) in line_dict.values():
                return ''.join(line_dict.keys())
            row_dict = Counter(line[i] for line in game_result if line[i] != '.')
            if len(row_dict) == 1 and len(game_result) in row_dict.values():
                return ''.join(row_dict.keys())
            diag_val_1 = game_result[i][i]
            diag_val_2 = game_result[i][-i - 1]
            if diag_val_1 != '.':
                diag_1[diag_val_1] = diag_1.get(diag_val_1, 0) + 1
            if diag_val_2 != '.':
                diag_2[diag_val_2] = diag_2.get(diag_val_2, 0) + 1
        if len(game_result) in diag_1.values():
            return max(diag_1, key=lambda x: diag_1[x])
        if len(game_result) in diag_2.values():
            return max(diag_2, key=lambda x: diag_2[x])
        return 'D'
    return ""


print("Example:")
print(checkio(["X.O", "XX.", "XOO"]))

# These "asserts" are used for self-checking
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

print("The mission is done! Click 'Check Solution' to earn rewards!")
