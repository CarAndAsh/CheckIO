#!/usr/bin/env checkio --domain=py run roman-numerals
from collections import OrderedDict


def checkio(number):
    reptbl = {'I': 1, 'X': 10, 'C': 100, 'M': 1000}
    not_reptbl = {'V': 5, 'L': 50, 'D': 500}
    reptbl_not_reptbl = {'IV': 4, 'XL': 40, 'CD': 400}
    reptbl_reptbl = {'IX': 9, 'XC': 90, 'CM': 900}
    roman_nums = reptbl | not_reptbl | reptbl_not_reptbl | reptbl_reptbl
    number_dict = OrderedDict()
    while number:
        max_roman = max(roman_nums.items(), key=lambda x: x[1])
        if number < max_roman[1]:
            roman_nums.pop(max_roman[0])
        else:
            number -= max_roman[1]
            number_dict[max_roman[0]] = number_dict.setdefault(max_roman[0], 0) + 1
    res = ''.join(num * count for num, count in number_dict.items())
    return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
