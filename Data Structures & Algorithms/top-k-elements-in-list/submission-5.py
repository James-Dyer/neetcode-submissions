class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums: # O(n)
            freq_map[num] += 1 

        res = []
        for num in freq_map: # O(n)
            heapq.heappush(res, (freq_map[num], num)) # O(log k)
            if len(res) > k:
                heapq.heappop(res) # O(log k)

        return [num for _, num in res]

        # O(n log k)
            