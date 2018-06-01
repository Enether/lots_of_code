from pprint import pprint

matrix_size = int(input())
UPPER_BOUND = matrix_size-1
GOAL_POSITION = (matrix_size-1, matrix_size-1)

import sys
def is_in_matrix(r, c):
    return r >= 0 and c >= 0 and r <= UPPER_BOUND and c <= UPPER_BOUND


def min(arr):
    min_num = sys.maxsize
    for num in arr:
        if num is not None and num < min_num:
            min_num = num

    if min_num == sys.maxsize:
        min_num = None

    return min_num

from queue import deque
def bfs(matrix, row, col, move):
    to_visit = deque()
    to_visit.append(((row, col), 0))
    visited = set()
    row_move, col_move = move

    while len(to_visit) != 0:
        curr_pos, steps = to_visit.popleft()
        # print(curr_pos)
        row, col = curr_pos
        new_moves = [
            # Upper left
            (row-row_move, col-col_move),
            (row-col_move, col-row_move),

            # Upper right
            (row-row_move, col+col_move),
            (row-col_move, col+row_move),

            # Down left
            (row+row_move, col-col_move),
            (row+col_move, col-row_move),

            # Down right
            (row+row_move, col+col_move),
            (row+col_move, col+row_move),
        ]
        for new_row, new_col in new_moves:
            if is_in_matrix(new_row, new_col) and (new_row, new_col) not in visited:
                if (new_row, new_col) == GOAL_POSITION:
                    return steps+1
                visited.add((new_row, new_col))
                to_visit.append(((new_row, new_col), steps+1))


matrix = []
for i in range(matrix_size):
    matrix.append([None for _ in range(matrix_size)])

for i in range(1, matrix_size):
    for j in range(1, matrix_size):
        if matrix[i][j] is not None:
            matrix[j][i] = matrix[i][j]
            break
        result = bfs(matrix, 0, 0, (i, j))
        # print(f'RESULT FOR {i}{# j} is {result}')
        # print(result)
        matrix[i][j] = result or -1
# pprint(matrix)

for i in range(1, len(matrix)):
    print(' '.join(str(p) for p in matrix[i][1:]))

