class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqs = defaultdict(int)
        n = len(hand)
        if n % groupSize != 0:
            return False

        # buld freq dict
        for val in hand:
            freqs[val] += 1

        hand.sort()
        
        for val in hand:
            if freqs[val] == 0:
                continue
            
            for x in range(val, val+groupSize):
                if freqs[x] == 0:
                    return False
                freqs[x] -= 1
                    
        return True
