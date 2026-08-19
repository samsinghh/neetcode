# get value in middle
# if value in middle is greater than value at right, then smallest val MUST be on right
# if value in middle is less than val on right, smallest val is either middle val or to the left

# [3, 4, 5, 6, 1, 2]
#              r
#              l   

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r-l)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[r]

