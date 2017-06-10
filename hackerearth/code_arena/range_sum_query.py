"""
#  https://leetcode.com/problems/range-sum-query-2d-immutable/#/description
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2

What we'll do is, in another matrix, store in every index the sum from 0,0 to i, j.
Then, when we get a query, we'll output the following
k, l = top-left coords
i,j = bottom-right coords
sum_matrix[i][j] - ((sum_matrix[k-1][j] + sum_matrix[i][l-1]) - sum_matrix[k-1][l-1])

This is hard to explain and needs a picture to be understood, but basically, we get a big rectangle sum
from 0,0 to i,j and remove the excess sum, which is 0,0 to i, l and 0,0 to k, j

"""
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

sum_matrix = []
for i in range(len(matrix)+1):
    sum_matrix.append([0] * (len(matrix[0])+1))
from pprint import pprint


for i in range(1, len(sum_matrix)):
    for j in range(1, len(sum_matrix)):
        sum_matrix[i][j] = matrix[i-1][j-1] + sum_matrix[i][j-1] + sum_matrix[i-1][j] - sum_matrix[i-1][j-1]


def sum_region(k, l, i, j):
    k, l, i, j = k+1, l+1, i+1, j+1
    return sum_matrix[i][j] - ((sum_matrix[k-1][j] + sum_matrix[i][l-1]) - sum_matrix[k-1][l-1])
pprint(sum_matrix)
print(sum_region(2, 1, 4, 3))
print(sum_region(1, 1, 2, 2))
print(sum_region(1, 2, 2, 4))