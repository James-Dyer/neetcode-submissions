class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # sliding window
        w_ct = 0
        
        for right in range(k):
            if blocks[right] == 'W':
                w_ct += 1

        left = 0
        res = w_ct
        for right in range(k, len(blocks)):
            if blocks[right] == 'W':
                w_ct += 1
            if blocks[left] == 'W':
                w_ct -= 1
            res = min(res, w_ct)
            
            left += 1
            
        return res
            
