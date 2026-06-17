class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def memoize(r, c, cache):
            if r == m or c == n:
                return 0

            if r == (m-1) or c == (n-1):
                return 1
            
            if cache[r][c] != 0:
                return cache[r][c]
            
            cache[r][c] = (memoize(r+1, c, cache) + memoize(r, c+1, cache))

            return cache[r][c]
        
        memo = [[0] * n for _ in range(m)]
        return memoize(0, 0, memo)