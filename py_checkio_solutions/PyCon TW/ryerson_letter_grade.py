#!/usr/bin/env checkio --domain=py run ryerson-letter-grade
# feel free to change table structure in any way
LETTERS = [ch + sign for ch in "ABCD" for sign in ("+", "", "-")] + ["F"]
MIN_PERCENTAGES = 90, 85, 80, 77, 73, 70, 67, 63, 60, 57, 53, 50, 0


def ryerson_letter_grade(pct: int) -> str:
    return LETTERS[sum(map(lambda num: pct < num, MIN_PERCENTAGES))]


print("Example:")
print(ryerson_letter_grade(57))

assert ryerson_letter_grade(45) == "F"
assert ryerson_letter_grade(62) == "C-"

print("The mission is done! Click 'Check Solution' to earn rewards!")
