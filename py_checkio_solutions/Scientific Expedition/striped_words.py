#!/usr/bin/env checkio --domain=py run striped-words
import re
import string


def checkio(line: str) -> int:
    res = 0
    if line:
        vowels = 'aeouiy'
        consonant = 'bcdfghjklmnpqrstvwxz'
        for word in re.split(f'[{string.punctuation} ]', line):
            if word.isalpha() and len(word) > 1:
                if (all(map(lambda x: x in vowels, word.lower()[::2])) and all(
                        map(lambda x: x in consonant, word.lower()[1::2]))) or (
                        all(map(lambda x: x in vowels, word.lower()[1::2])) and all(
                        map(lambda x: x in consonant, word.lower()[::2]))):      
                    res += 1

    return res


print("Example:")
print(checkio("Dog,cat,mouse,bird.Human."))

# These "asserts" are used for self-checking
assert checkio("My name is ...") == 3
assert checkio("Hello world") == 0
assert checkio("A quantity of striped words.") == 1
assert checkio("Dog,cat,mouse,bird.Human.") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
