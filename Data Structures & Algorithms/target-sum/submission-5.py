class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def search(i, total):
            if i == len(nums):
                return total == target
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = search(i+1, total+nums[i])
            dp[(i, total)] += search(i+1, total-nums[i])
            return dp[(i, total)]
        return search(0, 0) 
            