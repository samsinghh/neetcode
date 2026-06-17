class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))

    
    def dp(self, nums):
        if len(nums) == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(nums[i] + first, second)
            first, second = second, current
        
        return second

        
