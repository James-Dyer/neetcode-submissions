class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0]*26
        s2_freq = [0]*26
        for letter in s1:
            i = ord(letter) - ord("a")
            s1_freq[i] += 1
        
        for right in range(len(s2)):
            i = ord(s2[right]) - ord("a")
            s2_freq[i] += 1
            left = right - len(s1)
            if left >= 0:
                j = ord(s2[left]) - ord("a")
                s2_freq[j] -= 1

            if s1_freq == s2_freq:
                return True
        return False
            
