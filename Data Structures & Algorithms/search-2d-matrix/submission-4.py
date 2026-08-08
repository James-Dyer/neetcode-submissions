class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1
        while left <= right:
            center = left + (right - left) // 2
            cx, cy = center // m, center % m
            if matrix[cx][cy] < target:
                left = center + 1
            elif matrix[cx][cy] > target:
                right = center - 1
            else:
                return True
        return False