class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        prefixes = {0: 1}

        for num in nums:
            curr += num
            diff = curr - k
            res += prefixes.get(diff, 0)
            prefixes[curr] = 1 + prefixes.get(curr, 0)
        return res
