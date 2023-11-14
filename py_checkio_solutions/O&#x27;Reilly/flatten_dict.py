#!/usr/bin/env checkio --domain=py run flatten-dict
def flatten(dictionary: dict[str, str | dict]) -> dict[str, str]:
    # your code here
    if dictionary:
        res = {}
        for key, val in dictionary.items():
            if val and isinstance(val, dict):
                for inner_key, inner_val in flatten(val).items():
                    res[key+'/'+inner_key] = inner_val
            else:
                res[key] = dictionary.get(key, '') or ''
        return res
    return {}

print("Example:")
print(flatten({"key": "value"}))

# These "asserts" are used for self-checking
assert flatten({"key": "value"}) == {"key": "value"}
assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
    "key/deeper/more/enough": "value"
}
assert flatten({"empty": {}}) == {"empty": ""}
assert flatten(
    {
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }
) == {
    "name/first": "One",
    "name/last": "Drone",
    "job": "scout",
    "recent": "",
    "additional/place/zone": "1",
    "additional/place/cell": "2",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
