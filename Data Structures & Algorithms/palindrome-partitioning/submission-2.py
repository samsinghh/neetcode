class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(l, r, currPals):
            if r >= len(s):
                if l == r:
                    res.append(currPals.copy())
                return
            

            if self.isPali(s, l, r):
                currPals.append(s[l:r+1])
                backtrack(r+1, r+1, currPals)
                currPals.pop()
            
            backtrack(l, r+1, currPals)
        
        backtrack(0, 0, [])
        return res
    

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True