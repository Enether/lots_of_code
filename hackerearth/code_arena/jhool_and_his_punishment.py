#  https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/little-jhool-and-his-punishment/description/
t = int(input())
for _ in range(t):
    n = int(input())
    b, g = [int(p) for p in input().split()]
    if abs(g-b) > 1:
        print('Little Jhool wins!')
    else:
        print('The teacher wins!')