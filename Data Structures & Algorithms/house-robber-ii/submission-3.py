class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        def dp(arr):
            first = arr[0]
            second = max(arr[0], arr[1])

            for num in arr[2:]:
                new = max(first+num, second)
                first = second
                second = new
            return second
        
        return max(dp(nums[1:]), dp(nums[:-1]))


        
        
        

        

        
