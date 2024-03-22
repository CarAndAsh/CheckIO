#!/usr/bin/env checkio --domain=py run revorse-the-vewels
VOWELS = 'aeiouAEIOU'


def reverse_vowels(text: str) -> str:
    i = 0
    j = len(text)
    while i < j:
        if text[i] in VOWELS:
            j -= 1
            while text[j] not in VOWELS:
                j -= 1
            if i != j:
                text = text[:i] + (text[j].upper() if text[i] in VOWELS[5:] else text[j].lower()) + text[i + 1:j] + (text[i].upper() if text[j] in VOWELS[5:] else text[i].lower()) + text[j + 1:]
        i += 1
    print(text)
    return text


print("Example:")
print(reverse_vowels("Hello, World"))

# These "asserts" are used for self-checking
assert reverse_vowels("Bengt Hilgursson") == "Bongt Hulgirssen"
assert (
        reverse_vowels("Why do you laugh? I chose death.")
        == "Why da yee loigh? U chasu dooth."
)
assert (
        reverse_vowels("These are the people you protect with your pain!")
        == "Thisa uro thi peoplu yoe protect weth year peen!"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
