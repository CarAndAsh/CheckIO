#!/usr/bin/env checkio --domain=py run buildings-visibility
# https://py.checkio.org/mission/buildings-visibility/publications/yoichi/python-3/first/share/0f1fd5cf14674becd006491919cfda30/
from collections import namedtuple


def intersect(build, builds) -> bool:
    # check height and weight for every building and subtract from current
    for build_1 in builds:
        if build_1.height >= build.height:
            if (build.x[1] <= build_1.x[0] and build.x[0] < build_1.x[0]) or (
                    build.x[0] >= build_1.x[1] and build.x[1] > build_1.x[1]):
                continue
            elif build_1.x[1] > build.x[0] >= build_1.x[0]:
                build.x[0] = build_1.x[1]
            elif build_1.x[0] < build.x[1] and build.x[1] >= build_1.x[1]:
                build.x[1] = build_1.x[0]

    return build.x[0] < build.x[1]


def checkio(buildings):
    buildings.sort(key=lambda item: item[1])
    build_lst = []
    for params in buildings:
        building = namedtuple('Build', 'x,y,height')
        building.x, building.y, building.height = [params[0], params[2]], [params[1], params[3]], params[4]
        if not build_lst or intersect(building, build_lst):
            build_lst.append(building)

    for b in build_lst:
        print(b.x)
    print()

    return len(build_lst)


if __name__ == '__main__':
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
    ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
    ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third"
    assert checkio([
        [0, 0, 1, 1, 10]
    ]) == 1, "Alone"
    assert checkio([
        [2, 2, 3, 3, 4],
        [2, 5, 3, 6, 4]
    ]) == 1, "Shadow"
