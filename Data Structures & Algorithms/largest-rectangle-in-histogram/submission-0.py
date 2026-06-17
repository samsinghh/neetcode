class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] 

        for i, height in enumerate(heights):
            temp_i = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                maxArea = max(maxArea, h * (temp_i - index))
                i = index
            stack.append((i, height))
        
        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))
        
        return maxArea  