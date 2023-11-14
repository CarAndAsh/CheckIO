#!/usr/bin/env checkio --domain=py run lightbulb-operating
from datetime import datetime, timedelta
from typing import List, Optional, Union, Tuple


def get_switchlist(switchlist, start, end, operating):
    if operating:
        for i in range(0, len(switchlist), 2):
            if i + 1 <= len(switchlist) - 1:
                if operating >= (switchlist[i + 1] - switchlist[i]):
                    operating -= (switchlist[i + 1] - switchlist[i])
                elif operating == timedelta(0):
                    switchlist.pop(i), switchlist.pop(i)
                else:
                    switchlist.pop(i + 1)
                    switchlist.insert(i + 1, switchlist[i] + operating)
                    operating = timedelta(0)
            else:
                if operating:
                    switchlist.append(switchlist[i] + operating)
                else:
                    switchlist.pop(i)

    if end:
        light = False
        if len(switchlist) % 2:
            light = True
        while switchlist and switchlist[-1] > end:
            switchlist.pop()
            if light:
                light = False
            else:
                light = True
        if light:
            switchlist.append(end)

    if start:
        light = False
        while switchlist and switchlist[0] <= start:
            switchlist.pop(0)
            if light:
                light = False
            else:
                light = True
        if light:
            switchlist.insert(0, start)

    return switchlist


def sum_light(
        els: List[Union[datetime, Tuple[datetime, int]]],
        start_watching: Optional[datetime] = None,
        end_watching: Optional[datetime] = None,
        operating: Optional[timedelta] = None,
) -> int:
    """
    how long the light bulb has been turned on
    """

    total = timedelta(0)
    lamps = {}
    light = False
    res = []
    for click in els:
        if isinstance(click, datetime):
            click = (click, 1)
        lamps.setdefault(click[1], []).append(click[0])
    lamps = {key: get_switchlist(value, start_watching, end_watching, operating) for key, value in lamps.items()}

    for lamp in lamps:
        print(lamp, lamps[lamp])

    while any(lamps.values()):
        early_lamp = min([(key, switchlist[0]) for key, switchlist in lamps.items() if switchlist], key=lambda x: x[1])
        turn_on = lamps[early_lamp[0]].pop(0)
        turn_off = lamps[early_lamp[0]].pop(0)
        if res and turn_off > res[-1] >= turn_on:
            res.pop()
            res.append(turn_off)
        elif not res or res[-1] < turn_on:
            res.append(turn_on)
            res.append(turn_off)
    print(res)
    while res:
        total += (res.pop() - res.pop())

    return int(total.total_seconds())

if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ]
        )
    )
    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
            ]
        )
        == 610
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ]
        )
        == 1220
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 12, 10, 10),
            ]
        )
        == 4820
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 1),
            ]
        )
        == 1
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 13, 11, 0, 0),
            ]
        )
        == 86410
    )
    print(
        "The first mission in series is completed? Click 'Check' to earn cool rewards!"
    )
    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 5),
        )
        == 5
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 10
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 610
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 600
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
        )
        == 620
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 10, 11),
        )
        == 0
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 9, 11),
        )
        == 60
    )
    print("The second mission in series is done? Click 'Check' to earn cool rewards!")
    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 0),
            end_watching=datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 7),
        )
        == 7
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 3),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 7
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 0
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 30, 0),
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 0
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 10
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 20
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 9, 50, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 9, 0, 0),
            datetime(2015, 1, 12, 10, 5, 0),
        )
        == 300
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 5, 0),
            datetime(2015, 1, 12, 12, 0, 0),
        )
        == 310
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 11, 5, 0),
            datetime(2015, 1, 12, 11, 10, 0),
        )
        == 300
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 20
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 10, 0),
            datetime(2015, 1, 12, 10, 20, 20),
        )
        == 610
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 10, 0),
            datetime(2015, 1, 12, 10, 20, 20),
        )
        == 1220
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 9, 0),
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 0
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 9, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )
    print(
        "The third mission in series is completed? Click 'Check' to earn cool rewards!"
    )      
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ]
        )
        == 60
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 11, 0, 0), 2),
                (datetime(2015, 1, 12, 11, 1, 0), 2),
            ]
        )
        == 70
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ]
        )
        == 30
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ]
        )
        == 40
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 0), 3),
                (datetime(2015, 1, 12, 10, 1, 20), 3),
            ]
        )
        == 60
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 50),
        )
        == 10
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 30
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 30
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 50),
        )
        == 0
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 30
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 20), 2),
                (datetime(2015, 1, 12, 10, 1, 40), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 50
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 30
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 40
    )
    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 30
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 40
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 0
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 10
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 10
    )
    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )
    assert (
        sum_light(
            els=[
                (datetime(2015, 1, 11, 0, 0, 0), 3),
                datetime(2015, 1, 12, 0, 0, 0),
                (datetime(2015, 1, 13, 0, 0, 0), 3),
                (datetime(2015, 1, 13, 0, 0, 0), 2),
                datetime(2015, 1, 14, 0, 0, 0),
                (datetime(2015, 1, 15, 0, 0, 0), 2),
            ],
            start_watching=datetime(2015, 1, 10, 0, 0, 0),
            end_watching=datetime(2015, 1, 16, 0, 0, 0),
        )
        == 345600
    )
    print(
        "The forth mission in series is completed? Click 'Check' to earn cool rewards!"
    )




    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ]
        )
        == 60
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 11, 0, 0), 2),
                (datetime(2015, 1, 12, 11, 1, 0), 2),
            ]
        )
        == 70
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ]
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ]
        )
        == 40
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 0), 3),
                (datetime(2015, 1, 12, 10, 1, 20), 3),
            ]
        )
        == 60
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 50),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 30
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 30
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 50),
        )
        == 0
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 20), 2),
                (datetime(2015, 1, 12, 10, 1, 40), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 50
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 30),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 30
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 20),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 40
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 1, 0),
        )
        == 40
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 0
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 10
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 10
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 30),
        )
        == 20
    )

    assert (
        sum_light(
            els=[
                (datetime(2015, 1, 11, 0, 0, 0), 3),
                datetime(2015, 1, 12, 0, 0, 0),
                (datetime(2015, 1, 13, 0, 0, 0), 3),
                (datetime(2015, 1, 13, 0, 0, 0), 2),
                datetime(2015, 1, 14, 0, 0, 0),
                (datetime(2015, 1, 15, 0, 0, 0), 2),
            ],
            start_watching=datetime(2015, 1, 10, 0, 0, 0),
            end_watching=datetime(2015, 1, 16, 0, 0, 0),
        )
        == 345600
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            operating=timedelta(seconds=100),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            operating=timedelta(seconds=5),
        )
        == 5
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            operating=timedelta(seconds=100),
        )
        == 60
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 30),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            operating=timedelta(seconds=100),
        )
        == 60
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 30),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            operating=timedelta(seconds=20),
        )
        == 40
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 0), 3),
                (datetime(2015, 1, 12, 10, 1, 20), 3),
            ],
            operating=timedelta(seconds=10),
        )
        == 30
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 20), 2),
                (datetime(2015, 1, 12, 10, 1, 40), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 20),
            operating=timedelta(seconds=100),
        )
        == 50
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 20), 2),
                (datetime(2015, 1, 12, 10, 1, 40), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 20),
            operating=timedelta(seconds=10),
        )
        == 20
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 10),
            end_watching=datetime(2015, 1, 12, 10, 0, 30),
            operating=timedelta(seconds=20),
        )
        == 20
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 10),
            end_watching=datetime(2015, 1, 12, 10, 0, 30),
            operating=timedelta(seconds=10),
        )
        == 20
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 10),
            end_watching=datetime(2015, 1, 12, 10, 0, 30),
            operating=timedelta(seconds=5),
        )
        == 10
    )

    print(
        "The forth mission in series is completed? Click 'Check' to earn cool rewards!"
    )
