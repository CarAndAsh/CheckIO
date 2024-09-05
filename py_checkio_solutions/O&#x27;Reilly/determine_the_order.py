from itertools import chain


def checkio(data: list[str]) -> str:
    res = ''
    letter_lst = sorted(set(chain(*data)))

    while letter_lst:
        char = letter_lst.pop(0)
        if all(map(lambda word: char not in word or char == word[0], data)):
            res += char
            for i, word in enumerate(data):
                data[i] = word.replace(char, '')
        else:
            letter_lst.append(char)
    return res


print("Example:")
print(checkio(["acb", "bd", "zwa"]))

# These "asserts" are used for self-checking
assert checkio(["acb", "bd", "zwa"]) == "zwacbd"
assert checkio(["klm", "kadl", "lsm"]) == "kadlsm"
assert checkio(["a", "b", "c"]) == "abc"
assert checkio(["aazzss"]) == "azs"
assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg"
assert checkio(["hello", "low", "lino", "itttnosw"]) == "helitnosw"
assert checkio(["my", "name", "myke"]) == "namyke"
assert checkio(["xxxyyz", "yyww", "wwtt", "ttzz"]) == "xywtz"
assert checkio(["axton", "bxton"]) == "abxton"
assert checkio(["is", "not", "abc", "nots", "iabcn"]) == "iabcnots"
assert checkio(["qwerty", "asdfg", "zxcvb", "yagz"]) == "qwertyasdfgzxcvb"
