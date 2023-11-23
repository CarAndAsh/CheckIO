#!/usr/bin/env checkio --domain=py run fizz-buzz
def checkio(number: int) -> str:
    if not (number % 3) and not (number % 5):
        return 'Fizz Buzz'
    elif not number % 3:
        return 'Fizz'
    elif not number % 5:
        return 'Buzz'
    return f"{number}"


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
