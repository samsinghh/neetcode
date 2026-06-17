class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        def dfs(i, capacity):
            if capacity == 0:
                return True
            
            if i == len(nums) or capacity < 0:
                return False
            
            if (i, capacity) in dp:
                return dp[(i, capacity)]
            
            dp[(i, capacity)] = dfs(i+1, capacity) or dfs(i+1, capacity - nums[i])
            return dp[(i, capacity)]
            
        return dfs(0, total // 2)
        

    
#find subset which sums to total sum / 2
# 0 / 1 knapsack 
# max capacity is 
#