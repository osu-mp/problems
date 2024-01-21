import unittest

"""
Runtime
30
ms
Beats
93.47%
of users with Python3
Memory
16.58
MB
Beats
56.80%
of users with Python3
"""
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        result = []

        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

        
if __name__ == '__main__':
    unittest.main()