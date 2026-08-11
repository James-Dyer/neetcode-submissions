class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for point in points:
            dist = self.distance(point)
            if len(heap) < k:
                heapq.heappush(heap, (-dist, point))
                continue

            if -dist > heap[0][0]:
                heapq.heapreplace(heap, (-dist, point))

        return [point for _, point in heap]

    def distance(self, point):
        x, y = point
        return x**2 + y**2