n, m = [int(p) for p in input().split()]
ball_color_count = [int(p) for p in input().split()]  # idx: color, value: ball count of that color
row_capacity = [int(p) for p in input().split()]

matrix = []
fill_m = []
for _ in range(m):
    matrix.append([int(p) for p in input().split()])
    fill_m.append([0 for _ in range(len(matrix[0]))])

max_score = 0
def bf():
    global max_score
    # if max(ball_color_count) == 0:
    score = 0
    for i in range(len(fill_m)):
        for j in range(len(fill_m[0])):
            score += fill_m[i][j] * matrix[i][j]
    # print(score)
    penalty = 0
    for j in range(len(fill_m[0])):
        cnt = 0
        for i in range(len(fill_m)):
            cnt += fill_m[i][j]
        # print(f'Cnt is {cnt} max is {row_capacity[j]}')
        if cnt > row_capacity[j]:
            penalty += (cnt-row_capacity[j])**2
    # print(f'PENALTY IS {penalty}')
    score -= penalty
    if score > max_score:
        max_score = score
    # print(score-penalty)
        # if score-penalty == 14:
        #     print()
        # TODO: calc penalty
    for color, ball in enumerate(ball_color_count):
        if ball < 0:
            raise Exception()
        if ball == 0:
            continue

        for row, cap in enumerate(row_capacity):
            # [color][box]
            # for b_c in range(1, ball+1):
            if fill_m[color][row] > 1:
                raise Exception()
            if fill_m[color][row] == 1:
                continue
            ball_color_count[color] -= 1
            fill_m[color][row] += 1
            bf()
            fill_m[color][row] -= 1
            ball_color_count[color] += 1
    # for row, cap in enumerate(row_capacity):
    #
    #     for color, ball in enumerate(ball_color_count):
    #         if ball < 0:
    #             raise Exception()
    #         if ball == 0:
    #             continue
    #         # [box][color]
    #         # for 1 in range(1, ball+1):
    #         if fill_m[row][color] > 1:
    #             raise Exception()
    #         if fill_m[row][color] == 1:
    #             continue
    #         ball_color_count[color] -= 1
    #         fill_m[row][color] += 1
    #         bf()
    #         fill_m[row][color] -= 1
    #         ball_color_count[color] += 1
bf()
print(max_score)