class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxSoFar = 0
        left = 0
        right = len(heights)-1
        while left < right:
            heightofwater = min(heights[left],heights[right])
            lengthofwater = right - left 
            area = heightofwater * lengthofwater
            if area > maxSoFar:
                maxSoFar = area
                # left +=1
                # right -=1

            if heights[left] <= heights[right]:
                left +=1
            else:
                right -=1
        return maxSoFar