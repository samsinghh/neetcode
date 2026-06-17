class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        for char in t:
            t_freq[char] += 1
        
        l = 0
        have, need = 0, len(t_freq)

        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            char = s[r]
            s_freq[char] += 1

            if char in t_freq and s_freq[char] == t_freq[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                s_freq[s[l]] -= 1
                if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l+=1
        
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
                




