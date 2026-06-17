class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for string in strs:
            num = len(string)
            res += str(num) + '&' + string
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ''

            while(s[i] != '&'):
                length += s[i]
                i += 1
            word_length = int(length)
            i += 1
            word = s[i:i+word_length]
            res.append(word)
            i += word_length
            
        return res
                