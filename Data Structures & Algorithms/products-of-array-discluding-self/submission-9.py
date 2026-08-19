# loop through nums and get total product
# loop through nums again, divide total product by current element, append to result list
# [1, 0, 4, 6]
# [1, 0, 0, 0]
# [0, 0, 24, 6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        postfix = []

        temp = 1
        for num in nums:
            temp *= num
            prefix.append(temp)
        temp = 1 
        for num in nums[::-1]:
            temp*= num
            postfix.append(temp)

        postfix.reverse()

        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i+1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1] * postfix[i+1])
        return res 

