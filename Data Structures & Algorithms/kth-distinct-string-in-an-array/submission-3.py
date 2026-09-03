class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = defaultdict(int)
        distinct = 0
        for st in arr:
            freq[st] += 1

        for st in arr:
            if freq[st] == 1:
                distinct += 1
                if distinct == k:
                    return st

        return ""