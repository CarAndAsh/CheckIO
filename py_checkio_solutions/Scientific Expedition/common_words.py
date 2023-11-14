#!/usr/bin/env checkio --domain=py run common-words
from collections import Counter


def checkio(line1: str, line2: str) -> str:
    if line1 and line2:
        word_counter = Counter(line1.split(',')+line2.split(','))
        return ','.join(sorted(word for word in word_counter if word_counter[word] == 2))
    return ""


print("Example:")
print(checkio("hello,world", "hello,earth"))

# These "asserts" are used for self-checking
assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

print("The mission is done! Click 'Check Solution' to earn rewards!")
