class Solution:
    def climbStairs(self, n: int) -> int:
        # steps[n] for any n, = steps[n - 1] + steps[n - 2]

        if n <= 2:
            return n

        a, b = 1, 2

        for i in range(2, n):
            a, b = b, a + b
        
        return b

        