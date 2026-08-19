# 1, 2, 3, 3, 4, 4, 5


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for num in nums:
            if num-1 not in numset:
                k = num
                counter = 0
                while k in numset:
                    counter += 1
                    k += 1
                res = max(res, counter)
        
        return res

