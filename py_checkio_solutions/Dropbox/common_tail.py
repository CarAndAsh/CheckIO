#!/usr/bin/env checkio --domain=py run common-tail
def common_tail(a: list[int], b: list[int]) -> int | None:
    last_common = None
    a.reverse()
    b.reverse()
    for num_pair in zip(a, b):
        if num_pair[0] == num_pair[1]:
            last_common = num_pair[0]
        else:
            return last_common
    return last_common


print("Example:")
print(common_tail([1, 2, 3, 4], [5, 6, 3, 4]))

# These "asserts" are used for self-checking
assert common_tail([], [1, 2, 3]) == None
assert common_tail([1], [1]) == 1
assert common_tail([3], [1, 2, 3]) == 3
assert common_tail([1, 2, 3, 4, 5], [1, 7, 3, 4, 5]) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
