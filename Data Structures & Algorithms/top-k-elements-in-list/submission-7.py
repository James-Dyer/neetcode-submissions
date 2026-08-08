class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        buckets = [[] for _ in range(n + 1)]

        for num in freq:
            buckets[freq[num]].append(num)

        res = []

        for i in range(n, -1, -1):
            for v in buckets[i]:
                if len(res) < k:
                    res.append(v)
                else:
                    return res

        return res