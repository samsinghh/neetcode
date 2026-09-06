# 0 - 1
# 1 - 1
# 2 - 2
# 3 -  
class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 1

        curr = 1
        for i in range(2, n+1):
            curr = p1 + p2
            p1, p2 = p2, curr
        
        return curr

