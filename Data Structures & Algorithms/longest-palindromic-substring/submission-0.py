class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findLongest(string, index1, index2):
            l, r = index1, index2
            while l >= 0 and r < len(string) and string[r] == string[l]:
                l -= 1
                r += 1
            
            return [l+1, r-1]

        maxLen = 0
        res = ''

        for i in range(len(s)):
            l, r = findLongest(s, i, i)
            oddLen = r - l + 1
            if oddLen > maxLen:
                maxLen = oddLen
                res = s[l:r+1]
            if i < len(s) - 1 and s[i] == s[i+1]:
                l, r = findLongest(s, i, i+1)
                evenLen = r - l + 1
                if evenLen > maxLen:
                    maxLen = evenLen
                    res = s[l:r+1]
        return res
        
