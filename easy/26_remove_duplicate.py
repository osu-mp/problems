import unittest

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        val = float('inf')
        for i in range(len(nums)):
            if nums[i] != val:          # this avoids swapping the same value with itself, increased efficiency from 5% to 96%
                nums[k] = nums[i]
                k += 1
            val = nums[i]

        return k

    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [1,1,2]
        expected_k = 2
        expected_nums = [1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(expected_k, k)
        self.assertEqual(expected_nums, nums[:k])

        nums = [0,0,1,1,1,2,2,3,3,4]
        expected_k = 5
        expected_nums = [0,1,2,3,4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(expected_k, k)
        self.assertEqual(expected_nums, nums[:k])

    def test_mine(self):
        nums = []
        expected_k = 0
        expected_nums = []
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(expected_k, k)
        self.assertEqual(expected_nums, nums[:k])

        nums = [-1,-1,-1,-1]
        expected_k = 1
        expected_nums = [-1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(expected_k, k)
        self.assertEqual(expected_nums, nums[:k])

        nums = [-2,-1,-1,0]
        expected_k = 3
        expected_nums = [-2,-1, 0]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(expected_k, k)
        self.assertEqual(expected_nums, nums[:k])

        
if __name__ == '__main__':
    unittest.main()
