class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findLongest(string, index1, index2):
            l, r = index1, index2
            while l >= 0 and r < len(string) and string[r] == string[l]:
                l -= 1
                r += 1
            
            return [l+1, r-1]

        start, end = 0, 0 

        for i in range(len(s)):
            l1, r1 = findLongest(s, i, i)
            l2, r2 = findLongest(s, i, i+1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
          
        return s[start:end+1]
        
