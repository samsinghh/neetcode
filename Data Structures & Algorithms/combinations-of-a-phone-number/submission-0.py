class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, word):
            if i == len(digits):
                res.append(word)
                return
            
            for c in digitToChar[digits[i]]:
                temp = word
                word += c
                backtrack(i+1, word)
                word = temp
        

        backtrack(0, '')
        return res