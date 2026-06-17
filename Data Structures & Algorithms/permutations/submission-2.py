class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(notUsed, currPath):
            if len(currPath) == len(nums):
                res.append(currPath.copy())
                return
            

            for i, num in enumerate(notUsed):
                currPath.append(num)
                backtrack(notUsed[:i] + notUsed[i+1:], currPath)
                currPath.pop()
            
        
        backtrack(nums, [])
        return res

