import unittest

"""
Simple solution got 93%, quickSelect timed out
Runtime
448
ms
Beats
93.06%
of users with Python3
Memory
29.79
MB
Beats
66.12%
of users with Python3
"""
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[-k]
    
    def findKthLargest_quickSelect(self, nums: list[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(left, right):
            pivot = nums[right]
            p = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]

            if p > k:
                return quickSelect(left, p - 1)
            elif p < k:
                return quickSelect(p + 1, right)
            else:
                return nums[p]
            
        return quickSelect(0, len(nums) - 1)
            
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [3,2,1,5,6,4]
        k = 2
        self.assertEqual(self.solution.findKthLargest(nums, k), 5)

        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        self.assertEqual(self.solution.findKthLargest(nums, k), 4)
        
if __name__ == '__main__':
    unittest.main()