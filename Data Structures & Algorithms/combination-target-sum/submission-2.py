class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, currPath, currSum):
            if currSum == target:
                res.append(currPath.copy())
                return
            
            if i == len(nums) or currSum > target:
                return
            
            currPath.append(nums[i])
            backtrack(i, currPath, currSum+nums[i])
            currPath.pop()
            backtrack(i+1, currPath, currSum)
        
        backtrack(0, [], 0)
        return res
