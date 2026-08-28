import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i, v in enumerate(nums[0:k]):
            heap.append((-v, i))

        heapq.heapify(heap)
        res.append(-heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            res.append(-heap[0][0])
            
        
        return res
                



