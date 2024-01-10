import unittest

class Solution:
    """
    Runtime
Details
29ms
Beats 94.53%of users with Python3
Memory
Details
17.38MB
Beats 11.01%of users with Python3
    """
    class Solution:
    def climbStairs(self, n: int, memo: dict={}) -> int:
        if n in memo:
            return memo[n]
        
        if n in [0, 1, 2]:
            memo[n] = n
            return n
        
        take_1 = self.climbStairs(n - 1, memo)
        take_2 = self.climbStairs(n - 2, memo)
        memo[n] = take_1 + take_2

        return memo[n]
        
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        self.assertEqual(self.solution.climbStairs(2), 2)
        self.assertEqual(self.solution.climbStairs(3), 3)
        # 1 1 1 1; 1 1 2; 1 2 1; 2 1 1; 2 2 
        self.assertEqual(self.solution.climbStairs(4), 5)
        # 1 1 1 1 1; 1 1 1 2; 1 1 2 1; 1 2 1 1; 2 1 1 1; 2 2 1; 2 1 2; 1 2 2; 
        self.assertEqual(self.solution.climbStairs(5), 8)
        

if __name__ == '__main__':
    unittest.main()