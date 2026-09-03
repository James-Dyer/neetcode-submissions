class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen set
        # sliding window tracking seen set
        # right increments thru s, when we get a dupe, left = idx of dupe + 1
        # 
        res = 0
        seen = {} # char -> idx

        left = 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left: # ignore values outside of window
                left = seen[s[right]] + 1
            seen[s[right]] = right
            res = max(right + 1 - left, res)
        
        return res
                
