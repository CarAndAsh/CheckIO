#!/usr/bin/env checkio --domain=py run chess-knight
def chess_knight(start, moves, dest=None):
    if dest is None:
        dest = []
    for num_i in range(1, 3):
        if num_i == 1:
            char_d = 2
        elif num_i == 2:
            char_d = 1
        for j in (-num_i, num_i):
            for k in (-char_d, char_d):
                if 'h' >= chr(ord(start[0]) + k) >= 'a' and 8 >= int(start[1]) + j >= 1:
                    dest.append(f'{chr(ord(start[0]) + k)}{int(start[1]) + j}')
    if moves == 1:
        dest.sort()
        return dest
    else:
        mid_pos = tuple(dest[:])
        for pos in mid_pos:
            dest.extend(chess_knight(pos, moves - 1))
        dest = list(set(dest))
        dest.sort(key=lambda x: (ord(x[0]), x[1]))
        return dest


if __name__ == "__main__":
    print("Example:")
    print(chess_knight("a1", 1))
    print(chess_knight("a1", 1))
    print(chess_knight("h8", 2))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight("a1", 1) == ["b3", "c2"]
    assert chess_knight("h8", 2) == ["d6", "d8", "e5", "e7", "f4", "f7", "f8", "g5", "g6", "h4", "h6", "h8"]
    # print("Coding complete? Click 'Check' to earn cool rewards!")
