#!/usr/bin/env checkio --domain=py run how-deep

def how_deep(structure: tuple) -> int:
    if isinstance(structure, tuple) and len(structure) > 0:
        return 1 + max(how_deep(item) for item in structure)
    elif isinstance(structure, tuple) and len(structure) == 0:
        return 1
    return 0


print("Example:")
print(how_deep(()))

# These "asserts" are used for self-checking
assert how_deep((1, 2, 3)) == 1
assert how_deep((1, 2, (3,))) == 2
assert how_deep((1, 2, (3, (4,)))) == 3
assert how_deep(()) == 1
assert how_deep(((),)) == 2
assert how_deep((((),),)) == 3
assert how_deep((1, (2,), (3,))) == 2
assert how_deep((1, ((),), (3,))) == 3
assert how_deep((1, (2,), (2, (3,)))) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
