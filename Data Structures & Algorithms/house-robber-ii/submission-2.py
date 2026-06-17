class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [0] * (n-1)
        arr = nums[:-1]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        
        res = dp[-1]
        arr = nums[1:]
        dp = [0] * (n-1)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        
        res = max(res, dp[-1])
        return res
        

        

        
