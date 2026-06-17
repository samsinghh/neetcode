class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(currPath, i):
            if i == len(nums):
                res.append(currPath.copy())
                return
            
            currPath.append(nums[i])
            backtrack(currPath, i+1)
            currPath.pop()
            backtrack(currPath, i+1)
        
        backtrack([], 0)
        return res