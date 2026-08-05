class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        currMin = float('inf')

        for price in prices:
            currMin = min(currMin, price)
            res = max(res, price - currMin)
        
        return res
        