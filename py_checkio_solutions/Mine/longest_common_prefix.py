#!/usr/bin/env checkio --domain=py run longest-common-prefix
def longest_prefix(arr: list[str]) -> str:
    if len(arr) == 1:
        return arr[0]
    elif '' in arr:
        return ""
    else:
        res = ''
        for ch in zip(*arr):
            if len(set(ch)) == 1:
                res += ch[0]
            else:
                return res
        return res


print("Example:")
print(longest_prefix(["flower", "flow", "flight"]))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")
