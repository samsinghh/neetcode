class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1

        i = 2

        while i <= n:
            temp = second
            second = first + second
            first = temp

            i += 1
        
        return second 