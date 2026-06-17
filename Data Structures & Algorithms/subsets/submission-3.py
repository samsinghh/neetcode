class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, currPath):
            if i == len(nums):
                res.append(currPath.copy())
                return
            
            currPath.append(nums[i])
            backtrack(i+1, currPath)
            currPath.pop()

            backtrack(i+1, currPath)
        
        backtrack(0, [])
        return res
