#!/usr/bin/env checkio --domain=py run yaml-list-and-comments
# Taken from mission YAML. More Types
import re


def yaml(data: str) -> dict:
    bool_dict = {'false': False, 'true': True, 'null': None, '': None}
    cast_to_type = lambda line: bool_dict[line] if line in bool_dict else (int(line) if line.isdigit() else line.replace('\\"', '@').replace('"', '').replace('@', '"'))
    # separate one-line data on non-empty lines and without '-'
    data_1 = map(lambda line: line[1:] if line.startswith('-') else line, filter(lambda x: x, data.split('\n')))
    # if '#' in line return text before this or if '#' in line with quotes return all line
    data_2 = map(lambda line: (re.findall('".*"', line) or re.findall('.*#', line))[0] if '#' in line else line, data_1)
    # lines that not consist of only '#' and without spaces and not ended on '#'
    data_3 = list(map(lambda line: line[:-1].strip() if line.endswith('#') else line.strip(), filter(lambda line: line != '#', data_2)))
    if all(map(lambda line: ':' in line, data_3)):
        # pack in list striped lines and casting them to types
        res ={key: cast_to_type(value.strip()) for key, value in map(lambda line: tuple(line.split(':')),data_3)}
    else:
        # pack in list striped lines and casting them to types
        res = [cast_to_type(line) for line in data_3]
    return res


print("Example:")
print(yaml('- write some\n- "Alex Chii #sir"\n- 89'))

# These "asserts" are used for self-checking
assert yaml('- write some\n- "Alex Chii"\n- 89') == ["write some", "Alex Chii", 89]
assert yaml("- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5") == [1, 2, 3, 4, 5]
assert yaml("-\n-\n-\n- 7") == [None, None, None, 7]
assert yaml('# comment\n- write some # after\n# one mor\n- "Alex Chii #sir "\n- 89 #bl') == ["write some", "Alex Chii #sir ", 89]


assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {"name": "Alex Fox", "age": 12, "class": "12b",}
assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {"name": "Alex Fox", "age": 12, "class": "12b",}
assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {"name": 'Alex "Fox"', "age": 12, "class": "12b",}
assert yaml('name: "Bob Dylan"\nchildren: 6\nalive: false') == {"name": "Bob Dylan", "children": 6, "alive": False,}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding:') == {"name": "Bob Dylan", "children": 6, "coding": None,}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null') == {"name": "Bob Dylan", "children": 6, "coding": None,}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ') == {"name": "Bob Dylan", "children": 6, "coding": "null",}

print("The mission is done! Click 'Check Solution' to earn rewards!")
