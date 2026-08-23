class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        freq = [0] * 26

        for ch in magazine:
            freq[ord(ch) - ord('a')] += 1
        
        for ch in ransomNote:
            freq[ord(ch) - ord('a')] -= 1
            if freq[ord(ch) - ord('a')] < 0:
                return False
        
        return True
        