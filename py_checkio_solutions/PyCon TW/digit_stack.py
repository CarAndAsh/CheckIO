#!/usr/bin/env checkio --domain=py run digit-stack
def digit_stack(commands):
    nums = []
    res = 0
    for cmd in commands:
        if cmd.startswith('PUSH'):
            nums.append(int(cmd.split()[-1]))
        elif cmd == 'POP':
            if nums:
                res += nums.pop()
        elif cmd == 'PEEK':
            if nums:
                res += nums[-1]
        else:
            raise SyntaxError(" Use commands only 'POP', 'PEEK', 'PUSH <number>'")
    return res


if __name__ == '__main__':
    print("Example:")
    print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                       "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
