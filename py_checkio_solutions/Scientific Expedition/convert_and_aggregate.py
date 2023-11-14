def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    if data:
        res_dict = {}
        pairs = (pair for pair in data)
        for key, value in data:
            res_dict[key] = res_dict.get(key, 0) + value
            if res_dict[key] == 0 or not key:
                res_dict.pop(key)
        return res_dict
    return {}


print("Example:")
print(conv_aggr([("a", 5), ("", 15)]))

# These "asserts" are used for self-checking
assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")
