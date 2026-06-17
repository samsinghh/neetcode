class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        values = set()
        maxLength = 1

        l, r = 0, 1
        values.add(s[l])

        while r < len(s):
            while s[r] in values:
                values.remove(s[l])
                l += 1
            values.add(s[r])
            maxLength = max(maxLength, r - l + 1)
            r += 1
        
        return maxLength

