# s = "CXBBBZADKFJDLCXCZ" t = "XZ"
# l, r 
# move right pointer until all of t is in s[l:r]
# move left pointer while condition is still met
# start moving right pointer again
# as you're moving forward left pointer, if len(res) > r-l+1, res = s[l:r+1]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = [-1, -1]
        resLen = float('inf')
        have = 0

        t_map = [0] * 128
        s_map = [0] * 128
        for c in t:
            t_map[ord(c)] += 1
        need = sum(count > 0 for count in t_map)

        for r in range(len(s)):
            s_map[ord(s[r])] += 1
            if s_map[ord(s[r])] == t_map[ord(s[r])]:
                have += 1
            while have == need:
                if resLen > (r-l+1):
                    resLen = r-l+1
                    res = [l, r]
                s_map[ord(s[l])] -= 1
                if s_map[ord(s[l])] < t_map[ord(s[l])]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""



        
        
        