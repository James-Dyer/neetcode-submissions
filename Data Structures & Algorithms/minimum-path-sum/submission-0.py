class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # brute force: recursivly explore every path to bottom right >O(n*m)
        # 2d DP (bottom up): O(n*m)

        n = len(grid)
        m = len(grid[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        
        for x in range(n):
            for y in range(m):
                if x == 0 and y == 0:
                    continue
                # dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x][y]
                up = float('inf') if x == 0 else dp[x-1][y]
                left = float('inf') if y == 0 else dp[x][y-1]
                dp[x][y] = min(up, left) + grid[x][y]

        return dp[n - 1][m - 1]