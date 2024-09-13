#!/usr/bin/env checkio --domain=py run stressful-subject
import re


def is_stressful(subj: str) -> bool:
    """
    recognize stressful subject
    """
    return True if re.match('(.*?h+?\S??e+?\S??l+?\S??p+?\S*?)|(.*?a+?\S??s+?\S??a+?\S??p+?\S*?)|(.*?u+?\S??r+?\S??g+?\S??e+?\S??n+?\S??t+?\S*?)|(.*?[!]{3}\Z)',subj.lower()) or subj.isupper() else False


print("Example:")
print(is_stressful("!!!!!Hi aaaa!!!"))

assert is_stressful("Hi") == False
assert is_stressful("I neeed HELP") == True
assert is_stressful("I neeed HLEP") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
