class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        lookup = set()

        for num in nums:
            lookup.add(num)
        
        count = 0
        max_count = 0
        # for any number if prev number isnt in the set reset count
        # otherwise increase count
        # track max count

        for num in nums:
            if num - 1 not in lookup:
                count = 1
                while num + count in lookup:
                    count += 1
            max_count = max(max_count, count)

        return max_count