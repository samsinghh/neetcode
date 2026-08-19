# 1, 2, 3, 3, 4, 4, 5


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res, currCount = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == (nums[i-1] + 1):
                currCount += 1    
            else:
                res = max(res, currCount)
                currCount = 1
        return max(res, currCount)

# 0, 1, 1, 2, 3, 4, 5, 6