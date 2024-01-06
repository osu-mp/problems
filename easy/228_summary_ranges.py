import unittest

class Solution:
    """
    Runtime
Details
38ms
Beats 56.61%of users with Python3
Memory
Details
17.41MB
Beats 10.51%of users with Python3
"""
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        
        ranges = []
        start = nums[0]
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > (last + 1):
                if start != last:
                    ranges.append(f"{start}->{last}")
                else:
                    ranges.append(f"{start}")
                start = nums[i]
            last = nums[i]

        if start != last:
            ranges.append(f"{start}->{last}")
        else:
            ranges.append(f"{start}")

        return ranges

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [0,1,2,4,5,7]
        expected = ["0->2","4->5","7"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

        nums = [0,2,3,4,6,8,9]
        expected = ["0","2->4","6","8->9"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_mine(self):
        nums = []
        expected = []
        self.assertEqual(self.solution.summaryRanges(nums), expected)

        nums = ["5"]
        expected = ["5"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)
        
if __name__ == '__main__':
    unittest.main()
