class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        dp = [[-1] * (total+1) for _ in range(len(nums) + 1)]
        if total % 2 == 1:
            return False
        
        def dfs(i, capacity):
            if capacity == 0:
                return True
            
            if i == len(nums) or capacity < 0:
                return False
            
            if dp[i][capacity] != -1:
                return dp[i][capacity]
            
            dp[i][capacity] = dfs(i+1, capacity) or dfs(i+1, capacity - nums[i])
            return dp[i][capacity]

        return dfs(0, total // 2)
        
