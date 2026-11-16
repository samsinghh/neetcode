class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        curr = 0
        res = 0

        for i, val in enumerate(nums):
            curr += 1 if val == 1 else -1
            if curr in first_seen:
                res = max(res, i - first_seen[curr])
            else:
                first_seen[curr] = i
        return res
