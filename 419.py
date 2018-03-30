# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, 
# empty slots are represented with '.'s. You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of 
# the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count, rows, cols = 0, len(board), len(board[0])

        def is_new_ship(row, col):
        	return True if row < 0 or col < 0 or board[row][col] == '.' else False

        for row in xrange(rows):
        	for col in xrange(cols):
        		if board[row][col] == 'X' and is_new_ship(row-1, col) and is_new_ship(row, col-1):
        			count += 1

        return count

print Solution().countBattleships([['X', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X']])