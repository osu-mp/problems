import collections
import unittest

class Solution:
    """
    Runtime
Details
140ms
Beats 83.97%of users with Python3
Memory
Details
18.79MB
Beats 22.92%of users with Python3
    """
    def majorityElement(self, nums: list[int]) -> bool:
        target = len(nums) / 2
        found_nums = collections.defaultdict(int)
        for num in nums:
            found_nums[num] += 1
            if found_nums[num] > target:
                return num
            
        return None
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [3, 2, 3]
        self.assertEqual(self.solution.majorityElement(nums), 3)

        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(self.solution.majorityElement(nums), 2)


if __name__ == '__main__':
    unittest.main()
