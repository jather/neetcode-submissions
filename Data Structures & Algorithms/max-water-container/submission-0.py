class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        volume = 0
        while i < j:
            first = heights[i]
            second = heights[j]
            volume = max(volume, min(first, second) * (j - i))
            if first < second:
                while i < j and heights[i] <= first:
                    i += 1
            elif second < first:
                while i < j and heights[j] <= second:
                    j -= 1
            else:
                while i < j and heights[i] <= first:
                    i += 1
                while i < j and heights[j] <= second:
                    j -= 1
        return volume

        