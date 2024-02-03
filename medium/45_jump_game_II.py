import unittest

"""
Runtime
104
ms
Beats
85.24%
of users with Python3
Memory
17.45
MB
Beats
82.26%
of users with Python3
"""
class Solution:
    def jump(self, nums: list[int]) -> int:
        result = 0
        left = right = 0
        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            result += 1
        return result
    
    def jump_dp(self, nums: list[int]) -> int:
        memo = [float('inf')] * len(nums)
        memo[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if (i + j) > len(memo) - 1:
                    continue
                # print(f"{i=}, {j=}, {memo[i + j]=}, {memo[i]=}")
                memo[i + j] = min(memo[i + j], 1 + memo[i])
        return memo[len(nums) - 1]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        numbers = [2,3,1,1,4]
        self.assertEqual(self.solution.jump(numbers), 2)

        numbers = [2,3,0,1,4]
        self.assertEqual(self.solution.jump(numbers), 2)

if __name__ == '__main__':
    unittest.main()
