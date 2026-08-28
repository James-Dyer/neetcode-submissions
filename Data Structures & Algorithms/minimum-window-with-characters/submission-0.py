class Solution:

    def minWindow(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        for ch in t:
            freq[ch] += 1

        count = len(t)
        res = ""

        # freq begins as freq hashmap of t
        # count is chars not in window, starts at len(t)
        # as chars enter the window
            # if freq[char] > 0, consume and count--
        # if count <= 0, its valid, check if its the shortest substring
        # return shortest substring

        left = 0 # inclusive, exclusive
        for right in range(len(s)):
            
            freq[s[right]] -= 1
            if freq[s[right]] >= 0:
                count -= 1

            if count <= 0:
                while freq[s[left]] < 0:
                    freq[s[left]] += 1
                    left += 1
                
                if res == "" or right - left + 1 < len(res):
                    res = s[left:right + 1]
            

        return res

        



