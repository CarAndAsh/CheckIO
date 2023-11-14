#!/usr/bin/env checkio --domain=py run nonogram-encode
def nonogram_encode(data: list[str]) -> list[list[list[int]]]:
    def zfill_list(func):
        def wrapper(data):
            matrix = func(data)
            line_lenght = len(max(matrix, key=len))
            for line in matrix:
                while len(line) < line_lenght:
                    line.insert(0, 0)
            return matrix
        return wrapper

    def count_x(line: str) -> list:
        lst = []
        c = 0
        for char in line:
            if char == 'X':
                c += 1
            elif c > 0 and char == ' ':
                lst.append(c)
                c = 0
        if c > 0:
            lst.append(c)
        return lst

    @zfill_list
    def get_clue(matrix: list) -> list:
        res = []
        for line in matrix:
            res.append(count_x(line))
        return res

    res = []
    if data:
        rev_data = []
        for row in data:
            if rev_data:
                for i, char in enumerate(row):
                    rev_data[i] += char
            else:
                for char in row:
                    rev_data.append(char)
        rev_row_clue = get_clue(rev_data)
        row_clue = [[row[i] if i < len(row) else -1 for row in rev_row_clue] for i, _ in enumerate(rev_row_clue[0])]
        res.append(row_clue)
        res.append(get_clue(data))
    return res


print("Example:")
print(nonogram_encode(['XX X X',
                       ' X XXX',
                       ' X XX ',
                       ' XXX  ',
                       ' XXXX ',
                       '   X  ']))

# These "asserts" are used for self-checking
assert nonogram_encode([" X X ", "X X X", " X X "]) == [
    [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
    [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
]
assert nonogram_encode(["X"]) == [[[1]], [[1]]]
assert nonogram_encode(['XX   X', ' X XXX', ' X XX ', ' XXX  ', ' XXXX ', '   X  ']) == [
    [[0, 0, 0, 0, 2, 0], [1, 5, 2, 5, 1, 2]],
    [[2, 1], [1, 3], [1, 2], [0, 3], [0, 4], [0, 1]]
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
