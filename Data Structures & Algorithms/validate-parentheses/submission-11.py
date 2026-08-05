class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ')': '(', ']': '['}
        stack = []

        for b in s:
            if b in pairs:
                if not stack or stack.pop() != pairs[b]:
                    return False
            else:
                stack.append(b)
        return not stack