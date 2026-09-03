class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        stack = []
        for ch in s:
            if ch in lookup:
                stack.append(lookup[ch])
            else:
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()

        return True if not stack else False
            