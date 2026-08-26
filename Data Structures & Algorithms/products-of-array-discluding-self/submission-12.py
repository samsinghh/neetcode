# loop through nums and get total product
# loop through nums again, divide total product by current element, append to result list
# [1, 0, 4, 6]
# [1, 0, 0, 0]
# [0, 0, 24, 6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]

        curr = nums[0]
        for num in nums[1:]:
            res.append(curr)
            curr *= num

        curr = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= curr
            curr *= nums[i]
        return res


