class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = []

        for num1 in nums1:
            for num2 in nums2:
                res.append(num1 * num2)
        
        res.sort()

        return res[k - 1]
