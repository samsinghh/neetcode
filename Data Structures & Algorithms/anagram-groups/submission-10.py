class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupList = {}

        for word in strs:
            freqs = [0] * 26
            for ch in word: 
                freqs[ord(ch) - ord('a')] += 1
            if tuple(freqs) in groupList:
                groupList[tuple(freqs)].append(word)
            else:
                groupList[tuple(freqs)] = [word]
        
        return list(groupList.values())