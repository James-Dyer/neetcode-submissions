

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # num of days after i before a warmer temp w: w - i
        n = len(temperatures)
            
        res = [0] * n
        stack = deque() # idx, val

        for i in range(n):
            while stack and temperatures[i] > stack[-1][1]:
                j, val = stack.pop()
                res[j] = i - j
            stack.append((i, temperatures[i]))

        return res