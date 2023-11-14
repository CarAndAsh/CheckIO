#!/usr/bin/env checkio --domain=py run longest-substring-of-unique-characters
def longest_substr(s: str) -> int:
    # your code here
    if s:
        sub = ''
        res = 0
        for char in s:
            if char in sub:
                if res < len(sub):
                    res = len(sub)
                sub = sub[sub.index(char)+1:]
            sub += char
        return res if res > len(sub) else len(sub)
    return 0


print("Example:")
print(longest_substr("dvdf"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
