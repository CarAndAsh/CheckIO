#!/usr/bin/env checkio --domain=py run write-quadratic-equation
def quadr_equation(data: list[int]) -> str:
    a, b, с = data[0], data[0] * (data[1] + (data[2] if len(data) == 3 else data[1])), data[0] * data[1] * (data[2] if len(data) == 3 else data[1])
    return f"{('-' if a < 0 else '')}" \
           f"{(str(a)[1:] if a < 0 else str(a))+'*' if abs(a) != 1 else ''}x**2" \
           f"{(' + ' if b <= 0 else ' - ') if b != 0 else ''}" \
           f"{((str(b)[1:] if b < 0 else str(b))+'*' if abs(b) != 1 else '' )+'x' if b != 0 else ''}" \
           f"{(' - ' if с < 0 else ' + ') if с != 0 else ''}" \
           f"{(str(с)[1:] if с < 0 else str(с)) if с != 0 else ''} = 0"


print("Example:")
print(quadr_equation([-2, 4, 6]))

# These "asserts" are used for self-checking
assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
assert quadr_equation([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"
assert quadr_equation([2, 0]) == "2*x**2 = 0"
assert quadr_equation([2, 4]) == "2*x**2 - 16*x + 32 = 0"

print("The mission is done! Click 'Check Solution' to earn rewards!")
