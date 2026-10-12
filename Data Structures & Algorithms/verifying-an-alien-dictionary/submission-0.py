class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = {}
        for i, c in enumerate(order):
            hm[c] = i
        
        result = sorted(words, key=lambda word: [hm[ch] for ch in word])
        return result == words
