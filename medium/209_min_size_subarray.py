import unittest

"""
Sliding window
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_size = float('inf')
        sum = 0
        left = 0

        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                min_size = min(min_size, right - left + 1)
                sum -= nums[left]
                left += 1
        if min_size == float('inf'):
            min_size = 0     

        return min_size
    
"""
Runtime
Details
191ms
Beats 97.72%of users with Python3
Memory
Details
30.94MB
Beats 17.02%of users with Python3
"""

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        target = 7
        nums = [2,3,1,2,4,3]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 2)

        target = 4
        nums = [1,4,4]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

        target = 11
        nums = [1,1,1,1,1,1,1,1]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_hidden(self):
        target = 213
        nums = [12,28,83,4,25,26,25,2,25,25,25,12]        
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 8)
        
    def test_mine(self):
        target = 15
        nums = [2,3,1,2,4,3]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 6)
        

if __name__ == '__main__':
    unittest.main()

        