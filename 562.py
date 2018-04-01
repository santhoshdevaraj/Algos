# Given a 01 matrix M, find the longest line of consecutive one in the matrix. 
# The line could be horizontal, vertical, diagonal or anti-diagonal.
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
# Hint: The number of elements in the given matrix will not exceed 10,000.


class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        rows, cols = len(M), len(M and M[0])

        table = [[(0, 0, 0, 0) for i in xrange(cols+2)] for i in xrange(rows+1)]

        max_value = 0

        for row in xrange(rows):
        	for col in xrange(cols):
        		if M[row][col] == 1:
        			table[row+1][col+1] = (
        				table[row][col+1][0] + 1,
        				table[row+1][col][1] + 1,
        				table[row][col][2] + 1,
        				table[row][col+2][3] + 1
        			)
        			max_value = max(max(table[row+1][col+1]), max_value)

        return max_value

print Solution().longestLine(
[[0,1,1,0],
 [0,1,1,0],
 [1,1,1,1]]
 )