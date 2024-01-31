#!/usr/bin/env checkio --domain=py run square-board
from typing import Tuple

Coordinate = Tuple[int, int]


def square_board(side: int, token: int, steps: int) -> Coordinate:
    row, col = side - 1, side - 1
    cells_on_p = 4 * (side - 1)
    asc = True
    directions = ['left', 'up', 'right', 'down']
    direction = directions[0] if asc else directions[1]
    steps = steps % cells_on_p if steps >= 0 else -(abs(steps) % cells_on_p)
    for i in range(token + abs(steps)):
        if direction == 'down':
            row += 1
            if row == side - 1:
                direction = directions[0] if asc else directions[2]
        elif direction == 'right':
            col += 1
            if col == side - 1:
                direction = directions[3] if asc else directions[1]
        elif direction == 'up':
            row -= 1
            if row == 0:
                direction = directions[2] if asc else directions[0]
        elif direction == 'left':
            col -= 1
            if col == 0:
                direction = directions[1] if asc else directions[3]
        if i == (token - 1):
            # find start positon and choose direction
            if steps < 0:
                asc = False
                if (row, col) in [(0, 0), (side - 1, 0), (0, side - 1), (side - 1, side - 1)]:
                    # turn direction on couner positions
                    direction = directions[(directions.index(direction) + 1) % len(directions)]
                else:
                    # turn direction on side
                    direction = directions[(directions.index(direction) + 2) % len(directions)]
    return row, col


if __name__ == '__main__':
    print("Example:")
    print(square_board(4, 1, 4))
    assert square_board(4, 1, 4) == (1, 0)
    assert square_board(6, 2, -3) == (4, 5)
    assert square_board(3, 4, -3) == (2, 1)

    print("Coding complete? Click 'Check' to earn cool rewards!")
