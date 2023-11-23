#!/usr/bin/env checkio --domain=py run aggregate-by-operation
def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    agg_dict = {}
    for operation, num in data:
        if len(operation) > 1:
            if operation[0] == '+':
                agg_dict[operation[1:]] = agg_dict.get(operation[1:], 0) + num
            elif operation[0] == '-':
                agg_dict[operation[1:]] = agg_dict.get(operation[1:], 0) - num
            elif operation[0] == '*':
                agg_dict[operation[1:]] = agg_dict.get(operation[1:], 1) * num
            elif operation[0] == '/' and num > 0:
                agg_dict[operation[1:]] = agg_dict.get(operation[1:], 0) / num
            elif operation[0] == '=':
                agg_dict[operation[1:]] = num
        for key in agg_dict.copy():
            if agg_dict[key] == 0:
                agg_dict.pop(key)
    return agg_dict


print("Example:")
print(aggr_operation([("+a", 5), ("+a", -5), ("-c", 5), ("-a", -5),("+b", 5), ("+b", -5), ("-b", 5), ("-b", -5)]))

# These "asserts" are used for self-checking
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}
assert aggr_operation([('+a', 0), ('*b', 0), ('+', 35)]) == {}

print("The mission is done! Click 'Check Solution' to earn rewards!")
