import unittest

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = k % len_nums   
        # reverse the entire list first
        self.reverse(0, len_nums - 1, nums)
        
        # then reverse each sublist (using k as the divider)
        self.reverse(0, k - 1, nums)
        
        # reverse the second portion 
        self.reverse(k, len_nums - 1, nums)   
        
    def reverse(self, left, right, nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [1,2,3,4,5,6,7]
        k = 1
        expected_nums = [7,1,2,3,4,5,6]
        k = self.solution.rotate(nums, k)
        self.assertEqual(expected_nums, nums)

        nums = [1,2,3,4,5,6,7]
        k = 3
        expected_nums = [5,6,7,1,2,3,4]
        k = self.solution.rotate(nums, k)
        self.assertEqual(expected_nums, nums)

        
if __name__ == '__main__':
    unittest.main()
