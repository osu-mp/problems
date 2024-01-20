import unittest

"""
Runtime
82
ms
Beats
74.55%
of users with Python3
Memory
17.70
MB
Beats
32.72%
of users with Python3
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def binarySearch(startIndex, endIndex, indices, nums, num):
            if startIndex > endIndex:
                return startIndex
            
            middleIndex = (startIndex + endIndex) // 2
            if nums[indices[middleIndex]] < num:
                startIndex = middleIndex + 1
            else:
                endIndex = middleIndex - 1

            return binarySearch(startIndex, endIndex, indices, nums, num)
        
        indicies = [None for x in range(len(nums) + 1)]
        length = 0

        for i, num in enumerate(nums):
            updateLength = binarySearch(1, length, indicies, nums, num)
            indicies[updateLength] = i
            length = max(length, updateLength)

        return length
    
    def lengthOfLIS_dp(self, nums: list[int]) -> int:
        memo = [1] * len(nums)

        for i in range(len(nums) - 1, -1 , -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])

        return max(memo)
    
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [10,9,2,5,3,7,101,18]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

        nums = [0,1,0,3,2,3]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

        nums = [7,7,7,7,7,7]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

        
if __name__ == '__main__':
    unittest.main()
