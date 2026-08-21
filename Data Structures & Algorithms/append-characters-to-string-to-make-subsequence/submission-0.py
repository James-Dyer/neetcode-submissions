class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pt = 0

        for ps in range(len(s)):
            if s[ps] == t[pt]:
                pt += 1
                if pt == len(t):
                    return 0
        
        return len(t) - pt
