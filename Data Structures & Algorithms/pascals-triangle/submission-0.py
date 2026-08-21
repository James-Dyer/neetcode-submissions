class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def sum_parents(i, prev):
            left = prev[i - 1] if i - 1 >= 0 else 0
            right = prev[i] if i < len(prev) else 0
            return left + right
        
        # for idx curr[i], parents are prev[i - 1] + prev[i]

        res = [[1]]
        size = 1
        prev = [1]

        while size < numRows:
            size += 1
            curr = []
            for i in range(size):
                curr.append(sum_parents(i, prev))
            res.append(curr)
            prev = curr

        

        return res
