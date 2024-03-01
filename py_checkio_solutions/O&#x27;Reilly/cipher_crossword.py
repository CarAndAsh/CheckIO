#!/usr/bin/env checkio --domain=py run cipher-crossword
import re


def checkio(crossword: list[list[int]], words: list[str]) -> list[list[str]]:

    def add_to_dict(num_key, char_to_add):
        if num_key in num_set and char_to_add in char_set:
            num_set.discard(num_key)
            char_set.discard(char_to_add)
            num_char_dict[num_key] = char_to_add

    def add_to_dict_lines(num_line):
        word_line = ' '.join(words)
        ch_line = ''.join(map(lambda num: num_char_dict[num] if num not in num_set else '.', num_line))
        if ch_line == '.' * len(num_line):
            words_in_nums.append(num_line)
        else:
            found_words = re.findall(ch_line, word_line)
            found_words.sort()
            found_word = found_words[0] if found_words else ' '
            if ' ' not in found_word:
                words.remove(found_word)
                for num_key, ch in zip(num_line, found_word):
                    add_to_dict(num_key, ch)

    num_set = set(num for line in crossword for num in line if num)
    char_set = set(char for word in words for char in word)
    num_char_dict = {0: ' '}
    '''Find corner values'''
    for _ in words:
        h_word = words.pop(0)
        for v_word in words:
            char_to_add, num_key = '', 0
            if h_word[0] == v_word[0]:
                num_key = crossword[0][0]
                char_to_add = h_word[0]
            elif h_word[0] == v_word[-1]:
                num_key = crossword[-1][0]
                char_to_add = h_word[0]
            elif h_word[-1] == v_word[0]:
                num_key = crossword[0][-1]
                char_to_add = h_word[-1]
            elif h_word[-1] == v_word[-1]:
                num_key = crossword[-1][-1]
                char_to_add = h_word[-1]
            add_to_dict(num_key, char_to_add)
        words.append(h_word)

    v_words_in_nums = [tuple(col[ind] for col in crossword) for ind, _ in enumerate(crossword[0]) if 0 not in crossword[ind]]
    words_in_nums = []
    for line in crossword:
        if 0 not in line:
            words_in_nums.append(line)
    words_in_nums.extend(v_words_in_nums)

    while words_in_nums:
        num_line = words_in_nums.pop(0)
        add_to_dict_lines(num_line)

    res = [list(map(lambda num: num_char_dict[num], line)) for line in crossword]
    return res


print("Example:")
print(
    checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6],
        ],
        ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
    )
)

# These "asserts" are used for self-checking
assert checkio(
    [
        [21, 6, 25, 25, 17],
        [14, 0, 6, 0, 2],
        [1, 11, 16, 1, 17],
        [11, 0, 16, 0, 5],
        [26, 3, 14, 20, 6],
    ],
    ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
) == [
           ["h", "e", "l", "l", "o"],
           ["a", " ", "e", " ", "z"],
           ["b", "i", "m", "b", "o"],
           ["i", " ", "m", " ", "n"],
           ["t", "r", "a", "c", "e"],
       ]
assert checkio(
    [
        [19, 26, 8, 25, 18],
        [24, 0, 24, 0, 8],
        [4, 24, 23, 21, 3],
        [3, 0, 26, 0, 13],
        [8, 6, 15, 17, 13],
    ],
    ["world", "rings", "tache", "water", "racon", "dress"],
) == [
           ["w", "o", "r", "l", "d"],
           ["a", " ", "a", " ", "r"],
           ["t", "a", "c", "h", "e"],
           ["e", " ", "o", " ", "s"],
           ["r", "i", "n", "g", "s"],
       ]
assert checkio([
                [14, 9, 24, 10, 14],
                [24, 0, 13, 0, 13],
                [13, 26, 13, 20, 18],
                [6, 0, 25, 0, 9],
                [14, 6, 9, 3, 14]
                ],
    ['sodas', 'loofa', 'slots', 'stars', 'ovoid', 'sales'],
) == [
            ['s', 'a', 'l', 'e', 's'],
            ['l', ' ', 'o', ' ', 'o'],
            ['o', 'v', 'o', 'i', 'd'],
            ['t', ' ', 'f', ' ', 'a'],
            ['s', 't', 'a', 'r', 's']
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
