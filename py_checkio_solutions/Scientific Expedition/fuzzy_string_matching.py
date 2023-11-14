#!/usr/bin/env checkio --domain=py run fuzzy-string-matching
def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    if all((str1, str2, threshold)):
        if threshold >= abs(len(str1) - len(str2)):
            for char1, char2 in zip(str1, str2):
                if char1 != char2:
                    threshold -= 1
        return threshold >= 0
    return False


print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
