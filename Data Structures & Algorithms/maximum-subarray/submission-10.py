class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        sums = [0] * (len(nums) + 1)
        res = -float('INF')
        for right in range(1, len(nums) + 1):
            sums[right] = sums[right - 1] + nums[right - 1]
            curr = sums[right] - sums[left]
            res = max(res, curr)
            if curr <= 0:
                left = right

        return res