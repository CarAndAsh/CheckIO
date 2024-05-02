#!/usr/bin/env checkio --domain=py run ugly-numbers
def ugly_number(n: int) -> int:
    ugly = [1]
    index_2_3_5 = [0] * 3

    next_mul_of_2_3_5 = [2, 3, 5]

    for index in range(1, n):

        # Choose the min value of all available multiples
        ugly.append(min(next_mul_of_2_3_5))

        # Increment the value of index accordingly
        for i, n in zip((0, 1, 2), (2, 3, 5)):
            if ugly[index] == next_mul_of_2_3_5[i]:
                index_2_3_5[i] += 1
                next_mul_of_2_3_5[i] = ugly[index_2_3_5[i]] * n

    return ugly[-1]


if __name__ == "__main__":
    print("Example:")
    print(ugly_number(1137))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ugly_number(4) == 4
    assert ugly_number(6) == 6
    assert ugly_number(11) == 15
    assert ugly_number(29) == 75
    print("Ugly Numbers coding complete? Click 'Check' to earn cool rewards!")
