import collections
import unittest

"""
Runtime
250
ms
Beats
73.69%
of users with Python3
Memory
24.29
MB
Beats
36.21%
of users with Python3
"""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0 
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (0 <= r < rows and 
                        0 <= c < cols and
                        grid[r][c] == "1" and \
                        (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))
    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
        
 
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_given(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
        self.assertEqual(self.solution.numIslands(grid), 1)
        
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
        self.assertEqual(self.solution.numIslands(grid), 3)

        grid = [
            ["1","1","0","1","1"],
            ["0","0","0","0","0"],
            ["0","0","1","0","0"],
            ["1","0","0","1","1"]
            ]
        self.assertEqual(self.solution.numIslands(grid), 5)


if __name__ == '__main__':
    unittest.main()