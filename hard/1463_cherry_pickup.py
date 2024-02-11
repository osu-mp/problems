# import unitttest

class Solution:
    def cherryPickup_high(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(COLS)]
        for r in reversed(range(ROWS)):
            curr_dp = [[0] * COLS for _ in range(COLS)]
            for c1 in range(COLS - 1):
                for c2 in range(c1 + 1, COLS):
                    cherries = grid[r][c1] + grid[r][c2]
                    max_cherries = 0
                    for c1_d, c2_d in product([-1, 0, 1], [-1, 0, 1]):
                        nc1, nc2 = c1 + c1_d, c2 + c2_d
                        if nc1 < 0 or nc2 == COLS:
                            continue
                        max_cherries = max(
                            max_cherries,
                            cherries + dp[nc1][nc2]
                        )
                    curr_dp[c1][c2] = max_cherries
            dp = curr_dp
        return dp[0][COLS - 1]
    

    def cherryPickup_high_mem(self, grid: list[list[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        cache = {}

        def dfs(row, col1, col2):
            if (row, col1. col2) in cache:
                return cache[(row, col1, col2)]
            if col1 == col2 or min(col1, col2) < 0 or max(col1, col2) == COLS:
                return 0
            if row == ROWS - 1:
                return grid[row][col1] + grid[row][col2]
            
            result = 0
            for col1_diff in [-1, 0, 1]:
                for col2_diff in [-1, 0, 1]:
                    result = max(
                        result,
                        dfs(row + 1, col1 + col1_diff, col2 + col2_diff)
                    )
            cache[(row, col1, col2)] = result + grid[row][col1] + grid[row][col2]
            return cache[(row, col1, col2)]
        
        return dfs(0, 0, COLS - 1)
    
