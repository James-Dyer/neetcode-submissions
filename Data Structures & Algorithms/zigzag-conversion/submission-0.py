class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zig = [[] for _ in range(numRows)]
        # TODO edge cases for numRows < 3

        i = 0
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    zig[j].append(s[i])
                    i += 1
                else:
                    break
            for j in range(numRows - 2):
                if i < len(s):
                    zig[numRows - 2 - j].append(s[i])
                    i += 1
                else:
                    break
            
        res = []
        for row in zig:
            res += row

        return "".join(res)
            