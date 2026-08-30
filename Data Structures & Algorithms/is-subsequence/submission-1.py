class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        for pt in range(len(t)):
            if ps < len(s) and t[pt] == s[ps]:
                ps += 1
        
        return ps == len(s)