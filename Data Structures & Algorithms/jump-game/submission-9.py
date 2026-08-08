class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for idx in range(len(nums)-2, -1, -1):
            if goal <= nums[idx] + idx:
                goal = idx
        
        return goal == 0