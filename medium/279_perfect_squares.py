import math
import unittest

class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        memo = {}

        def minSquares(n):
            if n in memo:
                return memo[n]
            memo[n] = float('inf')
            for square in squares:
                if square <= n:
                    thisMin = 1 + minSquares(n - square)
                    memo[n] = min(memo[n], thisMin)

            return memo[n]

        for i in range(1, n + 1):
            if math.sqrt(i) % 1 == 0:
                squares.append(i)
                memo[i] = 1
                continue
            minSquares(i)

        return memo[n]
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        n = 12
        # self.assertEqual(self.solution.numSquares(n), 3)

        n = 13
        self.assertEqual(self.solution.numSquares(n), 2)
                
        
if __name__ == '__main__':
    unittest.main()