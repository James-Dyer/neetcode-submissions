class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [None] * len(nums)
        stack = deque()
        stack.append(0)

        while stack:
            i = stack.pop()
            if i in memo:
                return memo[i]
            if i >= len(nums) - 1:
                return True
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                stack.append(j)

            memo[i] = False

        return False
        