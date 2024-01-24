#!/usr/bin/env checkio --domain=py run integer-palindrome
def int_palindrome(number: int, B: int) -> bool:
    num_in_b = []
    while number >= B:
        num_in_b.append(str(number % B))
        number = number // B
    num_in_b.append(str(number) if number else '')
    return num_in_b == num_in_b[::-1]


print("Example:")
print(int_palindrome(6, 2))

# These "asserts" are used for self-checking
assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True
assert int_palindrome(3148, 16) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
