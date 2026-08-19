# loop through nums and get total product
# loop through nums again, divide total product by current element, append to result list

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        totalProduct = 1
        hasZero = False
        for num in nums:
            if num == 0:
                if hasZero:
                    return [0] * len(nums)
                else:
                    hasZero = True
            else:
                totalProduct *= num

        for num in nums:
            if hasZero:
                res.append(0 if num else totalProduct)
            else: 
                res.append(totalProduct // num)
        return res     
