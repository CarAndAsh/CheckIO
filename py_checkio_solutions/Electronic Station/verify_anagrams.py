#!/usr/bin/env checkio --domain=py run verify-anagrams
def verify_anagrams(text_1: str, text_2: str) -> bool:
    chars = [list(filter(lambda ch: ch != ' ', text.lower())) for text in (text_1, text_2)]
    return sorted(chars[0]) == sorted(chars[1])


print("Example:")
print(verify_anagrams("Programming", "Gram Ring Mop"))

assert verify_anagrams("Programming", "Gram Ring Mop") == True
assert verify_anagrams("Hello", "Ole Oh") == False
assert verify_anagrams("Kyoto", "Tokyo") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
