#!/usr/bin/env checkio --domain=py run number-radix
from string import digits, ascii_uppercase


class Scale:
    SYMBOLS = digits + ascii_uppercase

    def __init__(self, radix, str_numer):
        self.radix = radix
        self.str_num = str_numer
        self.symbs = self.SYMBOLS[:self.radix]

    def __enter__(self):
        if all(map(lambda x: x in self.symbs, self.str_num)):
            return sum([(self.symbs.index(symb) * (self.radix ** (pow)))for pow, symb in enumerate(reversed(self.str_num))])
        return -1

    def __exit__(self, type, value, traceback):
        return False


def checkio(str_number: str, radix: int) -> int:
    with Scale(radix, str_number) as scale:
        return scale


if __name__ == '__main__':
    print('Example:')
    print(checkio("AF", 11))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
