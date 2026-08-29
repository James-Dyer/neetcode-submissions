class Solution:
    def trap(self, height: List[int]) -> int:
        # at idx i, what is the water trapped at i
        # water[i] = min(prefix[i], suffix[i]) - height[i], cant be negative
        # prefix[i] = max height before idx i
        # suffix[i] = max height after idx i

        res = 0
        suffix = [0] * len(height)
        prefix = [0] * len(height)
        for i in range(len(height)-2,-1,-1):
            suffix[i] = max(height[i+1], suffix[i+1])

        for i in range(1, len(height) - 1):
            prefix[i] = max(height[i - 1], prefix[i-1])
            res += max(min(prefix[i], suffix[i]) - height[i], 0)

        return res