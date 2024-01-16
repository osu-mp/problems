from collections import Counter
import unittest

"""
Runtime
696
ms
Beats
78.73%
of users with Python3
Memory
21.53
MB
Beats
29.22%
of users with Python3
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triples = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    triples.append([nums[i], nums[left], nums[right]])
                    left += 1                    
                    while nums[left] == nums[left - 1] and left < right: 
                        left +=  1# right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return triples
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        # nums = [-1,0,1,2,-1,-4]
        # expected = [[-1,-1,2],[-1,0,1]]
        # self.assertEqual(self.solution.threeSum(nums), expected)

        # nums = [0,1,1]
        # expected = []
        # self.assertEqual(self.solution.threeSum(nums), expected)

        # nums = [0,0,0]
        # expected = [[0,0,0]]
        # self.assertEqual(self.solution.threeSum(nums), expected)

        nums = [-2,0,0,2,2]
        expected = [[-2,0,2]]
        self.assertEqual(self.solution.threeSum(nums), expected)
        
if __name__ == '__main__':
    unittest.main()
