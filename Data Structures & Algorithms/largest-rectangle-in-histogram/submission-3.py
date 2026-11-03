class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        currentMax = 0
        stack = []
        for i in range(len(heights)):
            c = 0
            while stack and stack[-1][0] > heights[i]:
                area = stack[-1][0] * (i - stack[-1][1])
                if area > currentMax:
                    currentMax = area
                c = i - stack[-1][1]
                stack.pop()
            stack.append((heights[i], i - c))
            print(heights[i], i - c)
        while stack:
            area = stack[-1][0] * (len(heights) - stack[-1][1])
            if area > currentMax:
                currentMax = area
            stack.pop()
        return currentMax
        
