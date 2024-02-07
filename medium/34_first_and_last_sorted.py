import unittest

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = -1
        end = -1
        if not nums:
            return [start, end]

        def binSearch(target, leftBias):
            left, right = 0, len(nums) - 1
            i = -1
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    i = mid
                    if leftBias:
                        right = mid - 1
                    else:
                        left = mid + 1
            return i
        
        left = binSearch(target, True)
        right = binSearch(target, False)

        return [left, right]
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [5,7,7,8,8,10]
        target = 8
        self.assertEqual(self.solution.searchRange(nums, target), [3, 4])

        nums = [5,7,7,8,8,10]
        target = 6
        self.assertEqual(self.solution.searchRange(nums, target), [-1, -1])

        nums = []
        target = 0
        self.assertEqual(self.solution.searchRange(nums, target), [-1, -1])
        
if __name__ == '__main__':
    unittest.main()
