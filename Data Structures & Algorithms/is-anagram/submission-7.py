class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts, t_counts = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            s_counts[s[i]] += 1
            t_counts[t[i]] += 1
        
        return s_counts == t_counts