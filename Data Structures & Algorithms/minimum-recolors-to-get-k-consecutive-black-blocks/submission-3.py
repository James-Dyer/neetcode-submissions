class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # sliding window
        w_ct = 0
        res = float('INF')
        
        for right in range(k):
            if blocks[right] == 'W':
                w_ct += 1

        left = 0
        for right in range(k - 1, len(blocks)):
            res = min(res, w_ct)
            if blocks[left] == 'W':
                w_ct -= 1
            left += 1

            if right < len(blocks) - 1 and blocks[right + 1] == 'W':
                w_ct += 1
            
        return res
            
