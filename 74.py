# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix and matrix[0])
        
        def search(row, col):
        	if row < 0 or col < 0 or row == rows or col == cols:
        		return False
        	if matrix[row][col] == target:
        		return True
        	elif matrix[row][col] < target:
        		return search(row, col+1)
        	else:
        		return search(row-1, col)

        return search(rows-1, 0)

print Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 0)