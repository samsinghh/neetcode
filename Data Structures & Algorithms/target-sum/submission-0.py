class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, remaining):
            if i == len(nums):
                return 1 if remaining == 0 else 0
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            
            # if you add it
            dp[(i, remaining)] = dfs(i+1, remaining - nums[i])
            dp[(i, remaining)] += dfs(i+1, remaining + nums[i])
            return dp[(i, remaining)]
        
        return dfs(0, target)


