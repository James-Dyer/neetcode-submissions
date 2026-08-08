class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        my_set = set()
        max_num = -(10 ** 9)
        min_num = 10 ** 9
        for num in nums:
            my_set.add(num)
            max_num = max(max_num, num)
            min_num = min(min_num, num)

        length = 1
        max_length = 1
        for num in range(min_num + 1, max_num + 1):
            if num in my_set:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 0

        return max_length


        
        