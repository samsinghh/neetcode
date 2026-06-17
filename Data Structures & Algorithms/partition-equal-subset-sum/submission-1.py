class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        def dfs(i, capacity):
            if capacity == 0:
                return True
            
            if i == len(nums):
                return False
            
            if dfs(i+1, capacity):
                return True
            
            newCap = capacity - nums[i]
            if newCap >= 0:
                if dfs(i+1, newCap):
                    return True
            
            return False
        
        return dfs(0, total // 2)
        

    
#find subset which sums to total sum / 2
# 0 / 1 knapsack 
# max capacity is 
#