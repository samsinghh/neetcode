class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def search(i, currComb, currSum):
            nonlocal res
            if currSum == target:
                res.append(currComb.copy())
                return
            
            for idx in range(i, len(nums)):
                if currSum + nums[idx] > target:
                    break
                currComb.append(nums[idx])
                search(idx, currComb, currSum+nums[idx])
                currComb.pop()

        search(0, [], 0)
        return res
            