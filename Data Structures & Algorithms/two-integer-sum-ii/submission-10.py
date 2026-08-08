class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if numbers[i] == complement:
                continue 
            left, right = 0, len(numbers)-1
            while left <= right:
                center = left + (right - left) // 2
                if numbers[center] == complement:
                    return [i + 1, center + 1] # 1-indexed
                elif numbers[center] < complement:
                    left = center + 1
                else:
                    right = center - 1
        
        return [-1]
                
                
