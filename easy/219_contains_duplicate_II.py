from collections import Counter
import unittest

"""
Runtime
499
ms
Beats
71.11%
of users with Python3
Memory
30.47
MB
Beats
37.51%
of users with Python3
"""
class Solution:
    def containsNearbyDuplicate_simple(self, nums: list[int], k: int) -> bool:
        
        for i in range(len(nums)):
            stop_ind = min(len(nums), i + k + 1)
            for j in range(i + 1, stop_ind):
                if nums[i] == nums[j]:
                    return True
        return False
    
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        counts = Counter(nums)

        # Keep only items that appear more than once
        non_unique_items = [item for item in nums if counts[item] > 1]
        
        for i in range(len(nums)):
            if nums[i] not in non_unique_items:
                continue
            stop_ind = min(len(nums), i + k + 1)
            for j in range(i + 1, stop_ind):
                if nums[i] == nums[j]:
                    return True
        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [1,2,3,1]
        k = 3
        self.assertTrue(self.solution.containsNearbyDuplicate(nums, k))

        nums = [1,0,1,1]
        k = 1
        self.assertTrue(self.solution.containsNearbyDuplicate(nums, k))

        nums = [1,2,3,1,2,3]
        k = 2
        self.assertFalse(self.solution.containsNearbyDuplicate(nums, k))

    def test_mine(self):
        nums = []
        for i in range(10000000):
            nums.append(i)
        self.assertFalse(self.solution.containsNearbyDuplicate(nums, 10))


if __name__ == '__main__':
    unittest.main()
 