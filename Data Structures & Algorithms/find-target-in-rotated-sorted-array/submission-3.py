class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        def binarySearch(left, right):
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        res = binarySearch(0, pivot - 1)

        if res != -1:
            return res
        
        return binarySearch(pivot, len(nums) - 1)

        
