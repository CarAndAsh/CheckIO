#!/usr/bin/env checkio --domain=py run checking-perfect-power
from math import log


def perfect_power(n: int) -> bool:
    for base in range(2, int(n ** 0.5) + 1):
        power = log(n, base)
        if power % 1 == 0:
            return not bool((n - int(base**power)) % 2)
    return False


print("Example:")
print(perfect_power(8))
#
# These "asserts" are used for self-checking
assert perfect_power(8) == True
assert perfect_power(42) == False
assert perfect_power(441) == True
assert perfect_power(469097433) == True
assert perfect_power(4922235242952026704037113243122008064) == True
assert perfect_power(4922235242952026704037113243122008063) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
