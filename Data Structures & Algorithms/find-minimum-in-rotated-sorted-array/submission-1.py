class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # before we do the regular boundary move, check:
        # if right value is less than center value:
        # right = center
        # if left value is greater than center value:
        # left = center

        left, right = 0, len(nums) - 1

        while left <= right:
            center = left + (right - left)//2
            
            if nums[right] < nums[center]:
                left = center + 1
            elif nums[right] > nums[center]:
                right = center
            else:
                break

        return nums[left]
        
        