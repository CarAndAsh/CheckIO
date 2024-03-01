#!/usr/bin/env checkio --domain=py run string-2-matrix
from string import ascii_lowercase as lc, ascii_uppercase as uc
Row = tuple[int, int, int, int, int]
Grid = tuple[Row, Row, Row, Row, Row]


def converter(text: str) -> Grid:
    return tuple(tuple((2 if uch in text else 1) if any(map(lambda ch: ch in text, (uch, lch))) else 0 for lch, uch in zip(lc[ind*5:(ind+1)*5], uc[ind*5:(ind+1)*5])) for ind in range(5))


print("Example:")
print(converter("sMcigkqow"))

# These "asserts" are used for self-checking
assert converter("sMcigkqow") == (
    (0, 0, 1, 0, 0),
    (0, 1, 0, 1, 0),
    (1, 0, 2, 0, 1),
    (0, 1, 0, 1, 0),
    (0, 0, 1, 0, 0),
)
assert converter("acSyIwoQkumGe") == (
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1),
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
