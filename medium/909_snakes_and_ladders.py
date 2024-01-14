from collections import deque
import numpy as np
import unittest

"""
Runtime
78
ms
Beats
99.80%
of users with Python3
Memory
17.52
MB
Beats
11.68%
of users with Python3
"""

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:

        length = len(board)
        n_squared = length * length

        board.reverse()
        def cellToRowCol(cell):
            row = (cell - 1) // length
            col = (cell -1 ) % length
            if row % 2:
                col = length - 1 - col
            
            return [row, col]

        q = deque()
        q.append([1, 0])
        visited = set()
        visited.add(1)
        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                next_square = square + i
                row, col = cellToRowCol(next_square)
                if board[row][col] != -1:
                    next_square = board[row][col]
                if next_square == n_squared:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    q.append([next_square, moves + 1])
        return -1

    def snakesAndLadders_old(self, board: list[list[int]]) -> int:
        board_matrix = np.array(board)
        reverse_lookup = {}
        n_squared = len(board) * len(board)
        for cell in range(n_squared - 1):
            board_value = self.boardValue(board, cell)
            if board_value != -1:
                print(f"thing at {cell+1} maps to {board_value}")
                reverse_lookup[board_value] = cell

        memo = {}
        for cell in range(n_squared - 1, -1, -1):
            # matrix = np.array(board)
            # row, col = self.boardValue(board, cell)
            # print(f"{cell+1=}, {row=}, {col=}")
            print(f"starting from {cell+1}")
            
        return 0
    
    def labelPositions(self, board):
        """
        Map from input matrix to board position
        Bottom left of matrix is 0, moving right and up from there
        Each new row changes direction
        """
        matrix = np.array(board)
        count = 0 
        board_n = len(board)
        for row_i in range(board_n): #range(board_n - 1, -1, -1):
            board_row = board_n - row_i - 1
            reverse_order = (board_row % 2 == 0)
            for col_i in range(len(board)):
                board_col = col_i
                if reverse_order:
                    board_col = board_n - col_i - 1
                matrix[board_row, board_col] = count
                count += 1
            
        print(matrix)

    def cellToMatrix(self, board, cell):
        cell = cell + 1
        board_n = len(board)
        board_row = board_n - (cell // board_n) - 1
        if board_row % 2 == 0:
            board_col = abs(((cell % board_n) - board_n) + 1)
        else:
            board_col = cell % board_n
        # return board[board_row][board_col]
        return board_row, board_col

    def translateBoard(self, board, row, col):
        board_n = len(board) - 1
        board_row = board_n - row
        board_col = board_n
        if (board_row % 2) == 0:
            board_col = board_n - col
        return board_row, board_col
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
         board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
         self.assertEqual(self.solution.snakesAndLadders(board), 4)
         
         board = [[-1,-1],[-1,3]]
         self.assertEqual(self.solution.snakesAndLadders(board), 1)

        
if __name__ == '__main__':
    unittest.main()
