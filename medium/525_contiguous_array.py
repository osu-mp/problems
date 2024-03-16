import unittest


class Solution:
	def findMaxLength(self, nums: list[int]) -> int:
		seen_at = {}
		seen_at[0] = -1

		res = 0
		count = 0
		for i, num in enumerate(nums):
			if num:
				count += 1
			else:
				count -= 1

			if count in seen_at:
				res = max(res, i - seen_at[count])
			else:
				seen_at[count] = i

		return res


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def test_given(self):
		nums = [0,1]
		self.assertEqual(self.solution.findMaxLength(nums), 2)


if __name__ == '__main__':
	unittest.main()