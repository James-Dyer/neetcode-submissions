class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two ptr apprach
        # when we hit the first mismatch, check the letters in front
        # if at least one letter in front can resolve (match the other pointer) it

        def is_palendrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return (
                    is_palendrome(left + 1, right) or
                    is_palendrome(left, right - 1)
                )
            left += 1
            right -= 1

        return True
            