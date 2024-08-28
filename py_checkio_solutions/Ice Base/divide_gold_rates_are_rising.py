#!/usr/bin/env checkio --domain=py run divide-gold-rates-are-rising
# Taken from mission Divide Gold

def winner_share(gold: int, sailors: int) -> int:
    sailors_initial = sailors
    while (gold_part := gold / (sailors + 2)) % 1 and sailors:
        if not (gold_part := gold / sailors) % 1 and sailors == sailors_initial:
            return int(gold_part)
        sailors -= 1
    return int(gold_part) * 2 if sailors else gold


print("Example:")
print(winner_share(100, 11))

# These "asserts" are used for self-checking
assert winner_share(15, 4) == 6
assert winner_share(16, 4) == 4
assert winner_share(100, 11) == 20
assert winner_share(15, 1) == 10
assert winner_share(28, 2) == 14
assert winner_share(54, 4) == 18
assert winner_share(1051, 38) == 1051

print("The mission is done! Click 'Check Solution' to earn rewards!")
