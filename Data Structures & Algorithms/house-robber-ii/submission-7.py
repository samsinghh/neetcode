class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            first, second = 0, 0

            for num in arr:
                temp = max(num + first, second)
                first = second
                second = temp
            
            return second
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))