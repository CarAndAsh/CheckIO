#!/usr/bin/env checkio --domain=py run cut-sentence
def cut_sentence(line: str, length: int) -> str:
    if length >= len(line):
        return line
    elif length < len(line) and line[length].isspace() or length == 0:
        return line[:length] + '...'
    return cut_sentence(line, length - 1)


print("Example:")
print(cut_sentence("Hi my name is Alex", 24))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")
