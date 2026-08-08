class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            for j in range(i + 1, len(numbers)):
                if i == j:
                    continue

                complement = target - numbers[i]
                if numbers[j] == complement:
                    return [i + 1, j + 1] # 1-indexed 
        
        return [-1]
                
                
