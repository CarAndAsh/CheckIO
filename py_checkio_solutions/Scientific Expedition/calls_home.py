#!/usr/bin/env checkio --domain=py run calls-home
from typing import List


def total_cost(calls: List[str]) -> int:
    res = 0
    if calls:
        call_dict = {}
        for call in calls:
            call = call.split()
            min, sec = divmod(int(call[2]), 60)
            call_dict[call[0]] = call_dict.get(call[0], 0) + min + (1 if sec else 0)
        for value in call_dict.values():
            if value > 100:
                res = res + 100 + (value - 100) * 2
            else:
                res += value
        return res
    return res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
