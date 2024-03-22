#!/usr/bin/env checkio --domain=py run factorial-zeros
def fact_zeros(n: int) -> int:
    zero_count = 0
    while n > 1:
        zero_count += n // 5
        n //= 5
    return zero_count


print("Example:")
print(fact_zeros(2000))

# These "asserts" are used for self-checking
assert fact_zeros(2) == 0
assert fact_zeros(5) == 1
assert fact_zeros(20) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
