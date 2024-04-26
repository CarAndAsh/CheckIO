#!/usr/bin/env checkio --domain=py run bishop-vs-aliens
def reach_corner(x: int, y: int, m: int, n: int, aliens: list[tuple[int, int]]) -> bool:
    corners = ((0, 0), (m - 1, 0), (0, n - 1), (m - 1, n - 1))

    def check_way(change_coords, x, y):
        start_pos = x, y
        while (x, y) not in aliens:
            if (x, y) in corners:
                return True
            if x == 0:
                change_coords[0] = 'x + 1'
            elif x == m - 1:
                change_coords[0] = 'x - 1'
            elif y == 0:
                change_coords[1] = 'y + 1'
            elif y == n - 1:
                change_coords[1] = 'y - 1'
            x, y = [eval(exp, {'x': x, 'y': y}) for exp in change_coords]
            if (x, y) == start_pos:
                return False
        return False

    return any(check_way(func, x, y) for func in (['x + 1', 'y + 1'], ['x + 1', 'y - 1'], ['x - 1', 'y + 1'], ['x - 1', 'y - 1']))


print("Example:")
print(reach_corner(3, 2, 4, 5, [(2, 3)]))

# These "asserts" are used for self-checking
assert reach_corner(0, 2, 5, 5, []) == False
assert reach_corner(4, 4, 9, 9, [(0, 0), (0, 8), (8, 0), (8, 8)]) == False
assert reach_corner(1, 1, 1000, 2, [(0, 0), (0, 1), (999, 0)]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
