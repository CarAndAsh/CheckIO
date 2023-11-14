#!/usr/bin/env checkio --domain=py run hidden-word
def checkio(text, word):
    res = []
    if text and word:
        coords = []
        chars = text.replace(' ', '').lower().split('\n')
        for i, line in enumerate(chars):
            ch_line = line
            while word[0] in ch_line:
                coords.append((i, ch_line.index(word[0])))
                ch_line = ch_line.replace(word[0], '*', 1)
        for i, j in coords:
            row_check = ''
            col_check = ''
            if len(chars[i][j:]) >= len(word):
                for k in range(len(word)):
                    row_check += chars[i][j + k]
            if len(chars[i:]) >= len(word):
                for k in range(len(word)):
                    if len(chars[i + k]) > j:
                        col_check += chars[i + k][j]
                    else:
                        break
            if row_check == word:
                res.extend([i + 1, j + 1, i + 1, j + len(word)])
                break
            elif col_check == word:
                res.extend([i + 1, j + 1, i + len(word), j + 1])
                break
    return res


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert (
        checkio(
            """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""",
            "noir",
        )
        == [4, 16, 7, 16]
    )
    assert (
        checkio(
            """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""",
            "ten",
        )
        == [2, 14, 2, 16]
    )
print("Coding complete? Click 'Check' to earn cool rewards!")
