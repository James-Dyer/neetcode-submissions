class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # in a prefix array, we know a subarray exists if y - x = target
        # where y is the current running sum, and x is a previous running sum.
        res = 0
        running_sum = 0
        prev_sums = defaultdict(int)
        prev_sums[0] = 1
        for i in range(len(nums)):
            running_sum += nums[i]
            complement = running_sum - k
            res += prev_sums[complement]
            prev_sums[running_sum] += 1

        return res