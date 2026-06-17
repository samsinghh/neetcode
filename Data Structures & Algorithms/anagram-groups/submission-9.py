class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            frequency = [0] * 26
            for char in word:
                frequency[ord(char) - ord('a')] += 1

            res[tuple(frequency)].append(word)
        
        return res.values()
