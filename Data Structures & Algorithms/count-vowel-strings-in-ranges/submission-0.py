class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        prefix = [0] * (len(words) + 1) # prefix[i] = how many targets come before i
        # ans[li, ri] = prefix[ri] - prefix[li]
        # O(words + queries) time
        # O(words + queries) space

        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] = 1
            prefix[i + 1] += prefix[i]

        ans = []

        for li, ri in queries:
            ans.append(prefix[ri + 1]-prefix[li])

        return ans
            