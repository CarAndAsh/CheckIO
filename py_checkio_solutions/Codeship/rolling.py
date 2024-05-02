#!/usr/bin/env checkio --domain=py run rolling
def rolling_dice(moves: str) -> int:
    dice = [[1, 3, 6, 4], [1, 5, 6, 2]]
    zero_moves = ('SN', 'NS', 'WE', 'EW', 'NNNN', 'SSSS', 'WWWW', 'EEEE')
    while any(map(lambda zero_move: zero_move in moves, zero_moves)):
        for zero_move in zero_moves:
            moves = moves.replace(zero_move, '')
    for side in moves:
        if side == "N":
            dice[1].insert(0, dice[1].pop())
            dice[0][0], dice[0][2] = dice[1][0], dice[1][2]
        elif side == "S":
            dice[1].append(dice[1].pop(0))
            dice[0][0], dice[0][2] = dice[1][0], dice[1][2]
        elif side == "E":
            dice[0].insert(0, dice[0].pop())
            dice[1][0], dice[1][2] = dice[0][0], dice[0][2]
        elif side == "W":
            dice[0].append(dice[0].pop(0))
            dice[1][0], dice[1][2] = dice[0][0], dice[0][2]
    return dice[0][0]


print("Example:")
print(rolling_dice("NNNSESNESWNENSWNNWSWNSSNWWSWNW"))

# These "asserts" are used for self-checking
assert rolling_dice("SN") == 1
assert rolling_dice("") == 1
assert rolling_dice("EESWN") == 6
assert rolling_dice("NWSNWEESNW") == 3
assert rolling_dice("NNNSESNESWNENSWNNWSWNSSNWWSWNW") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
