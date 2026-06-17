class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i - 1]:
                continue

            target = 0 - num
            l, r = i+1, len(nums) - 1
            while l < r:
                summy = nums[l] + nums[r]
                if summy < target:
                    l += 1
                elif summy > target:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
