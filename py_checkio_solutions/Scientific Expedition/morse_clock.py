#!/usr/bin/env checkio --domain=py run morse-clock
def checkio(time_string: str) -> str:
    # your code here

    if time_string:
        res = []
        time_unit = ''
        time_list = [num.zfill(2) for num in time_string.split(':')]
        for num in time_list:
            time_unit = ''
            if time_list.index(num) == 0:
                time_unit += str(bin(int(num[0])))[2:].zfill(2).replace('0', '.').replace('1', '-') +' '+ str(bin(int(num[1])))[2:].zfill(4).replace('0', '.').replace('1', '-')
            else:
                time_unit += str(bin(int(num[0])))[2:].zfill(3).replace('0', '.').replace('1', '-') +' '+ str(bin(int(num[1])))[2:].zfill(4).replace('0', '.').replace('1', '-')
            res.append(time_unit)
        return ' : '.join(res)
    return ""


print("Example:")
print(checkio("10:37:49"))

# These "asserts" are used for self-checking
assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"
assert checkio("0:10:2") == ".. .... : ..- .... : ... ..-."

print("The mission is done! Click 'Check Solution' to earn rewards!")