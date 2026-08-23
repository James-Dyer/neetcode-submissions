from collections import defaultdict
import heapq

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        # dict freqs: (hashed patterns) -> freq

        # build dict visits: (name) -> [sites in order of timestamp]
        # iterate thru visits and update freq for every subsequence in [sites in order of timestamp]

        # track and return larges freq value

        max_score = 0
        best = None

        freqs = defaultdict(int) # (hashed patterns) -> freq
        visits = defaultdict(list) # (name) -> [sites in order of timestamp]
        consolidated_data = list(zip(timestamp, website, username))
        consolidated_data.sort()

        for time, site, user in consolidated_data:
            visits[user].append(site)

        for user, sites in visits.items():
            seen = set()

            for i in range(len(sites)):
                for j in range(i + 1, len(sites)):
                    for k in range(j + 1, len(sites)):
                        pattern = (sites[i], sites[j], sites[k])
                        seen.add(pattern)

            for pattern in seen:
                freqs[pattern] += 1 
                if freqs[pattern] > max_score:
                    max_score = freqs[pattern]
                    best = pattern
                elif freqs[pattern] == max_score:
                    best = min(best, pattern)

        return list(best)
        

        
        







# username = ["bob","bob","bob","alice","alice","alice","alice","charlie","charlie","charlie"],

# timestamp = 
# [1,2,3,4,5,6,7,8,9,10], 

# website = ["home","about","career","home","cart","maps","home","home","about","career"]

# Output: ["home","about","career"]

