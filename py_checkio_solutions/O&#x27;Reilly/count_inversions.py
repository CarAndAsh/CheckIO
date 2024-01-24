#!/usr/bin/env checkio --domain=py run count-inversions
def count_inversion(sequence):
    """
    Count inversions in a sequence of numbers
    """
    c = 0
    sequence = list(sequence)
    while sequence != sorted(sequence):
        for i in range(len(sequence) - 1):
            if sequence[i] > sequence[i + 1]:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                c += 1
    return c


if __name__ == "__main__":
    print("Example:")
    print(count_inversion([1, 2, 5, 3, 4, 7, 6]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
