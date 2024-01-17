from collections import defaultdict
import unittest

"""
Runtime
76
ms
Beats
69.74%
of users with Python3
Memory
17.38
MB
Beats
56.68%
of users with Python3
"""
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        def slope_of_points(pt_a, pt_b):
            x_a, y_a = pt_a[0], pt_a[1]
            x_b, y_b = pt_b[0], pt_b[1]

            if (x_b - x_a) == 0:
                return float('inf')
            
            return (y_b - y_a) / (x_b - x_a)
        
        max_pts = 0
        for i, point in enumerate(points):
            pts_per_slope = defaultdict(int)
            for j, j_point in enumerate(points):
                if j == i:
                    continue
                slope = slope_of_points(point, j_point)
                pts_per_slope[slope] += 1
            if pts_per_slope:
                max_pts = max(max_pts, max(pts_per_slope.values()))
        return max_pts + 1
        
    
    
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        points = [[1,1],[2,2],[3,3]]
        self.assertEqual(self.solution.maxPoints(points), 3)

        points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        self.assertEqual(self.solution.maxPoints(points), 4)




        
if __name__ == '__main__':
    unittest.main()
