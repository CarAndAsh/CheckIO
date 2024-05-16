#!/usr/bin/env checkio --domain=py run count-and-say
def count_and_say(digits: str) -> str:
    res = ''
    if digits:
        digit = digits[0]
        count = 0
        for d in digits:
            if d == digit:
                count += 1
            else:
                res += str(count) + digit
                count = 1
                digit = d
        res += str(count) + digit
    return res


print("Example:")
print(count_and_say("123"))

# These "asserts" are used for self-checking
assert count_and_say("333388822211177") == "4338323127"
assert count_and_say("1") == "11"
assert count_and_say("") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
