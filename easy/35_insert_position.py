import unittest

class Solution:
    """
    Runtime
Details
41ms
Beats 98.60%of users with Python3
Memory
Details
18.13MB
Beats 11.56%of users with Python3
    """
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if target < nums[left]:
            return 0
        if target > nums[right - 1]:
            return right + 1
        
        while left <= right:
            print(f"{left=}, {right=}")
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left
    


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [1,3,5,6]
        target = 5
        self.assertEqual(self.solution.searchInsert(nums, target), 2)

        nums = [1,3,5,6]
        target = 2
        self.assertEqual(self.solution.searchInsert(nums, target), 1)

        nums = [1,3,5,6]
        target = 7
        self.assertEqual(self.solution.searchInsert(nums, target), 4
                         )


if __name__ == '__main__':
    unittest.main()