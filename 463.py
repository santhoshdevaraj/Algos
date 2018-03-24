# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
# and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water
# inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid 
# is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example:

# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols, perimeter = len(grid), len(grid[0]), 0

        def is_island(row, col):
            return False if (row < 0 or row == rows or col < 0 or col == cols) else grid[row][col] == 1

        for row in xrange(rows):
            for col in xrange(cols):
                if grid[row][col] == 1:
                    perimeter += 4 - sum((is_island(row-1, col), is_island(row+1, col), is_island(row, col-1), is_island(row, col+1)))

        return perimeter

print Solution().islandPerimeter([
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
 ])