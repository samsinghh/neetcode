# left and right pointer which track endpoints
# of the substring that we currently are at
# move the right pointer forward, maintain a frequencies array
# of each letter, increment freqs[s[r]]
# while freqs[s[r]] > 2, move left pointer forward
# and decremenet freqs[s[l]]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0 
        freqs = {}

        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            
            while freqs[s[r]] == 2:
                freqs[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res 