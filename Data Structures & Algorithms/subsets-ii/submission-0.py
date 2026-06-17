class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.backtrack(0, nums, [])
        return self.res


    def backtrack(self, i, nums, subset):
        if i == len(nums):
            self.res.append(subset.copy())
            return
        
        subset.append(nums[i])
        self.backtrack(i+1, nums, subset)

        subset.pop()

        while i < len(nums) - 1 and nums[i+1] == nums[i]:
            i += 1
        
        self.backtrack(i+1, nums, subset)
        
