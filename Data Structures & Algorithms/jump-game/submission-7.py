class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        idx = len(nums)-1
        while goal != 0:
            if idx == -1:
                return False
            idx -= 1
            if goal - idx <= nums[idx]:
                goal = idx
        
        return True