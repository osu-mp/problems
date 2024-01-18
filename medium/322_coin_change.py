import unittest

"""
Runtime
785
ms
Beats
82.65%
of users with Python3
Memory
17.51
MB
Beats
61.45%
of users with Python3
"""
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0

        for total in range(1, amount + 1):
            for coin in coins:
                if total - coin >= 0:
                    memo[total] = min(memo[total], 1 + memo[total - coin])

        if memo[amount] == float('inf'):
            return -1
        return memo[amount]

    def coinChange_brute(self, coins: list[int], amount: int) -> int:
        count = 0

        for coin in sorted(coins, reverse=True):

            count += amount // coin
            amount = amount % coin
            if amount == 0:
                return count
        return -1
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        coins = [186,419,83,408]
        amount = 6249
        self.assertEqual(self.solution.coinChange(coins, amount), 20)

        coins = [1,2,5]
        amount = 11
        self.assertEqual(self.solution.coinChange(coins, amount), 3)

        coins = [2]
        amount = 3
        self.assertEqual(self.solution.coinChange(coins, amount), -1)

        coins = [1]
        amount = 0
        self.assertEqual(self.solution.coinChange(coins, amount), 0)

        




        
if __name__ == '__main__':
    unittest.main()
