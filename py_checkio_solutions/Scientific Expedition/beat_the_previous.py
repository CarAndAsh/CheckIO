def beat_previous(digits: str) -> list[int]:
    el = ''
    res = []
    for char in digits:
        el += char
        if not res or int(el) > int(res[-1]):
            res.append(int(el))
            el = ''
    return res

print("Example:")
print(beat_previous("123"))

# These "asserts" are used for self-checking
assert beat_previous("600005") == [6]
assert beat_previous("6000050") == [6, 50]
assert beat_previous("045349") == [0, 4, 5, 34]
assert beat_previous("77777777777777777777777") == [7, 77, 777, 7777, 77777, 777777]

print("The mission is done! Click 'Check Solution' to earn rewards!")
