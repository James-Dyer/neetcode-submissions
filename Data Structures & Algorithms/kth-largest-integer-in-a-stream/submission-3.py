class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        else:
            curr = self.heap[0]
            if val <= curr:
                return curr
            else:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
                return self.heap[0]

        