# you only need to start searching for a sequence from
# a number n IFF n-1 is not in nums

# loop through nums, for each n, if n-1 not in set(nums)
# start a while loop with x = n, break when x not in set(nums)
# keep a recurring counter going in while loop

# O(N)
# Space: O(N)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        res = 0

        for num in numset:
            if (num-1) not in numset:
                curr = 0
                k = num
                while k in numset:
                    curr += 1
                    k += 1
                res = max(res, curr)
        
        return res
                    




