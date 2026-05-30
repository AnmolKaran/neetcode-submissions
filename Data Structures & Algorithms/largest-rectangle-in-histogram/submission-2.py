class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, v in enumerate(heights):
            popped =i
            while stack and stack[-1][1] > v:
                ind, height = stack.pop()
                maxArea = max(maxArea, height * (i - ind) )
                popped = ind

            
            stack.append((popped,v))
           
        for entry in stack:
            i, v = entry[0], entry[1]
            area = (len(heights) - i) * v
            maxArea = max(area,maxArea)

        return maxArea
            
        


