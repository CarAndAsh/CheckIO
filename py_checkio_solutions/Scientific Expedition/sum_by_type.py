#!/usr/bin/env checkio --domain=py run sum-by-type
def sum_by_types(items: list[str, int]) -> tuple[str, int] | list[str, int]:
    if items:
        res = ["", 0]
        for char in items:
            if isinstance(char, str):
                res[0] += char
            else:
                res[1] += char

        return res
    return ["", 0]


print("Example:")
print(list(sum_by_types([])))

assert list(sum_by_types([])) == ["", 0]
assert list(sum_by_types([1, 2, 3])) == ["", 6]
assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
assert list(sum_by_types(["1", "2", 3])) == ["12", 3]
assert list(sum_by_types(["1", "2", "3"])) == ["123", 0]
assert list(sum_by_types(["size", 12, "in", 45, 0])) == ["sizein", 57]

print("The mission is done! Click 'Check Solution' to earn rewards!")
