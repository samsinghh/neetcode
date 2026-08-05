class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ')': '(', ']': '['}
        stack = []

        for b in s:
            if b in pairs:
                if stack:
                    if stack[-1] != pairs[b]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        return len(stack) == 0