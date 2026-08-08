class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] is the max money made robbing house[i] + prev houses
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        res = 0
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        res = max(dp)
        
        

        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
            res = max(res, dp[i])
        
        return res