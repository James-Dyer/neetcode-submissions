class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        res = []
        for num in freq_map:
            heapq.heappush(res, (freq_map[num], num))
            if len(res) > k:
                heapq.heappop(res)
        

        return [num for _, num in res]
        
            