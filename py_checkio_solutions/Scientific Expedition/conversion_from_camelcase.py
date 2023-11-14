#!/usr/bin/env checkio --domain=py run conversion-from-camelcase
def from_camel_case(name: str) -> str:
    if name:
        return "".join(char if char.islower() else '_'+char.lower() for char in name)[1:]
    return ""


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
