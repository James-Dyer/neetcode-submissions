class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            subset_sum = sum(subset)
            if subset_sum == target:
                res.append(subset.copy())
                return
            elif subset_sum > target or i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res