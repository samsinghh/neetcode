class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        arr = []
        arr.append(nums[0])
        max_length = 1
        for i in range(1, len(nums)):
            num = nums[i]
            if num == nums[i-1] + 1:
                arr.append(num)
                max_length = max(len(arr), max_length)
            elif num == nums[i-1]:
                continue
            else:
                max_length = max(len(arr), max_length)
                arr = []
                arr.append(num)
        return max_length