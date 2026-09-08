from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[i][j] = dp[i-1][j] + dp[i][j-1] (num of unique paths to get to grid[i][j])
        # fill dp array bottom up using bfs

        # dp[0][0] = 1

        queue = deque()
        queue.append((0, 0))
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        seen = set()

        while queue:
            y, x = queue.popleft()
            if (y, x) in seen:
                continue
            seen.add((y, x))

            # dp logic
            if (y, x) != (0, 0):
                top = dp[y-1][x] if y - 1 >= 0 else 0
                left = dp[y][x-1] if x - 1 >= 0 else 0
                dp[y][x] = top + left


            
            # bfs logic
            if y + 1 < m:
                queue.append((y + 1, x))
            if x + 1 < n:
                queue.append((y, x + 1))

        
        return dp[-1][-1]