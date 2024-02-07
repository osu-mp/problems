import unittest

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        

        row = (top + bot) // 2
        left, right = 0, cols - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            elif target == matrix[row][mid]:
                return True
        
        return False
                

    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        # self.assertEqual(self.solution.searchMatrix(matrix, target), True)

        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        # self.assertEqual(self.solution.searchMatrix(matrix, target), False)

        matrix = [[1]]
        target = 1
        self.assertEqual(self.solution.searchMatrix(matrix, target), True)

        matrix = [[1],[ 3]]
        target = 3
        self.assertEqual(self.solution.searchMatrix(matrix, target), True)

        
if __name__ == '__main__':
    unittest.main()