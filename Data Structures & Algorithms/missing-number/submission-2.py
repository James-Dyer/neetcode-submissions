class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]

        return xorr
        # key idea: xor itself twice, 
        # one from clean list 0 -> n - 1, 
        # one from nums[0] -> nums[n - 1]