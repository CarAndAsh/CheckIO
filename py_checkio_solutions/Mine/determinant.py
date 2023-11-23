#!/usr/bin/env checkio --domain=py run determinant
def checkio(data):
    if len(data[0]) == 1:
        return data[0][0]
    elif len(data[0]) == 2:
        return (data[0][0] * data[1][1]) - (data[0][1] * data[1][0])
    else:
        return sum([((-1) ** n) * el * checkio([line[:n] + line[n + 1:] for line in data[1:]]) for n, el in enumerate(data[0])])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio([[4, 3], [6, 3]]) == -6, "First example"
    assert checkio([[1, 3, 2], [1, 1, 4], [2, 2, 1]]) == 14, "Second example"
