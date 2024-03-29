#!/usr/bin/env checkio --domain=py run non-empty-lines
def non_empty_lines(text: str) -> int:
    return len(list(filter(str.strip, text.split('\n')))) if text else 0


print("Example:")
print(non_empty_lines("one simple line\n"))

# These "asserts" are used for self-checking
assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
