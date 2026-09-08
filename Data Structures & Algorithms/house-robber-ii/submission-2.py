class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        nums1 = nums[:-1]
        nums2 = nums[1:]

        dp = [0] * (len(nums) - 1)
        for i in range(len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + nums1[i])

        first_max = dp[-1]

        dp = [0] * (len(nums) - 1)
        for i in range(len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + nums2[i])

        sec_max = dp[-1]

        return max(first_max, sec_max)
