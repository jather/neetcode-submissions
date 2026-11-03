class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        i, j = 0, len(height) - 1
        leftMax, rightMax = height[i], height[j]
        while i < j:
            if leftMax < rightMax:
                i += 1
                while height[i] < leftMax:
                    area += leftMax - height[i]
                    i += 1
                leftMax = height[i]
            else:
                j -= 1
                while height[j] < rightMax:
                    area += rightMax - height[j]
                    j -= 1
                rightMax = height[j]
        return area


        # if next height is taller, max = next height. 
        # if next height is shorter, volume += max - next height. move onto next. 
        # 
            

        