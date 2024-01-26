import copy
import itertools
import unittest

"""
Runtime
29
ms
Beats
96.50%
of users with Python3
Memory
16.40
MB
Beats
86.42%
of users with Python3
"""

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        copied = copy.deepcopy(board)
        x_width = len(board)
        y_height = len(board[0])

        for x in range(x_width):
            for y in range(y_height):
                # print(f"{x=}, {y=}, {board[x][y]=}") 

                # Define the range of values
                values = [-1, 0, 1]
                
                # Use itertools.product to get all combinations
                combinations = list(itertools.product(values, repeat=2))

                live_neighbors = 0
                for combo in combinations:
                    if combo == (0, 0):
                        continue
                    test_x = x + combo[0]
                    test_y = y + combo[1]

                    
                    if 0 <= test_x < x_width and \
                        0 <= test_y < y_height and \
                        copied[test_x][test_y]:
                        live_neighbors += 1

                if copied[x][y] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[x][y] = 0
                if copied[x][y] == 0 and live_neighbors == 3:
                    board[x][y] = 1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

        board = [[1,1],[1,0]]
        expected = [[1,1],[1,1]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

        
if __name__ == '__main__':
    unittest.main()