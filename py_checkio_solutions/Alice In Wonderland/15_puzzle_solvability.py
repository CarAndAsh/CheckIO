#!/usr/bin/env checkio --domain=py run 15-puzzle-solvability
def fifteen_puzzle(position: list[list[int]]) -> bool:
    steps = 0
    if position[len(position) - 1][len(position[0]) - 1] != 16:
        # find where 16
        for i, line in enumerate(position):
            if 16 in line:
                steps += (len(position) - 1 - i) + (len(position[0]) - 1 - line.index(16))
                break

    pos = [el for line in position for el in line]
    hop_c = 0
    last_hop = (0, 0)
    while pos != list(range(1, 17)):
        i = 0
        while i < 15:
            if (el := pos[i]) != i + 1:
                if el in last_hop and pos[el - 1] in last_hop:
                    return False
                hop_c += 1
                last_hop = (el, pos[el - 1])
                pos[i], pos[el - 1] = pos[el - 1], pos[i]
            i += 1
    return (hop_c - steps) % 2 == 0


print("Example:")
print(fifteen_puzzle([[1, 4, 5, 8], [2, 3, 6, 7], [9, 10, 13, 14], [16, 11, 12, 15]]))

# These "asserts" are used for self-checking
assert fifteen_puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == True
assert fifteen_puzzle([[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 16]]) == False
assert fifteen_puzzle([[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]) == True
assert fifteen_puzzle([[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12], [13, 15, 14, 16]]) == True
assert fifteen_puzzle([[1, 9, 2, 10], [3, 11, 4, 12], [5, 13, 6, 14], [7, 15, 8, 16]]) == True
assert fifteen_puzzle([[1, 4, 5, 8], [2, 3, 6, 7], [9, 10, 13, 14], [16, 11, 12, 15]]) == True
assert fifteen_puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 15, 14, 16]]) == False
assert fifteen_puzzle([[1, 15, 11, 7], [14, 6, 5, 8], [4, 10, 3, 13], [16, 12, 9, 2]]) == False
print("The mission is done! Click 'Check Solution' to earn rewards!")
