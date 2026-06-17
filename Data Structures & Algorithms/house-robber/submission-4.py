class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def helper(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(helper(i - 1), nums[i] + helper(i - 2))
            return memo[i]

        return helper(len(nums) - 1)