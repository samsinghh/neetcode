class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            freqs = [0] * 26
            for ch in word: 
                freqs[ord(ch) - ord('a')] += 1
            res[tuple(freqs)].append(word)
        
        return list(res.values())