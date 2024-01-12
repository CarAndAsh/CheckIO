#!/usr/bin/env checkio --domain=py run reverse-integer
def reverse_digits(num: int) -> int:
    text_num = str(num)
    return int(text_num[-1::-1]) if text_num[0].isdigit() else int(text_num[0]+text_num[-1:0:-1])


print("Example:")
print(reverse_digits(32))

# These "asserts" are used for self-checking
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5
assert reverse_digits(-9) == -9
assert reverse_digits(100) == 1
assert reverse_digits(-100) == -1
assert reverse_digits(54321) == 12345
assert reverse_digits(1111) == 1111
assert reverse_digits(987654321) == 123456789

print("The mission is done! Click 'Check Solution' to earn rewards!")
