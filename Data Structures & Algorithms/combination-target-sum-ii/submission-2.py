class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, currPath, currSum):
            if currSum == target:
                res.append(currPath.copy())
                return
            
            if i == len(candidates) or currSum > target:
                return
            
            currPath.append(candidates[i])
            backtrack(i+1, currPath, currSum + candidates[i])
            currPath.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, currPath, currSum)

        backtrack(0, [], 0)
        return res