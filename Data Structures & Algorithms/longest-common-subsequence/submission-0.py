class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2) 
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        def func(i, j):
            if i == n or j == m:
                return 0

            if dp[i][j] != -1: # use memoized value
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + func(i + 1, j + 1) 
            else:
                dp[i][j] = max(
                    func(i + 1, j),
                    func(i, j + 1)
                )

            return dp[i][j]

        return func(0, 0)