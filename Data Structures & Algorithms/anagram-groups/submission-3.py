class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        # create freq array for every string
        for string in strs:
            freq_arr = [0] * 26
            for letter in string:
                freq_arr[ord(letter) - ord('a')] += 1
            # append to dict
            res[tuple(freq_arr)].append(string)
        
        # convert dict back to list of lists
        return list(res.values())
