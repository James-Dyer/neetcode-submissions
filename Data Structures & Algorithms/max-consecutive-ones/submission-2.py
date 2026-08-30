class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct = 0
        res = 0
        prev = None
        for num in nums:
            # num is 1 and prev = 1, counter++
            # else reset
            if num == 1 and prev == 1:
                ct += 1
                res = max(ct , res)
            elif num == 1 and prev != 1:
                ct = 1
                res = max(ct , res)
            else:
                ct = 0
            prev = num
        return res

