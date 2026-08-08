class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ss = []
        candidates.sort()

        def dfs(i):
            my_sum = sum(ss)
            if my_sum == target:
                res.append(ss.copy())
                return
            if i >= len(candidates) or my_sum > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                ss.append(candidates[j])
                dfs(j + 1)
                ss.pop()

        dfs(0)
        return res
            
