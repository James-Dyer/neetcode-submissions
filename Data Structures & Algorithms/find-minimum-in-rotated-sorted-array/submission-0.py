class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # before we do the regular boundary move, check:
        # if right value is less than center value:
        # right = center
        # if left value is greater than center value:
        # left = center

        left, right = 0, len(nums) - 1
        res = 1000

        while left <= right:
            center = left + (right - left)//2
            
            if nums[right] < nums[center]:
                left = center + 1
                res = min(res, nums[left], nums[right])
            elif nums[left] > nums[center]:
                right = center
                res = min(res, nums[left], nums[right])
            else:
                res = min(res, nums[left])
                break

        return res
        
        