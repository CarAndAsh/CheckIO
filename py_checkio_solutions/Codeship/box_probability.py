#!/usr/bin/env checkio --domain=py run box-probability


def checkio(marbles: str, step: int, to_round=True) -> float:
        if step == 1:
            return (marbles.count('w') / len(marbles))

        elif any(map(lambda ch: marbles.count(ch) == len(marbles), ('w', 'b'))):
            res = checkio(marbles.replace('w', 'b', 1), step - 1, False) if marbles.count('w') == len(marbles) \
                else checkio(marbles.replace('b', 'w', 1), step - 1, False)

        else:
            res = checkio(marbles.replace('w', 'b', 1), step - 1, False) * marbles.count('w')/len(marbles) \
                  + checkio(marbles.replace('b', 'w', 1), step - 1, False) * marbles.count('b')/len(marbles)
        return round(res, 2) if to_round else res



    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    print("Example:")
    print(checkio('wwwwwwwwwwwwwwwwwwww', 20)) #0.57

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
