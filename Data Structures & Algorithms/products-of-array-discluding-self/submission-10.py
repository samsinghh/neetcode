# loop through nums and get total product
# loop through nums again, divide total product by current element, append to result list
# [1, 0, 4, 6]
# [1, 0, 0, 0]
# [0, 0, 24, 6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        temp = 1
        for i in range(len(nums)):
            res[i] = temp
            temp *= nums[i]
        
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        
        return res

