import unittest

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
            
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [3,2,2,3]
        val = 3
        expected_k = 2
        expected_nums = [2, 2]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(expected_k, k)
        self.assertEqual(expected_nums, nums[:k])

        nums = [0,1,2,2,3,0,4,2]; val = 2
        expected_k = 5
        expected_nums = [0,1,3,0,4]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(expected_k, k)
        self.assertEqual(expected_nums, nums[:k])

        
if __name__ == '__main__':
    unittest.main()
