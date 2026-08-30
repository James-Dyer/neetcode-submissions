class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0

        s = s.strip()
        idx = len(s) - 1
        while idx >= 0 and s[idx] != ' ':
            idx -= 1
        
        return len(s) - idx - 1