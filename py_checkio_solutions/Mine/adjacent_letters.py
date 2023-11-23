#!/usr/bin/env checkio --domain=py run adjacent-letters
def adjacent_letters(line: str) -> str:
    res = ''
    for char in line:
        if res and char == res[-1]:
            res = res[:-1]
        else:
            res += char
    return res


print("Example:")
print(adjacent_letters("abbaca"))

# These "asserts" are used for self-checking
assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
