"""
Roy has a matrix of size NxN. Rows and Columns are numbered from 0 to N-1.
jth column of ith row contains absolute difference between i and j.
In other words, Matrix[i][j] = abs(i-j) where 0 ≤ i, j < N.

This produces a matrix such as this one, for the value 10

[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
 [2, 1, 0, 1, 2, 3, 4, 5, 6, 7],
 [3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
 [4, 3, 2, 1, 0, 1, 2, 3, 4, 5],
 [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
 [6, 5, 4, 3, 2, 1, 0, 1, 2, 3],
 [7, 6, 5, 4, 3, 2, 1, 0, 1, 2],
 [8, 7, 6, 5, 4, 3, 2, 1, 0, 1],
 [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
"""
def find_lower_part(n):
    # Find the lower part of matrix's sum
    n -= 1
    mp = 1
    sum = 0
    while n != 0:
        sum += mp * n
        n-=1
        mp+=1
    return sum
# 4 * 1 + 3 * 2 + 2 * 3 + 1 * 4
for q in range(int(input())):
    n = int(input())
    # print(build_matrix(n))
    print(find_lower_part(n)*2)