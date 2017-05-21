"""
This is a greedy solution which does not work all the time
I suppose the real explanation is some DP
i.e in the example
2 3
2 1
1 0 0
6 7 8
3 1 1
answer is 16
2 3
2 1
1 0 0
6 7 8
3 5 1
answer is 17
Since what we get from the 0th row changes the possible outcomes on the 1st row
"""
n, m = [int(p) for p in input().split()]
ball_color_count = [int(p) for p in input().split()]  # idx: color, value: ball count of that color
row_capacity = [int(p) for p in input().split()]
curr_cap = [0 for _ in range(len(row_capacity))]
max_row_score = [0 for _ in range(len(row_capacity))]
matrix = []
fill_m = []
for _ in range(n):
    matrix.append([int(p) for p in input().split()])
    fill_m.append([0 for _ in range(len(matrix[0]))])


class Cell:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

    def __lt__(self, other):
        """ A Cell is less than another if its profit is less"""
        profit, other_profit = self.calc_profit(), other.calc_profit()
        if profit == other_profit:
            # print(profit, other_profit)
            # return profit < other_profit
            return curr_cap[self.col] > curr_cap[other.col]
            # raise Exception('EQUAL PROFIT')
        return profit < other_profit

    def __str__(self):
        return f'Coords:{self.row}:{self.col} Val: {self.value}'

    def __repr__(self):
        return self.__str__()

    def calc_profit(self):
        penalty = 0
        if curr_cap[self.col]+1 > row_capacity[self.col]:
            penalty = ((curr_cap[self.col]+1) - row_capacity[self.col]) ** 2
        profit = self.value - penalty
        return profit

ball_count = sum(ball_color_count)
ball_positions = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        ball_positions.append(Cell(value=matrix[i][j], row=i, col=j))
ball_positions = list(reversed(sorted(ball_positions)))


idx = 0
score = 0
box_colors = {j:set() for j in range(len(matrix[0]))}  # sets()
while idx < len(ball_positions) and ball_count > 0:
    # TODO: See if it makes sense
    cell = ball_positions[idx]
    value, i, j = cell.value, cell.row, cell.col

    if cell.calc_profit() < 0:
        idx += 1
        break
    if ball_color_count[i] == 0 or i in box_colors[j]:
        pass
    else:
        # we can add a ball
        if i in box_colors[j]:
            raise Exception()
        if ball_color_count[i] < 0:
            raise Exception()
        score += cell.calc_profit()
        box_colors[j].add(i)
        curr_cap[j] += 1
        ball_color_count[i] -= 1
        ball_count -= 1
        if ball_color_count[i] < 0:
            raise Exception()

    ball_positions.pop(idx)
    idx = 0
    ball_positions = list(reversed(sorted(ball_positions)))
print(score)
