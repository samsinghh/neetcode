class Solution:
    def countBits(self, n: int) -> List[int]:
        def find(num):
            res = 0
            while num > 0:
                res += num & 1
                num >>= 1
            return res
        res = []
        for i in range(n+1): 
            ones = find(i)
            res.append(ones)
        return res