import unittest

"""
Runtime
3961
ms
Beats
71.94%
of users with Python3
Memory
16.60
MB
Beats
71.35%
of users with Python3
"""
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                word[i] != board[row][col] or 
                (row, col) in visited):
                return False
            
            visited.add((row, col))
            result = (dfs(row + 1, col, i + 1) or
                   dfs(row - 1, col, i + 1) or
                   dfs(row, col + 1, i + 1) or 
                   dfs(row, col - 1, i + 1))
            visited.remove((row, col))
            return result
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        self.assertEqual(self.solution.exist(board, word), True)

        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        self.assertEqual(self.solution.exist(board, word), True)

        [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        self.assertEqual(self.solution.exist(board, word), False)

if __name__ == '__main__':
    unittest.main()