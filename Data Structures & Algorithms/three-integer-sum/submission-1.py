class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums)-1
            while j < k:
                if i == j:
                    j += 1
                if i == k:
                    k -= 1
                    
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif curr_sum < 0:
                    j += 1
                else:
                    k -= 1

        return triplets
