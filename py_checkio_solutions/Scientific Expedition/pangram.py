#!/usr/bin/env checkio --domain=py run pangram
def check_pangram(text: str) -> bool:
    alphabet_dict = {s: 0 for s in 'abcdefghijklmnopqrstuvwxyz'}
    for s in text:
        if s.isalpha():
            alphabet_dict[s.lower()] += 1
    if 0 not in alphabet_dict.values():
        return True
    return False


print("Example:")
print(check_pangram("The quick brown fox jumps over the lazy dog."))

# These "asserts" are used for self-checking
assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
assert check_pangram("ABCDEF") == False
assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
assert check_pangram("abcdefghijklmnopqrstuvwxy") == False
assert (
        check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!")
        == True
)
assert check_pangram("As quirky joke, chefs won't pay devil magic zebra tax.") == True
assert check_pangram("Six big devils from Japan quickly forgot how to walt.") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
