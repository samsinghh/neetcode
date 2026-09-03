# first, do a forward pass to calculate prefix products
# then, backward pass and multiply on postfix products
# [-1, 0, 1, 2, 3]
# [0, -6, 0, 0, 0]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        curr = 1
        for i in range(len(nums)):
            res[i] *= curr
            curr *= nums[i]
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= curr
            curr *= nums[i]
        
        return res

