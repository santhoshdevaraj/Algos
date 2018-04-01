# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.

# Given target = 20, return false.


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
