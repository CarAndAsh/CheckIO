#!/usr/bin/env checkio --domain=py run yaml-more-types
import re


def yaml(data: str) -> dict:
    # your code here
    res = {}
    data_gen = (tuple(pair.split(':')) for pair in data.split('\n') if pair)
    for key, value in data_gen:
        value = value.strip()
        try:
            value_type = eval(f'type({value.title() if value.isalpha() else value})')
        except (SyntaxError, NameError, TypeError):
            value_type = type(value)

        if value_type is bool:
            res[key] = eval(f'{value.title()}')
        elif value.lower() in ('', 'null'):
            res[key] = None
        else:
            value = re.sub('(^[\'\"]|[\'\"]$)', '', value)
            value = value.replace('\\', '')
            res[key] = value_type(value)
    return res


print("Example:")
print(yaml('name: "Bob Dylan"\nchildren: 6\nalive: false'))

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {
    "name": 'Alex "Fox"',
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Bob Dylan"\nchildren: 6\nalive: false') == {
    "name": "Bob Dylan",
    "children": 6,
    "alive": False,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding:') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": "null",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
