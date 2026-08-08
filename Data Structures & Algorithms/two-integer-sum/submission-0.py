class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mySet = dict()

        for i in range(len(nums)):
            # check for complement
            complement = target - nums[i]
            if complement in mySet:
                if i < mySet[complement]:
                    return [i, mySet[complement]]
                else:
                    return [mySet[complement], i]
            # if not add to set
            else:
                mySet[nums[i]] = i

        return []
