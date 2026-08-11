class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # Max heap: negative frequencies
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        # (remaining_count, time_when_available_again)
        queue = deque()

        time = 0

        while heap or queue:
            time += 1

            # If a task is available, execute the most frequent one
            if heap:
                count = heapq.heappop(heap)
                count += 1  # e.g. -3 becomes -2

                if count < 0:
                    queue.append((count, time + n))

            # Put cooled-down task back into heap
            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush(heap, count)

        return time