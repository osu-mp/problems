import unittest

"""
Runtime
96
ms
Beats
96.64%
of users with Python3
Memory
18.36
MB
Beats
12.09%
of users with Python3
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for row_i, row in enumerate(matrix):
            for col_i, col in enumerate(row):
                if col == 0:
                    rows.add(row_i)
                    cols.add(col_i)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in rows or col in cols:
                    matrix[row][col] = 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        expected = [[1,0,1],[0,0,0],[1,0,1]]
        self.solution.setZeroes(matrix)
        print(f"BLAH {matrix}")
        self.assertEqual(matrix, expected)

        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

        
if __name__ == '__main__':
    unittest.main()
