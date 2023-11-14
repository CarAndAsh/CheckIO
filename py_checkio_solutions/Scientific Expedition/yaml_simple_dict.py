def yaml(data: str) -> dict:
    data_gen = (tuple(pair.split(': ')) for pair in data.split('\n') if pair)
    return {key: int(value) if value.isdigit() else value for key, value in data_gen}


print("Example:")
print(
    yaml("name: Alex Fox\nage: 12\n\nclass: 12b")
)

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
