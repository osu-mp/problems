import unittest

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        
        points.sort()
        prev = points[0]
        count = 1
        for start, end in points[1:]:
            if start > prev[1]:
                count += 1
                prev = [start, end]
            else:
                prev[1] = min(prev[1], end)
        
        return coufrom
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        points = [[10,16],[2,8],[1,6],[7,12]]
        self.assertEqual(self.solution.findMinArrowShots(points), 2)

        points = [[1,2],[3,4],[5,6],[7,8]]
        self.assertEqual(self.solution.findMinArrowShots(points), 4)

        points = [[1,2],[2,3],[3,4],[4,5]]
        self.assertEqual(self.solution.findMinArrowShots(points), 2)

        
if __name__ == '__main__':
    unittest.main()
