class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += "" + str(len(word)) + "&" + word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != "&":
                length += s[i]
                i += 1
            length = int(length)
            currWord = ''
            for j in range(i+1, i + length + 1):
                currWord += s[j]
            
            res.append(currWord)
            i += length + 1
        
        return res