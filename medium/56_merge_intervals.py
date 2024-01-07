import unittest

class Solution:
    """
    Runtime
Details
128ms
Beats 83.42%of users with Python3
Memory
Details
22.04MB
Beats 7.06%of users with Python3
    """
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i : i[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(self.solution.merge(intervals), expected)

        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_mine(self):
        intervals = [[1,3],[2,9],[8,10],[15,18]]
        expected = [[1,10],[15,18]]
        self.assertEqual(self.solution.merge(intervals), expected)


if __name__ == '__main__':
    unittest.main()
