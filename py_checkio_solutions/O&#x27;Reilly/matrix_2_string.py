#!/usr/bin/env checkio --domain=py run matrix-2-string
from string import ascii_lowercase as lc
Row = tuple[int, int, int, int, int]
Grid = tuple[Row, Row, Row, Row, Row]


def converter(matrix: Grid) -> str:
    return ''.join(lc[(ii + len(row) * ri)-1] if item == 1 else lc[(ii + len(row) * ri)-1].upper() for ri, row in enumerate(matrix) for ii, item in enumerate(row, 1) if item)


print("Example:")
print(
    converter(
        (
            (0, 0, 1, 0, 0),
            (0, 1, 0, 1, 0),
            (1, 0, 2, 0, 1),
            (0, 1, 0, 1, 0),
            (0, 0, 1, 0, 0),
        )
    )
)

# These "asserts" are used for self-checking
assert (
        converter(
            (
                (0, 0, 1, 0, 0),
                (0, 1, 0, 1, 0),
                (1, 0, 2, 0, 1),
                (0, 1, 0, 1, 0),
                (0, 0, 1, 0, 0),
            )
        )
        == "cgikMoqsw"
)
assert (
        converter(
            (
                (1, 0, 1, 0, 1),
                (0, 2, 0, 2, 0),
                (1, 0, 1, 0, 1),
                (0, 2, 0, 2, 0),
                (1, 0, 1, 0, 1),
            )
        )
        == "aceGIkmoQSuwy"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
