class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        real_sum = 0
        nums_sum = 0
        for i in range(len(nums)):
            nums_sum += nums[i]
            real_sum += i + 1

        return real_sum - nums_sum

        