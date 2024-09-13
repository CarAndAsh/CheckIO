#!/usr/bin/env checkio --domain=py run good-radix
from string import ascii_uppercase


def checkio(number):
    digit_tpl = tuple(map(lambda ch: int(ch) if ch.isdigit() else (10 + ascii_uppercase.index(ch)), number))
    dec_num = sum(digit_tpl)
    base = max(digit_tpl) + 1
    while dec_num % (base - 1) and base <= 10 + len(ascii_uppercase):
        base += 1
    return base if base <= 10 + len(ascii_uppercase) else 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio('IDDQD'))
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k is not exist"
    print('Local tests done')
