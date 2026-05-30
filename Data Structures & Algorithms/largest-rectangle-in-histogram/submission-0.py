class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum = 0
        for i ,v in enumerate(heights):
            currArea = v
            minHeight = v
            if currArea > maximum:
                maximum = currArea
            for j in range(1, len(heights)-i):
            
               
                if heights[i+j] < minHeight:
                    minHeight = heights[i + j]
                
                currArea = minHeight * (j+1)

                if currArea > maximum:
                    maximum = currArea
        return maximum

            