class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in s:
            freq1[ord(ch) - ord('a')] += 1
        
        for ch in t:
            freq2[ord(ch) - ord('a')] += 1
        
        return freq1 == freq2

        