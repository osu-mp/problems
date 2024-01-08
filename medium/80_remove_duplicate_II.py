import unittest

class Solution:
    """
    Runtime
Details
49ms
Beats 91.68%of users with Python3
Memory
Details
17.44MB
Beats 6.91%of users with Python3
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0 
        right = 0
        nums_size = len(nums)
        while right < nums_size:
            count = 1
            while right + 1 < nums_size and nums[right] == nums[right + 1]:
                right += 1
                count += 1

            for i in range(min(2, count)):
                nums[left] = nums[right]
                left += 1

            right += 1
        return left
    
    def removeDuplicates_fail(self, nums: list[int]) -> int:
        if len(nums) in [0, 1, 2]:
            return len(nums)
        
        k = 2
        count = 0
        val = float('inf')
        # TODO not done
        print(f"{nums=}")
        for i in range(2, len(nums)):
            print(f"{i=}, {k=}, {nums[i]=}, {nums[k]=}, {nums[k-1]=}, {nums[k-2]=}")
            if  (nums[i] == nums[k] and nums[i] == nums[k - 1] and nums[i] == nums[k - 2]):
                k += 1
                print("  HIT")

            else:
                print("  NOT HIT")
            nums[i] = nums[k]
                
            print(f"  {nums=}")
            
            # if nums[i] == val:
            #     count += 1
            #     if count > 2:
            #         k += 1
            # elif nums[i] != val:          # this avoids swapping the same value with itself, increased efficiency from 5% to 96%
            #     nums[k] = nums[i]
            #     k += 1
            # val = nums[i]

        return k

    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        nums = [1,1,1,2,2,3]
        expected_k = 5
        expected_nums = [1, 1, 2, 2, 3]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(expected_k, k)
        self.assertEqual(expected_nums, nums[:k])

        nums = [0,0,1,1,1,1,2,3,3]
        expected_k = 7
        expected_nums = [0,0,1,1,2,3,3]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(expected_k, k)
        self.assertEqual(expected_nums, nums[:k])

    # def test_mine(self):
    #     nums = []
    #     expected_k = 0
    #     expected_nums = []
    #     k = self.solution.removeDuplicates(nums)
    #     self.assertEqual(expected_k, k)
    #     self.assertEqual(expected_nums, nums[:k])

    #     nums = [-1,-1,-1,-1]
    #     expected_k = 1
    #     expected_nums = [-1]
    #     k = self.solution.removeDuplicates(nums)
    #     self.assertEqual(expected_k, k)
    #     self.assertEqual(expected_nums, nums[:k])

    #     nums = [-2,-1,-1,0]
    #     expected_k = 3
    #     expected_nums = [-2,-1, 0]
    #     k = self.solution.removeDuplicates(nums)
    #     self.assertEqual(expected_k, k)
    #     self.assertEqual(expected_nums, nums[:k])

        
if __name__ == '__main__':
    unittest.main()
