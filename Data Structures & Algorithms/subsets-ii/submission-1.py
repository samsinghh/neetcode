class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []   
        nums.sort()

        def backtrack(i, currPath):
            if i == len(nums):
                res.append(currPath.copy())
                return
            
            currPath.append(nums[i])
            backtrack(i+1, currPath)
            currPath.pop()

            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1, currPath)
        
        backtrack(0, [])
        return res
        
