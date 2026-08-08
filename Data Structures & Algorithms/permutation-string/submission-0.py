class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        for letter in s1:
            s1_freq[letter] += 1
        
        for right in range(len(s2)):
            s2_freq[s2[right]] += 1
            left = right - len(s1)
            if left >= 0:
                s2_freq[s2[left]] -= 1
                if s2_freq[s2[left]] == 0:
                    del s2_freq[s2[left]]

            if s1_freq == s2_freq:
                return True
        return False
            
