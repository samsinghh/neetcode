# loop through t, store frequencies of chars in t in a hashmap
# left and right pointer iterating through s
# when r gets to new char, increase hm_s[s[r]] by 1
# if s[r] is in hm_t, then check if by incrementing value, that made the two freqs equal
# have a need and have counter, increment have
# while have == need, close window by moving left pointer up and updating hm_s accordingly
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        resLen = float('inf')

        hm_t, hm_s = {}, {}

        for c in t:
            hm_t[c] = hm_t.get(c, 0) + 1
        
        have, need = 0, len(hm_t)

        l = 0

        for r in range(len(s)):
            c = s[r]
            hm_s[c] = hm_s.get(c, 0) + 1

            if c in hm_t and hm_t[c] == hm_s[c]:
                have += 1

            while have == need:
                if r-l+1 < resLen: 
                    resLen = r-l+1
                    res = [l, r]
                cr = s[l]
                hm_s[cr] -= 1
                if cr in hm_t and hm_s[cr] < hm_t[cr]:
                    have -= 1 
                l += 1
        l, r = res 
        return s[l:r+1] if resLen != float('inf') else ''
