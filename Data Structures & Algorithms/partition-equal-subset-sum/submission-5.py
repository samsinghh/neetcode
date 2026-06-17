class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for j in range(target, n-1, -1):
                if dp[j-n]:
                    dp[j] = True 

        return dp[target]
        
        

    
#find subset which sums to total sum / 2
# 0 / 1 knapsack 
# max capacity is 
#