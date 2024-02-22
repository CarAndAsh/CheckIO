#!/usr/bin/env checkio --domain=py run wrong-family
def is_family(tree: list[list[str]]) -> bool:
    dads = set()
    sons = set()
    for dad, son in tree:
        if [son, dad] in tree or (son in sons):
            return False
        dads.add(dad)
        sons.add(son)
    if len(dads) > 1:
        return not bool(len(dads) - len(dads & sons) - 1)
    return True


print("Example:")
print(is_family([["Logan", "Mike"]]))

assert is_family([["Logan", "Mike"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Alexander"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Logan"]]) == False
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Jack"]]) == False
assert is_family([["Logan", "William"], ["Logan", "Jack"], ["Mike", "Alexander"]]) == False
assert is_family([["Jack", "Mike"], ["Logan", "Mike"], ["Logan", "Jack"]]) == False
assert is_family([['Logan', 'Mike'], ['Alexander', 'Jack'], ['Jack', 'Logan']]) == True
assert is_family([['Logan', 'Mike'], ['Alexander', 'Jack'], ['Jack', 'Logan'], ['Alex', 'Bob']]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
