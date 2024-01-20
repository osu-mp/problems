import unittest

"""
Runtime
155
ms
Beats
97.51%
of users with Python3
Memory
23.56
MB
Beats
95.82%
of users with Python3
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        
        # first pass: prefix
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
            
        # second pass: postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [1,2,3,4]
        expected = [24,12,8,6]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

        nums = [-1,1,0,-3,3]
        expected = [0,0,9,0,0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

        
if __name__ == '__main__':
    unittest.main()