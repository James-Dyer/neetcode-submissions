class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = {"+", "-", "*", "/"}
        for element in tokens:
            if element in operators:
                opd2 = int(stack.pop())
                opd1 = int(stack.pop())
                match element:
                    case "+":
                        ans = opd1 + opd2
                    case "-":
                        ans = opd1 - opd2
                    case "*":
                        ans = opd1 * opd2
                    case "/":
                        ans = int(opd1 / opd2)
                stack.append(ans)
            else:
                stack.append(element)
        
        return int(stack[-1])
        