class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1

        for i in range(len(nums)-2, -1, -1):
            curMax = dp[i]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    curMax = max(curMax, dp[i] + dp[j])
            dp[i] = curMax
            res = max(res, curMax)
        
        return res
        

                

                
            


