class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        used = set()

        def bt():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            for j in range(len(nums)):
                if nums[j] in used:
                    continue

                permutation.append(nums[j])
                used.add(nums[j])
                bt()
                permutation.pop()
                used.remove(nums[j])

        bt()
        return res