class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in ops:
                match token:
                    case '/':
                        div2 = int(stack.pop())
                        div1 = int(stack.pop())
                        res = int(div1/div2)
                        stack.append(res)

                    case '*':
                        first = int(stack.pop())
                        second = int(stack.pop())
                        res = first * second
                        stack.append(res)
                    case '+':
                        first = int(stack.pop())
                        second = int(stack.pop())
                        res = first + second
                        stack.append(res)
                    case '-':
                        first = int(stack.pop())
                        second = int(stack.pop())
                        res = second - first
                        stack.append(res)
            else:
                stack.append(token)
    
        return int(stack.pop())