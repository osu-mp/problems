import unittest

class Solution:
    """
    Runtime
Details
42ms
Beats 43.31%of users with Python3
Memory
Details
17.37MB
Beats 11.57%of users with Python3
    """
    def rob(self, nums: list[int]) -> int:
        rob_this = 0
        skip_this = 0

        for n in nums:
            temp = max(n + rob_this, skip_this)
            rob_this = skip_this
            skip_this = temp

        return skip_this
    
    def max_rob(self, nums: list[int], memo: dict={}) -> int:
        if not nums:
            return 0
        count = len(nums)
        if count in memo:
            return memo[count]
        
        rob_this = nums[0] + self.max_rob(nums[2:], memo)
        skip_this = self.max_rob(nums[1:], memo)

        memo[count] = max(rob_this, skip_this)
        print(f"{memo=}")
        return memo[count]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [1,2,3,1]
        expected = 4
        self.assertEqual(self.solution.rob(nums), expected)

        nums = [2,7,9,3,1]
        expected = 12
        self.assertEqual(self.solution.rob(nums), expected)
        
    def test_hidden(self):
        nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
        expected = 3365
        # self.assertEqual(self.solution.rob(nums), expected)
        

if __name__ == '__main__':
    unittest.main()        