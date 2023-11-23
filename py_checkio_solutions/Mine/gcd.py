#!/usr/bin/env checkio --domain=py run gcd
def greatest_common_divisor(*args: int) -> int:
    data = list(args)
    while len(data) != 1:
        data.sort()
        b = data.pop(0)
        if b != 0:
            data = list(map(lambda x: x % b, data))
            data.append(b)
    return data[0]


if __name__ == "__main__":
    print("Example:")
    print(greatest_common_divisor(8, 2, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert greatest_common_divisor(6, 4) == 2
    assert greatest_common_divisor(2, 4, 8) == 2
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1
    assert greatest_common_divisor(3, 9, 3, 9) == 3
    assert greatest_common_divisor(2226172404, 2652430846, 3702223254, 3260139372, 2021191608) == 2
    assert greatest_common_divisor(210, 330, 462, 770) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
