#!/usr/bin/env checkio --domain=py run is-string-a-number-part-ii
import re


def is_number(val: str) -> bool:
    return re.fullmatch('[+-]?((\d+[.]?\d*)|(\d*[.]\d+))', val) != None if val else False


print("Example:")
print(is_number("10"))

# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("+10.0") == True
assert is_number("1OOO") == False
assert is_number("1.") == True
assert is_number("+.l") == False
assert is_number("++1+.2-") == False
assert is_number("3e4") == False
assert is_number('+.123') == True
assert is_number('+.') == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
