#!/usr/bin/env checkio --domain=py run excel-column-number
import string


def column_number(name: str) -> int:
    return sum((string.ascii_uppercase.index(ch) + 1) * 26 ** i for i, ch in enumerate(name[::-1]))


print("Example:")
print(column_number("AB"))

# These "asserts" are used for self-checking
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701

print("The first mission is done! Click 'Check' to earn cool rewards!")
