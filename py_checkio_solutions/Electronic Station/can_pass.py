#!/usr/bin/env checkio --domain=py run can-pass
def can_pass(matrix, first, second, path=None, path_val=None):
    if path == None:
        path = []
    if first == second:
        return True
    if first in path:
        return False
    if path_val == None:
        path_val = matrix[first[0]][first[1]]
    path.append(first)
    return any([can_pass(matrix, (dh if ((dh := first[0]+1) < len(matrix)) and (matrix[dh][first[1]] == path_val) and ((dh,first[1]) not in path) else first[0], first[1]), second, path, path_val),
                can_pass(matrix, (dh if (0 <= (dh := first[0]-1)) and (matrix[dh][first[1]] == path_val) and ((dh,first[1]) not in path) else first[0], first[1]), second, path, path_val),
                can_pass(matrix, (first[0], dv if ((dv := first[1]+1) < len(matrix[0])) and (matrix[first[0]][dv] == path_val) and ((first[0],dv) not in path) else first[1]), second, path, path_val),
                can_pass(matrix, (first[0], dv if (0 <= (dv := first[1]-1)) and (matrix[first[0]][dv] == path_val) and ((first[0],dv) not in path) else first[1]), second, path, path_val)])


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
    assert can_pass(((5, 6),
                     (6, 6),
                     (6, 5),
                     (6, 6),
                     (7, 6),
                     (6, 6),
                     (6, 7),
                     (6, 6),
                     (8, 6),
                     (6, 6),),
                    (9, 1), (0, 1)) == True, 'Edge example'

