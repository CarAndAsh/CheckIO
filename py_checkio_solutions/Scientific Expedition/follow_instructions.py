#!/usr/bin/env checkio --domain=py run follow-instructions
def follow(instructions: str) -> tuple[int, int] | list[int]:
    if instructions:
        pos = [0, 0]
        for cmnd in instructions:
            if cmnd == 'f':
                pos[1] += 1
            elif cmnd == 'b':
                pos[1] -= 1
            elif cmnd == 'r':
                pos[0] += 1
            elif cmnd == 'l':
                pos[0] -= 1
        return pos
    return (0, 0)


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
