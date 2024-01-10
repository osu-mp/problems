import unittest

"""
Runtime
Details
717ms
Beats 96.21%of users with Python3
Memory
Details
28.15MB
Beats 28.08%of users with Python3
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_buy = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_buy:
                min_buy = price
            else:
                max_profit = max(max_profit, price - min_buy)
        return max_profit
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(self.solution.maxProfit(prices), 5)

        prices = [7,6,4,3,1]
        self.assertEqual(self.solution.maxProfit(prices), 0)

if __name__ == '__main__':
    unittest.main()
