class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'{': '}', '[':']', '(':')'}
        stack = []
        if s[0] in [')', ']', '}']:
            return False
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if len(stack) > 0:
                    bracket = stack.pop()
                    if ch != pairs[bracket]:
                        return False
                else: 
                    return False
        if len(stack) > 0:
            return False
        return True