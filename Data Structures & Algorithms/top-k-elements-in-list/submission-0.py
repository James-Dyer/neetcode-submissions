class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build frequency dictionary
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # build frequency counter
        counter = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            counter[count].append(num)
        
        # fill output array with top k frequent numbers
        output = []
        for i in range(len(counter)-1, 0, -1):
            for num in counter[i]:
                output.append(num)
                if len(output) == k:
                    return output
        
        return output
        
        

            