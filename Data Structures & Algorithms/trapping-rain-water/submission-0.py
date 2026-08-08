class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        prefix = [0]*(len(height))
        suffix = [0]*(len(height))

        prefix_max, suffix_max = 0, 0
        for i in range(len(height)):
            prefix[i] = max(prefix_max, height[i])
            prefix_max = prefix[i]
            j = len(height) - 1 - i
            suffix[j] = max(suffix_max, height[j])
            suffix_max = suffix[j]

        area = 0
        for i in range(len(height)):
            area += min(prefix[i],suffix[i]) - height[i]

        return area