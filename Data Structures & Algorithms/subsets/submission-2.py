class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        ss = []
        def dfs(i):
            if i >= len(nums):
                return res.append(ss.copy())
            
            ss.append(nums[i])
            dfs(i+1)

            ss.pop()
            dfs(i+1)
            
        dfs(0)
        return res