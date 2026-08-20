# calculate frequencies of letters in t
# sliding window and update freqs of letters in curr window
# when one frequency becomes = to a freq in t, add 1 to have var
# while have == need, increase l

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        resLen = float('inf')
        t_freq, s_freq = {}, {}
        have = 0
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        
        need = len(t_freq)
        l = 0

        for r in range(len(s)):
            c = s[r]
            s_freq[c] = s_freq.get(c, 0) + 1
            if c in t_freq and s_freq[c] == t_freq[c]:
                have += 1
            while have == need:
                if resLen > (r-l+1):
                    resLen = r-l+1
                    res = [l, r]
                s_freq[s[l]] -= 1
                if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ''
            

