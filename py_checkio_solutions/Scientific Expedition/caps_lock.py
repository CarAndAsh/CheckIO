#!/usr/bin/env checkio --domain=py run caps-lock
def caps_lock(text: str) -> str:
    return "".join([string.upper() if i % 2 != 0 else string for i, string in enumerate(text.split('a'))])


print("Example:")
print(caps_lock("Why are you asking me that?"))

# These "asserts" are used for self-checking
assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"

print("The mission is done! Click 'Check Solution' to earn rewards!")
