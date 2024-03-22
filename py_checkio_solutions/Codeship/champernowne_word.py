#!/usr/bin/env checkio --domain=py run champernowne-word
def num_gen():
    i = 0
    while True:
        i += 1
        yield str(i)


def counting_series(n: int) -> int:
    number_gen = iter(num_gen())
    num = next(number_gen)
    while n >= len(num):
        n -= len(num)
        num = next(number_gen)
    return int(num[n])


print("Example:")
print(counting_series(1))

# These "asserts" are used for self-checking
assert counting_series(0) == 1
assert counting_series(10) == 0
assert counting_series(100) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
