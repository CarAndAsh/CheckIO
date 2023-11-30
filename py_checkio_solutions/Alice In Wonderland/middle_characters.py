#!/usr/bin/env checkio --domain=py run middle-characters
def middle(text: str) -> str:
    return text[len(text)//2] if len(text) % 2 else text[len(text)//2-1:len(text)//2+1]


print("Example:")
print(middle("example"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")
