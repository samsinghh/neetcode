class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            
            for j in range(i+1, len(height)):
                rightMax = max(rightMax, height[j])
            
            ans += min(leftMax, rightMax) - height[i]
        
        return ans
