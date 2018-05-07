"""
An over-engineered solution of the findMinXor problem (https://www.interviewbit.com/problems/min-xor-value/?ref=random-problem),
    where given a list of integers you need to find the pair whose XOR is the minimum value

The best solution is O(N log N), sorting the array and comparing each adjacent values.
Here, we have a recursive solution greedily comparing only those pairs which have the most equal bits.
Solution is O(N) I think, we do at most 32 * N traversals
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        self.max_col_size = 32
        self.matrix = [list('{0:b}'.format(num).zfill(self.max_col_size)) for num in A]
        return self.min_xor_pair(range(len(self.matrix)))

    def min_xor_pair(self, row_indices, column=0):
        """
        Returns the minimum XOR pair in the matrix, comparing only the given rows
        """
        import sys
        if not row_indices:
            return sys.maxsize

        zero_rows, one_rows = [], []
        for row in row_indices:
            arr = zero_rows if self.matrix[row][column] == '0' else one_rows
            arr.append(row)

        if column == self.max_col_size-1:
            if not zero_rows or not one_rows:
                # All possible pairs have matched
                return 0
            # They're all the same number, so simply take the first element in the array
            return self.binary_row_to_int(zero_rows[0]) ^ self.binary_row_to_int(one_rows[0])
        elif len(zero_rows) == 1 and len(one_rows) == 1:
            return self.binary_row_to_int(zero_rows[0]) ^ self.binary_row_to_int(one_rows[0])
        elif len(zero_rows) == 1:
            return self.min_xor_pair(one_rows, column+1)
        elif len(one_rows) == 1:
            return self.min_xor_pair(zero_rows, column+1)
        else:
            return min(self.min_xor_pair(zero_rows, column+1), self.min_xor_pair(one_rows, column+1))

    def binary_row_to_int(self, row_idx):
        return int(''.join(self.matrix[row_idx]), 2)

