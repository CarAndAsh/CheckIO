#!/usr/bin/env checkio --domain=py run bird-language
def translate(text: str) -> str:
    if text:
        res = ''
        char_gen = (char for char in text)
        for char in char_gen:
            if char in 'aeiouy':
                res += char
                next(char_gen)
                next(char_gen)
            elif char.isalpha():
                res += char
                next(char_gen)
            else:
                res += char
        return res
    return ""


print("Example:")
print(translate("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
