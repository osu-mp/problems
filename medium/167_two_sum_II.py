import unittest

"""
Runtime
100
ms
Beats
96.00%
of users with Python3
Memory
18.22
MB
Beats
29.90%
of users with Python3
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        numbers = [2,7,11,15]
        target = 9
        expected = [1, 2]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

        numbers = [2,3,4]
        target = 6
        expected = [1, 3]
        self.assertEqual(self.solution.twoSum(numbers, target), expected)

        
if __name__ == '__main__':
    unittest.main()
