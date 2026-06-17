class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            chars = [0] * 26
            for ch in word:
                chars[ord(ch) - ord('a')] += 1
            ans[tuple(chars)].append(word)
        return list(ans.values())