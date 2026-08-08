class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # stack contains days that havent resolved yet
        stack = deque()
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # check stack
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                res[j] = i - j

            # add current to stack
            stack.append(i)

        return res
