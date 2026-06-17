class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curMin = float('inf')

        for num in prices:
            if num < curMin:
                curMin = num
            
            res = max(res, num - curMin)
        
        return res