# Given a picture consisting of black and white pixels, find the number of black lonely pixels.

# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

# A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

# Example:
# Input: 
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]

# Output: 3
# Explanation: All the three 'B's are black lonely pixels.
# Note:
# The range of width and height of the input 2D array is [1,500].

# Using counter

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        pixels = 0

        for row in picture:
        	if row.count('B') == 1: 
	        	for col in xrange(len(row)):
	        		if row[col] == 'B' and [_row[col] for _row in picture].count('B') == 1: 
	        			pixels += 1
        return pixels

# Using hashmap

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        rows, cols, pixels = len(picture), len(picture and picture[0]), 0

        pixel_map = {'ROW': {row: picture[row].count('B') for row in xrange(rows)}, 'COL': {col: [_row[col] for _row in picture].count('B') for col in xrange(cols)}}

        for row in xrange(rows):
        	if pixel_map['ROW'][row] != 1: 
        		continue
	        for col in xrange(cols):
	        	if picture[row][col] == 'B' and pixel_map['COL'][col] == 1: 
	        		pixels += 1
        
        return pixels

print Solution().findLonelyPixel([
 ['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']])
