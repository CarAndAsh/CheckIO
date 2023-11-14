#!/usr/bin/env checkio --domain=py run most-wanted-letter
from collections import Counter


def checkio(text: str) -> str:
    if text:
        char_counter = Counter(sorted(list(filter(lambda x: x.isalpha(),text.lower())), key=lambda x: ord(x)))
        return char_counter.most_common(1)[0][0]
    return ""


print("Example:")
print(checkio("Hello World!"))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
