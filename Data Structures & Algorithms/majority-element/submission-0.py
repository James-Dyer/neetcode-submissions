class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = None
        max_freq = 0
        for num in nums:
            freq[num] += 1
            if freq[num] > max_freq:
                max_freq = freq[num]
                res = num
        
        return res