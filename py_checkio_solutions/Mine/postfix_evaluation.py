#!/usr/bin/env checkio --domain=py run postfix-evaluation
def postfix_evaluate(items: list[int | str]) -> int:
    num_stack = []
    for i in items:
        if isinstance(i, int):
            num_stack.append(i)
        else:
            sec_num = str(num_stack.pop())
            first_num = str(num_stack.pop())
            if sec_num == '0' and i == '/':
                num_stack.append(0)
            else:
                num_stack.append(eval(first_num + ('//' if i == '/' else i) + sec_num))
    return num_stack[0]


print("Example:")
# print(postfix_evaluate([1, 2, "+"]))

# These "asserts" are used for self-checking
assert postfix_evaluate([2, 3, "+", 4, "*"]) == 20
assert postfix_evaluate([2, 3, 4, "*", "+"]) == 14
assert postfix_evaluate([3, 3, 3, "-", "/", 42, "+"]) == 42

print("The mission is done! Click 'Check Solution' to earn rewards!")
