#!/usr/bin/env checkio --domain=py run perfect-number-checking
def is_perfect(n: int) -> bool:
    return n == sum([divisor for divisor in range(1, n//2+1) if n % divisor == 0])


print("Example:")
print(is_perfect(3))

# These "asserts" are used for self-checking
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False
assert is_perfect(496) == True
assert is_perfect(30) == False
assert is_perfect(8128) == True
assert is_perfect(100) == False
assert is_perfect(500) == False
assert is_perfect(1000) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
