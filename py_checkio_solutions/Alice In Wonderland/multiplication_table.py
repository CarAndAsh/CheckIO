#!/usr/bin/env checkio --domain=py run multiplication-table
def checkio(first, second):
    first_bin, second_din = bin(first)[2:], bin(second)[2:]  # binary expression of numbers in text without sign bit and number system literal
    and_sum = 0
    or_sum = 0
    xor_sum = 0
    and_num = ''
    or_num = ''
    xor_num = ''
    for digit in first_bin:
        for digit_2 in second_din:
            and_num += str(int(digit) and int(digit_2))
            or_num += str(int(digit) or int(digit_2))
            xor_num += str(0 if int(digit) == int(digit_2) else 1)
        and_sum += int(and_num, 2)
        or_sum += int(or_num, 2)
        xor_sum += int(xor_num, 2)
        and_num = ''
        or_num = ''
        xor_num = ''
    return and_sum + or_sum + xor_sum


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
