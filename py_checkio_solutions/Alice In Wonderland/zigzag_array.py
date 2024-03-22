#!/usr/bin/env checkio --domain=py run zigzag-array
def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    reverse_flag = True
    num = start
    res = []
    for r in range(rows):
        res.append([])
        if reverse_flag:
            reverse_flag = False
        else:
            reverse_flag = True
        for c in range(cols):
            if reverse_flag:
                res[r].insert(0, num)
            else:
                res[r].append(num)
            num += 1
    return res


print("Example:")
print(create_zigzag(3, 5))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
