
import unittest

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        result = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])
            # print(f"{left=}, {mid=}, {right=}, {nums[left]=}, {nums[mid]=}, {nums[right]=}")
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            
        return result
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [3,1,2]
        self.assertEqual(self.solution.findMin(nums), 1)

        nums = [3,4,5,1,2]
        self.assertEqual(self.solution.findMin(nums), 1)

        nums = [4,5,6,7,0,1,2]
        self.assertEqual(self.solution.findMin(nums), 0)

        nums = [11,13,15,17]
        self.assertEqual(self.solution.findMin(nums), 11)
        
if __name__ == '__main__':
    unittest.main()
