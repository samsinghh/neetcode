class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        while l <= r:
            mid = l + (r - l) // 2

            if nums[r] < nums[mid]:
                res = min(res, nums[r])
                l = mid + 1
            else:
                res = min(res, nums[mid])
                r = mid - 1
        
        return res


''' 
[2, 3, 4, 5, 6, 1]
'''
            