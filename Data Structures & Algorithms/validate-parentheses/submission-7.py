class Solution:
    def isValid(self, s: str) -> bool:

        chars = {')':'(', '}':'{', ']':'['}
        stack = deque([])
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif not stack:
                return False
            elif chars[char] != stack.pop():
                return False

        if stack:
            return False
        else:
            return True


