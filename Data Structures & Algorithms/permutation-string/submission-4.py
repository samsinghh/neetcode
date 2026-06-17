class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s1)

        if len(s2) < n:
            return False
            
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(n):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == s2_count:
            return True
        
        l, r = 0, n - 1
        while r < len(s2):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1 
            if r == len(s2):
                return False
            s2_count[ord(s2[r]) - ord('a')] += 1
        
        return False

