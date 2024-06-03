#!/usr/bin/env checkio --domain=py run the-nearest-square-number
nearest_square = lambda num: (d[0] + 1) ** 2 if (d := divmod(num ** 0.5, 1))[1] > 0.5 else d[0] ** 2


print("Example:")
print(nearest_square(8))

# These "asserts" are used for self-checking
assert nearest_square(8) == 9
assert nearest_square(13) == 16

print("The mission is done! Click 'Check Solution' to earn rewards!")
