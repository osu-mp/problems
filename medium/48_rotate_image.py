import unittest

class Solution:
    """
    Runtime
Details
33ms
Beats 95.45%of users with Python3
Memory
Details
17.26MB
Beats 24.59%of users with Python3
"""
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top = left
                bot = right
                # save top left
                top_left = matrix[top][left + i]

                # move bottom left to top left
                matrix[top][left + i] = matrix[bot - i][left]
                # bot right to bot left
                matrix[bot - i][left] = matrix[bot][right - i]
                matrix[bot][right - i] = matrix[top + i][right]
                matrix[top + i][right] = top_left

            left += 1
            right -=  1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [[7,4,1],[8,5,2],[9,6,3]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

        

if __name__ == '__main__':
    unittest.main()
