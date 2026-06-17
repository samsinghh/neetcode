class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'{': '}', '[':']', '(':')'}
        stack = []
        
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if stack:
                    bracket = stack.pop()
                    if ch != pairs[bracket]:
                        return False
                else: 
                    return False
        return True if not stack else False