#!/usr/bin/env checkio --domain=py run lightbulb-more
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
        req: Optional[int] = 1,
) -> int:
    """
    how long the light bulb has been turned on
    """

    total = timedelta(0)
    lamps = {}
    light = 0
    work_period = []
    res = []
    for click in els:
        if isinstance(click, datetime):
            click = (click, 1)
        lamps.setdefault(click[1], []).append(click[0])
    lamps = {key: get_switchlist(value, start_watching, end_watching, operating) for key, value in lamps.items()}

    lamp = 1
    while any(lamps.values()):
        if lamps[lamp]:
            turn_on = lamps[lamp].pop(0), True
            turn_off = lamps[lamp].pop(0), False
            work_period.append(turn_on)
            work_period.append(turn_off)
            lamps.values()
        if not lamps[lamp]:
            lamp += 1

    work_period.sort(key=lambda x: x[0])
    while work_period:
        action = work_period.pop(0)
        if action[1]:
            light += 1
            if light == req:
                res.append(action[0])
        else:
            light -= 1
            if req - light == 1:
                res.append(action[0])
    while res:
        total += (res.pop() - res.pop())

    return int(total.total_seconds())


if __name__ == "__main__":
    print("Example:")

    print(
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                (datetime(2015, 1, 12, 10, 0, 50), 3),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            req=3,
        )
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

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                (datetime(2015, 1, 12, 10, 0, 0), 2),
                datetime(2015, 1, 12, 10, 0, 10),
                (datetime(2015, 1, 12, 10, 1, 0), 2),
            ],
            req=1,
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
            req=2,
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
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            req=1,
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
            req=2,
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
            req=3,
        )
        == 0
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 10), 3),
                datetime(2015, 1, 12, 10, 0, 20),
                (datetime(2015, 1, 12, 10, 0, 50), 3),
                (datetime(2015, 1, 12, 10, 0, 30), 2),
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            req=3,
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
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 1, 0),
            req=2,
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
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 1, 0),
            req=2,
            operating=timedelta(seconds=15),
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
                datetime(2015, 1, 12, 10, 0, 40),
                (datetime(2015, 1, 12, 10, 0, 50), 2),
                (datetime(2015, 1, 12, 10, 1, 20), 2),
                (datetime(2015, 1, 12, 10, 1, 40), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 20),
            operating=timedelta(seconds=100),
            req=2,
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
                (datetime(2015, 1, 12, 10, 1, 20), 2),
                (datetime(2015, 1, 12, 10, 1, 40), 2),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 20),
            operating=timedelta(seconds=100),
            req=3,
        )
        == 0
    )

    assert (
        sum_light(
            [
                (datetime(2015, 1, 12, 10, 0, 0), 4),
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
            req=3,
        )
        == 20
    )

    print(
        "The forth mission in series is completed? Click 'Check' to earn cool rewards!"
    )
