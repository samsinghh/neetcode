class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(numsLeft, currPath):
            if len(currPath) == len(nums):
                res.append(currPath.copy())
                return
            
            for i in range(len(numsLeft)):
                currPath.append(numsLeft[i])
                backtrack(numsLeft[:i] + numsLeft[i+1:], currPath)
                currPath.pop()
        
        backtrack(nums, [])
        return res
