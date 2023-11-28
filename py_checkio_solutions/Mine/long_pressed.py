#!/usr/bin/env checkio --domain=py run long-pressed
def long_pressed(text: str, typed: str) -> bool:
    prev_char = ''
    if text == typed:
        return False
    while text:
        while typed[0] != text[0]:
            if typed[0] == prev_char:
                typed = typed[1:]
            else:
                return False
        prev_char = text[0]
        text = text[1:]
        typed = typed[1:]
    return not bool(typed)


print("Example:")
print(long_pressed("alex", "aaleex"))

# These "asserts" are used for self-checking
# assert long_pressed("no, we don't have assignments", "no, we don't have asssignments") == True
assert long_pressed("alex", "aaleex") == True
assert long_pressed("welcome to checkio", "weeeelcome to cccheckio") == True
assert long_pressed("there is an error here", "there is an errorrr hereaa") == False
assert long_pressed("hi, my name is...", "hi, my name is...") == False
assert long_pressed('anagram', 'anagram') == False
assert long_pressed('welcome boss!', 'welcooome bos!!') == False
print("The mission is done! Click 'Check Solution' to earn rewards!")
