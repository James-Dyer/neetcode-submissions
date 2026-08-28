class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # pin one element down and perform a two pointer scan over a sorted array to find the other two elements for the triplet
        # O(n^2) time

        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1 
            while left < right:
                target = -nums[i]

                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1

        return res