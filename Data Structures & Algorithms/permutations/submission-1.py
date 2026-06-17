class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, path, res):
        if not nums:  # Base case: if nums is empty, we found a full permutation
            res.append(path)
            return
        
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)  # Recur with remaining numbers