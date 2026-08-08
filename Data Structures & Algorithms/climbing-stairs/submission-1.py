class Solution:
    def climbStairs(self, n: int) -> int:
        # steps[n] for any n, = steps[n - 1] + steps[n - 2]

        if n <= 2:
            return n

        dp = [1, 2]

        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        
        return dp[n - 1]

        